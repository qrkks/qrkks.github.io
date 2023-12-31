const typography = require('@tailwindcss/typography');
const forms = require('@tailwindcss/forms');
const colors = require('tailwindcss/colors');


module.exports = {
  content: [
    './**/themes/simple/**/*.html',
  ],
  // darkMode: media, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        sans: ['Arial', 'Helvetica', 'sans'],
        serif: ['Georgia', 'serif'],
        mono: ['Courier', 'monospace'],
        'noto-sans-sc': ['Noto Sans SC', 'sans'],
        // nunito: ['Nunito'],
        // montserrat: ['Montserrat'],
        // ubuntu: ['Ubuntu'],
      },
      typography: {
        DEFAULT: {
          css: {
            a: {
              textDecoration: 'none', // 移除下划线
              color: colors.sky[500],       // 设置链接颜色
              '&:hover': {
                textDecoration: 'underline', // 悬停时添加下划线
              },
            },
          },
        },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [
    typography,
    forms,
  ],
}
