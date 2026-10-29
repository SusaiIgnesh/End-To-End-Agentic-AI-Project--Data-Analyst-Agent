import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic
load_dotenv()

# llm = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0,
#     api_key=os.environ["GROQ_API_KEY"],
# )



def pick_llm(level: str):
    """
    Picks the appropriate LLM based on the level of the question.

    Args:
        level (str): The level of the question, can be "low", "medium", or "high".

    Returns:
        ChatOpenAI: The LLM instance to be used.
    """
    if level.lower() == "low":
        llm = ChatGroq(model="openai/gpt-oss-120b",temperature=0,api_key=os.environ["GROQ_API_KEY"],)
    elif level.lower() == "medium":
        llm = ChatGroq(model="openai/gpt-oss-120b",temperature=0,api_key=os.environ["GROQ_API_KEY"],)
    elif level.lower() == "high":
        llm = ChatGroq(model="openai/gpt-oss-120b",temperature=0,api_key=os.environ["GROQ_API_KEY"],)
    elif level.lower() == "claude":
        llm = ChatAnthropic(model="claude-sonnet-4-6", temperature=0.7)
    else:
        raise ValueError(f"Unsupported Level: {level}")

    return llm


if __name__ == "__main__":
    llm_obj = pick_llm("low")
    print(llm_obj.invoke("what is agentic ai"))