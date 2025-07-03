def individual_news(news):
    return {
        "id": str(news["_id"]),
        "title": news["title"],
        "url": news["url"],
        "thumbnail_url": news["thumbnail_url"],
        "date": news["date"],
        "authors": news["authors"],
        "content": news["content"],
    }

def news_list(news_list):
    return [individual_news(news) for news in news_list]