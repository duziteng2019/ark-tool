# 🎨 ARK AI 生图 CLI 工具

> 基于火山引擎 ARK API 的命令行 AI 图片生成工具  
> 支持 Seedream 5.0 / 4.5 / 4.0 模型

## ✨ 功能

- ✅ **文字生图** - 输入提示词，一键生成 AI 图片
- ✅ **图生图** - 基于参考图片生成新图
- ✅ **多模型** - 支持 Seedream 5.0/4.5/4.0
- ✅ **模型列表** - 查看当前账号可用模型
- ✅ **无依赖** - 仅需 Python 3 + requests

## 🚀 快速开始

### 1. 获取 API Key

在 [火山引擎 ARK 控制台](https://console.volcengine.com/ark/region:arkCN) 注册并创建 API Key。

> 新用户有免费额度，不需要花钱。

### 2. 下载脚本

```bash
git clone https://github.com/duziteng2019/ark-tool.git
cd ark-tool
```

### 3. 安装依赖

```bash
pip install requests
```

### 4. 设置 API Key

```bash
export ARK_API_KEY="你的火山引擎API Key"
```

### 5. 开始使用

```bash
# 查看可用模型
python3 ark_tool.py list

# 文字生图
python3 ark_tool.py image doubao-seedream-5-0-260128 '一只可爱的柴犬，高清摄影，自然光'

# 自定义尺寸
python3 ark_tool.py image doubao-seedream-5-0-260128 '赛博朋克城市夜景' '1920x1080'
```

## 📋 命令说明

| 命令 | 参数 | 说明 |
|------|------|------|
| `image` | `<model> <prompt> [size]` | 生成图片 |
| `list` | 无 | 列出可用模型 |

### 可用模型

| 模型ID | 说明 |
|--------|------|
| `doubao-seedream-5-0-260128` | Seedream 5.0（最新最强） |
| `doubao-seedream-4-5-251128` | Seedream 4.5 |
| `doubao-seedream-4-0-250828` | Seedream 4.0 |

## 🔧 高级用法

### 图生图

```bash
python3 ark_tool.py image doubao-seedream-5-0-260128 '参考这张图的风格，改为春天' 1920x1920 --image参考图.jpg
```

### 持久化 API Key

```bash
# 写入 ~/.bashrc 避免每次设置
echo 'export ARK_API_KEY="你的Key"' >> ~/.bashrc
```

## 📝 注意事项

- API Key 请妥善保管，不要提交到代码仓库
- 图片生成为异步任务，通常 5-30 秒完成
- 不同模型生成的图片质量和风格有差异
- 火山引擎 ARK 按调用量计费，请关注 [官方定价](https://www.volcengine.com/docs/82379)

## 💖 支持

如果你觉得这个工具有用，欢迎打赏支持一下 🐒


---

**项目地址:** [github.com/duziteng2019/ark-tool](https://github.com/duziteng2019/ark-tool)
**技术栈:** Python + 火山引擎 ARK API
**许可证:** MIT
