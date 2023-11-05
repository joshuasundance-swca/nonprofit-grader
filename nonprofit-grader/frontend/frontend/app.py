import streamlit as st

# Custom MongoDB-like styling
st.markdown("""
    <style>
    body {
        font-family: 'MongoDB', sans-serif; /* Replace with actual font if available */
        color: #01313f; /* MongoDB Dark Blue */
        background-color: #e8edf3; /* MongoDB Light Blue */
    }
    .sidebar .sidebar-content {
        background-color: #004051; /* MongoDB Dark Blue for Sidebar */
        color: white;
    }
    a {
        color: #01984C; /* MongoDB Green */
    }
    </style>
    """, unsafe_allow_html=True)

# Brief Page Content
def brief_page():
    st.title("Brief")
    st.subheader("About our team:")
    st.markdown("""
    - Joyce Li
    - Joshua Sundance
    - Leo Walker
    - Ambro Quach
    """)
    st.subheader("Mission Statement:")
    st.subheader("Solution:")
    st.subheader("Synopsis:")
    st.markdown("""
        - Ideation:
        - Design:
        - Implementation:
        - AI Usage:
        - Constraints:
        - Considerations:
        """)
    st.subheader("Causes We Care:")

# Application Page Content
def fetch_charities(interests):
    # Replace this with your actual function to get charities data
    charities_info = [
        {
            'name': 'Charity A',
            'mission': 'To save the bees.',
            'spending': '80% on programs, 20% on admin and fundraising.',
            'alignment': 'High'
        },
        # ...add more charities
    ]
    return charities_info

def application_page():
    st.title("What causes are you most passionate about?")

    # Text input
    text_input = st.text_input("Enter your interests")

    # Send button
    send_button = st.button('Send')

    # Initialize session state for storing charities info
    if 'charities_info' not in st.session_state:
        st.session_state['charities_info'] = []

    if send_button and text_input:
        # Fetch and store the charity info in session state
        st.session_state['charities_info'] = fetch_charities(text_input)

    # Check if there is any charity info in the session state to display
    if st.session_state['charities_info']:
        # Display each charity's information
        for charity in st.session_state['charities_info']:
            with st.container():
                st.subheader(charity['name'])
                st.text(f"Mission: {charity['mission']}")
                st.text(f"Spending: {charity['spending']}")
                st.text(f"Alignment with your interests: {charity['alignment']}")

# Conclusion Page Content
def conclusion_page():
    st.title("Conclusion")
    st.subheader("Goal:")
    st.subheader("Stretch:")

# Sidebar navigation with session state to remember the last active page
def main():
    st.sidebar.title("SF AI Hackathon")
    st.sidebar.header("Sponsored by: LangChain, LlamaIndex, Together.AI, MongoDB")
    st.sidebar.subheader("team { big dev nrg }")

    # Define session state key for the active page
    if 'active_page' not in st.session_state:
        st.session_state['active_page'] = 'Brief'

    # Update session state when a sidebar button is pressed
    if st.sidebar.button('Brief'):
        st.session_state['active_page'] = 'Brief'
    if st.sidebar.button('Application'):
        st.session_state['active_page'] = 'Application'
    if st.sidebar.button('Conclusion'):
        st.session_state['active_page'] = 'Conclusion'

    # Call the function associated with the current active page
    if st.session_state['active_page'] == 'Brief':
        brief_page()
    elif st.session_state['active_page'] == 'Application':
        application_page()
    elif st.session_state['active_page'] == 'Conclusion':
        conclusion_page()

# Run the main function to display the sidebar and associated page
main()
