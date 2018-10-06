# 火山通信协议 4.8.5版本协议签名

## 简介

通过火山通信协议实现自动化爬取火山视频，批量注册登录，点赞，评论, 视频下载上传等功能

火山通信协议支持火山 iOS 4.8.5（最新）协议，提供生成iOS设备信息功能，方便调用协议

提供生成签名服务，方便对火山通信协议进行签名。签名参数: `as`, `mas`, `ts`

项目持续更新中...

## 使用说明
通过调用API加签服务来完成获取新的设备信息及协议签名。

实现过程:
1. 通过访问 `https://api.appsign.vip:2688/token/huoshan/version/4.8.5` 获取火山协议4.8.5的加签token，其他版本如2.6.0，修改version后面的版本号，如果不添加/version/<版本号>参数，默认版本号为最新版本，token有效期为60分钟
2. 如果没有设备信息可以请求 `https://api.appsign.vip:2688/huoshan/device/new/version/4.8.5` 获取新的设备信息，包括install_id, vid, device_id, openudid 等， 设备信息为永久使用，版本号参考token获取中的版本号设置
3. 有了设备信息和加签Token， 需要通过参数构造加签字符串，调用 `https://api.appsign.vip:2688/sign` 完成参数的加签

---

> token有效期为一个小时，支持多线程进行加签，token失效之前无需重复获取
> 设备信息依据需要进行获取

## API参数
1. 获取火山加签Token
```
https://api.appsign.vip:2688/token/huoshan  # 默认版本为最新
https://api.appsign.vip:2688/token/huoshan/version/4.8.5
```
```
{
    "token":"5826aa5b56614ea798ca42d767170e74",
    "success":true
}
```

2. 生成新的设备属性
```
https://api.appsign.vip:2688/huoshan/device/new  # 默认版本为最新
https://api.appsign.vip:2688/huoshan/device/new/version/4.8.5
```
```
{
    "data":{
        "os_api":"23",
        "screen_width":"1334",
        "vid":"39******-ABCD-DA1D-C2C5-******995D7",
        "os_version":"11.0",
        "new_user":1,
        "install_id":4286******3,
        "iid":***********,
        "idfa":"95******-87D6-F152-04F1-88B******418",
        "device_type":"iPhone8.1",
        "device_platform":"iphone",
        "openudid":"b9f9a7c2c9******45c9aafec7b******24cc6",
        "device_id":57000******
    },
    "success":true
}
```

3. 参数加签
```
https://api.appsign.vip:2688/sign
{
    "token":"TOKEN",
    "query":"通过参数生成的加签字符串"
}
```
```
{
    "data":{
        "mas":"0041******cf******511116******1f17624******2e7******8e",
        "as":"a1a506881111aba6******",
        "ts":"153******4"
    },
    "success":true
}
```

## APP版本信息
针对不同版本的火山，可以使用如下版本信息：
```
APPINFO = {
    "version_code": "4.8.5",
    "live_sdk_version": "4.8.5",
    "channel": "App Stroe",
    "app_name": "live_stream",
    "aid": "1112",
}

等其他
```


## 实例

* [x] 爬取首页视频: `feed.py`
* [x] 视频搜索: `search.py`
* [ ] 注册 
* [ ] 登录
* [ ] 点赞
* [ ] 评论
* [ ] 视频下载 无水印 
* [ ] 视频上传


## 更新

* 2018.09.19 更新支持最新版4.8.5协议
