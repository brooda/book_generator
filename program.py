import json
import os
from ModelType import ModelType
from langchain_openai import ChatOpenAI
import json
from langchain.schema import HumanMessage
import streamlit as st

with open("spis_tresci.json", 'r') as file:
    book_summary = json.load(file)


os.environ["OPENAI_API_KEY"] = "XZYZ"
def generate_full_chapter(chapter_title, chapter_content):
    model = ChatOpenAI(temperature=0.5, model_name=ModelType.GPT_3_5_TURBO_1106.value)
    messages = [
        HumanMessage(
            content=f"Napisz rozbudowany rozdział na temat {chapter_title}, który opiera się na streszczeniu: {chapter_content}."
        ),
    ]
    return model(messages).content


for elem in book_summary["chapters"]:
    title = elem["title"]
    description = elem["description"]
    print("")
    print(title)
    print(description)

    st.title(title)


    chapter_content = generate_full_chapter(title, description)
    st.write(chapter_content)

