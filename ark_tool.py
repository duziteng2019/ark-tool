#!/usr/bin/env python3
"""
火山引擎 ARK AI 生图 CLI 工具
支持 Seedream 5.0/4.5/4.0 模型图片生成

使用前请设置环境变量：
  export ARK_API_KEY="你的火山引擎API Key"
  
获取API Key: https://console.volcengine.com/ark/region:arkCN
"""
import sys, json, os, requests, time

def get_api_key():
    """获取API Key，优先从环境变量读取"""
    key = os.getenv("ARK_API_KEY")
    if not key:
        print("❌ 错误: 未设置 ARK_API_KEY 环境变量")
        print("   请在火山引擎控制台获取API Key: https://console.volcengine.com/ark/region:arkCN")
        print("   然后执行: export ARK_API_KEY=\"你的Key\"")
        sys.exit(1)
    return key

API_KEY = get_api_key()
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# ========== 图片生成 ==========

def generate_image(model, prompt, size="1920x1920", n=1, image=None):
    """生图 - 支持 Seedream 4.0/4.5/5.0"""
    payload = {"model": model, "prompt": prompt, "n": n, "size": size}
    if image:
        import base64
        with open(image, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        payload["image"] = f"data:image/jpeg;base64,{b64}"

    resp = requests.post(f"{BASE_URL}/images/generations", headers=HEADERS, json=payload, timeout=120)
    data = resp.json()
    if "data" in data:
        return [d["url"] for d in data["data"]]
    raise Exception(f"生图失败: {data.get('error', data)}")

# ========== 查询可用模型 ==========

def list_models():
    """列出当前账号可用的模型"""
    resp = requests.get(f"{BASE_URL}/models", headers=HEADERS, timeout=15)
    data = resp.json()
    count = 0
    for m in data.get("data", []):
        domain = m.get("domain", "")
        status = m.get("status", "")
        mid = m["id"]
        name = m.get("name", "")
        if status == "active":
            print(f"  [{domain:20s}] {name:30s} {mid}")
            count += 1
    return count

# ========== 主入口 ==========

def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  生图: python3 ark_tool.py image <model> <prompt> [size]")
        print("  列模型: python3 ark_tool.py list")
        print("")
        print("可用的模型:")
        print("  - doubao-seedream-5-0-260128   (Seedream 5.0)")
        print("  - doubao-seedream-4-5-251128   (Seedream 4.5)")
        print("  - doubao-seedream-4-0-250828   (Seedream 4.0)")
        print("")
        print("示例:")
        print("  python3 ark_tool.py image doubao-seedream-5-0-260128 '一只可爱的柴犬, 高清摄影'")
        print("  python3 ark_tool.py list")
        sys.exit(1)

    action = sys.argv[1]

    if action == "image":
        if len(sys.argv) < 4:
            print("❌ 用法: python3 ark_tool.py image <model> <prompt> [size]")
            sys.exit(1)
        model = sys.argv[2]
        prompt = sys.argv[3]
        size = sys.argv[4] if len(sys.argv) > 4 else "1920x1920"

        print(f"🎨 正在用 {model} 生成图片...")
        print(f"📝 提示词: {prompt[:50]}{'...' if len(prompt) > 50 else ''}")
        try:
            urls = generate_image(model, prompt, size)
            for url in urls:
                print(f"✅ 生成成功!")
                print(f"🖼️  URL: {url}")
        except Exception as e:
            print(f"❌ 失败: {e}")
            sys.exit(1)

    elif action == "list":
        print("📋 可用模型:")
        count = list_models()
        print(f"\n共 {count} 个活跃模型")

    else:
        print(f"❌ 未知操作: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
