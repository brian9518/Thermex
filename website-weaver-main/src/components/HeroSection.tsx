import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { ArrowRight, Shield, Zap, Thermometer } from "lucide-react";
import heroProduct from "@/assets/hero-product.png";

const features = [
  { icon: Shield, text: "Гарантия 5 лет" },
  { icon: Zap, text: "Быстрый нагрев" },
  { icon: Thermometer, text: "Точный контроль" },
];

export const HeroSection = () => {
  return (
    <section className="relative min-h-screen bg-gradient-hero overflow-hidden">
      {/* Background decorative elements */}
      <div className="absolute inset-0">
        <div className="absolute top-1/4 -left-32 w-96 h-96 bg-copper/10 rounded-full blur-3xl" />
        <div className="absolute bottom-1/4 -right-32 w-96 h-96 bg-copper/5 rounded-full blur-3xl" />
      </div>

      <div className="container mx-auto px-6 pt-32 pb-20 relative z-10">
        <div className="grid lg:grid-cols-2 gap-12 items-center min-h-[80vh]">
          {/* Text Content */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            className="text-cream"
          >
            <motion.span
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2, duration: 0.6 }}
              className="inline-block px-4 py-2 bg-copper/20 rounded-full text-copper-light text-sm font-medium mb-6"
            >
              Официальный дилер в Узбекистане
            </motion.span>

            <motion.h1
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3, duration: 0.6 }}
              className="font-display text-5xl md:text-6xl lg:text-7xl font-bold leading-tight mb-6"
            >
              Премиальные
              <span className="text-gradient-copper block">водонагреватели</span>
              для вашего дома
            </motion.h1>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4, duration: 0.6 }}
              className="text-cream/70 text-lg md:text-xl mb-8 max-w-lg"
            >
              Европейское качество и инновационные технологии. 
              Более 10 000 довольных клиентов по всему Узбекистану.
            </motion.p>

            {/* CTA Buttons */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.5, duration: 0.6 }}
              className="flex flex-wrap gap-4 mb-12"
            >
              <Button variant="hero">
                Подобрать модель
                <ArrowRight className="w-5 h-5" />
              </Button>
              <Button variant="hero-outline">
                Бесплатная консультация
              </Button>
            </motion.div>

            {/* Feature Pills */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.6, duration: 0.6 }}
              className="flex flex-wrap gap-4"
            >
              {features.map((feature, index) => (
                <div
                  key={index}
                  className="flex items-center gap-2 px-4 py-2 bg-cream/5 rounded-full border border-cream/10"
                >
                  <feature.icon className="w-4 h-4 text-copper" />
                  <span className="text-cream/80 text-sm">{feature.text}</span>
                </div>
              ))}
            </motion.div>
          </motion.div>

          {/* Product Image */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1, delay: 0.3 }}
            className="relative flex items-center justify-center"
          >
            <div className="absolute inset-0 bg-gradient-radial from-copper/20 via-transparent to-transparent rounded-full blur-2xl" />
            <motion.img
              src={heroProduct}
              alt="Thermex Premium Water Heater"
              className="relative z-10 w-full max-w-lg animate-float drop-shadow-2xl"
              whileHover={{ scale: 1.02 }}
              transition={{ duration: 0.3 }}
            />
            
            {/* Floating Stats */}
            <motion.div
              initial={{ opacity: 0, x: 50 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.8, duration: 0.6 }}
              className="absolute -right-4 top-1/4 bg-card/90 backdrop-blur-sm rounded-xl p-4 shadow-elevated"
            >
              <p className="text-3xl font-display font-bold text-copper">10K+</p>
              <p className="text-sm text-muted-foreground">Довольных клиентов</p>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: -50 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 1, duration: 0.6 }}
              className="absolute -left-4 bottom-1/4 bg-card/90 backdrop-blur-sm rounded-xl p-4 shadow-elevated"
            >
              <p className="text-3xl font-display font-bold text-copper">5 лет</p>
              <p className="text-sm text-muted-foreground">Гарантия качества</p>
            </motion.div>
          </motion.div>
        </div>
      </div>

      {/* Scroll indicator */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.2, duration: 0.6 }}
        className="absolute bottom-8 left-1/2 -translate-x-1/2"
      >
        <div className="w-6 h-10 border-2 border-cream/30 rounded-full flex justify-center pt-2">
          <motion.div
            animate={{ y: [0, 12, 0] }}
            transition={{ repeat: Infinity, duration: 1.5 }}
            className="w-1.5 h-1.5 bg-cream rounded-full"
          />
        </div>
      </motion.div>
    </section>
  );
};
