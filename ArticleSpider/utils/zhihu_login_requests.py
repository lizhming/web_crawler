import requests 
import re

try:
    import cookielib
except:
    import http.cookiejar as cookielib

header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
}

def get_xsrf():
    response = requests.get("https://www.zhihu.com", headers=header)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        print(match_obj.group(1))


def zhihu_login(account, password):

     if re.match("^1\d{10}",account):
         print("mobile login")
         post_url = "https://www.zhihu.com/login/phone_num"
         post_data = {
             "_xsrf": get_xsrf(),
             "phone_num": account,
             "password": password
         }

         requests.post(post_url, data=post_data, headers=header)

