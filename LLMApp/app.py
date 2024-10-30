# langchain+ openai code 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import JSONLoader
import json
from pathlib import Path
from pprint import pprint
import os
from dotenv import load_dotenv

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")



file_path='lite_pricing_json'
loader = JSONLoader(file_path, jq_schema='.content',text_content=False, json_lines=True)
data = json.loads(Path(file_path).read_text())

# print(data)
data2= loader.load()    
print(data2)


# prompt = ChatPromptTemplate.from_message(
#     [
#         ("system","You are a bot who can read json data really well and answer user queries based on pricing and features available. PLease respond to the user based on the context and data "),
#         ("user","Question:{question}\nContext:{context}"),
#     ]
    
# )

