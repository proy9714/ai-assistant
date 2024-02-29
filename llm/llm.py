from langchain_google_genai import ChatGoogleGenerativeAI
from .prompt import TEXT_CORRECTION_PROMPT

def get_chat_completion(prompt: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    response = llm.invoke(prompt)
    
    return response.content
    
def get_corrected_text(text: str) -> str:
    prompt = TEXT_CORRECTION_PROMPT.format(text=text)
    corrected_text = get_chat_completion(prompt)
    
    return corrected_text