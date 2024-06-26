import streamlit as st
import requests

st.title('Customer Feedback System')
st.title('We will get back to you as soon as possible ')

BASE_URL = 'http://localhost:3000/api'

def submit_feedback(user, message):
    try:
        response = requests.post(f'{BASE_URL}/feedback', json={'user': user, 'message': message})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error submitting feedback: {e}")
        return None

def get_feedbacks():
    try:
        response = requests.get(f'{BASE_URL}/feedback')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching feedback: {e}")
        return []

user = st.text_input('User:')
message = st.text_area('Message:')
if st.button('Submit'):
    if user and message:
        feedback = submit_feedback(user, message)
        if feedback:
            st.success('Feedback submitted successfully')
    else:
        st.warning('Please provide both user and message.')

st.write('## Feedbacks')

feedbacks = get_feedbacks()
if feedbacks:
    filter_user = st.text_input('Filter by user:')
    filtered_feedbacks = [f for f in feedbacks if filter_user.lower() in f['user'].lower()] if filter_user else feedbacks

    for feedback in filtered_feedbacks:
        st.write(f"**{feedback['user']}**: {feedback['message']} (Submitted on {feedback['created_at']})")
