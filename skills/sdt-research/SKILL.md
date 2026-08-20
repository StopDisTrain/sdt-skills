---
name: sdt-research
description: "只读检索小红书公开内容，并把账号数据、标题、封面、互动量、作者近期内容和低粉爆款整理成可追溯证据。用户要求查公开账号或笔记数据时使用；不得点赞、收藏、评论、发布、删除或导出登录凭证。 English: Read-only research for public Xiaohongshu content, collecting traceable evidence such as account data, titles, covers, engagement, recent posts, and low-follower breakout examples. Use for public account or post research; never like, save, comment, publish, delete, or export credentials."
---

# SDT 内容检索

把小红书检索结果规范成后续可计算、可回溯的证据。优先使用 Redbook CLI；未安装时只报告依赖缺失，不伪造结果。

## 安全边界

只允许以下 Redbook 操作：

- whoami
- search
- user
- user-posts
- read
- comments
- analyze-viral
- viral-template
- topics

禁止 post、comment、reply、batch-reply、like、collect、uncollect、delete、auth export、auth save。

详细内容读取必须顺序执行并保持人工节奏。遇到验证码、NeedVerify、会话过期、IP 限制或重复空响应时立即停止，不自动重试，不保存 cookie、xsec_token 或其他登录材料。

## 工作流

1. 明确检索目的、关键词、时间范围和目标账号。
2. 运行 scripts/redbook_readonly.py；先做搜索列表，再按需要顺序读取详情。
3. 保存每条样本的来源链接、作者、作者粉丝、发布日期、标题、封面地址和可见互动。
4. 对视频样本检查可见点赞；只有点赞数大于等于 3,000 的视频才可标记为“正式对标候选”，其余最多作为“灵感样本”。
5. 获取作者近期内容，用中位点赞计算相对爆发倍数。
6. 无法获得粉丝或基线时，将样本标为“数据不完整”，不得宣称低粉爆款。
7. 输出研究证据表，不直接生成选题。

## 证据字段

读 references/evidence-schema.md。至少保留 sample_id、query、lane、source_url、author、followers、published_at、title、cover_url、likes、collects、comments、recent_median_likes、viral_multiplier、captured_at 和 limitations。

## 可见性声明

平台指标会变化，交付时写明采集时间。封面 URL 只作为研究证据；下载、复制或再发布图片前另行确认版权与用途。
