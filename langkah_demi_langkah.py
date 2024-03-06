from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import gradio as gr

openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="YOUR OPENAI API KEY"
)

# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
prompt ="""Question: {question}
    please provide step by step Answer based on {language} language:
    """

def generate_cover_letter(question: str, language: str) -> str:
    formatted_prompt = prompt.format(question=question, language=language)
    return openai.invoke(formatted_prompt).content

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Question"),
    gr.Textbox(label="Language (optional)"),
]

output = gr.Textbox(label="Output")

gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(share=True)