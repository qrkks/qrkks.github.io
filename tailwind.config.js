const typography = require('@tailwindcss/typography');
const forms = require('@tailwindcss/forms');


module.exports = {
    content: [
      './**/projects/themes/simple/**/*.html',
    ],
    // darkMode: media, // or 'media' or 'class'
    theme: {
      extend: {},
    },
    variants: {
      extend: {},
    },
    plugins: [
        typography,
        forms,
    ],
  }
  