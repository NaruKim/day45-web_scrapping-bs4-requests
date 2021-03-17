from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])

# articles = []
# for i in range(len(article_upvotes)):
#     articles.append({
#         "text":article_texts[i],
#         "link":article_links[i],
#         "score":article_upvotes[i]
#     })
#
# big = 0
# big_index = 0
# for i in range(len(article_upvotes)):
#     if article_upvotes[i] > big:
#         big = article_upvotes[i]
#         big_index = i
# print(article_texts[big_index])
# print(article_links[big_index])
# print(article_upvotes[big_index])

