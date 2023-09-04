from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.timeanddate.com/worldclock/").text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['heading','summary','vid_id'])

article = soup.find('article')

for article in soup.find_all('article'):
    heading = article.h2.a.text
    summary = article.find('div',class_='entry-content').p.text

    #grab source or link in the form of dictionary

    vid_src = article.find('iframe',class_='youtube-player')['src']
    vid_id = vid_src.split('/')[4]
    vid_id=vid_id.split('?')[0]


    yt_link = f'htpps://youtube.come/watch?v={vid_id}'

    print()

    csv_writer.writerow([heading, summary, yt_link])

csv_file.close()