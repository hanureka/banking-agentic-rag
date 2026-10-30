# Uses Gemini Pro to answer queries strictly based on provided context
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0
)

def reasoning_agent(question, context):
    prompt = f"""You are a Banking Knowledge Assistant.Answer ONLY using the provided context.Context:{context}Question:{question}Provide:1. Answer2. Explanation3. Sources used"""
    response = llm.invoke(prompt)
    return response.content