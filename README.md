Documentation for APGAR Health Architecture  

 

The APGAR-Health project aims to provide users of Cloud Clinic with free/quick medical consultation, insight into their health condition, and determine if a medical consultation with a medical practitioner is necessary.  
 

With the introduction of the large language model, it has become possible for humans to interact with computers meaningfully. Large language models can understand the semantics of words in sentences and predict the next word given some initial words, and this has made possible domain adaptation of large language models to perform several tasks such as text summarization, chatbot, and so on. 

   

LLM can be further finetuned to answer questions from a dataset of questions and answer pairs. This makes them very powerful because, given the suitable dataset, they could be adapted for different domain-specific tasks.  

There are several means of achieving domain-specific chatbots which includes finetuning, prompting, few-shot prompting.  

  

This project aims to provide a medical chatbot capable of interacting with users, providing insight into their health status, and advising users on the critical tical needs of seeing a medical expert based on their medical conditions.  

  

The Project can be largely divided into three separate parts:  

Medical Chatbot: The medical chatbot is a chatbot that is capable of interacting with users, providing answers to user's questions, and deducing from the users' responses the severity of their health status and advising them on the need to see a medical practitioner  

API: A server-side implementation for exposing data to the users, providing data needed for the chatbot to make inferences.   

Frontend: A user-friendly and interactive interface for sending and receiving data.  

  

The proposed core component of the entire system is described below.  

 

Backend Implementation: The users are expected to send and receive messages to the AI chatbot in real-time. This requires a two-way communication between the chatbot and the users. The proposed framework for this is a WebSocket which allows for bi-directional communication. The goal is to have the user used the cloud clinic online consultation services. The AI chatbot is capable of making inference from patient user data on cloudclinic patient database. There will be a user model, conversation model, which allows for persisting user data. 

 

 

High-level Architecture for the Abgar Backend 

 

Chabot: AI model capable of having conversations with users. Chatbots are able to have long-running conversations and have access to information that users want to know about. The core component of chatbots is prompting and LLMs. There is also memory and retrieval. 

Basic Component Requirements for the chatbot: 

Memory: This allows a chatbot to remember past interactions, 

Prompts: This comprise of chat history, user input and additional retrieved contextual information. 

Functions 

Vector stores 

Langchain provides a very robust tools in implementing all the core component of a chatbot. This project will leverage the langchain library to implement all the key component of the chatbot. 

 

 

High-level of the different component for the chatbot 