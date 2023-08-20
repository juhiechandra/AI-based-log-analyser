from langchain.llms import OpenAI
from langchain import PromptTemplate

users_question = "What are the anomalies, error in the logs and how can we resolve it?"


# define the prompt template
template = """
You are an information security system, you will be given some rules that are from the compliance of the company's software system. I will also give you the logs generated from the production system.

Your job is to give me insights from the logs and tell me the actionable items

give me resolution"

Context sections:
Error in add_to_cart. Response: 403 - Unauthorized',
       'Error in remove_from_cart. Response: 502 - Internal Server Error',
       'Error in return. Response: 500 - Service Unavailable',
       'Error in purchase. Response: 500 - Internal Server Error',
       'Error in purchase. Response: 401 - Service Unavailable',
       'Error in remove_from_cart. Response: 500 - Bad Request',
       'Error in purchase. Response: 504 - OK',
       'Error in purchase. Response: 504 - Not Found',
       'Error in remove_from_cart. Response: 301 - Not Found',
       'Error in return. Response: 403 - Bad Request',
       'Error in return. Response: 400 - Unauthorized',
       'Error in remove_from_cart. Response: 504 - Bad Gateway',
       'Error in purchase. Response: 500 - Forbidden',
       'Error in add_to_cart. Response: 503 - Moved Permanently',
       'Error in login. Response: 400 - Service Unavailable',
       'Error in login. Response: 503 - Forbidden',
       'Error in view_product. Response: 500 - Bad Gateway',
       'Error in return. Response: 502 - Not Found',
       'Error in remove_from_cart. Response: 404 - Bad Request',
       'Error in purchase. Response: 404 - Internal Server Error',
       'Error in view_product. Response: 401 - Unauthorized',
       'Error in purchase. Response: 404 - Gateway Timeout',
       'Error in remove_from_cart. Response: 502 - Forbidden',
       'Error in login. Response: 504 - Unauthorized',
       'Error in return. Response: 301 - Bad Gateway'

Question:
{users_question}

Answer:
"""

prompt = PromptTemplate(template=template)

# fill the prompt template
prompt_text = prompt.format(context = results, users_question = users_question)

# ask the defined LLM
llm(prompt_text)