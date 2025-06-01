from pprint import pprint
from utils import fetch_article_content, analyze_readability, analyze_structure
from prompts import build_improvement_prompt
from agent import ask_gpt

def analyze_article(url: str) -> dict:
    raw = fetch_article_content(url)

    readability = analyze_readability(raw)
    structure   = analyze_structure(raw)

    llm_prompt = build_improvement_prompt(raw)
    llm_feedback = ask_gpt(llm_prompt)

    return {
        "url": url,
        "readability": readability,
        "structure": structure,
        "llm_feedback": llm_feedback,
    }

if __name__ == "__main__":
    test_url = (
        "https://help.moengage.com/hc/en-us/articles/28476977883412-How-to-Set-Up-Purchase-Confirmation-Emails"
    )
    report = analyze_article(test_url)
    pprint(report)

    input("\nPress Enter to exit...")
