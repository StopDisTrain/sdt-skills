# SDT 轻量归档规范

## 建议结构

SDT 项目根下按账号建立：

    accounts/{account_id}/profile.md
    research/{account_id}/{YYYY-MM-DD}/sources.json
    research/{account_id}/{YYYY-MM-DD}/mechanisms.md
    deliverables/{account_id}/{topic_id}/topic-card.md
    deliverables/{account_id}/{topic_id}/content-v001.md
    deliverables/{account_id}/{topic_id}/review-v001.md
    deliverables/{account_id}/{topic_id}/performance.md

## ID

- account_id：稳定英文或拼音短名，不随主页昵称变化。
- topic_id：YYYYMMDD-简短主题。
- 版本：v001 起，内容变化新增版本，不覆盖历史。

## 状态

- researched
- shortlisted
- approved
- drafted
- qa-passed
- published
- measured
- archived

## 发布回填

记录发布链接、发布时间、标题、封面版本、开头版本、观察窗口、播放或阅读、点赞、收藏、评论、分享代理信号、增粉和转化线索。未知值留空，不写 0。

