/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../hir_backend/templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
  // purge: {
  //   enabled: true,
  //   content: ['../hir_backend/templates/**/*.html'],
  // },
}

