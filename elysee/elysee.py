from lxml import html
import requests
import csv

first_page = requests.get('http://www.elysee.ch/expositions-et-evenements/expositions-dans-le-monde/precedentes')
tree = html.fromstring(first_page.content)

follow_page = tree.xpath('//li[@class="tx-pagebrowse-next"]/a/attribute::href')

for one_url in pages_list:
        one_page = requests.get(one_url)
        domo = html.fromstring(one_page.content)
        content = domo.xpath("//div[@class='mel_module_liste']/div[@class='item']/a/attribute::href")

        file = open('beauxArts.txt', 'a')
        two_p = ""
        for one_p in content:
                two_p += one_p
                print(two_p)
        file.write(two_p)






