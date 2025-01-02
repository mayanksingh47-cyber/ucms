import streamlit as st
import openai
import pandas as pd

# Set the OpenAI API key
openai.api_key = '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'

# Load the Excel file
file_path = "issues.xlsx"
df = pd.read_excel(file_path)

# Function to generate responses from the language model
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Use "gpt-4" if you have access
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

# Streamlit interface
st.title("Mayank's UCMS GPT")

# Input text box
user_input = st.text_input("You:", "")

# Display past conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

if st.button("Send"):
    if user_input:
        # Add user input to conversation history
        st.session_state.conversation.append({"role": "user", "text": user_input})

        # Generate response
        response_text = generate_response(user_input)

        # Add response to conversation history
        st.session_state.conversation.append({"role": "assistant", "text": response_text})

# Display the conversation history
for entry in st.session_state.conversation:
    if entry['role'] == 'user':
        st.text_area("User", entry['text'], height=100, disabled=True)
    else:
        st.text_area("ChatGPT", entry['text'], height=100, disabled=True)

# Option to clear the conversation
if st.button("Clear"):
    st.session_state.conversation = []
