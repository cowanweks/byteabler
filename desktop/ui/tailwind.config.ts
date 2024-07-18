import type { Config } from "tailwindcss";


const config = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      screens: {
        'md': '780px'
      },
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
      fontFamily: {
        roboto: ['Roboto', 'sans-serif'],
      },
      gridTemplateAreas: {
        layout: [
          'header header',
          'sidebar content',
          'footer footer',
        ],
      },
    },
  },
  plugins: [require("tailwindcss-animate"),
  function ({ addUtilities }) {
    const newUtilities = {
      '#App': {
        'height': '100dvh',
        'display': 'grid',
        'grid-template-areas': `"sidebar header" "sidebar content" "sidebar footer"`,
        'grid-template-rows': '40px auto 30px',
        'grid-template-columns': '200px 1fr',
      },
      '#Header': {
        'grid-area': 'header',
      },
      '#SideBar': {
        'grid-area': 'sidebar',
      },
      '#Content': {
        'grid-area': 'content',
      },
      '#Footer': {
        'grid-area': 'footer',
      },
    };
    addUtilities(newUtilities, ['responsive', 'hover']);
  }
  ],
} satisfies Config

export default config