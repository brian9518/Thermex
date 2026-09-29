/* Thermex Uzbekistan — site scripts (no dependencies) */
(function () {
  'use strict';

  // URL of the Cloudflare Worker from telegram-worker/ (see its README).
  // While empty, forms fall back to opening WhatsApp.
  var LEAD_ENDPOINT = '';

  // WhatsApp number for the sales line; service forms override it via data-wa.
  var CONTACT = {
    whatsapp: '998903745254'
  };

  var PRODUCTS = {
    'thermo-50v': {
      name: 'Thermo 50 V', series: 'Thermo', volume: 50,
      desc: 'Круглый вертикальный водонагреватель с тремя режимами мощности и ускоренным нагревом. Бак с покрытием из биостеклофарфора, ТЭН из нержавеющей стали.',
      images: ['p-thermo-50v.webp', 'p-thermo-50v-2.webp'],
      specs: [
        ['Артикул', '111 011'], ['Объём', '50 л'], ['Мощность', '1000 / 1500 / 2500 Вт'],
        ['Время нагрева (Δt 45°)', '60 мин'], ['Ускоренный нагрев', 'да'],
        ['Материал бака', 'биостеклофарфор'], ['Нагревательный элемент', 'нержавеющая сталь, трубчатый'],
        ['Установка / подводка', 'вертикальная, нижняя'], ['Макс. температура', '75 °C'],
        ['Давление воды', '0,05–0,6 МПа'], ['Класс защиты', 'IPX4, УЗО'],
        ['Размеры (В×Ш×Г)', '722 × 365 × 378 мм'], ['Вес', '16,8 кг'],
        ['Гарантия', 'бак — 5 лет, изделие — 2 года'], ['Производство', 'Россия']
      ]
    },
    'edisson-50v': {
      name: 'Edisson ER 50 V', series: 'Edisson', volume: 50,
      desc: 'Компактный круглый водонагреватель закрытого типа для квартиры или дома. Надёжная защита IPX4 и простое подключение к стандартной розетке.',
      images: ['p-edisson-50v.webp', 'p-edisson-50v-2.webp'],
      specs: [
        ['Артикул', 'SpT066445'], ['Объём', '50 л'], ['Мощность', '1,5 кВт'], ['Напряжение', '220 В'],
        ['Тип', 'закрытый, настенный'], ['Давление воды', '0,5–6 бар'], ['Подвод воды', 'G 1/2'],
        ['Класс защиты', 'IPX4'], ['Размеры (В×Ш×Г)', '527 × 445 × 459 мм'], ['Вес', '16,5 кг'],
        ['Производство', 'Россия']
      ]
    },
    'ers-80v': {
      name: 'ERS 80 V Silverheat', series: 'Champion Silverheat', volume: 80,
      desc: 'Вместительный водонагреватель на 80 литров для семьи из 3–4 человек. ТЭН с серебряным покрытием Silverheat устойчив к накипи и служит дольше.',
      images: ['p-ers-80v.webp', 'p-ers-80v-2.webp'],
      specs: [
        ['Артикул', '111 035'], ['Объём', '80 л'], ['Мощность', '1500 Вт'],
        ['Время нагрева (Δt 45°)', '170 мин'], ['Материал бака', 'биостеклофарфор'],
        ['Нагревательный элемент', 'Silverheat, трубчатый'], ['Установка / подводка', 'вертикальная, нижняя'],
        ['Макс. температура', '75 °C'], ['Давление воды', '0,1–0,6 МПа'], ['Класс защиты', 'IPX4, УЗО'],
        ['Размеры (В×Ш×Г)', '751 × 445 × 459 мм'], ['Вес', '21,2 кг'],
        ['Гарантия', 'бак — 5 лет, изделие — 2 года'], ['Производство', 'Россия']
      ]
    },
    'nobel-10u': {
      name: 'Nobel 10 U', series: 'Nobel', volume: 10,
      desc: 'Малолитражный водонагреватель для установки под мойку (верхняя подводка). Бак из нержавеющей стали, медный ТЭН, нагрев всего за 16 минут.',
      images: ['p-nobel-10u.webp'],
      specs: [
        ['Артикул', '151 120'], ['Объём', '10 л'], ['Мощность', '2000 Вт'],
        ['Время нагрева (Δt 45°)', '16 мин'], ['Материал бака', 'нержавеющая сталь'],
        ['Нагревательный элемент', 'медь, трубчатый'], ['Установка / подводка', 'под мойку, верхняя'],
        ['Регулировка температуры', '+18…+74 °C'], ['Давление воды', '0,05–0,7 МПа'],
        ['Класс защиты', 'IPX4, УЗО'], ['Размеры (В×Ш×Г)', '398 × 260 × 270 мм'], ['Вес', '5,6 кг'],
        ['Гарантия', 'бак — 5 лет, изделие — 1 год'], ['Производство', 'Россия']
      ]
    },
    'nobel-10o': {
      name: 'Nobel 10 O', series: 'Nobel', volume: 10,
      desc: 'Малолитражный водонагреватель для установки над мойкой (нижняя подводка). Идеален для кухни, офиса или дачи.',
      images: ['p-nobel-10o.webp'],
      specs: [
        ['Артикул', '151 095'], ['Объём', '10 л'], ['Мощность', '2000 Вт'],
        ['Время нагрева (Δt 45°)', '16 мин'], ['Материал бака', 'нержавеющая сталь'],
        ['Нагревательный элемент', 'медь, трубчатый'], ['Установка / подводка', 'над мойкой, нижняя'],
        ['Регулировка температуры', '+18…+74 °C'], ['Давление воды', '0,05–0,7 МПа'],
        ['Класс защиты', 'IPX4, УЗО'], ['Размеры (В×Ш×Г)', '398 × 260 × 270 мм'], ['Вес', '5,6 кг'],
        ['Гарантия', 'бак — 5 лет, изделие — 1 год'], ['Производство', 'Россия']
      ]
    },
    'nobel-15o': {
      name: 'Nobel 15 O', series: 'Nobel', volume: 15,
      desc: 'Водонагреватель на 15 литров для установки над мойкой. Больше горячей воды при тех же компактных габаритах по ширине.',
      images: ['p-nobel-15o.webp'],
      specs: [
        ['Артикул', '151 097'], ['Объём', '15 л'], ['Мощность', '2000 Вт'],
        ['Время нагрева (Δt 45°)', '28 мин'], ['Материал бака', 'нержавеющая сталь'],
        ['Нагревательный элемент', 'медь, трубчатый'], ['Установка / подводка', 'над мойкой, нижняя'],
        ['Регулировка температуры', '+18…+74 °C'], ['Давление воды', '0,05–0,7 МПа'],
        ['Класс защиты', 'IPX4, УЗО'], ['Размеры (В×Ш×Г)', '533 × 260 × 270 мм'], ['Вес', '6,7 кг'],
        ['Гарантия', 'бак — 5 лет, изделие — 1 год'], ['Производство', 'Россия']
      ]
    }
  };

  var IMG = '/assets/img/';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* Header shadow on scroll */
  var header = $('.header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* Overlay helpers (drawer + modal) */
  var lastFocus = null;
  function openLayer(el) {
    lastFocus = document.activeElement;
    el.classList.add('is-open');
    el.setAttribute('aria-hidden', 'false');
    document.body.classList.add('no-scroll');
    var f = el.querySelector('[data-autofocus]') || el.querySelector('button, a');
    if (f) setTimeout(function () { f.focus(); }, 50);
  }
  function closeLayer(el) {
    el.classList.remove('is-open');
    el.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('no-scroll');
    if (lastFocus) lastFocus.focus();
  }
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    $$('.drawer.is-open, .modal.is-open').forEach(closeLayer);
  });

  /* Mobile drawer */
  var drawer = $('#drawer');
  if (drawer) {
    $$('[data-open-drawer]').forEach(function (b) { b.addEventListener('click', function () { openLayer(drawer); }); });
    $$('[data-close-drawer]', drawer).forEach(function (b) { b.addEventListener('click', function () { closeLayer(drawer); }); });
    $$('nav a', drawer).forEach(function (a) { a.addEventListener('click', function () { closeLayer(drawer); }); });
  }

  /* Scroll reveal */
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* Product filters: several chip groups on one grid combine (brand AND volume) */
  $$('[data-filters]').forEach(function (group) {
    var gridId = group.getAttribute('data-filters');
    var grid = document.getElementById(gridId);
    $$('.chip', group).forEach(function (chip) {
      chip.addEventListener('click', function () {
        $$('.chip', group).forEach(function (c) { c.classList.remove('is-active'); c.setAttribute('aria-pressed', 'false'); });
        chip.classList.add('is-active');
        chip.setAttribute('aria-pressed', 'true');
        var active = $$('[data-filters="' + gridId + '"] .chip.is-active')
          .map(function (c) { return c.getAttribute('data-filter'); })
          .filter(function (f) { return f !== 'all'; });
        var shown = 0;
        $$('.product', grid).forEach(function (p) {
          var tags = ' ' + p.getAttribute('data-tags') + ' ';
          var ok = active.every(function (f) { return tags.indexOf(' ' + f + ' ') > -1; });
          p.hidden = !ok;
          if (ok) shown++;
        });
        var empty = $('.filter-empty', grid.parentNode);
        if (empty) empty.hidden = shown > 0;
      });
    });
  });

  /* Product modal */
  var modal = $('#product-modal');
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  // Models from the price list have no spec entry: build a short card from the button's data.
  function productFromButton(b) {
    var img = b.closest('.product') && b.closest('.product').querySelector('.product-media img');
    var specs = [['Бренд', b.getAttribute('data-brand')], ['Объём', b.getAttribute('data-vol') + ' л']];
    if (b.getAttribute('data-mount')) specs.push(['Монтаж', b.getAttribute('data-mount')]);
    if (b.getAttribute('data-kind')) specs.push(['Тип нагрева', b.getAttribute('data-kind')]);
    if (b.getAttribute('data-origin')) specs.push(['Производство', b.getAttribute('data-origin')]);
    return {
      title: b.getAttribute('data-name'),
      label: b.getAttribute('data-brand'),
      images: [img ? img.getAttribute('src') : ''],
      desc: 'Подробные характеристики, наличие и цену уточняйте у менеджера — ответим в течение 15 минут в рабочее время.',
      specs: specs
    };
  }
  function openProduct(id, btn) {
    var p = PRODUCTS[id] || (window.THERMEX_CATALOG && window.THERMEX_CATALOG[id]) ||
      (btn && btn.hasAttribute('data-name') ? productFromButton(btn) : null);
    if (!p || !modal) return;
    var title = p.title || 'Thermex ' + p.name;
    var imgs = p.images.map(function (x) { return x.charAt(0) === '/' ? x : IMG + x; });
    var main = $('.modal-main img', modal);
    main.src = imgs[0];
    main.alt = 'Водонагреватель ' + title;
    var thumbs = $('.thumbs', modal);
    thumbs.innerHTML = imgs.length > 1 ? imgs.map(function (src, i) {
      return '<button type="button" class="' + (i ? '' : 'is-active') + '" data-src="' + src + '" aria-label="Фото ' + (i + 1) + '"><img src="' + src + '" alt=""></button>';
    }).join('') : '';
    $$('button', thumbs).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('button', thumbs).forEach(function (x) { x.classList.remove('is-active'); });
        b.classList.add('is-active');
        main.src = b.getAttribute('data-src');
      });
    });
    $('.product-series', modal).textContent = p.label || 'Серия ' + p.series;
    $('#modal-title', modal).textContent = title;
    $('.desc', modal).textContent = p.desc;
    $('.spec-table tbody', modal).innerHTML = p.specs.map(function (r) {
      return '<tr><th scope="row">' + esc(r[0]) + '</th><td>' + esc(r[1]) + '</td></tr>';
    }).join('');
    var msg = 'Здравствуйте! Интересует водонагреватель ' + title + '. Подскажите цену и наличие.';
    $('[data-wa]', modal).href = 'https://wa.me/' + CONTACT.whatsapp + '?text=' + encodeURIComponent(msg);
    openLayer(modal);
  }
  if (modal) {
    $$('[data-product]').forEach(function (b) {
      b.addEventListener('click', function (e) { e.preventDefault(); openProduct(b.getAttribute('data-product'), b); });
    });
    $$('[data-close-modal]', modal).forEach(function (b) { b.addEventListener('click', function () { closeLayer(modal); }); });
    if (location.hash.indexOf('#model-') === 0) openProduct(location.hash.slice(7));
  }

  /* Volume picker */
  var picker = $('#picker');
  if (picker) {
    var TABLE = { 1: [30, 30], 2: [30, 50], 3: [50, 80], 4: [80, 100], 5: [100, 120], 6: [120, 150] };
    var state = { people: 2, use: 'full' };
    var render = function () {
      var min, rec;
      if (state.use === 'kitchen') { min = 10; rec = state.people > 2 ? 15 : 10; }
      else { min = TABLE[state.people][0]; rec = TABLE[state.people][1]; }
      $('[data-rec]', picker).textContent = rec;
      $('[data-min]', picker).textContent = min;
      var pid = rec <= 10 ? 'nobel-10o' : rec <= 15 ? 'nobel-15o' : rec <= 50 ? 'thermo-50v' : 'ers-80v';
      var p = PRODUCTS[pid];
      var box = $('.picker-rec', picker);
      $('img', box).src = IMG + p.images[0];
      $('strong', box).textContent = 'Thermex ' + p.name;
      $('[data-note]', box).textContent = rec > 80
        ? 'Для объёма ' + rec + ' л подберём модель под заказ — оставьте заявку.'
        : p.volume + ' л · ' + p.specs[2][1];
      $('[data-product-link]', box).setAttribute('data-product', pid);
    };
    $$('[data-people] button', picker).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('[data-people] button', picker).forEach(function (x) { x.classList.remove('is-active'); x.setAttribute('aria-pressed', 'false'); });
        b.classList.add('is-active'); b.setAttribute('aria-pressed', 'true');
        state.people = +b.value; render();
      });
    });
    $$('[data-use] button', picker).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('[data-use] button', picker).forEach(function (x) { x.classList.remove('is-active'); x.setAttribute('aria-pressed', 'false'); });
        b.classList.add('is-active'); b.setAttribute('aria-pressed', 'true');
        state.use = b.value; render();
      });
    });
    var link = $('[data-product-link]', picker);
    if (link) link.addEventListener('click', function () { openProduct(link.getAttribute('data-product')); });
    render();
  }

  /* Lazy YouTube */
  $$('[data-youtube]').forEach(function (box) {
    var btn = $('.video-play', box);
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube.com/embed/' + box.getAttribute('data-youtube') + '?autoplay=1&rel=0';
      f.title = btn.getAttribute('aria-label') || 'Видео';
      f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
      f.allowFullscreen = true;
      box.appendChild(f);
      btn.remove();
    });
  });

  /* Request forms → Telegram group (via LEAD_ENDPOINT) or WhatsApp */
  $$('form[data-lead]').forEach(function (form) {
    var submitBtn = $('button[value="send"]', form);
    var label = submitBtn ? submitBtn.innerHTML : '';
    var setState = function (state) {
      form.classList.remove('is-sent', 'is-wa', 'is-error');
      if (state) form.classList.add(state);
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var via = (e.submitter && e.submitter.value) || 'send';

      if (via === 'whatsapp' || !LEAD_ENDPOINT) {
        var lines = ['Заявка с сайта thermex.uz', 'Имя: ' + (d.get('name') || '')];
        if (d.get('phone')) lines.push('Телефон: ' + d.get('phone'));
        if (d.get('topic')) lines.push('Тема: ' + d.get('topic'));
        if (d.get('message')) lines.push('Сообщение: ' + d.get('message'));
        var wa = form.getAttribute('data-wa') || CONTACT.whatsapp;
        window.open('https://wa.me/' + wa + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
        setState('is-wa');
        return;
      }

      setState(null);
      submitBtn.disabled = true;
      submitBtn.textContent = 'Отправляем…';
      fetch(LEAD_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: d.get('name'), phone: d.get('phone'), topic: d.get('topic'),
          message: d.get('message'), website: d.get('website'),
          page: document.title + ' — ' + decodeURIComponent(location.pathname)
        })
      }).then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        setState('is-sent');
        form.reset();
      }).catch(function () {
        setState('is-error');
      }).then(function () {
        submitBtn.disabled = false;
        submitBtn.innerHTML = label;
      });
    });
  });

  /* Current year */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
