#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: coderfly
@file: app.py
@time: 2020/10/13
@email: coderflying@163.com
@desc: 
"""
import platform
import time
import binascii
import random
import os
import urllib.request
import subprocess
import re
import json
from flask import Flask, jsonify

def get_random_mc():
    mc = '{}:{}:{}:{}:{}:{}'.format("".join(random.choices(mc_random,k=2)),"".join(random.choices(mc_random,k=2)),"".join(random.choices(mc_random,k=2)),"".join(random.choices(mc_random,k=2)),"".join(random.choices(mc_random,k=2)),"".join(random.choices(mc_random,k=2)))
    return mc

def get_system():
    system = platform.system()
    if system.startswith("Win"):
        return "win"+platform.machine()[-2:]
    elif system.startswith("Lin"):
        return "linux" + platform.machine()[-2:]
    else:
        return "osx64"

def hexStr_to_str(hex_str):
    hexadecimal = hex_str.encode('utf-8')
    str_bin = binascii.unhexlify(hexadecimal)
    return str_bin

os.environ['WORKON_HOME']="value"
system = "linux64"
nativate_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"nativate")
jar_path = os.path.join(nativate_path,"unidbg.jar")
jni_path = os.path.join(os.path.join(nativate_path,"prebuilt"),system)
os.chdir(nativate_path)
mc_random = ["a","1","2","3","4","5","6","7","8","9"]
headers = {
    'User-Agent':'okhttp/3.8.1',
    'Content-Type':'application/octet-stream;tt-data=a'
}
app = Flask(__name__)

@app.route("/", methods=['GET'])
def register():
    gen_time = str(int(time.time()*1000))
    udid = str(random.randint(321480502743165,921480502743165))
    openudid = "".join([random.choice("abcdefghijklmn1234567890") for i in range(16)])
    mc = get_random_mc()
    message = " ".join([gen_time,udid,openudid,mc])
    command = r"java -jar -Djna.library.path={} -Djava.library.path={} unidbg.jar {}".format(jni_path,jni_path,message)
    stdout,stderr = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
    hex_str = re.search(r'hex=([\s\S]*?)\nsize',stdout.decode()).group(1)
    astr = hexStr_to_str(hex_str)
    register_url = 'https://log.snssdk.com/service/2/device_register/'
    request = urllib.request.Request(url=register_url,data=astr,headers=headers)
    response = urllib.request.urlopen(request)
    return jsonify(json.loads(response.read()))

if __name__ == '__main__':
    app.run(host="0.0.0.0")