import requests
from pyquery import PyQuery as pq

def get_url(num):
    url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
    return url

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
               'cookie':'bid=BJZOUrHdrbI; douban-fav-remind=1; ll="118218"; _ga=GA1.2.1441933785.1547893169; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19021; __yadk_uid=1fdXWGoQHiBvl3QRq1uOWZ05mRFjD1sZ; _vwo_uuid_v2=D8EA93E4D7B54C696505B710EBE4B3367|4be055591738990d20ec03d79e48ab6a; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1551579128%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1441933785.1547893169.1551438093.1551579128.16; __utmc=30149280; __utmz=30149280.1551579128.16.12.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1441933785.1547893169.1551438093.1551579128.11; __utmb=223695111.0.10.1551579128; __utmc=223695111; __utmz=223695111.1551579128.11.7.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; __utmt=1; dbcl2="190216822:8TkZIUQjPCU"; ck=YPQi; __utmb=30149280.3.10.1551579128; _pk_id.100001.4cf6=ab036b2e76efb6e3.1548298314.11.1551579252.1551438093.',
               'host':'movie.douban.com'}
for a in range(0,250,25):
    url = get_url(a)
    r = requests.get(url, headers = headers)
    html = pq(r.text)
    first = html('#content')
    second = first.find('li').items()
    for b in second:
        rank = b.find('em').text()
        film_name = b('.title').text()
        file_score = b('.rating_num').text()
        with open('top250.txt','a',encoding='utf-8') as f:
            f.write('\n'.join([rank,film_name,file_score]))
            f.write('\n' + '='*50+'\n')
