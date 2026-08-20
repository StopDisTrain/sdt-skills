---
name: sdt-xhs-title
description: "根据主题、正文或已有标题生成并筛选小红书标题，提供改写和 A/B 方案，同时检查账号调性、真实性以及正文能否兑现标题承诺。用户要起标题、改标题、套用标题模式或检查标题时使用。 English: Generate and filter Xiaohongshu titles from a topic, draft, or existing title, offering rewrites and A/B options while checking voice, truthfulness, and whether the content fulfills the promise. Use to write, improve, pattern-match, or review titles."
---

# SDT 小红书标题

从 SDT 自有标题模式库选择可追溯结构，再按账号调性、正文承诺和事实边界过滤。

## 前置门

单独调用最低只需要一个主题、正文或已有标题。材料较少时直接生成轻量候选并写明假设，不强制用户先跑完整生产。

## 工作流

1. 从输入提取话题、目标受众、真实素材和希望触发的反应；缺少受众时基于上下文做一个可撤销假设。
2. 读取 references/title-patterns.md，选择跨至少 3 种触发器的模式。
3. 先生成 10 个候选，每个标注 SDT 模式编号。
4. 使用 scripts/validate_titles.py 检查长度。
5. 过滤每个候选：
   - 不超过 20 个字符，标点计入
   - 不提前说完整答案
   - 正文能够兑现
   - 数字、身份和结果真实
   - 与账号语气匹配
6. 交付 Top 3，并分别标注点击假设、风险和适配场景。

## 规则

- 必须保留 SDT 模式编号。
- “扩大话题”不能扩大成与正文无关的人群承诺。
- 不用制造健康、财富或结果焦虑来换点击。
- 标题不是爆款结论，只是待发布假设。

## 单项输出

用户只要标题时，直接输出：

- 主题与受众假设
- 10 个标题及模式编号
- Top 3 与选择理由
- 长度和兑现风险

不要自动生成正文、封面或开头。
