import requests
import json
import openai


def request_sent(sent):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-*"
    }
    data = {"model": "gpt-3.5-turbo",
            "messages": [{"role": "assistant",
                          "content": sent}]}
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data, timeout=100)
    return response.text


query = '保持身体健康的秘诀是什么？'
print(request_sent(query))


"""
27zRAOMt5jYbH8zkQlIpT3BlbkFJEdEMpRxmBwsYq6ctRTTb
"""



