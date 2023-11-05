import streamlit as st

# Custom MongoDB-like styling (replace with actual MongoDB styles if available)
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
def application_page():
    def userInput():
        # Top card
        st.markdown("""
                        ### User Interests
                        This is the content of the third card.
                        - Detail 1
                        - Detail 2
                        """)

        st.title("Streamlit Input Widgets")

        # Text input
        text_input = st.text_input("Enter some text")

        # Text area
        text_area = st.text_area("Enter a lot of text")

        # Number input
        number_input = st.number_input("Enter a number")

        # Slider
        slider = st.slider("Choose a number", 0, 100)

        # Select slider
        select_slider = st.select_slider("Choose from a range", options=[1, 2, 3, 4, 5])

        # Checkbox
        checkbox = st.checkbox("Check for Yes")

        # Selectbox
        select = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])

        # Multiselect
        multiselect = st.multiselect("Choose multiple options", ["Option A", "Option B", "Option C"])

        # Radio button
        radio = st.radio("Choose an option", ["Option X", "Option Y", "Option Z"])

        # File Uploader
        uploaded_file = st.file_uploader("Upload a file")

        # Date input
        date_input = st.date_input("Select a date")

        # Time input
        time_input = st.time_input("Select a time")

        # Color picker
        color_picker = st.color_picker("Pick a color")

        # Display the input values (optional)
        st.write("Text input:", text_input)
        st.write("Text area:", text_area)
        st.write("Number input:", number_input)
        st.write("Slider:", slider)
        st.write("Select slider:", select_slider)
        st.write("Checkbox:", checkbox)
        st.write("Selectbox:", select)
        st.write("Multiselect:", multiselect)
        st.write("Radio button:", radio)
        st.write("File Uploader:", uploaded_file)
        st.write("Date input:", date_input)
        st.write("Time input:", time_input)
        st.write("Color picker:", color_picker)

    userInput()
    st.title("Application")
    st.markdown("""
            ### Process
            This is the content of the third card.
            - Detail 1
            - Detail 2
            """)
    # Top two cards using columns
    scoreCard, addInfo = st.columns(2)
    with scoreCard:
        st.markdown("""
            ### Score Card Ouput
            - Point 1
            - Point 2
            """)
        # You can add more content here, like charts, images, etc.

    with addInfo:
        st.markdown("""
            ### Additional Information
            This is the content of the second card.
            - Point 1
            - Point 2
            """)
        # Again, add more content as needed
    # Bottom card

    # Additional content for the third card can be added here

    st.write("This is the application page.")
# Conclusion Page Content
def conclusion_page():
    st.title("Conclusion")
    st.subheader("Goal:")
    st.subheader("Stretch:")
# Sidebar navigation
st.sidebar.title(" SF AI Hackathon")
st.sidebar.header("Sponsored by: LangChain, LlamaIndex, Together.AI, MongoDB")
st.sidebar.subheader("team { big dev nrg }")
if st.sidebar.button('Brief'):
    brief_page()
if st.sidebar.button('Application'):
    application_page()
if st.sidebar.button('Conclusion'):
    conclusion_page()



