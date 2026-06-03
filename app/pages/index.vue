<script setup lang="ts">
const appStore = useAppStore()

const isMenuOpen = ref(false)
const isScrolled = ref(false)

const plainCardUi = {
  body: 'p-0 sm:p-0',
}

const deviceCards = [
  {
    title: '智能腕表 (Smart Watch)',
    description: '核心中枢，内置4G模组可独立通讯。支持动态血压、心率、血氧饱和度实时监测。',
    image: '/static/website2.ced50ef4f4ae.webp',
    alt: '智能腕表',
    features: ['无感采集体征数据', '任务提醒实时通知', 'AI智能问答交互'],
  },
  {
    title: '医疗级物联网外设',
    description: '实时监测，异常预警。集成智能血压计、血糖计、体重秤，自动同步数据至云端。',
    image: '/static/website3.36feca51c1a0.webp',
    alt: '医疗级物联网外设',
    features: ['上臂式医疗级精准测量', '筛查疾病风险监控 (体重)', '指夹式血氧饱和度监测'],
  },
]

const dtxItems = [
  {
    icon: '💊',
    title: '药物管理',
    points: ['个性化用药方案制定', '居家服药依从性提醒', '药品副作用监测与预警'],
  },
  {
    icon: '📈',
    title: '指标监测',
    points: ['血压、心率、血氧连续追踪', '运动步数与睡眠质量分析', '基线指标异常自动预警'],
  },
  {
    icon: '🗣️',
    title: '症状跟踪',
    points: ['气促、胸闷、咳嗽评估', '疼痛/疲倦风险评估', '疼痛量表定期随访评估'],
  },
  {
    icon: '📑',
    title: '复查解读',
    points: ['CT影像/生化报告解读', '根据指南调整复查计划', '肿瘤标志物趋势化分析'],
  },
  {
    icon: '🥗',
    title: '膳食营养',
    points: ['肺癌专病定制化食谱建议', '体重波动风险评估与干预', '营养健康宣教指导'],
  },
  {
    icon: '💪',
    title: '心理/运动',
    points: ['焦虑/抑郁量表定期评估', '术后肺功能康复运动指导', '情感关怀与陪伴交互'],
  },
]

function closeMenu() {
  isMenuOpen.value = false
}

function onScroll() {
  isScrolled.value = window.scrollY > 24
}

onMounted(() => {
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<template>
  <main>
    <nav class="site-nav" :class="{ 'site-nav--scrolled': isScrolled }" aria-label="主导航">
      <a class="site-logo" href="#home" aria-label="智医康科技首页" @click="closeMenu">
        <img src="/static/website1.41b7aa717623.webp" alt="智医康科技 Logo" height="40">
      </a>

      <UButton
        class="nav-toggle"
        type="button"
        variant="ghost"
        color="primary"
        :aria-expanded="isMenuOpen"
        aria-label="打开导航菜单"
        @click="isMenuOpen = !isMenuOpen"
      >
        <span />
        <span />
        <span />
      </UButton>

      <div class="nav-links" :class="{ 'nav-links--open': isMenuOpen }">
        <a
          v-for="item in appStore.navItems"
          :key="item.href"
          :href="item.href"
          @click="closeMenu"
        >
          {{ item.label }}
        </a>
      </div>
    </nav>

    <section id="home" class="hero-section">
      <div class="hero-copy">
        <h1>基于AI与智能硬件的<br>肺癌数字化康复管理</h1>
        <p>
          连接患者与医生的数字化桥梁。通过医疗级物联网硬件实现连续体征监测，
          将院外康复由“盲盒”状态转为精细化管理。
        </p>
        <UButton
          to="#carrier"
          class="primary-button"
          color="primary"
          variant="solid"
          label="了解详情"
        />
      </div>

      <div class="hero-visual" aria-hidden="true">
        <div class="orbit orbit--outer">
          <span class="orbit-node orbit-node--one" />
          <span class="orbit-node orbit-node--two" />
        </div>
        <div class="orbit orbit--inner">
          <span class="orbit-node orbit-node--three" />
          <span class="orbit-node orbit-node--four" />
        </div>
        <div class="ai-core">
          <UIcon name="i-lucide-flask-conical" class="flask-icon" />
        </div>
      </div>
    </section>

    <section id="carrier" class="section section--white">
      <div class="section-title">
        <h2>服务载体</h2>
        <p>由软/硬件系统驱动，构建居家康复数据基座</p>
      </div>

      <div class="carrier-grid">
        <UCard v-for="card in deviceCards" :key="card.title" class="carrier-card" :ui="plainCardUi">
          <h3>{{ card.title }}</h3>
          <p>{{ card.description }}</p>
          <div class="device-frame">
            <img :src="card.image" :alt="card.alt">
          </div>
          <ul>
            <li v-for="feature in card.features" :key="feature">
              <UIcon name="i-lucide-check" class="check-icon" />
              {{ feature }}
            </li>
          </ul>
        </UCard>
      </div>
    </section>

    <section id="dtx" class="section dtx-section">
      <div class="section-title">
        <h2>数字疗法内容</h2>
        <p>全方位的院外治、管、防闭环体系</p>
      </div>

      <div class="dtx-grid">
        <UCard v-for="item in dtxItems" :key="item.title" class="dtx-card" :ui="plainCardUi">
          <h3><span>{{ item.icon }}</span>{{ item.title }}</h3>
          <ul>
            <li v-for="point in item.points" :key="point">{{ point }}</li>
          </ul>
        </UCard>
      </div>
    </section>

    <section class="section platform-section">
      <span class="platform-glow" aria-hidden="true" />
      <div class="section-title">
        <h2>三端协同数字化平台</h2>
        <p>医生驾驶舱 + 患者端贴身管家</p>
      </div>

      <div class="platform-showcase">
        <div class="doctor-screen">
          <img src="/static/website4.4e6ad6832fe1.webp" alt="医生驾驶舱">
        </div>
        <div class="patient-screens">
          <img src="/static/website5.c387b17e79a5.webp" alt="健康档案患者端">
          <img src="/static/website6.921b7d7fd064.webp" alt="任务提醒患者端">
          <img src="/static/website7.f315ee86f362.webp" alt="诊疗记录患者端">
        </div>
      </div>
    </section>

    <UCard id="about" class="about-section" :ui="plainCardUi">
      <div class="section-title">
        <h2>关于智医康</h2>
        <p>连接生命，赋能健康</p>
      </div>
      <p class="about-copy">
        上海智医康科技有限公司是一家专注于慢病数字化疗法的前沿医疗科技企业。我们深度融合AI大模型能力与医疗级物联网硬件，
        通过结构化真实世界数据（RWD）赋能医生决策，提升患者生存质量与生存期。智医康创始团队由来自平安、哈佛、上海二军医的人工智能、
        医学、物联网专家组成，我们致力于帮助慢病患者科学康复，并坚持以循证医学为底座，助力“健康中国2030”建设。
      </p>
    </UCard>

    <footer class="site-footer">
      <p>
        © 2026 上海智医康科技有限公司 |
        <a href="https://beian.miit.gov.cn/" target="_blank" rel="noreferrer">沪ICP备2024092528号-4</a>
        |
        <a
          href="https://www.beian.gov.cn/portal/registerSystemInfo"
          target="_blank"
          rel="noreferrer"
        >
          沪公网安备31010402336532号
        </a>
      </p>
      <p>地址：上海市徐汇区东安路800弄25号502 | 邮箱：kefu@zencare.com | 电话：4006889982</p>
    </footer>
  </main>
</template>
