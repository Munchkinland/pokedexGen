import openai

class OpenAIService:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, prompt, max_tokens=150):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content'].strip()