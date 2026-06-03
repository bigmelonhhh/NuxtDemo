# Nuxt Vue Project

基于 Nuxt 4 最新稳定版搭建的前端项目基线，当前首页复刻 `https://zencare.imht.site/` 的官网视觉效果。

## 技术栈

### 核心框架

| 依赖 | 版本 | 说明 |
|---|---|---|
| Nuxt | 4.4.7 | 全栈 Vue 框架（Nuxt 4，采用 `app/` 目录结构）|
| Vue | 3.5.35 | 渐进式 JavaScript 框架 |
| TypeScript | 5.9.3 | 类型安全的 JavaScript 超集 |
| Vue Router | 5.1.0 | Vue 官方路由（Nuxt 内置） |

### 状态管理

| 依赖 | 版本 | 说明 |
|---|---|---|
| Pinia | 3.0.4 | Vue 3 官方状态管理库 |
| @pinia/nuxt | 0.11.3 | Pinia 的 Nuxt 模块集成 |

### UI 框架

| 依赖 | 版本 | 说明 |
|---|---|---|
| @nuxt/ui | 4.8.1 | Nuxt 官方 UI 组件库，基于 Tailwind CSS + Reka UI |
| Tailwind CSS | 4.3.0 | 原子化 CSS 框架（v4，CSS-first 配置方式） |

### 开发工具

| 依赖 | 版本 | 说明 |
|---|---|---|
| @nuxt/eslint | 1.15.2 | Nuxt 集成的 ESLint 配置 |
| ESLint | 10.4.1 | JavaScript/TypeScript 代码检查 |
| Prettier | 3.8.3 | 代码格式化工具 |
| vue-tsc | 3.1.5 | Vue TypeScript 类型检查 CLI |

## 项目结构

```
.
├── app/                        # Nuxt 4 应用目录
│   ├── app.vue                 # 根组件（UApp + NuxtLayout + NuxtPage）
│   ├── assets/
│   │   └── styles/
│   │       └── main.css        # 全局样式（Tailwind CSS + Nuxt UI + 自定义）
│   ├── composables/
│   │   └── useApi.ts           # API 请求封装（基于 useFetch + runtimeConfig）
│   ├── layouts/
│   │   └── default.vue         # 默认布局
│   ├── pages/
│   │   └── index.vue           # 首页（官网落地页）
│   └── stores/
│       └── app.ts              # 全局状态（站点名称、导航菜单）
├── public/
│   └── static/                 # 静态资源（WebP 图片）
├── server/
│   └── api/
│       └── health.get.ts       # 健康检查 API
├── scripts/
│   ├── verify_homepage.py      # 首页验证脚本
│   └── verify_nuxt_ui.py       # Nuxt UI 组件验证脚本
├── nuxt.config.ts              # Nuxt 配置
├── eslint.config.mjs           # ESLint 配置
├── package.json
└── .env.example                # 环境变量模板
```

## 已安装的 Nuxt 模块

```ts
// nuxt.config.ts
modules: ['@pinia/nuxt', '@nuxt/eslint', '@nuxt/ui']
```

| 模块 | 功能 |
|---|---|
| `@pinia/nuxt` | Pinia 状态管理自动导入与 SSR 支持 |
| `@nuxt/eslint` | ESLint 开箱即用的 Nuxt 预设规则 |
| `@nuxt/ui` | 组件库（UButton, UCard, UIcon 等）+ Tailwind CSS |

## 核心功能

### 首页组件（index.vue）

- **响应式导航栏** — 固定顶部，滚动时背景加深，移动端汉堡菜单
- **Hero 区域** — 渐变背景 + CSS 动画轨道节点，标语展示
- **服务载体卡片** — 使用 `UCard` 展示智能腕表与物联网外设
- **数字疗法网格** — 6 大服务模块（药物管理、指标监测、症状跟踪、复查解读、膳食营养、心理/运动）
- **三端协同展示** — 医生驾驶舱 + 患者端界面截图
- **关于我们** — 企业介绍
- **页脚** — ICP 备案信息

### Composable

- `useApi<T>(path, options)` — 基于 `useFetch` 的请求封装，自动注入 `runtimeConfig.public.apiBase`

### Pinia Store

- `useAppStore` — 管理站点名称与导航菜单项

### API

- `GET /api/health` — 返回 `{ ok: true, service: "nuxt-vue-project" }`

## 开发命令

```bash
npm install        # 安装依赖
npm run dev        # 启动开发服务器（http://localhost:3000）
npm run build      # 生产构建
npm run generate   # 静态站点生成
npm run preview    # 预览生产构建
npm run lint       # ESLint 代码检查
npm run format     # Prettier 代码格式化
```

## 环境变量

复制 `.env.example` 为 `.env` 并按需修改：

```bash
NUXT_PUBLIC_API_BASE=https://your-api-server.com  # API 服务地址
```

## 首页预览

开发服务默认运行在 `http://localhost:3000`，首页复刻智医康官网视觉设计，包含：

- 🧬 AI 核心动画轨道
- 📱 智能硬件展示卡片
- 🏥 六大数字疗法模块
- 💻 多端协同平台展示
- 📋 企业信息与备案
