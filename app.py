import streamlit as st
from utils.search import search_web
from utils.scrape import scrape_page
from utils.summarize import summarize_content

st.title("🌐 Web Research Agent")
query = st.text_input("Enter your research question")

if st.button("Search") and query:
    results = search_web(query)
    pages = [scrape_page(r['link']) for r in results]
    summaries = [summarize_content(p, query) for p in pages]
    final = "\n\n".join(summaries)
    st.write("### Summary Report")
    st.write(final)