export const useAppStore = defineStore('app', () => {
  const siteName = ref('智医康科技')
  const navItems = readonly([
    { label: '首页', href: '#home' },
    { label: '服务载体', href: '#carrier' },
    { label: '数字疗法', href: '#dtx' },
    { label: '关于我们', href: '#about' },
  ])

  return {
    siteName,
    navItems,
  }
})
