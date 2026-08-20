# SDT Skills

SDT 是一套面向小红书内容研究、选题、创作、质检与资产沉淀的 Codex Skills。

## 包含模块

- `sdt`：技能族总入口与任务路由
- `sdt-account`：账号档案与定位
- `sdt-research`：公开内容检索与证据采集
- `sdt-benchmark`：对标样本筛选
- `sdt-spread`：传播机制分析
- `sdt-topic`：选题生成、迁移与筛选
- `sdt-content`：正文与口播稿生产
- `sdt-hook`：短视频前五秒开头
- `sdt-cover`：小红书封面方案
- `sdt-xhs-title`：小红书标题生成与筛选
- `sdt-script-flow`：口播节奏和衔接质检
- `sdt-resonate`：传播心理与共鸣质检
- `sdt-ai-check`：AI 写作特征与账号语气质检
- `sdt-wechat-html`：微信公众号 HTML 转换
- `sdt-content-system`：长期内容资产沉淀

## 目录结构

每个子目录都是一个独立 Skill，入口文件为 `SKILL.md`。

```text
skills/
├── sdt/
│   └── SKILL.md
├── sdt-account/
│   └── SKILL.md
└── ...
```

## 使用方式

### 让 Codex 帮你安装（推荐）

把仓库链接发给 Codex，并发送：

> 请使用 skill-installer，从 https://github.com/StopDisTrain/sdt-skills 安装 `skills/` 下所有以 `sdt` 开头的 Skill。

安装完成后，在下一轮对话中直接说“用 SDT 帮我做选题”“用 sdt-hook 优化开头”等即可。

### Install with Codex (recommended)

Share the repository link with Codex and say:

> Use skill-installer to install every Skill whose folder name starts with `sdt` under `skills/` from https://github.com/StopDisTrain/sdt-skills.

The installed Skills become available on the next turn. You can then ask Codex to “use SDT to develop content ideas” or “use sdt-hook to improve this opening.”

### 手动安装 / Manual installation

也可以将所需的 Skill 目录复制到 `~/.codex/skills/`。每个 Skill 都应保持独立目录结构，并包含自己的 `SKILL.md`。安装后重新加载 Codex。

Alternatively, copy the desired Skill folders into `~/.codex/skills/`. Keep each Skill in its own directory with its `SKILL.md`, then reload Codex.

本仓库只包含技能定义，不包含本地账号档案、研究样本、生成报告或 QA 渲染文件。
