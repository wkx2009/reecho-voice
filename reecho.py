#本脚本由不会取名编写，若有侵权请联系3401594212@qq.com
import os
import json
import requests
#import http.client

# 文件名，用于保存API
CONFIG_FILE = 'reecho_config.json'

# 获取或保存API
def get_api_key():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get('api_key')
    else:
        api_key = input("请输入你的睿声api: ")
        with open(CONFIG_FILE, 'w') as f:
            json.dump({'api_key': api_key}, f)
            response.text
        return api_key
        
#用于测试api
def test_api(api_key):
    url = "https://v1.reecho.cn/api/account/info"
    payload={}
    headers = {
       'Authorization': f'Bearer {api_key}'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

#用于查看当前账号中的角色    
def view_account_roles(api_key):
    url = "https://v1.reecho.cn/api/tts/voice?from"
    payload={}
    headers = {
       'Authorization': f'Bearer {api_key}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
'''
    data = response.json()  # 将响应内容解析为JSON对象
    
    if isinstance(data, list):  # 如果返回的是一个列表
            for item in data:
                print(f"ID: {item['id']}")
                print(f"Name: {item['name']}")
                print(f"Status: {item['status']}")
                print("-" * 20)
    else:
            print("Unexpected response format:", data)
'''    
#用于生成语音
def generate_voice(api_key):
    url = "https://v1.reecho.cn/api/tts/simple-generate"
    # 让用户输入文本
    text = input("请输入要生成语音的文本: ")    
    # 让用户输入语音角色id
    voice = input("请输入生成语音角色id: ")
    payload = json.dumps({
       "voiceId": f"{voice}",
       "text": text,
       "texts": [text],
       "promptId": "default",
       "model": "reecho-neural-voice-001",
       "randomness": 97,
       "stability_boost": 100,
       "probability_optimization": 99,
       "break_clone": False,
       "flash": False,
       "origin_audio": False,
       "stream": False
    })
    headers = {
       'Authorization': f'Bearer {api_key}',
       'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

#用户选择界面
def menu():
    print("\n请选择一个操作:")
    print("1. 查看当前账号中的角色")
    print("2. 生成语音")
    print("3. 测试API连接")
    print("4. 退出")
    return input("输入选项编号: ")

#主函数    
def main():
    api_key = get_api_key()
    while True:
        choice = menu()
        if choice == '1':
            view_account_roles(api_key)
        elif choice == '2':
            generate_voice(api_key)
        elif choice == '3':
            test_api(api_key)
        elif choice == '4':
            print("退出程序")
            break
                       
        else:
            print("无效的选项，请重新选择")

if __name__ == "__main__":
    main() 