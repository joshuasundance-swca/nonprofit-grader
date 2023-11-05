import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage
from langchain.schema.runnable import RunnableMap
from langserve import RemoteRunnable

nonprofit = RemoteRunnable("http://backend-service:8084/nonprofit/")

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
    st.subheader("Problem Statement: ")
    st.markdown("In the midst of the largest wealth transfer in history, an estimated \$72.6 trillion passing to younger generations, donors are swamped by the choice of 1.3 million charities. Discerning which ones truly align with their values for impactful philanthropy is as formidable as finding a needle in a haystack, despite the $500 billion given annually.")
    st.subheader("Solution: ")
    st.markdown("Impact Aligner is an AI-powered platform that extracts and interprets complex data from charity filings. This innovative approach transforms cumbersome and expensive research into a seamless experience, empowering donors to effortlessly discover and contribute to organizations that genuinely contribute to impact goals they care most about. ")



# Application Page Content
def fetch_charities(interests: str) -> str:
    output = str(nonprofit.invoke({"query": str(interests)}))
    return output

def application_page():
    st.subheader("What causes are you most passionate about?")
    st.markdown("May you consider the following:")
    st.markdown(" - Climate Change, Environment, and Animals")
    # Text input
    text_input = st.text_input("Enter your interests", key="input")

    # Inline buttons
    button_container = st.container()
    button_container.markdown(
        """
        <style>
        .button-container {
            display: flex;
            justify-content: space-between;
            flex-direction: row;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with button_container:
        with st.container():
            # Send button
            if st.button('Send'):
                # Fetch and store the charity info in session state
                st.session_state['charities_info'] = fetch_charities(text_input)

    # Initialize session state for storing charities info
    if 'charities_info' not in st.session_state:
        st.session_state['charities_info'] = []

    # Check if there is any charity info in the session state to display
    if st.session_state['charities_info']:
        # Display each charity's information
        st.markdown(st.session_state.charities_info)

# Conclusion Page Content
def conclusion_page():
    st.subheader("Potential: ")
    st.markdown("In future iterations, we can enhance our AI platform to track and analyze charity filings over time, spotlighting performance and spotting irregularities. Our expanded metrics will include financial details like compensation and grants, offering donors a transparent view of a charity's genuine impact. This next step isn't just an upgrade—it's a leap towards a transparent, accountable philanthropy sector, aligning with the values of a new generation of donors.")

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
