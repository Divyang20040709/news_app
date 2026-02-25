import streamlit as st
import json
import requests

st.title("News App")
response = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=829a47d11a3a4d7c82a76890d9b942a3')
data_news = response.json()
articles = data_news['articles']
for article in articles:
    st.subheader(article['title'])
    st.write(article['description'])
    st.write(f"Published at: {article['publishedAt']}")
    st.write(f"Source: {article['source']['name']}")
    st.link_button(f"Source: Read Full Article", article['url'])
    img_url = article.get('urlToImage')
    if img_url:
        st.image(img_url)

response = requests.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=829a47d11a3a4d7c82a76890d9b942a3')
data_news = response.json()
articles = data_news['articles']
for article in articles:
    st.subheader(article['title'])
    st.write(article['description'])
    st.write(f"Published at: {article['publishedAt']}")
    st.write(f"Source: {article['source']['name']}")
    st.link_button(f"Source: Read Full Article", article['url'])
    img_url = article.get('urlToImage')
    if img_url:
        st.image(img_url)


response = requests.get('https://newsapi.org/v2/everything?domains=wsj.com&apiKey=829a47d11a3a4d7c82a76890d9b942a3')
data_news = response.json()
articles = data_news['articles']
for article in articles:
    st.subheader(article['title'])
    st.write(article['description'])
    st.write(f"Published at: {article['publishedAt']}")
    st.write(f"Source: {article['source']['name']}")
    st.link_button(f"Source: Read Full Article", article['url'])
    img_url = article.get('urlToImage')
    if img_url:
        st.image(img_url)
