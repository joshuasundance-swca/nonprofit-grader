import os
from fastapi import FastAPI
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
from ocr import qa

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple api server using Langchain's Runnable interfaces",
)


prompt = ChatPromptTemplate.from_template("Find organization(s) that deals with {interest}, and tell me about them.")

add_routes(
    app,
    qa | (lambda r: r["result"]),
    path="/nonprofit",
)
