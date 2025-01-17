#CAPTURED BY SHAJON

import requests

cookies = {
    'datr': 'Lo4vZ5sKrHmuKkkVf1sqXLgc',
    'sb': 'x4N3Zxh0PwvOch3gN49HKkzR',
    'locale': 'en_GB',
    'dpr': '3.1883959770202637',
    'ps_l': '1',
    'ps_n': '1',
    'fr': '0qLiDDXWY7xeKXjPZ.AWVkJkKBioJ92Hxa18eAk5ujtSk.BnL44u..AAA.0.0.BniSxD.AWUtPXPRoMA',
    'wd': '980x1931',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=Lo4vZ5sKrHmuKkkVf1sqXLgc; sb=x4N3Zxh0PwvOch3gN49HKkzR; locale=en_GB; dpr=3.1883959770202637; ps_l=1; ps_n=1; fr=0qLiDDXWY7xeKXjPZ.AWVkJkKBioJ92Hxa18eAk5ujtSk.BnL44u..AAA.0.0.BniSxD.AWUtPXPRoMA; wd=980x1931',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/r.php?entry_point=login',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-lsd': 'AVpevgrYFgw',
}

data = {
    'jazoest': '21080',
    'lsd': 'AVpevgrYFgw',
    'firstname': 'Atif',
    'lastname': 'Akbar',
    'birthday_day': '24',
    'birthday_month': '11',
    'birthday_year': '2000',
    'birthday_age': '',
    'did_use_age': 'false',
    'sex': '2',
    'preferred_pronoun': '',
    'custom_gender': '',
    'reg_email__': 'tarantula54twyw29@mixzu.net',
    'reg_email_confirmation__': '',
    'reg_passwd__': '#PWD_BROWSER:5:1737043051:AW1QAAe1FNYH299KHUA11oIQJGuJa0TaYubexkC97yc9Lu0TetgRdplkE4JNy2woghIUPL7nylzKyX7MnUlZK9gkzK/0MKNc11NEcwXuOuVTyFrH4HOi0jNBb+rGTMuaUPLra3QY0aOMwOTuXb8=',
    'referrer': '',
    'asked_to_login': '0',
    'use_custom_gender': '',
    'terms': 'on',
    'ns': '0',
    'ri': '7ac686a6-5e49-4b1f-8b3a-9a9d06a5134d',
    'action_dialog_shown': '',
    'invid': '',
    'a': '',
    'oi': '',
    'locale': 'en_GB',
    'app_bundle': '',
    'app_data': '',
    'reg_data': '',
    'app_id': '',
    'fbpage_id': '',
    'reg_oid': '',
    'reg_instance': 'Lo4vZ5sKrHmuKkkVf1sqXLgc',
    'openid_token': '',
    'uo_ip': '',
    'guid': '',
    'key': '',
    're': '',
    'mid': '',
    'fid': '',
    'reg_dropoff_id': '',
    'reg_dropoff_code': '',
    'ignore': 'captcha|reg_email_confirmation__',
    'captcha_persist_data': 'AZlkQh0mZpZIJNywXRFhfIkTwk17lS8DfTQjHCA9XGsPi_K9gq9TUqS6sS7JbcmQlLF4x5LagE1AQlW1KS60_ZE5vs2tuw2C9C0pJqw3Sj3Qoi794c9mKovkcOvUNQ_soPTc8e6yuYM4ekqeTnBbkaQWmmqb4eBNXwWKb3S-9nliIDJI0M_-8Vs5vUkGUVNGx1QZOWnkK46IGtFzlq77ZAzlKOpd0QUAJw9N0xE_9d_H968XJfb5a81vKhJsx3RoIEg9xblSibOTplfF5MqSlFORjSrr0_Rm1W-99lC-Ay7qYjZqi50iUDGe_dIPOKs1GhFGLN3_hHQmshcIXfJc7d0imywhONX_n0vlK1rxi3ZuL7rbf7u26ZzOpZSEqIeTARI',
    'captcha_response': '',
    '__user': '0',
    '__a': '1',
    '__req': '7',
    '__hs': '20104.BP:DEFAULT.2.0.0.0.0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1019376741',
    '__s': 'wszick:tb5kvq:0h3u6k',
    '__hsi': '7460542925810636607',
    '__dyn': '7xe6EsK36Q5E5ObwKBWg5S1Dxu13wqovzEdEc8uw9-3K0lW4o3Bw5VCwjE3awdu0FE2awpUO0n24o5-0me1Fw5uwbO0KU3mwaS0zE5W08HwSyE1582ZwrU1Xo1UU3jwea',
    '__csr': '',
    '__spin_r': '1019376741',
    '__spin_b': 'trunk',
    '__spin_t': '1737043011',
}

response = requests.post('https://www.facebook.com/ajax/register.php', cookies=cookies, headers=headers, data=data)


import requests

cookies = {
    'datr': 'Lo4vZ5sKrHmuKkkVf1sqXLgc',
    'sb': 'x4N3Zxh0PwvOch3gN49HKkzR',
    'wd': '980x1931',
    'c_user': '61572374241804',
    'fr': '0qLiDDXWY7xeKXjPZ.AWVSaBlwuR2xsZAVHUOwksDImyw.BnL44u..AAA.0.0.BniSqe.AWV7IjH2aXo',
    'locale': 'en_GB',
    'xs': '37%3Apub4Iso1AcugOA%3A2%3A1737042601%3A-1%3A-1',
    'dpr': '3.1883959770202637',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    # 'cookie': 'datr=Lo4vZ5sKrHmuKkkVf1sqXLgc; sb=x4N3Zxh0PwvOch3gN49HKkzR; wd=980x1931; c_user=61572374241804; fr=0qLiDDXWY7xeKXjPZ.AWVSaBlwuR2xsZAVHUOwksDImyw.BnL44u..AAA.0.0.BniSqe.AWV7IjH2aXo; locale=en_GB; xs=37%3Apub4Iso1AcugOA%3A2%3A1737042601%3A-1%3A-1; dpr=3.1883959770202637',
    'dpr': '2.9000000953674316',
    'referer': 'https://www.facebook.com/r.php',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'viewport-width': '980',
}

params = {
    'next': 'https://www.facebook.com/?lsrc=lbr',
    '__req': 'a',
}

response = requests.get('https://www.facebook.com/confirmemail.php', params=params, cookies=cookies, headers=headers)



import requests

cookies = {
    'datr': 'Lo4vZ5sKrHmuKkkVf1sqXLgc',
    'sb': 'x4N3Zxh0PwvOch3gN49HKkzR',
    'c_user': '61572374241804',
    'fr': '0qLiDDXWY7xeKXjPZ.AWVSaBlwuR2xsZAVHUOwksDImyw.BnL44u..AAA.0.0.BniSqe.AWV7IjH2aXo',
    'locale': 'en_GB',
    'xs': '37%3Apub4Iso1AcugOA%3A2%3A1737042601%3A-1%3A-1',
    'dpr': '3.1883959770202637',
    'wd': '981x1933',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=Lo4vZ5sKrHmuKkkVf1sqXLgc; sb=x4N3Zxh0PwvOch3gN49HKkzR; c_user=61572374241804; fr=0qLiDDXWY7xeKXjPZ.AWVSaBlwuR2xsZAVHUOwksDImyw.BnL44u..AAA.0.0.BniSqe.AWV7IjH2aXo; locale=en_GB; xs=37%3Apub4Iso1AcugOA%3A2%3A1737042601%3A-1%3A-1; dpr=3.1883959770202637; wd=981x1933',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/confirmemail.php?next=https%3A%2F%2Fwww.facebook.com%2F%3Flsrc%3Dlbr&__req=a',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-fb-lsd': '-3L7pG8HO9efFJn-hlEKfD',
}

params = {
    'next': 'https://www.facebook.com/?lsrc=lbr',
    'cp': 'tarantula5429@mixzu.net',
    'from_cliff': '1',
    'conf_surface': 'hard_cliff',
    'event_location': 'cliff',
}

data = {
    'jazoest': '25607',
    'fb_dtsg': 'NAcOMzsgnnl0hO5OOD58r9exJ3msOj31kxeSR0mhhbEpwqnxZABZcYA:37:1737042601',
    'code': '26332',
    'source_verified': 'www_reg',
    'confirm': '1',
    '__user': '61572374241804',
    '__a': '1',
    '__req': '4',
    '__hs': '20104.BP:DEFAULT.2.0.0.0.0',
    'dpr': '3',
    '__ccg': 'EXCELLENT',
    '__rev': '1019376741',
    '__s': 'umjubi:kldxof:bnwan0',
    '__hsi': '7460541172804187057',
    '__dyn': '7xeUmBwjbg7ebwKBAg5S3G2O5U4e1Fx-ewSwMxW0DUS2S0im4E9ohwem0nCq1ew8y11wdu0FE5-2G1Qw5Mx61vwnE2PwBgao6C0lW0H83bwdq1iwmE2ewnE2Lw5XwSyES0gq0Lo6-1Fw63w7zwtU5K0UE',
    '__csr': '',
    'lsd': '-3L7pG8HO9efFJn-hlEKfD',
    '__spin_r': '1019376741',
    '__spin_b': 'trunk',
    '__spin_t': '1737042603',
}

response = requests.post(
    'https://www.facebook.com/confirm_code/dialog/submit/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)


