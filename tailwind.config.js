const typography = require('@tailwindcss/typography');
const forms = require('@tailwindcss/forms');


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
        }
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
  