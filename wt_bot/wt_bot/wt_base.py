import json
import requests
from datetime import datetime
from typing import List
from pydantic.v1 import BaseModel, Field
from langchain.chat_models import AzureChatOpenAI

from langchain.tools import tool
from langchain.llms.base import BaseLLM
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.tools.render import format_tool_to_openai_function
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain.tools.render import format_tool_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.schema.output_parser import StrOutputParser

from wt_bot.wt_bot.cache import history
from wt_bot.wt_bot import llms
from wt_bot.wt_bot.prompts import create_prompt_template, _PROMPT
from wt_bot.wt_bot.rag import retriever

from langchain.chat_models import ChatLiteLLM
import litellm
litellm.set_verbose=True


class ChatApgar:

    def __init__(self) -> None:
        tools_instance = Tools()
        self.list_tools = tools_instance()
        self.list_tools = [getattr(tools_instance, method_name) for method_name in self.list_tools]


    def _create_llm(
            self,
            model,
            temperature=0,
            streaming=False
    ) -> BaseLLM:
        """
        Determine the language model to be used.
        :param model: Language model name to be used.
        :param streaming: Whether to enable streaming of the model
        :return: Language model instance
        """
        
        return AzureChatOpenAI(
            **model
        )
    
    def generate_response(self, data):
        
        llm = self._create_llm(llms.model)
        
        chain = (
            {"context":retriever, "question":RunnablePassthrough()}
            | _PROMPT
            | llm
            | StrOutputParser()
        )



        results = chain.invoke(data)
        results = {"output":results}

        return results




class OpenMeteoInput(BaseModel):
    latitude: float = Field(
        ..., description="Latitude of the location to fetch weather data for"
    )
    longitude: float = Field(
        ..., description="Longitude of the location to fetch weather data for"
    )

class Tools:
    def __init__(self):
        # Get the names of all methods in the class
        pass

    def __call__(self) -> List :
        # Return the list of implemented methods when the class is called like a function
        methods = [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith("__")]
        
        return methods

    @tool(args_schema=OpenMeteoInput)
    def get_current_temperature(latitude: float, longitude: float) -> dict:
        """Fetch current temperature for given coordinates."""

        BASE_URL = "https://api.open-meteo.com/v1/forecast"

        # Parameters for the request
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
            "forecast_days": 1,
        }

        # Make the request
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            results = response.json()
        else:
            raise Exception(f"API Request failed with status code: {response.status_code}")

        current_utc_time = datetime.datetime.utcnow()
        time_list = [
            datetime.datetime.fromisoformat(time_str.replace("Z", "+00:00"))
            for time_str in results["hourly"]["time"]
        ]
        temperature_list = results["hourly"]["temperature_2m"]

        closest_time_index = min(
            range(len(time_list)), key=lambda i: abs(time_list[i] - current_utc_time)
        )
        current_temperature = temperature_list[closest_time_index]

        return f"The current temperature is {current_temperature}°C"

    # @tool
    # def create_your_own(self, query: str) -> str:
    #     """This function can do whatever you would like once you fill it in"""
    #     print(type(query))
    #     return query[::-1]

# Instantiate the class


# Call the instance like a function to get the list of implemented methods
#implemented_methods = tools()
#print("Implemented Methods:", implemented_methods)


# tools_instance = Tools()
# list_tools = tools_instance()
# list_tools = [getattr(tools_instance, method_name) for method_name in list_tools]

# print(type(list_tools[0]))