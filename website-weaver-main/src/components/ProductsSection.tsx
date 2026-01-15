import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { ArrowRight, Check } from "lucide-react";

const products = [
  {
    name: "Champion",
    capacity: "50-100L",
    description: "Классическая модель для небольших семей",
    price: "от 2 500 000",
    features: ["Нержавеющий бак", "Эко-режим", "LED дисплей"],
    popular: false,
  },
  {
    name: "Flat Diamond",
    capacity: "30-80L",
    description: "Ультраплоский дизайн для современного интерьера",
    price: "от 3 800 000",
    features: ["Плоский корпус", "Wi-Fi управление", "Сенсорное управление", "Таймер"],
    popular: true,
  },
  {
    name: "Sprint",
    capacity: "80-150L",
    description: "Максимальная производительность для больших семей",
    price: "от 4 500 000",
    features: ["Двойной ТЭН", "Быстрый нагрев", "Увеличенный объём", "Антибактериальное покрытие"],
    popular: false,
  },
];

export const ProductsSection = () => {
  return (
    <section id="products" className="py-24 bg-background">
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
            Каталог продукции
          </span>
          <h2 className="font-display text-4xl md:text-5xl font-bold text-foreground mb-4">
            Найдите свой <span className="text-gradient-copper">идеальный</span> водонагреватель
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            Широкий ассортимент моделей для любых потребностей и бюджета
          </p>
        </motion.div>

        {/* Products Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {products.map((product, index) => (
            <motion.div
              key={product.name}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className={`relative bg-card rounded-2xl p-8 border transition-all duration-300 hover:shadow-elevated hover:-translate-y-1 ${
                product.popular 
                  ? "border-copper shadow-copper" 
                  : "border-border"
              }`}
            >
              {product.popular && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                  <span className="bg-gradient-copper text-secondary-foreground text-xs font-semibold px-4 py-1 rounded-full">
                    Популярный выбор
                  </span>
                </div>
              )}

              <div className="mb-6">
                <h3 className="font-display text-2xl font-bold text-foreground mb-1">
                  {product.name}
                </h3>
                <p className="text-copper font-medium">{product.capacity}</p>
              </div>

              <p className="text-muted-foreground mb-6">{product.description}</p>

              <ul className="space-y-3 mb-8">
                {product.features.map((feature, i) => (
                  <li key={i} className="flex items-center gap-3">
                    <div className="w-5 h-5 rounded-full bg-copper/10 flex items-center justify-center">
                      <Check className="w-3 h-3 text-copper" />
                    </div>
                    <span className="text-foreground text-sm">{feature}</span>
                  </li>
                ))}
              </ul>

              <div className="border-t border-border pt-6">
                <p className="text-sm text-muted-foreground mb-2">Цена</p>
                <p className="text-2xl font-display font-bold text-foreground mb-4">
                  {product.price} <span className="text-sm font-normal text-muted-foreground">сум</span>
                </p>
                <Button 
                  variant={product.popular ? "copper" : "outline"} 
                  className="w-full"
                >
                  Подробнее
                  <ArrowRight className="w-4 h-4" />
                </Button>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};
