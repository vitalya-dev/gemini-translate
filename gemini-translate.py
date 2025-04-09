import argparse
import os
import sys

from google import genai

def translate_text(client, text, target_lang, model):
    prompt = f"""
    Translate the following text to {target_lang}. Follow these rules:
    1. Only provide the translation
    2. No additional commentary or notes
    3. Preserve any formatting like line breaks if present
    4. Maintain the original tone
    
    Text to translate: {text}
    """
    response = client.models.generate_content(
        model=model, contents=prompt
    )
    return response.text

def main():
    parser = argparse.ArgumentParser(description='Translate text using Google Gemini.')
    parser.add_argument('--api-key', required=True, help='Google Gemini API key')
    parser.add_argument('--proxy', help='Proxy settings (e.g., socks5://user:pass@ip:port)')
    parser.add_argument('--target-lang', default='russian', 
                       help='Target language for translation (default: russian)')
    parser.add_argument('--model', default='gemini-2.0-flash',
                       help='Model to use for generation (default: gemini-2.0-flash)')

    args = parser.parse_args()

    if args.proxy:
        os.environ["ALL_PROXY"] = args.proxy

    client = genai.Client(api_key=args.api_key)
    

    input_text = sys.stdin.read().strip()
    if not input_text:
        print("Error: No input text provided via stdin", file=sys.stderr)
        sys.exit(1)
    

    translated = translate_text(client, input_text, args.target_lang, args.model)
    print(translated)

if __name__ == "__main__":
    main()


