# SDT 单步骤路由

默认只选择一个模块。用户明确指定模块时尊重其选择。

| 用户当前要做的事 | 使用模块 | 最低输入 |
|---|---|---|
| 不知道从哪一步开始 | sdt | 当前目标或材料 |
| 建账号档案、分析调性 | sdt-account | 账号链接、截图或说明 |
| 查小红书账号、笔记、封面、数据 | sdt-research | 关键词或账号 |
| 找低粉爆款、筛对标 | sdt-benchmark | 候选样本或研究结果 |
| 分析为什么火 | sdt-spread | 一条完整内容或链接证据 |
| 想选题、跨赛道迁移 | sdt-topic | 账号简档与来源样本；纯发散可只给方向 |
| 把选题写成内容 | sdt-content | 已确认选题 |
| 做小红书标题 | sdt-xhs-title | 主题、正文或已有标题 |
| 做封面 | sdt-cover | 核心命题或正文 |
| 优化视频前五秒 | sdt-hook | 正文或完整内容结构 |
| 检查逐字稿是否顺 | sdt-script-flow | 逐字稿 |
| 检查能否打中受众 | sdt-resonate | 文稿与目标受众 |
| 检查 AI 味 | sdt-ai-check | 文稿 |
| 制作公众号 HTML | sdt-wechat-html | 定稿 Markdown |
| 保存和复用内容资产 | sdt-content-system | 本次生产材料或素材目录 |

## 路由边界

- “给我 10 个标题”直接用 sdt-xhs-title，不要求先做选题研究。
- “这个开头怎么样”直接用 sdt-hook，不自动重写全文。
- “这条为什么火”直接用 sdt-spread，不自动迁移选题。
- “给 Daisy 找 5 个选题”使用 sdt-topic；缺少真实账号信息时只补最关键的一项。
- “整套做完”才读取 pipeline.md 并执行完整生产。

