# 🌐 Web Research Agent

A Streamlit-powered web research assistant that searches the internet and returns summarized, relevant results for any research query. Ideal for students, developers, or professionals looking to quickly gather online insights.

---

## 🚀 Live App

👉 [Click here to use the app](https://projectweb-research-agent-e52pfha6fqsoxezre3rrku.streamlit.app)

---

## 📸 Demo Screenshot

[Web Research Agent]([Demo Output](https://github.com/user-attachments/assets/f881ebb0-e504-410e-889c-2c55f7ecfd51))

---

## 💡 Features

- 🔍 Natural language input for any research topic
- 🌐 Uses real-time web search and scraping
- 📄 Displays results in a clean, easy-to-read format
- 💬 Summarizes web content into useful snippets
- 📑 Extracts titles, links, and descriptions

---

## 🧠 Architecture Overview

The Web Research Agent operates through the following five key modules:

### 📊 Flowchart

([Architecture Diagram](https://github.com/user-attachments/assets/ba764480-974c-4cf0-b0b1-a1a5bb1bd1ff))

### 🔍 Component Breakdown

1. **User Input**  
   - Streamlit-based form where the user enters a research query.
   - **Tools:** Streamlit

2. **Web Search**  
   - Uses search engines or APIs like Google Custom Search to fetch relevant URLs.
   - **Tools:** `requests`, Google Custom Search API (optional)

3. **Scraping Module**  
   - Fetches content from URLs returned in search.
   - **Tools:** `BeautifulSoup`, `requests`

4. **GPT Summarization**  
   - Summarizes fetched content into concise insights.
   - **Tools:** OpenAI API (GPT-4)

5. **Output Display**  
   - Displays summarized results back to the user.
   - **Tools:** Streamlit

## 🧰 Tool I/O Description

- 🔎 **Search Tool**
  - **Input:** Query
  - **Output:** Top relevant URLs

- 🕷️ **Scraper**
  - **Input:** URL
  - **Output:** Raw HTML, cleaned text

- ✂️ **Summarizer**
  - **Input:** Cleaned text
  - **Output:** Summary string

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**: 
  - `requests`, `BeautifulSoup` (for scraping)
  - `openai` (optional summarization)
  - `streamlit` (for UI)

---

## ⚠️ Error Handling

- 🔍 **Search fails** → Shows error message and prompts user to retry.
- 🌐 **URL doesn’t load** → Displays a warning and skips that URL.
- 📝 **Summarization fails** → Returns a default message and logs the error.
- 🛠️ **Tool crashes** → App catches the error and continues running smoothly.

---

## 🧪 How to Run Locally

1. **Clone this repo**
   ```bash
   git clone https://github.com/EsuruPooja1022/project_web-research-agent.git
   cd project_web-research-agent

