---
name: sdt-wechat-html
description: "把已经完成并通过质检的 Markdown 内容转换成可粘贴到微信公众号后台的 HTML，并支持选择样式、生成预览和检查粘贴兼容性。用户要制作公众号排版稿或微信发布版本时使用。 English: Convert a finished, quality-checked Markdown draft into HTML that can be pasted into the WeChat Official Accounts editor, with style selection, preview generation, and paste-compatibility checks. Use when the user needs a formatted WeChat publishing version."
---

# SDT 公众号发布

使用 SDT 自带样式和渲染脚本，把内容包适配成公众号发布文件，不修改观点和事实。

## 前置门

- 输入内容已经定稿。
- 标题、引用和图片占位明确。
- 事实核验已完成。

未定稿内容先回到对应生产或质检模块，不在排版阶段顺手改文案。

## 工作流

1. 读取 references/styles.md。用户已指定风格时直接执行；未指定时根据内容选择一个，无法判断时使用 minimal。
2. 运行 scripts/render_wechat_html.py 生成单个风格；用户明确要比较时使用 --all 生成全部内置风格。
3. 把 SDT 内容包中的图片位置保留为明确占位，不外链未知资源。
4. 执行其静态检查：无 style 标签、class、id、脚本、外链和伪元素；正文可见元素具备完整行内样式。
5. 输出文件并说明粘贴和手机端预览步骤。

## 独立运行

最低输入是一份定稿 Markdown。无需账号档案、选题卡或其他 SDT 步骤。

示例命令：

    python3 scripts/render_wechat_html.py article.md --style minimal
    python3 scripts/render_wechat_html.py article.md --all

## SDT 增量记录

归档时同时保存：

- 来源 Markdown 版本
- style id
- HTML 文件
- 生成时间
- 发布后使用的实际版本

不得把公众号排版表现误写为内容机制验证结果。
