# 抖音设备注册

模拟设备信息无限量生成device_id和install_id

# 环境准备
经过测试发现抖音的设备注册并非单独的一个请求就可以完成的，虽然模拟请求获得了device_id和install_id，但是如果使用这些刚获得的设备信息去访问加密接口，将得到空的响应。查阅资料得知是有后续的激活请求，在下才疏学浅暂未找到，如果有知道的大佬还请不吝指教，感谢！

# Docker
`docker run -it -v /your_code_path/douyin_device_register:/app --name douyin --rm korekontrol/ubuntu-java-python3 python3 /app/register.py`

# test
![](https://github.com/coder-fly/douyin_device_register/blob/master/screenshots/20200120092306.png)


# thanks
 - [unidbg](https://github.com/zhkl0228/unidbg)
