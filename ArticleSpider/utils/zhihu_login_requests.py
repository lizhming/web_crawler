import requests 
import re

try:
    import cookielib
except:
    import http.cookiejar as cookielib


session = requests.session()  
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt") 
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cannot load cookie')    

header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
}

def is_login():
    inbox_url = "https://www.zhihu.com/inbox"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True    

def get_xsrf():
    response = session.get("https://www.zhihu.com", headers=header)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        print(match_obj.group(1))
    else:
        return ""    

def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", "wb") as f:
        f.write(response.text.encode("utf-8"))

def zhihu_login(account, password):

     if re.match("^1\d{10}",account):
         print("mobile login")
         post_url = "https://www.zhihu.com/login/phone_num"
         post_data = {
             "_xsrf": get_xsrf(),
             "phone_num": account,
             "password": password
         }
         session.cookies.save()
    else:   
        if "@" in account:
            print("email login")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": get_xsrf(),
                "phone_num": account,
                "password": password
            }    

    response_text = session.post(post_url, data=post_data, headers=header)        


#zhihu_login("18782902568","admin123")         
get_index()
