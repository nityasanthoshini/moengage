def build_improvement_prompt(article_text: str) -> str:
    """Compose the instruction GPT will follow for analysis."""
    return f"""
You are a senior technical writer. Evaluate the article below on four axes:
1. Readability for a non-technical marketer
2. Structure & flow
3. Completeness of information & examples
4. Adherence to Microsoft Style Guide principles (clarity, active voice)

For each axis, return:
- A brief assessment
- 2-3 concrete, actionable suggestions

Respond in GitHub-flavored Markdown using this template:

## Readability
- …

## Structure & Flow
- …

## Completeness
- …

## Style
- …

---
ARTICLE START
{article_text}
ARTICLE END
"""
