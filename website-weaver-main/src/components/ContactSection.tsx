import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Phone, MapPin, Clock, Send } from "lucide-react";
import { useState } from "react";
import { toast } from "sonner";

const contactInfo = [
  {
    icon: Phone,
    title: "Телефон",
    value: "+998 90 123 45 67",
    link: "tel:+998901234567",
  },
  {
    icon: MapPin,
    title: "Адрес шоурума",
    value: "г. Ташкент, ул. Навои, 100",
    link: "#",
  },
  {
    icon: Clock,
    title: "Режим работы",
    value: "Пн-Сб: 9:00 - 19:00",
    link: "#",
  },
];

export const ContactSection = () => {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    // Simulate form submission
    setTimeout(() => {
      toast.success("Заявка отправлена! Мы свяжемся с вами в ближайшее время.");
      setName("");
      setPhone("");
      setIsSubmitting(false);
    }, 1000);
  };

  return (
    <section id="contact" className="py-24 bg-primary">
      <div className="container mx-auto px-6">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <span className="inline-block px-4 py-2 bg-copper/20 rounded-full text-copper-light text-sm font-medium mb-4">
              Свяжитесь с нами
            </span>
            <h2 className="font-display text-4xl md:text-5xl font-bold text-cream mb-4">
              Получите <span className="text-gradient-copper">бесплатную</span> консультацию
            </h2>
            <p className="text-cream/70 text-lg mb-8">
              Оставьте заявку и наши специалисты помогут подобрать идеальный водонагреватель для ваших потребностей
            </p>

            {/* Contact Info */}
            <div className="space-y-4">
              {contactInfo.map((item, index) => (
                <motion.a
                  key={item.title}
                  href={item.link}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.4, delay: index * 0.1 }}
                  className="flex items-center gap-4 p-4 rounded-xl bg-cream/5 border border-cream/10 hover:bg-copper/10 hover:border-copper/30 transition-all duration-300"
                >
                  <div className="w-12 h-12 rounded-lg bg-gradient-copper flex items-center justify-center shrink-0">
                    <item.icon className="w-6 h-6 text-secondary-foreground" />
                  </div>
                  <div>
                    <p className="text-cream/60 text-sm">{item.title}</p>
                    <p className="text-cream font-medium">{item.value}</p>
                  </div>
                </motion.a>
              ))}
            </div>
          </motion.div>

          {/* Form */}
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <form
              onSubmit={handleSubmit}
              className="bg-card rounded-2xl p-8 shadow-elevated"
            >
              <h3 className="font-display text-2xl font-bold text-foreground mb-6">
                Заказать обратный звонок
              </h3>

              <div className="space-y-4 mb-6">
                <div>
                  <label htmlFor="name" className="block text-sm font-medium text-foreground mb-2">
                    Ваше имя
                  </label>
                  <Input
                    id="name"
                    type="text"
                    placeholder="Введите ваше имя"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                    className="h-12"
                  />
                </div>
                <div>
                  <label htmlFor="phone" className="block text-sm font-medium text-foreground mb-2">
                    Номер телефона
                  </label>
                  <Input
                    id="phone"
                    type="tel"
                    placeholder="+998 90 123 45 67"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                    required
                    className="h-12"
                  />
                </div>
              </div>

              <Button 
                type="submit" 
                variant="copper" 
                className="w-full h-12"
                disabled={isSubmitting}
              >
                {isSubmitting ? (
                  "Отправка..."
                ) : (
                  <>
                    Отправить заявку
                    <Send className="w-4 h-4" />
                  </>
                )}
              </Button>

              <p className="text-xs text-muted-foreground text-center mt-4">
                Нажимая кнопку, вы соглашаетесь с политикой конфиденциальности
              </p>
            </form>
          </motion.div>
        </div>
      </div>
    </section>
  );
};
