from lxml import html
import requests
import csv

i = 0
while i < 1:
        i += 1
        first_page = requests.get('https://www.beauxarts.com/categorie/expos/page/' + str(i))
        tree = html.fromstring(first_page.content)

        pages_list = tree.xpath('//div[@class="hp__items-list"]/a/attribute::href')

        for one_url in pages_list:
                one_page = requests.get(one_url)
                domo = html.fromstring(one_page.content)
                content = domo.xpath("//div[@class='editor-content__container']/p[@class='editor-content__paragraph']//text()")

                file = open('beauxArts.txt', 'a')
                two_p = ""
                for one_p in content:
                        two_p += one_p.encode("utf-8")
                        # print(two_p)
                file.write(two_p)

