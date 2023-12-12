from langchain.vectorstores import faiss, chroma
from langchain.embeddings import OpenAIEmbeddings, AzureOpenAIEmbeddings
from wt_bot.wt_bot import llms
from wt_bot.core.config import settings

# create a vector store and retriever
WT_TECH = [
    "We transform your ideas into great products through design and technology",
    "Wazobia Technologies is a professional software development agency dedicated to producing high quality products.", 
    "We have intensive experience in building bespoke software applications for SMEs and large enterprises.",
    "With years of work, experience and a team of creative minds that are always on tap, your satisfaction is our goal and were here to get it done"
    "OFFFICES & CONTACTS London London +44 330 133 5245 +44 330 133 5245 hello@wazobia.tech hello@wazobia.tech Lagos Lagos +234(0) 706 338 9627 +234(0) 706 338 9627 hello@waobia.tech hello@wazobia.tech"
]
vectorstores = chroma.Chroma.from_texts(
    WT_TECH, embedding=AzureOpenAIEmbeddings(
        
        **llms.embeddings
    )
)
#chroma.Chroma.from_texts
retriever = vectorstores.as_retriever()