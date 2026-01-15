import { motion } from "framer-motion";
import { Shield, Truck, Wrench, Award, Clock, Headphones } from "lucide-react";

const advantages = [
  {
    icon: Shield,
    title: "Гарантия 5 лет",
    description: "Официальная гарантия от производителя на все модели водонагревателей",
  },
  {
    icon: Truck,
    title: "Бесплатная доставка",
    description: "Доставим в любую точку Узбекистана в течение 1-3 рабочих дней",
  },
  {
    icon: Wrench,
    title: "Профессиональный монтаж",
    description: "Установка и подключение сертифицированными специалистами",
  },
  {
    icon: Award,
    title: "Европейское качество",
    description: "Продукция соответствует международным стандартам ISO и CE",
  },
  {
    icon: Clock,
    title: "Быстрый нагрев воды",
    description: "Инновационные ТЭНы нагревают воду на 30% быстрее аналогов",
  },
  {
    icon: Headphones,
    title: "Поддержка 24/7",
    description: "Круглосуточная техническая поддержка и консультации",
  },
];

export const AdvantagesSection = () => {
  return (
    <section id="advantages" className="py-24 bg-primary">
      <div className="container mx-auto px-6">
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="inline-block px-4 py-2 bg-copper/20 rounded-full text-copper-light text-sm font-medium mb-4">
            Почему выбирают нас
          </span>
          <h2 className="font-display text-4xl md:text-5xl font-bold text-cream mb-4">
            6 причин <span className="text-gradient-copper">доверять</span> нам
          </h2>
          <p className="text-cream/70 text-lg max-w-2xl mx-auto">
            Мы не просто продаём водонагреватели — мы обеспечиваем комфорт вашего дома
          </p>
        </motion.div>

        {/* Advantages Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {advantages.map((advantage, index) => (
            <motion.div
              key={advantage.title}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="group p-8 rounded-2xl bg-cream/5 border border-cream/10 hover:bg-copper/10 hover:border-copper/30 transition-all duration-300"
            >
              <div className="w-14 h-14 rounded-xl bg-gradient-copper flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                <advantage.icon className="w-7 h-7 text-secondary-foreground" />
              </div>
              <h3 className="font-display text-xl font-bold text-cream mb-3">
                {advantage.title}
              </h3>
              <p className="text-cream/60">
                {advantage.description}
              </p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};
