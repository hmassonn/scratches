from lxml import html
import requests
import csv

follow_page = ['http://flux-news.be/2019/05/04/flux-news-magazine-79/']

two_p = ""

while 1:
    follow_page = requests.get(follow_page[0])
    tree = html.fromstring(follow_page.content)
    follow_page = tree.xpath('//div[@class="mh-col-1-2 mh-post-nav-item mh-post-nav-prev"]/a/attribute::href')

    print(follow_page)

    content = tree.xpath("//div[@class='entry-content mh-clearfix']/p/text()")

    print(content)
    file = open('fluxNews.txt', 'a')
    for one_p in content:
        two_p += one_p
    file.write(two_p)





