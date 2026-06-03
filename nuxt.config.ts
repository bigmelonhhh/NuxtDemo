export default defineNuxtConfig({
  compatibilityDate: '2026-06-03',
  devtools: { enabled: false },
  modules: ['@pinia/nuxt', '@nuxt/eslint', '@nuxt/ui'],
  css: ['~/assets/styles/main.css'],
  app: {
    head: {
      htmlAttrs: {
        lang: 'zh-CN',
      },
      title: '智医康 - 基于AI与智能硬件的肺癌数字化康复管理',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            '智医康通过AI与医疗级物联网硬件，为肺癌患者提供院外数字化康复管理。',
        },
        { name: 'theme-color', content: '#f0fdfa' },
      ],
    },
  },
  runtimeConfig: {
    public: {
      apiBase: '',
    },
  },
})
