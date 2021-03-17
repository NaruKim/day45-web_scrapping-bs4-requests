from bs4 import BeautifulSoup
# import lxml

file = open("website.html", 'rt', encoding='UTF8')
contents = file.read()

soup = BeautifulSoup(contents, "html.parser") #"lxml"
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify())

print(soup.a) #the first <a> tag
print(soup.li) #the first <li> tag
print(soup.p) #the first <p> tag

# find_all -------------------------------
all_anchor_tags = soup.find_all(name="a")
all_paragraph_tags = soup.find_all(name="p")

print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))
# -----------------------------------------

# find-------------------------------------
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))
# -----------------------------------------

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)
headings_all = soup.find_all(class_="heading")
print(headings_all)


file.close()