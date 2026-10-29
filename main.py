# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0,
#     api_key=os.environ["GROQ_API_KEY"],
# )

# messages = [
#     (
#         "user",
#         "Explain why fast inference is critical for reasoning models"
#     )
# ]

# response = llm.invoke(messages)

# print(response.content)
