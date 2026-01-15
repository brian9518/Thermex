import { motion } from "framer-motion";
import { Star, Quote } from "lucide-react";

const reviews = [
  {
    name: "Азиз Каримов",
    location: "Ташкент",
    rating: 5,
    text: "Заказали Flat Diamond 80L для большой семьи. Качество отличное, доставили за 2 дня. Монтажники установили профессионально. Рекомендую!",
    date: "Декабрь 2024",
  },
  {
    name: "Малика Рахимова",
    location: "Самарканд",
    rating: 5,
    text: "Долго выбирали водонагреватель, консультанты помогли определиться. Взяли Champion 50L — идеально для квартиры. Уже год пользуемся без проблем.",
    date: "Ноябрь 2024",
  },
  {
    name: "Шухрат Юсупов",
    location: "Бухара",
    rating: 5,
    text: "Третий водонагреватель от Thermex! Ставили в квартиру родителям. Качество как всегда на высоте. Гарантийное обслуживание тоже радует.",
    date: "Октябрь 2024",
  },
];

export const ReviewsSection = () => {
  return (
    <section id="reviews" className="py-24 bg-background">
      <div className="container mx-auto px-6">
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="inline-block px-4 py-2 bg-copper/10 rounded-full text-copper text-sm font-medium mb-4">
            Отзывы клиентов
          </span>
          <h2 className="font-display text-4xl md:text-5xl font-bold text-foreground mb-4">
            Нам <span className="text-gradient-copper">доверяют</span> тысячи семей
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            Читайте реальные отзывы наших клиентов со всего Узбекистана
          </p>
        </motion.div>

        {/* Reviews Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {reviews.map((review, index) => (
            <motion.div
              key={review.name}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="bg-card rounded-2xl p-8 border border-border hover:shadow-elevated transition-all duration-300"
            >
              {/* Quote Icon */}
              <div className="w-10 h-10 rounded-full bg-copper/10 flex items-center justify-center mb-6">
                <Quote className="w-5 h-5 text-copper" />
              </div>

              {/* Rating */}
              <div className="flex gap-1 mb-4">
                {[...Array(review.rating)].map((_, i) => (
                  <Star key={i} className="w-5 h-5 fill-copper text-copper" />
                ))}
              </div>

              {/* Review Text */}
              <p className="text-foreground mb-6 leading-relaxed">
                "{review.text}"
              </p>

              {/* Reviewer Info */}
              <div className="flex items-center justify-between pt-4 border-t border-border">
                <div>
                  <p className="font-semibold text-foreground">{review.name}</p>
                  <p className="text-sm text-muted-foreground">{review.location}</p>
                </div>
                <span className="text-xs text-muted-foreground">{review.date}</span>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Stats */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.3 }}
          className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-6"
        >
          {[
            { value: "10,000+", label: "Клиентов" },
            { value: "4.9", label: "Средний рейтинг" },
            { value: "12", label: "Лет на рынке" },
            { value: "99%", label: "Довольных покупателей" },
          ].map((stat, index) => (
            <div key={index} className="text-center p-6 bg-muted rounded-xl">
              <p className="font-display text-3xl md:text-4xl font-bold text-copper mb-1">
                {stat.value}
              </p>
              <p className="text-sm text-muted-foreground">{stat.label}</p>
            </div>
          ))}
        </motion.div>
      </div>
    </section>
  );
};
