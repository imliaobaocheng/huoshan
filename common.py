#!/usr/bin/env python
# encoding: utf-8
import requests

API = "https://api.appsign.vip:2688"

APPINFO = {
    "version_code": "4.8.5",
    "live_sdk_version": "4.8.5",
    "channel": "App Stroe",
    "app_name": "live_stream",
    "aid": "1112",
}

header = {
    "User-Agent": "LiveStreaming/4.8.5 (iPhone; iOS 10.2; Scale/2.00)",
    "sdk-version": "1"
}

# 获取Token       有效期60分钟
def getToken():
    #resp = requests.get(API + "/token/huoshan").json()
    resp = requests.get(API + "/token/huoshan/version/2.7.0").json()
    token = resp['token']
    print("Token: " + token)
    return token

# 获取新的设备信息  有效期60分钟永久
def getDevice():
    #resp = requests.get(API + "/huoshan/device/new").json()
    resp = requests.get(API + "/huoshan/device/new/version/2.7.0").json()
    device_info = resp['data']
    print("设备信息: " + str(device_info))
    return device_info

# 拼装参数
def params2str(params):
    query = ""
    for k, v in params.items():
        query += "%s=%s&" % (k, v)
    query = query.strip("&")
    print("Sign str: " + query)
    return query

# 使用拼装参数签名
def getSign(token, query):
    if isinstance(query, dict):
        query = params2str(query)
    resp = requests.post(API + "/sign", json={"token": token, "query": query}).json()
    print("签名返回: " + str(resp))
    sign = resp['data']
    return sign