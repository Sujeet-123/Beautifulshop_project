import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

r = requests.get(url)
# content = requests.get(url)
htmlContent = r.content

print(htmlContent)


soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)


title = soup.title
print(type(title)) 


print(title)

# paras = soup.find_all('p')
# print(paras)

# anchors = soup.find_all('a')
# print(anchors)

# print(soup.find('p'))


# print(soup.find('p')['class'])

# print(soup.find('p')['id'])

# print(soup.find_all("p", class_="lead"))

# print(soup.find('p').get_text())

# print(soup.get_text())


# anchorss = soup.find_all('a')

# all_links = set()

# for link in anchorss:
#     if(link.get('href') != '#'):

#         linkText = "https://codewithharry.com" +link.get('href')

#         all_links.add(link)

#         print(linkText)


# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p)




# elem = soup.select('.modal-footer')
# print(elem)

