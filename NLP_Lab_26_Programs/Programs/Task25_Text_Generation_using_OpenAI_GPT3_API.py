import os

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("SKIPPED: OPENAI_API_KEY is not set. Add your API key in PowerShell before running this task.")
        return
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        model = os.getenv("OPENAI_MODEL", "text-davinci-003")
        prompt = "Write a short, simple explanation of natural language processing:"
        # Uses the legacy GPT-3 text-completions model named in many introductory lab examples.
        response = client.completions.create(model=model, prompt=prompt, max_tokens=90, temperature=0.7)
        print("Model:", model)
        print("Prompt:", prompt)
        print("Generated text:", response.choices[0].text.strip())
    except ImportError:
        print("SKIPPED: OpenAI Python package is missing. Run setup_core.ps1.")
    except Exception as exc:
        print("SKIPPED: API/model request could not be completed:", type(exc).__name__, str(exc))
        print("Note: access to the legacy text-davinci-003 model may not be available; set OPENAI_MODEL to a model enabled for your API account.")

if __name__ == "__main__":
    main()
