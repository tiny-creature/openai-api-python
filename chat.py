from openai import OpenAI
import readline

api_key = '{你的api key}'
base_url = "{api网址}"
client = OpenAI(
    api_key = api_key, 
    base_url = base_url
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("〈提示〉q退出 del清除上下文")

while True:
    user_input = input("〈 user 〉\n ")
    if user_input.lower() == 'q' or user_input.lower() == '':
        break
    if user_input.lower() == "del":
        messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]    
        print("已删除聊天记录，开始新的会话")
        continue
            
    print("")  
    print("〈 deepseek 〉")  
    messages.append(
        {"role": "user", "content": user_input}
    )
    completion = client.chat.completions.create(
        model="{模型}",
        messages = messages,
        stream=True,        
    )
    responses = []
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="",flush=True)
            response = chunk.choices[0].delta.content
            responses.append(response)
    
    response_merge = "".join(responses)
    print("") 
    messages.append(
        {"role": "assistant", "content": response_merge}
    )
