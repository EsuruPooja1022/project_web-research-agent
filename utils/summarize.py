import openai
openai.api_key = "your-api-key"

def summarize_content(content, query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Summarize this content for: {query}\n\n{content}"}
        ]
    )
    return response['choices'][0]['message']['content']
