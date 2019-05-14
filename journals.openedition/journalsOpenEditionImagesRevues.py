from lxml import html
import requests
import csv

first_page = requests.get('https://journals.openedition.org/imagesrevues/55')
tree = html.fromstring(first_page.content)

pages_list = tree.xpath('//ul[@class="collection summary"]/li/a/attribute::href')

pages_list = pages_list[2:len(pages_list)]
print(pages_list)

for one_url in pages_list:
    one_page = requests.get('https://journals.openedition.org/imagesrevues/' + one_url)
    domo = html.fromstring(one_page.content)
    # content = domo.xpath("//p[@class='has-normal-font-size']//text()")
    links_list = domo.xpath("//div[@class='title']/a[@lang='fr']/attribute::href")

    for new_link in links_list:
        print(new_link)
        new_page = requests.get('https://journals.openedition.org/imagesrevues/' + new_link)
        domino = html.fromstring(new_page.content)
        new_content = domino.xpath("//div[@id='text']//p[@class='texte']/text()")

        file = open('imagesrevues.txt', 'a')
        two_p = ""
        for one_p in new_content:
            print(one_p)
            two_p += one_p
            print(two_p)
        file.write(two_p)

