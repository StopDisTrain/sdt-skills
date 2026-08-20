---
name: sdt-benchmark
description: "从公开内容中筛选真正值得学习、能够迁移的对标样本，并排除名人效应、粉丝体量和独特资源造成的假象。用户要找低粉爆款、垂直对标、邻近受众样本或跨赛道灵感时使用。 English: Find public benchmark content that is genuinely learnable and transferable while filtering out celebrity effects, follower-size bias, and unique-resource noise. Use for low-follower breakout posts, niche benchmarks, adjacent audiences, or cross-category inspiration."
---

# SDT 对标筛选

同时检查“是否看懂、是否可模仿、主体差异是否构成噪音”和单条内容的相对爆发证据。账号商业对标与单条内容对标使用不同标准，不把粉丝多等同于值得模仿。

## 五项过滤

1. 证据：链接、作者、时间和指标是否可核对。
2. 相对表现：相对作者自身近期基线是否异常。
3. 主体差异：明星、新闻、独家资源或投流是否承担了主要结果。
4. 机制可懂：能否说清哪种情绪、信息或叙事结构在起作用。
5. 执行可仿：目标账号能否用真实资源重建机制，而不是复制表面。

## 三条来源线

- 垂直：同品类、同场景或同主题。
- 邻近：受众处境、人物身份或消费动机相似。
- 跨域：主题不同，但承重情绪和传播结构可迁移。

完整选题研究默认收集 6 条垂直、6 条邻近、8 条跨域候选；数据不足时如实缩减。

## 低粉爆款判定

优先使用：

viral_multiplier = note_likes / creator_recent_median_likes

正式对标视频先过绝对门槛：可见点赞数必须大于等于 3,000。点赞数小于 3,000、点赞不可见的视频不得进入正式对标池，最多标记为“灵感样本”。

通过绝对门槛后，主样本建议同时满足：

- 发布时间在约定范围内
- viral_multiplier 不低于 3
- 作者粉丝约为目标账号的 0.3–3 倍
- 收藏、评论或分享代理信号至少一项异常
- 承重机制可以在目标账号的真实资源内重建

跨域样本可放宽粉丝带，但必须提高迁移性审查。明星、重大新闻、昂贵独家资源、一次性奇观、不可核实结果和纯投流样本降级或剔除。

## 输出

逐条标记：

- 来源线
- 数据完整度
- 相对爆发证据
- 主体差异
- 可复制元素
- 不可复制元素
- 是否进入 sdt-spread

不要因为设置了 3,000 点赞硬门槛就只按点赞绝对值排序；过门槛后仍按相对爆发、主体差异和可迁移性筛选。
