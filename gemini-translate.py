from google import genai
import os
import sys

os.environ["ALL_PROXY"] = "socks5://user:pass@ip:port"

client = genai.Client(api_key="API KEY")

def translate_text(text):
    prompt = f"""
    Translate the following text to russian. Follow these rules:
    1. Only provide the translation
    2. No additional commentary or notes
    3. Preserve any formatting like line breaks if present
    4. Maintain the original tone
    
    Text to translate: {text}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

input_text = sys.stdin.read().strip()
if input_text:
    translated = translate_text(input_text)
    print(translated)
