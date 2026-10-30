# Validates whether the generated response is grounded in the retrieved contex
from langchain_google_genai import ChatGoogleGenerativeAI

validator = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0
)

def validation_agent(question, context, answer):
    prompt = f"""Verify whether the answer is fullysupported by the context.Question:{question}Context:{context}Answer:{answer}Return format:STATUS: VALID or REVISECOMMENTS:Explain why."""
    result = validator.invoke(prompt)
    return result.content