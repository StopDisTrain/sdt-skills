---
name: sdt-ai-check
description: "检查文稿里的 AI 味和账号语气偏差，包括机器化表达、翻译腔、虚构脆弱感和过度金句。用户问文案是否像 AI 写的、是否像本人说话，或希望降低 AI 痕迹时使用。 English: Check drafts for AI-writing signals and voice mismatch, including robotic phrasing, translation-like prose, fabricated vulnerability, and forced quotable lines. Use when the user wants the copy to sound more human or more like the target account."
---

# SDT AI 痕迹质检

使用 SDT 自有识别清单检查机器化写作特征。默认只报告；完整 SDT 生产模式可依据账号档案和已核实原话做有限修复。

## 工作流

1. 先识别体裁，读取 references/ai-signals.md 并应用其中的误伤规则。
2. 按文本顺序引用命中位置并标严重度。
3. 另做账号语气比对：常用句长、口头词、确定程度、幽默方式、禁用表达。
4. 只修复强信号和明显语气偏差；保留人的重复、犹豫和毛边。
5. 任何修复不得新增事实、经历、结果或情绪细节。

## 完整生产模式的修复依据

优先级：

1. 账号本人真实口播或历史文稿
2. sdt-account 已验证语气特征
3. 用户本轮明确偏好
4. 通用口语规则

没有个人语料时，只做低幅度清理，不宣称“像本人”。

## 单项输出

用户只要求检查时，按原文顺序引用命中位置，标记强、中、弱信号，最后总结最突出的一类问题。不要自动重写全文。
