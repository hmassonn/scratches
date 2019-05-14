from lxml import html
import requests
import csv

i = 0
while i < 28:
        i += 1
        first_page = requests.get('https://www.artpress.com/category/expositions/page/' + str(i))
        tree = html.fromstring(first_page.content)

        pages_list = tree.xpath('//div[@class="blog_holder blog_large_image "]/article//h2//a/attribute::href')
        # print(pages_list)

        for one_url in pages_list:
                one_page = requests.get(one_url)
                domo = html.fromstring(one_page.content)
                content = domo.xpath("//div[@class='post_text_inner']//p//text()")

                file = open('artPress.txt', 'a')
                two_p = ""
                for one_p in content:
                        two_p += one_p
                        print(two_p)
                file.write(two_p)

