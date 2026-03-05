import streamlit as st
import requests

st.set_page_config(page_title="News App", layout="wide")

st.title("📰 Global News Hub")

# function to display news in grid cards
def display_news(articles):

    cols = st.columns(3)

    for i, article in enumerate(articles):

        with cols[i % 3]:

            with st.container(border=True):

                img_url = article.get("urlToImage")

                if img_url:
                    st.image(img_url, use_container_width=True)

                st.subheader(article["title"])

                if article["description"]:
                    st.write(article["description"])

                st.caption(f"🕒 {article['publishedAt']}")
                st.caption(f"📡 Source: {article['source']['name']}")

                st.link_button("🔗 Read Full Article", article["url"])


# ---------------- BUSINESS NEWS ----------------

st.header("💼 Business News")

response = requests.get(
    "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=829a47d11a3a4d7c82a76890d9b942a3"
)

data_news = response.json()
articles = data_news["articles"]

display_news(articles)

st.divider()

# ---------------- TECHCRUNCH NEWS ----------------

st.header("💻 TechCrunch News")

response = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=829a47d11a3a4d7c82a76890d9b942a3"
)

data_news = response.json()
articles = data_news["articles"]

display_news(articles)

st.divider()

# ---------------- WSJ NEWS ----------------

st.header("🏦 Wall Street Journal")

response = requests.get(
    "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=829a47d11a3a4d7c82a76890d9b942a3"
)

data_news = response.json()
articles = data_news["articles"]

display_news(articles)
