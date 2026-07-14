# Nuxt 项目 AGENTS.md 设计规格

## 目标

在仓库根目录创建一份面向 Codex 及其他代码代理的 `AGENTS.md`。文档需要同时体现专业前端工程实践与代理式开发约束，让代理能够快速理解当前项目、在正确目录内修改代码，并以可复现的证据完成验证和交付。

## 适用范围

- 规则覆盖整个仓库，除非未来子目录增加更具体的 `AGENTS.md`。
- 内容必须基于当前仓库的真实技术栈和脚本，不编造尚未存在的基础设施。
- 本次只新增仓库级开发规范，不修改应用代码、依赖或现有文档。

## 项目事实

- Nuxt 4.4.7，使用 Nuxt 4 的 `app/` 源码目录结构。
- Vue 3.5、TypeScript、Pinia、Nuxt UI 4、Tailwind CSS 4。
- `app/app.vue` 使用 `UApp`、`NuxtLayout` 和 `NuxtPage` 组成根结构。
- 客户端代码位于 `app/`，Nitro API 位于 `server/`，原样公开的资源位于 `public/`。
- `app/composables/useApi.ts` 是现有 SSR 友好型 API 请求封装。
- 现有检查包括 ESLint、Nuxt 生产构建和两个 Python/Playwright 验证脚本。

## 文档结构

目标 `AGENTS.md` 使用一份完整但便于扫描的仓库级规范，包含以下部分：

1. 项目定位、技术栈和指令作用域。
2. 修改原则与代理工作流。
3. Nuxt 4 目录、组件和架构边界。
4. Vue、TypeScript、SSR、数据获取及 Pinia 规范。
5. Nuxt UI、Tailwind CSS 4、视觉一致性、响应式及可访问性规范。
6. Nitro API、Runtime Config 和安全边界。
7. CodeGraph、`rg`、文件读取和调试工具的选择规则。
8. 按改动类型划分的验证矩阵。
9. 完成定义、交付报告格式和明确禁止事项。
10. Nuxt 官方参考链接。

## 核心规则

### 修改与架构

- 先读取真实入口和相邻实现，再做最小范围修改；不进行无关重构。
- 遵守 Nuxt 4 目录约定：应用代码放在 `app/`，服务端代码放在 `server/`，静态文件放在 `public/`。
- 不手工编辑 `.nuxt/`、`.output/`、`node_modules/` 或测试输出。
- 页面、布局、组件、组合式函数和 Store 各自承担单一职责；重复界面模式才提取组件。

### Vue、Nuxt 与数据

- 新增 Vue 组件默认使用 `<script setup lang="ts">` 和 Composition API。
- 保持 SSR 安全，浏览器专属 API 必须限制在客户端生命周期或 `import.meta.client` 分支。
- SSR 页面数据优先使用 `useFetch`、`useAsyncData` 或现有 `useApi`；用户事件触发的一次性请求使用 `$fetch`。
- 页面局部状态保留在组件或 composable，只有跨页面或跨组件共享状态才进入 Pinia。
- 公共配置使用 `runtimeConfig.public`，密钥只能存在于服务端私有 runtime config。

### UI 与体验

- 优先复用 Nuxt UI 组件和当前设计令牌，不重复实现已有基础组件。
- Tailwind CSS 4 采用 CSS-first 配置，不引入旧式 `tailwind.config.js`，除非需求明确要求。
- 保持当前医疗科技风格、中文界面和桌面/移动端响应式行为。
- 所有交互必须具备清晰的加载、空、错误和禁用状态；满足语义 HTML、键盘操作、焦点可见性和图片替代文本要求。

### Codex 工作方式

- 结构性查询优先使用 CodeGraph；字面文本和日志搜索使用 `rg`；CodeGraph 不可用时再使用本地只读搜索。
- 遇到故障时先复现、读取完整错误和定位根因，确认后再修改。
- 保留用户已有修改，不覆盖、不清理与任务无关的工作区状态。
- 不声称未实际运行的检查通过；交付时区分已验证、未验证和环境阻塞。

## 验证设计

验证应与改动风险匹配：

| 改动类型 | 最低验证 |
|---|---|
| 纯文档 | 检查 diff、链接、命令和仓库事实 |
| Vue、TypeScript、样式 | `npm run lint` + `npm run build` |
| 首页视觉或交互 | 上述检查 + 启动开发服务器 + `python scripts/verify_homepage.py` |
| Nuxt UI 集成 | 上述相关检查 + `python scripts/verify_nuxt_ui.py` |
| Nitro API | `npm run lint` + `npm run build` + 实际请求对应端点 |
| 依赖或 Nuxt 配置 | `npm run lint` + `npm run build`，并检查 lockfile 和启动日志 |

运行 Playwright 脚本前必须确认开发服务可访问，并满足脚本所需的 Python、Playwright 和 Chromium 环境。若环境不具备条件，应如实记录而不是跳过后宣称通过。

## 完成标准

- 根目录 `AGENTS.md` 能让首次进入仓库的代码代理定位入口、选择正确目录并执行对应验证。
- 规则具体、可操作，与当前仓库保持一致，没有模板化空话或未定义的命令。
- 文档清楚区分强制要求、按需建议和禁止事项。
- 不包含占位符、互相矛盾的规则或未经确认的架构假设。

## 官方依据

- [Nuxt 4 目录结构](https://nuxt.com/docs/4.x/directory-structure/)
- [Nuxt `useFetch`](https://nuxt.com/docs/4.x/api/composables/use-fetch)
- [Nuxt Runtime Config](https://nuxt.com/docs/4.x/guide/going-further/runtime-config)
