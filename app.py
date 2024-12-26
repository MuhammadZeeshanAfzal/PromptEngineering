# from flask import Flask, jsonify, request
# from langchain.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain.chains import LLMChain
# import openai
# import os
# from dotenv import load_dotenv, find_dotenv

# # Load environment variables
# _ = load_dotenv(find_dotenv())
# api_key  = os.getenv('MY_OPENAI_API_KEY')

# # Initialize the Flask app
# app = Flask(__name__)

# # Initialize the language model (GPT)
# llm = ChatOpenAI(api_key=api_key, model="gpt-4o-mini", temperature=1)

# TEMPLATE = '''
# "Write an engaging and informative article on the topic of {text}.
# The article should be 150–200 words long, written in a professional tone, and targeted at a general audience. 
# Include an introduction to explain the topic, a few key points with examples, and a conclusion summarizing the main ideas. 
# Ensure the content is clear, concise, and free of jargon."
# '''

# artical_generation = PromptTemplate(
#     input_variables=["text"],
#     template=TEMPLATE
# )

# chain = LLMChain(llm=llm, prompt=artical_generation)

# @app.route("/", methods=["GET"])
# def hello_world():
#     return "Hello, World!"

# # Route for generating articles
# @app.route("/generate_article", methods=["POST"])
# def generate_article():
#     # Get the topic from the JSON request
#     data = request.get_json()
#     topic = data.get("topic")

#     if not topic:
#         return jsonify({"error": "Topic is required!"}), 400

#     # Generate the article
#     output = chain.run(topic).strip()
#     return "good"
#     # return jsonify({"article": output})

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import openai
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
_ = load_dotenv(find_dotenv())
api_key  = os.getenv('MY_OPENAI_API_KEY')

# Initialize the Flask app
app = Flask(__name__)

# Initialize the language model (GPT)
llm = ChatOpenAI(api_key="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", model="gpt-4o-mini", temperature=1)

TEMPLATE = '''
"Write an engaging and informative article on the topic of {text}.
The article should be 150–200 words long, written in a professional tone, and targeted at a general audience. 
Include an introduction to explain the topic, a few key points with examples, and a conclusion summarizing the main ideas. 
Ensure the content is clear, concise, and free of jargon."
'''

artical_generation = PromptTemplate(
    input_variables=["text"],
    template=TEMPLATE
)

chain = LLMChain(llm=llm, prompt=artical_generation)

# Route to display the form
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route to handle form submission
@app.route("/generate_article", methods=["POST"])
def generate_article():
    topic = request.form.get("topic")

    if not topic:
        return jsonify({"error": "Topic is required!"}), 400

    # Generate the article
    output = chain.run(topic).strip()

    return render_template("index.html", article=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
