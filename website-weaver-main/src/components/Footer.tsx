import { motion } from "framer-motion";

export const Footer = () => {
  return (
    <footer className="bg-foreground py-12">
      <div className="container mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="flex flex-col md:flex-row items-center justify-between gap-6"
        >
          {/* Logo */}
          <a href="#" className="flex items-center gap-2">
            <div className="w-10 h-10 rounded-full bg-gradient-copper flex items-center justify-center">
              <span className="text-secondary-foreground font-display font-bold text-lg">T</span>
            </div>
            <span className="text-cream font-display text-xl font-semibold tracking-wide">
              Thermex
            </span>
          </a>

          {/* Links */}
          <div className="flex flex-wrap items-center justify-center gap-6">
            <a href="#products" className="text-cream/60 hover:text-cream transition-colors text-sm">
              Каталог
            </a>
            <a href="#advantages" className="text-cream/60 hover:text-cream transition-colors text-sm">
              Преимущества
            </a>
            <a href="#reviews" className="text-cream/60 hover:text-cream transition-colors text-sm">
              Отзывы
            </a>
            <a href="#contact" className="text-cream/60 hover:text-cream transition-colors text-sm">
              Контакты
            </a>
          </div>

          {/* Copyright */}
          <p className="text-cream/40 text-sm">
            © 2025 Thermex Uzbekistan. Все права защищены.
          </p>
        </motion.div>
      </div>
    </footer>
  );
};
