import requests
import streamlit as st
from propublica import latest_pdf

__version__ = "0.0.1"

# --- Initialization ---
st.set_page_config(
    page_title=f"nonprofit-grader v{__version__}",
    page_icon="🦜",
)


def st_init_null(*variable_names) -> None:
    for variable_name in variable_names:
        if variable_name not in st.session_state:
            st.session_state[variable_name] = None

st_init_null("org_name", "org_pdf")

st.session_state.org_name = st.text_input("Organization Name", value="")

def show_pdf(pdf_content: bytes) -> None:
    base64_pdf = base64.b64encode(pdf_content).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

if st.session_state.org_name:
    st.session_state.org_name = st.session_state.org_name.strip()
    st.session_state.org_pdf = latest_pdf(st.session_state.org_name)
    st.markdown(f"Latest 990 PDF: [{st.session_state.org_pdf}]({st.session_state.org_pdf})")

    response = requests.get(st.session_state.org_pdf)
    content = response.content
    
    show_pdf(content)
    

show_pdf('post1-compressed.pdf')