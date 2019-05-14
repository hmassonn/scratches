from lxml import html
import requests
import csv

follow_page = ['http://www.elysee.ch/expositions-et-evenements/expositions-dans-le-monde/precedentes']

two_p = ""
pages = 0

while pages < 62:
    pages += 1
    follow_page = requests.get(follow_page[0])
    tree = html.fromstring(follow_page.content)
    follow_page = tree.xpath('//li[@class="tx-pagebrowse-next"]/a/attribute::href')
    link_list = tree.xpath("//div[@class='mel_module_liste']/div[@class='item']/a/attribute::href")

    print(follow_page)

    for one_url in link_list:
        one_page = requests.get(one_url)
        domo = html.fromstring(one_page.content)
        content = domo.xpath("//div[@class='mel_module_expo']//p[@class='bodytext']/text()")

        print(content)
        file = open('elysee.txt', 'a')
        for one_p in content:
            two_p += one_p


file.write(two_p)




