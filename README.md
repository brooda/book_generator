## How to run this project?

This project is for python, you need to install following packages:
* langchain-openai
* streamlit


You need to fill this line
```python
os.environ["OPENAI_API_KEY"] = "XZYZ"
```

with a proper value of your openai api key.
If you have openai account, you can get it from here
https://platform.openai.com/api-keys


Then you can run the project with the following command:
```bash
streamlit run program.py
```