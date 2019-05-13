from lxml import html
import requests
import csv

first_page = requests.get('http://pointcontemporain.com/articles/en-direct-des-expositions/')
tree = html.fromstring(first_page.content)

pages_list = tree.xpath('//div[@class="entry-thumb"]/a/attribute::href')

for one_url in pages_list:
    one_page = requests.get(one_url)
    domo = html.fromstring(one_page.content)
    # content = domo.xpath("//p[@class='has-normal-font-size']//text()")
    content = domo.xpath("//div[@class='single-content']//p//text()")
    print("liens du site:                                     ", one_url)

    file = open('result', 'a')
    for one_p in content:
        two_p = one_p.encode("utf-8")
        print(two_p)
        file.write(two_p)


# one_page = requests.get('http://pointcontemporain.com/strates-partitions-du-vide-exposition-personnelle-dharold-guerin/')
# domo = html.fromstring(one_page.content)
# content = domo.xpath("//p[@class='has-normal-font-size']//text()")
# # print(content)

# file = open('result', 'a')
# for one_p in content:
#     two_p = one_p.encode("utf-8")
#     file.write(two_p)