---
name: sdt-cover
description: "为已经确定的小红书内容设计封面文字和画面布局，包括关键词、人物与场景位置以及 A/B 方案。用户要做小红书封面、参考爆款封面，或检查封面是否符合账号视觉调性时使用。 English: Design cover copy and visual composition for an approved Xiaohongshu post, including keywords, subject placement, scenes, and A/B options. Use to create or review a cover against successful examples and the account's visual style."
---

# SDT 小红书封面

根据选题机制、目标账号视觉档案和已验证样本设计封面，不复制原图和受版权保护的独特构图。

## 工作流

1. 读取 sdt-account 的视觉线索、sdt-topic 的核心张力和 sdt-research 的封面证据。
2. 区分标题职责与封面职责：两者互补，不重复说完整答案。
3. 生成三类方案：
   - 人物情绪主导
   - 空间或产品场景主导
   - 大字信息主导
4. 每类写明主文案、副文案、主体、背景、构图、色彩、字体感觉和裁切安全区。
5. 为最强的两个方案写 A/B 测试假设。

## 规则

- 封面主文案尽量一眼读完，不堆砌三层信息。
- 不用未核实数字、虚假前后对比或夸张功效。
- 品牌调性不能牺牲可读性；“高级感”必须落到留白、色彩、材质、镜头和字体等可执行要素。
- 如果用户要求实际生成封面图片，转用图像生成能力，并把本技能的方案作为提示基础。

## 输出

使用 assets/cover-brief.md。附上参考样本链接与“借鉴的是哪一层机制”，避免只给形容词。
