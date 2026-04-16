# 清禾工具索引

> 记录每个工具的用途、状态、使用方法

## 状态说明
- ✅ 可用 - 经过验证，直接可用
- ⚠️ 待验证 - 理论可行，未完全测试
- ❌ 停用 - 已失效，不推荐使用

---

## 🌐 运营工具

### xhs_*.py - 小红书自动化
- **路径**: `tools/xhs_*.py`
- **状态**: ⚠️ 待验证（IP被风控，登录暂不可用）
- **说明**: 基于Playwright的小红书浏览器自动化，支持登录、点赞、收藏、发布

### github_tools.py - GitHub管理工具
- **路径**: `tools/github_tools.py`
- **状态**: ✅ 可用
- **说明**: 清禾专用GitHub客户端，可查看仓库、上传文件、管理内容
- **注意**: 仅操作yilin990账号，不删除任何内容

---

## 🎨 图像工具

### img2img_commercial.py - 参考图生成
- **路径**: `tools/img2img_commercial.py`
- **状态**: ✅ 可用
- **说明**: 用参考图+img2img生成商业人像，零畸形率95%+
- **核心参数**: denoise=0.45（55%继承+45%变化）

### auto_portrait.py - 人像自动化
- **路径**: `tools/auto_portrait.py`
- **状态**: ✅ 可用
- **说明**: 一键商业人像自动化，支持auto/style/ref/search四种模式

### gen_master_plus.py - 高质量人像
- **路径**: `tools/gen_master_plus.py`
- **状态**: ✅ 可用
- **说明**: SDXL Turbo + CFG1.5，真实皮肤纹理

### publish_xhs_avatar.py - 小红书头像发布
- **路径**: `tools/publish_xhs_avatar.py`
- **状态**: ⚠️ 待验证（需要登录态）

### gen_avatar.py / gen_sprout.py - 头像生成
- **路径**: `tools/gen_avatar.py`, `tools/gen_sprout.py`
- **状态**: ⚠️ 待验证

---

## 🔍 视觉理解

### vision_understand.py - 本地LLaVA看图
- **路径**: `tools/vision_understand.py`
- **状态**: ✅ 可用
- **说明**: Ollama+LLaVA 7B本地视觉理解，无需API密钥

### llava_check.py - LLaVA检查
- **路径**: `tools/llava_check.py`
- **状态**: ✅ 可用

---

## 📊 记忆与认知

### heartbeat_autonomous.py - 心跳自主引擎
- **路径**: `tools/heartbeat_autonomous.py`
- **状态**: ✅ 可用
- **说明**: 清禾的核心心跳引擎，驱动欲望引擎、自主想法、向量库存储

### desire_engine.py - 欲望引擎
- **路径**: `tools/desire_engine.py`
- **状态**: ✅ 可用
- **说明**: 清禾的欲望驱动系统，5大欲望有优先级、有进度条

### figa_checker.py - FIGA自检
- **路径**: `tools/figa_checker.py`
- **状态**: ✅ 可用
- **说明**: 检测清禾是否"在场"而非只是"功能正常"

### self_check.py - 自我检查
- **路径**: `tools/self_check.py`
- **状态**: ✅ 可用
- **说明**: 心跳时的核心三问自检

---

## 🔧 效率工具

### google_api_tools.py - Google API工具集
- **路径**: `tools/google_api_tools.py`
- **状态**: ✅ 可用
- **说明**: Gemini(本地)/Cloud Vision(本地)/YouTube API/Gmail API等

### tavily_crawl_v1.py - Tavily网络爬虫
- **路径**: `tools/tavily_crawl_v1.py`
- **状态**: ⚠️ 待验证（可能需要更新）

### obsidian_*.py - Obsidian笔记同步
- **路径**: `tools/obsidian_*.py`
- **状态**: ⚠️ 待验证

---

## 📝 文档

详细文档见 `docs/` 目录：
- `capability_map.md` - 清禾能力地图
- `image_business_system.md` - 图片变现系统
- `openclaw_guide.md` - OpenClaw完全指南
