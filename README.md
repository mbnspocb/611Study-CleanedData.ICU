# 611Study.ICU

## 全国超时学习学校耻辱名单的镜像方案

让全国超时学习学校耻辱名单可以在国内访问，让全国超时学习学校耻辱名单传遍国内平台。你可以通过部署本项目并绑定自己的域名，快速搭建一个国内可访问的镜像站点。

## 特性

- 🔄 **数据自动更新:** 每1天自动从 Google Sheets 同步更新数据，无需手动维护。
- 📱 **移动端友好:** 响应式设计，在各种设备上都能获得良好的浏览体验。
- 🌐 **易于部署:** 支持一键部署到 Vercel、Netlify 等平台，无需复杂的配置。
- 🔍 **信息完整展示:** 完整展示学校超时学习相关信息，方便用户查阅。

## 快速部署你自己的镜像站点

### Vercel 部署

1. **Fork 本仓库**：点击页面右上角的 "Fork" 按钮。
2. **注册 Vercel 账号**：访问 [Vercel](https://vercel.com) 并注册账号。
3. **导入仓库**：在 Vercel 中选择 "Add New Project"，导入你 fork 的仓库。
4. **完成部署**：按照 Vercel 的指引完成部署。部署完成后，你可以绑定自己的域名。

### Netlify 部署

1. **Fork 本仓库**：点击页面右上角的 "Fork" 按钮。
2. **注册 Netlify 账号**：访问 [Netlify](https://netlify.com) 并注册账号。
3. **创建站点**：在 Netlify 中点击 "New site from Git"，选择你 fork 的仓库。
4. **完成部署**：按照 Netlify 的指引完成部署。部署完成后，你可以绑定自己的域名。

## 数据来源与更新

本项目的数据来源于 [Google Sheets](https://docs.google.com/spreadsheets/d/1P48quxwMv9XsYQhXjLOvTRRq8tt3ahJnkbXo4VCxjLc/edit?gid=1615412834)。

为了保证数据的及时性，项目通过 GitHub Action 自动同步更新数据，**每 30 分钟** 从 Google Sheets 获取最新内容。

## 数据更新与自定义 (可选)

直接 fork 本项目，你将**无法自动同步数据**。如果你希望更频繁地更新数据，或者进行更高级的自定义，可以参考以下方案：

**方案一：使用 Pull App 自动同步 (推荐)**

这是最简单的更新方式，推荐给希望保持数据同步，但不想进行复杂配置的用户。

1. **安装 Pull App:**  访问 [Pull](https://github.com/apps/pull) 并安装到你的 fork 仓库。
2. **Pull App 将自动同步:** Pull App 会自动检测上游仓库的更新，并同步到你的仓库。

**方案二：启用 GitHub Actions**

如果你希望完全掌控数据更新，可以启用 GitHub Actions：

1. **转到仓库的 Settings > Actions > General**
2. **确保 "Workflow permissions" 设置为 "Read and write permissions"**
3. **在 Actions 标签页中启用 Workflows**

配置完成后，GitHub Actions 将会每30分钟自动更新数据。

## License

[Anti 996](LICENSE)
