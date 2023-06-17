# Stock Query Tools as OpenAI Functions
# Make sure langchain after 0.0.202
# pip install --upgrade --force-reinstall langchain

import json
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool
from langchain.schema import HumanMessage

from stock_price import StockPriceTool
from stock_peformace import StockPercentageChangeTool, StockGetBestPerformingTool

model = ChatOpenAI(model="gpt-3.5-turbo-0613")
tools = [StockPriceTool(), StockPercentageChangeTool(),
         StockGetBestPerformingTool()]
open_ai_agent = initialize_agent(tools,
                                 model,
                                 agent=AgentType.OPENAI_FUNCTIONS,
                                 verbose=False)

while True:
    try:
        question = input("Question: ")
        tool_result = open_ai_agent.run(question)
        print("Answer: ", tool_result)
    except KeyboardInterrupt:
        break
