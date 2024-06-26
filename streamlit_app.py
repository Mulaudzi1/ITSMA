import streamlit as st
import requests

st.title('Customer Feedback System')

user = st.text_input('User:')
message = st.text_area('Message:')
if st.button('Submit'):
    response = requests.post('http://localhost:3000/api/feedback', json={'user': user, 'message': message})
    if response.status_code == 201:
        st.success('Feedback submitted successfully')
    else:
        st.error('Error submitting feedback')

feedbacks = requests.get('http://localhost:3000/api/feedback').json()
st.write('## Feedbacks')
for feedback in feedbacks:
    st.write(f"**{feedback['user']}**: {feedback['message']}")
