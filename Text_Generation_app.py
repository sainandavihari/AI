import streamlit as slt
import os
os.environ['GEMINI_API_KEY']='AIzaSyCPClqlqYgRmQEJcIr5AtBbuRNjpQUJYU0'
slt.title("Text Generation  App using Gemini AI")
slt.write("This app generates responses to your questions")
import google. generativeai as genai


genai.configure(api_key='AIzaSyCPClqlqYgRmQEJcIr5AtBbuRNjpQUJYU0')

input_prompt = slt.text_input(
    label="Enter your prompt:",
    placeholder="Ask me anything..."
)
if slt.button("Generate Response"):
    with slt.spinner("Generating response..."):
        model=genai.GenerativeModel('gemini-2.0-flash')
        response=model.generate_content(input_prompt)
        slt.success("Response:")
        slt.write(response.text)
slt.markdown('____')
slt.write("Built By Vihari")