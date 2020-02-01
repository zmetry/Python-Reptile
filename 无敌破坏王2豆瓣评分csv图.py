import pygal
import requests
from pyquery import PyQuery as pq
import re

def the_url(num):
    part = 'start='
    url = 'https://movie.douban.com/subject/20438964/comments?'+part+str(num)+'&limit=20&sort=new_score&status=P'
    return url

def get_score(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
               'cookie':'bid=BJZOUrHdrbI; douban-fav-remind=1; ll="118218"; _ga=GA1.2.1441933785.1547893169; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19021; __yadk_uid=1fdXWGoQHiBvl3QRq1uOWZ05mRFjD1sZ; _vwo_uuid_v2=D8EA93E4D7B54C696505B710EBE4B3367|4be055591738990d20ec03d79e48ab6a; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; __utma=30149280.1441933785.1547893169.1548479364.1548482469.10; __utmz=30149280.1548482469.10.8.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/safety/unlock_sms/resetpassword; __utmt=1; dbcl2="190216822:YwV7v6vml/M"; ck=kaeE; __utmb=30149280.3.10.1548482469; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1548482498%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E6%2597%25A0%25E6%2595%258C%25E7%25A0%25B4%25E5%259D%258F%25E7%258E%258B%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.1441933785.1547893169.1548479364.1548482498.5; __utmb=223695111.0.10.1548482498; __utmz=223695111.1548482498.5.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; _pk_id.100001.4cf6=ab036b2e76efb6e3.1548298314.5.1548482576.1548479364.',
               'host':'movie.douban.com'}
    html = requests.get(url,headers = headers).text
    doc = pq(html)
    html = doc('#content')
    htmls = html('.comment-item').items()
    result = []
    for html in htmls:
        customer = html('.comment-info')
        span = customer.find('span')
        txt = str(span)
        scores = re.findall('<span.*class="allstar(\d)(\d).*</span>',txt,re.S)
        for score in scores:
            result.append(int(score[0]))
    return result
       
result = []        

for i in range(0,500,20):
    url = the_url(i)
    temp = get_score(url)
    for m in temp:
        result.append(m)

frequencies = []
for value in range(1,6):
    frequency = result.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()

hist.title = '无敌破坏王2：大闹互联网评分分布直方图'
hist.x_labels = ['1', '2', '3', '4', '5']
hist._x_title = '评分'
hist.y_title = '人数'
hist.add('分数',frequencies)
hist.render_to_file('电影评分.svg')
