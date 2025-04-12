from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

repo_id = "tiiuae/falcon-7b-instruct"
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceHub(
    repo_id=repo_id,
    huggingfacehub_api_token=token,  # make sure this is NOT None
    model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
)

prompt = PromptTemplate(
    input_variables=["user_input"],
    template="You are a supportive mental health chatbot. Respond empathetically to: {user_input}"
)

chain = LLMChain(llm=llm, prompt=prompt)
