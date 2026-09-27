// Cloudflare Worker: receives request forms from thermex.uz and posts them
// to a Telegram group or channel. The bot token never reaches the browser.
//
// Secrets / variables (Cloudflare dashboard → Worker → Settings → Variables):
//   TELEGRAM_BOT_TOKEN  secret, from @BotFather
//   TELEGRAM_CHAT_ID    id of the group or channel, e.g. -1001234567890
//   ALLOWED_ORIGINS     optional, comma-separated; defaults to thermex.uz

const DEFAULT_ORIGINS = 'https://thermex.uz,https://www.thermex.uz';

export default {
  async fetch(request, env) {
    const allowed = (env.ALLOWED_ORIGINS || DEFAULT_ORIGINS).split(',').map((s) => s.trim());
    const origin = request.headers.get('Origin') || '';
    const cors = {
      'Access-Control-Allow-Origin': allowed.includes(origin) ? origin : allowed[0],
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Vary': 'Origin',
    };

    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
    if (request.method !== 'POST') return reply({ ok: false, error: 'method' }, 405, cors);
    if (!allowed.includes(origin)) return reply({ ok: false, error: 'origin' }, 403, cors);
    if (!env.TELEGRAM_BOT_TOKEN || !env.TELEGRAM_CHAT_ID) return reply({ ok: false, error: 'config' }, 500, cors);

    let data;
    try {
      data = await request.json();
    } catch {
      return reply({ ok: false, error: 'json' }, 400, cors);
    }

    // Honeypot: real visitors never fill this hidden field.
    if (data.website) return reply({ ok: true }, 200, cors);

    const name = clean(data.name, 100);
    const phone = clean(data.phone, 40);
    if (!name || phone.replace(/\D/g, '').length < 7) return reply({ ok: false, error: 'validation' }, 400, cors);

    const lines = [
      '<b>🔔 Новая заявка с сайта</b>',
      '',
      `<b>Имя:</b> ${name}`,
      `<b>Телефон:</b> ${phone}`,
    ];
    const topic = clean(data.topic, 120);
    const message = clean(data.message, 1500);
    const page = clean(data.page, 200);
    if (topic) lines.push(`<b>Тема:</b> ${topic}`);
    if (message) lines.push(`<b>Сообщение:</b> ${message}`);
    if (page) lines.push('', `<i>Страница: ${page}</i>`);

    const tg = await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: env.TELEGRAM_CHAT_ID,
        text: lines.join('\n'),
        parse_mode: 'HTML',
        disable_web_page_preview: true,
      }),
    });

    return reply({ ok: tg.ok }, tg.ok ? 200 : 502, cors);
  },
};

function clean(value, max) {
  return String(value ?? '')
    .trim()
    .slice(0, max)
    .replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[c]);
}

function reply(body, status, headers) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...headers, 'Content-Type': 'application/json' },
  });
}
