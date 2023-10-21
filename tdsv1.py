import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system('clear')
os.system('cls')
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m=>"
banner = f"""
\033[1;34m╔════════════════════════════════════╗
\033[0m\033[1;31m[\033[1;97m×.×\033[1;31m] \033[1;97m=> \033[1;92mAdmin: \033[1;33mMrDuy \033[1;34m
\033[0m\033[1;31m[\033[1;97m×.×\033[1;31m] \033[1;97m=> \033[1;32mHotline/Zalo: \033[1;31m0939174946
\033[0m\033[1;31m[\033[1;97m×.×\033[1;31m] \033[1;97m=> \033[1;32mBản Quyền:\033[1;33m MrDuy
\033[0m\033[1;31m[\033[1;97m×.×\033[1;31m] \033[1;97m=> \033[1;32mMomo:\033[1;31m 0939174946
\033[0m\033[1;31m[\033[1;97m×.×\033[1;31m] \033[1;97m=> \033[1;32mFb.com/mxh.fast
\033[1;34m╚════════════════════════════════════╝
\033[1;32m Tool Free Nhiều Chức Năng
\033[1;34m======================================
\033[1;34m Bản Quyền: \033[1;33mMrDuy (FB: Duy Nguyễn)
\033[1;34m======================================"""
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0003)
ngay=int(strftime('%d'))
key1=str(ngay*1246881818+2888181472) 
key = 'One/'+key1
keyv1 = 'Key Víp Tùy Chỉnh'
url = 'https://facevip247.id.vn/key.html?key='+key
token_link1s = '1de3c9720c4e74e0048a4dc2e5b5a0e9ea412429'
link1s = requests.get(f'https://traffic1s.com/api?api={token_link1s}&url={url}').json()
if link1s['status']=="error": 
    print(link1s['message'])
    quit()
else:
    link_key=link1s['shortenedUrl']
h=open('keyDEV.txt',mode='a+')
h=open('keyDEV.txt',mode='r')
thien=h.read()
h.close()
print()
if thien== keyv1 or thien== key:
    print(dau,'\033[1;33mXIN CHÀO \033[1;32m! CHÚC BẠN CHẠY TOOL VUI VẺ...')
    sleep(1)
    exec(requests.get('https://run.mocky.io/v3/0c6813a6-a75c-49ad-83b6-a0e5cce2359e').text)
else:
     print(dau,'\033[1;96mKey Sẽ Thây Đổi Theo Ngày !')

print(dau,'\033[1;33mLink Lấy Key:\033[1;31m '+link_key)

keynhap = input('\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m=> \033[1;32mNhập Key Để Vào Tool\033[1;33m ~>\033[1;03m ')
print("\033[1;34m======================================")
if keynhap == key or keynhap== keyv1:
    print(dau,'\033[1;32mAPI KEY ĐÚNG OPEN TOOL !')
    print("\033[1;34m======================================")
    sleep(2)
    h=open('keyDEV.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://run.mocky.io/v3/0c6813a6-a75c-49ad-83b6-a0e5cce2359e').text)
else:
    print(dau,'\033[1;33mAPI KEY SAI !')
    print("\033[1;34m======================================")
    