from langchain.chat_models import AzureChatOpenAI
from wt_bot.core.config import settings

# model = AzureChatOpenAI(
#     deployment_name=settings.OPENAI_ENGINE,
#     openai_api_version=settings.OPENAI_API_VERSION,
#     openai_api_key=settings.OPENAI_API_KEY,
#     openai_api_base=settings.OPENAI_API_BASE,
# )


model = {
    #"model": "gpt-3.5-turbo", # model alias 
    #"litellm_params": { # params for litellm completion/embedding call 
    "azure_deployment": f"{settings.OPENAI_ENGINE}", # actual model name
    "openai_api_key": settings.OPENAI_API_KEY,
    "openai_api_version": settings.OPENAI_API_VERSION,
    "openai_api_base": settings.OPENAI_API_BASE
    #}
}

embeddings = {
    "deployment": f"{settings.E_ENGINE}", # actual model name
    #"openai_api_type":settings.E_OPENAI_API_TYPE,
    "openai_api_key": settings.E_OPENAI_API_KEY,
    "openai_api_version": settings.E_OPENAI_API_VERSION,
    "azure_endpoint": settings.E_OPENAI_API_BASE
}

