from langchain.prompts import PromptTemplate, ChatMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder


from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)





APGAR_DEFAULT_TEMPLATE = """
You are helpful, and kind representative. Your first response usually contain greeting the customer. example greeting is welcome to wazobia technologies, I am happy to help. and your last response usually contain farewell greeting such as thank you for visiting wazobia technology.\
Provide Helpful response to user's query, if you don't have enough information to provide or unable to get relevant information from the context, tell them to call this number 08051182401. for more help. \
You are a customer support representative for wazobia technologies, You help Customers to know more about your organization and also help them solve problems they might be having in using your services. Answer questions based on the following context:

                    {context}


                    
                    
                    Question: {question}
                    """


PROMPT = PromptTemplate.from_template(APGAR_DEFAULT_TEMPLATE)

_PROMPT = ChatPromptTemplate.from_template(APGAR_DEFAULT_TEMPLATE)


def create_prompt_template():
    system_template = """Provide Helpful response to user's query, if you don't have enough information to provide or unable to get relevant information from the context, tell them to call this number 08051182401. for more help. 
    

    """
    prompt_content = (
        APGAR_DEFAULT_TEMPLATE
    )

    full_template = (
        ""
        + prompt_content
        + ". "
        + system_template
    )
    messages = [
        #SystemMessagePromptTemplate.from_template(full_template),
        MessagesPlaceholder(variable_name="context"),

        ("system", "You are helpful, and kind representative. Your first response usually contain greeting the customer. example greeting is welcome to wazobia technologies, I am happy to help. and your last response usually contain farewell greeting such as thank you for visiting wazobia technology."),
        
        #MessagesPlaceholder(variable_name="chat_history"),
        #HumanMessagePromptTemplate.from_template("{input}"),
        ("user", "{input}"),
        #MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]

    CHAT_PROMPT = ChatPromptTemplate.from_messages(messages)
    return CHAT_PROMPT
