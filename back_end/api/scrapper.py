from fastapi import APIRouter, HTTPException
from configuration import db
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta

router = APIRouter()
collection = db["news"]

@router.post("/scrape-news")
async def scrape_news(pages: int = 10):
    x = 1
    inserted = 0
    for i in range(1, pages + 1):
        print('get news in page ' + str(i))
        response = requests.get(f'https://news.detik.com/indeks?page={i}')
        soup = BeautifulSoup(response.text, 'html.parser')
        for list_content in soup.find_all('article', class_='list-content__item'):
            title = list_content.find('h3', class_='media__title')
            title_text = title.text.strip()
            link = title.a.get('href')
            thumbnail = list_content.find('img')
            thumbnail_url = thumbnail.get('src')
            if thumbnail_url and '.jpeg' in thumbnail_url:
                thumbnail_url = thumbnail_url.split('.jpeg')[0] + '.jpeg'

            print(str(x) + ' get data for news ' + title_text)
            x += 1
            response_news = requests.get(link)
            news_soup = BeautifulSoup(response_news.text, 'html.parser')
            if '20.detik.com' in link:
                vertical = news_soup.find('div', class_='video-vertical-right-text')
                if vertical:
                    authors_class = 'vertical__right__author'
                    date_div = news_soup.find('div', class_='vertical__right__view')
                    if date_div:
                        date_text = date_div.text.strip()
                        if "|" in date_text:
                            date = date_text.split("|", 1)[1].strip()
                        else:
                            date = date_text
                    else:
                        date = ''
                    content_class = 'vertical__right__desc'
                else:
                    authors_class = 'color-gray-light-1 font-xs'
                    date_div = news_soup.find('div', class_='detail__date')
                    if date_div:
                        date_text = date_div.text.strip()
                        if "|" in date_text:
                            date = date_div.text.strip().split("|", 1)[1].strip()
                        else:
                            date = date_text
                    else:
                        date = ''
                    content_class = 'detail__body-text'
            else:
                authors_class = 'detail__author'
                date_div = news_soup.find('div', class_='detail__date')
                if date_div:
                    date = date_div.text.strip()
                else:
                    date = ''
                content_class = 'detail__body-text'
            authors = news_soup.find('div', class_=authors_class)
            if authors:
                author_text = authors.text.strip()
            else:
                author_text = 'Unknown'
            content_div = news_soup.find('div', class_=content_class)
            if content_div:
                content_text = ''
                for ads2 in content_div.find_all('div', class_='parallaxindetail'):
                    ads2.decompose()
                for text in content_div.find_all('p'):
                    paragraph = text.get_text(" ", strip=True)
                    if paragraph:
                        content_text += paragraph + ' '
                content_text = content_text.strip()
            else:
                content_text = ''
            try:
                date_val = date.split(',')[1]
                format_string = " %d %b %Y %H:%M WIB"
                datetime_object = datetime.strptime(date_val, format_string)
                jakarta_tz = timezone(timedelta(hours=7))
                datetime_object = datetime_object.replace(tzinfo=jakarta_tz)
            except Exception:
                datetime_object = None

            news_data = {
                'title': title_text,
                'url': link,
                'thumbnail_url': thumbnail_url,
                'date': datetime_object,
                'authors': author_text,
                'content': content_text
            }
            collection.insert_one(news_data)
            inserted += 1
    return {"status_code":200,"message": f"Scraping selesai. {inserted} berita berhasil disimpan."}