#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *
"""
搜索视频
Host: api.huoshan.com
User-Agent: LiveStreaming/4.8.5 (iPhone; iOS 10.2; Scale/2.00)
"""

keyword = u"美女"      # 搜索内容
offset = "0"         # 偏移位置

# 获取Token       有效期60分钟
token = getToken()
# 获取新的设备信息  有效期永久
device_info = getDevice()

# 拼装参数
params = {
    "iid":              device_info['iid'],
    "idfa":             device_info['idfa'],
    "vid":              device_info['vid'],
    "device_id":        device_info['device_id'],
    "openudid":         device_info['openudid'],
    "device_type":      device_info['device_type'],
    "os_version":       device_info['os_version'],
    "os_api":           device_info['os_api'],
    "screen_width":     device_info['screen_width'],
    "device_platform":  device_info['device_platform'],
    "version_code":     APPINFO['version_code'],
    "channel":          APPINFO['channel'],
    "app_name":         APPINFO['app_name'],
    "live_sdk_version": APPINFO['live_sdk_version'],
    "aid":              APPINFO['aid'],
    "ac":           "WIFI",
    "count":        "10",
    "query":        keyword,
    "offset":       offset,
    "search_type":  "0",
    "user_action":  "initiative"

}
sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

resp = requests.get("https://api.huoshan.com/hotsoon/general_search/", params=params, headers=header).json()
print(resp)

