#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *
"""
拉取首页视频
Host: api.huoshan.com
User-Agent: LiveStreaming/4.8.5 (iPhone; iOS 10.2; Scale/2.00)
"""

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
    "type":         "video",
    "action":       "refresh",
    "diff_stream":  "0",
    "req_from":     "feed_refresh",
    #"ab_version": "521974,520931,526091,523183,522269,488743,374107,502900,524355,376187,384501,510345,480223,493077,517866,493885,508367,430969,299910,457534,524372,518147,404280,493546,378845,513799,500052,399990,526010,465280"
}

sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

# 拉取首页视频列表
resp = requests.get("https://api.huoshan.com/hotsoon/feed/", params=params, headers=header).json()
print(resp)

