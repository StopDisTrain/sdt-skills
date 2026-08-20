# 研究证据字段

每条样本使用同一结构：

| 字段 | 类型 | 说明 |
|---|---|---|
| sample_id | string | 本地稳定编号 |
| query | string | 找到样本的检索词 |
| lane | enum | vertical、adjacent、cross-domain |
| source_url | string | 可回溯原链接 |
| author | string | 公开作者名 |
| author_url | string | 公开主页 |
| followers | number/null | 采集时公开粉丝数 |
| published_at | datetime/null | 发布时间 |
| title | string | 原标题 |
| cover_url | string/null | 封面地址，仅研究用途 |
| likes | number/null | 可见点赞 |
| collects | number/null | 可见收藏 |
| comments | number/null | 可见评论 |
| recent_median_likes | number/null | 作者近期同口径点赞中位数 |
| viral_multiplier | number/null | likes / recent_median_likes |
| captured_at | datetime | 采集时间和时区 |
| evidence_level | enum | complete、partial、inspiration-only |
| limitations | array | 缺失、登录、时间或口径限制 |

## 计算规则

- 中位数优先使用作者最近 10–20 条同形式内容。
- 置顶、广告、抽奖、重大新闻和明显异常样本应单独标记，不直接进入基线。
- 分母为 0 或缺失时不计算倍数。
- 平台缩写数值先规范化为数值，并保留原始显示值。
- 不把收藏和评论缺失写成 0。

