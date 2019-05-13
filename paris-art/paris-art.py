from lxml import html
import requests
import csv

# first_page = requests.get('https://www.paris-art.com/art/exposition-art/page/1')
i = 0
# while i < 88:
#         i += 1
#         first_page = requests.get('https://www.paris-art.com/art/critique-art/page/' + str(i))
while i < 477:
        i += 1
        first_page = requests.get('https://www.paris-art.com/art/exposition-art/page/' + str(i))
        tree = html.fromstring(first_page.content)

        pages_list = tree.xpath('//li[@class="post-col"]/a/attribute::href')

        for one_url in pages_list:
                one_page = requests.get(one_url)
                domo = html.fromstring(one_page.content)
                #     content = domo.xpath("//div[@class='post-content']/p[contains(@style, 'text-align: justify') and not(contains(@style, 'text-align: -'))]//text()")
                content = domo.xpath("//div[@class='post-content']/p//text()")

                print("liens du site:  ", one_url, "     page =>   ", i)

                file = open('expo.txt', 'a')
                two_p = ""
                for one_p in content:
                        two_p += one_p.encode("utf-8")
                        # print(two_p)
                file.write(two_p)








# one_page = requests.get('http://pointcontemporain.com/strates-partitions-du-vide-exposition-personnelle-dharold-guerin/')
# domo = html.fromstring(one_page.content)
# content = domo.xpath("//p[@class='has-normal-font-size']//text()")
# # print(content)

# file = open('result', 'a')
# for one_p in content:
#     two_p = one_p.encode("utf-8")
#     file.write(two_p)