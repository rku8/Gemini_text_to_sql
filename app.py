from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## Configure genai key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Model
def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0], question])
    return response.text

## Function to retrieve query from database
def read_sql_query(sql, db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows 

## Define the prompt
prompt=[
    """
    You are an expert in converting the English questions into SQL query!
    The SQL database has the name STUDENT and has columns - NAME, CLASS, SECTION \n\n 
    For example, \n Example1 - How many entries of records are present?, the SQL command will be something like this 
    SELECT COUNT(*) FROM STUDENT;
    also the sql code should not have ``` in the beginning or end and sql word in output
    """
]

## Streamlit app
st.set_page_config(page_title ="I can retrieve any query")
st.header("Gemini app to retrieve SQL Data")
question = st.text_input("Input: ", key= 'input')
submit=st.button("Ask the question: ")
if submit:
    response = get_gemini_response(question, prompt)
    response = read_sql_query(response, "student.db")
    st.subheader("The response is: ")
    for row in response:
        print(row)
        st.header(row)