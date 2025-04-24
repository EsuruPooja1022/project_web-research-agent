# AGENT_DOCUMENTATION.md

## 🧠 Architecture Summary

The Web Research Agent consists of the following main components:

1. **User Input Interface**
   - A Streamlit-based input field where users can enter research queries in natural language.

2. **Query Analyzer**
   - Parses and analyzes the user's query to determine intent, key terms, and type of information needed.

3. **Web Search Tool**
   - Generates search queries and uses APIs like Google Custom Search or SerpAPI to retrieve relevant links and snippets.

4. **Web Scraper/Crawler**
   - Visits each link, fetches the HTML, and extracts meaningful content using `BeautifulSoup` and `requests`.

5. **Content Analyzer (LLM)**
   - Summarizes extracted content using the OpenAI API, filtering noise and focusing on relevant, coherent insights.

6. **Results Synthesizer**
   - Merges results from multiple sources, resolves conflicting information, and ranks content by relevance.

7. **Output Presenter**
   - Displays structured summaries in Streamlit with clickable titles, source URLs, and key takeaways.

---

## 🔌 Tool Descriptions

### 1. Web Search Tool
- **Input**: User query (text)
- **Output**: List of URLs with snippets and titles
- **Use**: Initiates research by finding relevant pages to crawl

### 2. Web Scraper/Crawler
- **Input**: List of URLs
- **Output**: Raw web page content
- **Use**: Extracts textual and structured data (paragraphs, tables, headings)

### 3. Content Analyzer (LLM)
- **Input**: Extracted text
- **Output**: Summarized insights (bullet points, paragraphs)
- **Use**: Converts raw data into human-friendly summaries

---

## ✍️ Prompt Design

Prompt design is focused on clarity, extraction, and summarization. Example:

```python
system_prompt = "You are a research assistant. Given content from a web page and the original query, return a clear, concise summary highlighting the most relevant information."

user_prompt = f"""
User Query: {user_query}

Web Page Content:
{text_excerpt}

Summarize the key points that best address the user's question. Be concise, informative, and neutral in tone.
"""
```

The prompt ensures the AI model understands both the user’s intent and the content context.

---

## ⚠️ Error Handling Strategy

1. **Network Failures**
   - Retry failed requests with exponential backoff.
   - Log broken links and skip to the next one.

2. **Empty or Malformed HTML**
   - Validate HTML response before parsing.
   - Use fallback parsers or skip URL with logging.

3. **Conflicting Information**
   - Summarize all perspectives.
   - Highlight divergence in results with tags like "[Conflicting]" or "[Mixed Evidence]".

4. **Rate Limits & API Errors**
   - Implement error-specific handling (e.g., `openai.error.RateLimitError`).
   - Respect delay between calls, rotate API keys if applicable.

5. **No Useful Results**
   - Present a fallback message like: "We couldn’t find high-quality sources for your query. Please try refining your question."

---

## 🧩 Multi-Source Information Synthesis

To synthesize information from multiple web sources:

1. **Group Similar Topics**
   - Cluster summaries by subtopics using keyword matching or embeddings.

2. **Prioritize Reliable Sources**
   - Use domain authority or known publication sources to rank results.

3. **Identify Consensus**
   - Highlight repeating facts or statements as "verified by multiple sources."

4. **Handle Conflicts Transparently**
   - If content disagrees, show both sides (e.g., "Some sources say X, others say Y.")

5. **Final Summary**
   - Combine grouped insights into a logical structure (Intro, Findings, Conclusion) using GPT to format and polish.

---
