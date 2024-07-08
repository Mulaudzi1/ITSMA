import streamlit as st
import requests

st.title('Service-Oriented Architecture (SOA) System')

# Function to fetch services from the backend
def get_services():
    response = requests.get('http://localhost:5000/services')
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch services')
        return []

# Function to fetch a single service by ID
def get_service(service_id):
    response = requests.get(f'http://localhost:5000/service/{service_id}')
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch service')
        return None

# Display all services
st.header('Available Services')
services = get_services()
for service in services:
    st.subheader(service['name'])
    st.write(service['description'])

# Input for service ID to fetch details
service_id = st.number_input('Enter service ID to fetch details', min_value=1)
if st.button('Get Service Details'):
    service = get_service(service_id)
    if service:
        st.subheader(service['name'])
        st.write(service['description'])

