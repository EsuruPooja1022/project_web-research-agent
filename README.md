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
Stage | Description | Tools
User Input | Streamlit form where the user enters a research query | Streamlit
Web Search | Fetches relevant URLs based on user query | requests, Google Custom Search API (optional)
Scraping Module | Extracts web page content | BeautifulSoup, requests
GPT Summarization | Summarizes extracted content into concise insights | OpenAI API (GPT-4)
Output Display | Presents summarized results | Streamlit

### 📊 Flowchart

User Query ➔ Search URLs ➔ Scrape Pages ➔ Summarize Content ➔ Display Results

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

Tool | Input | Output
🔎 Search Tool | Query string | List of URLs
🕷️ Scraper | URL | Raw HTML and Cleaned Text
✂️ Summarizer | Cleaned Text | Summarized Insights

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**: 
  - `requests`, `BeautifulSoup` (for scraping)
  - `openai` (optional summarization)
  - `streamlit` (for UI)

---

## 🧪 How to Run Locally

1. **Clone this repo**
   ```bash
   git clone https://github.com/EsuruPooja1022/project_web-research-agent.git
   cd project_web-research-agent

2. **Install dependencies**
    ```bash
   pip install -r requirements.txt

3. **Run the application**
   ```bash
   streamlit run app.py

---

## 🔥 Example Queries
You can try entering queries like:

- "Latest trends in artificial intelligence 2025"
- "Top 10 electric car companies in 2024"
- "History of the Silk Road trade route"
- "Best practices for remote working"
- "Recent breakthroughs in cancer research"

The agent will search the web, extract information, and present easy-to-read summarized results.

---

## ⚠️ Error Handling

Situation | Handling
Search fails | Displays error message and suggests retrying
URL doesn't load | Skips that URL and continues processing
Summarization fails | Shows default fallback message
Unexpected tool crash | App gracefully catches error and keeps running

---

## 📜 License

- This project is licensed under the MIT License.
- Feel free to use, modify, and distribute with attribution.

---

✉️ Contact
Maintained by [Esuru Pooja.C].
For any questions, reach out to: [e20esurupooja@gmail.com]
