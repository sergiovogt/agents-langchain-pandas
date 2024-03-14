from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import (
    create_pandas_dataframe_agent
    )
from langchain_openai import ChatOpenAI
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

import pandas as pd

df = pd.read_csv("supermarket.csv")

agent = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)
agent.handle_parsing_errors = True