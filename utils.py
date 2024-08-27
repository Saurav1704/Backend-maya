
import os

def set_front_page(session_state):
    # Any Flask-specific setup can go here, but you don't need `set_page_config`
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(parent_dir, "logo.svg")

    

def load_css(file_path , st):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)