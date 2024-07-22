from streamlit_navigation_bar import st_navbar
import os
def set_front_page(st):
    # st.logo('logo.jpg')
    st.set_page_config(page_title="Maya", page_icon= "logo.png")
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(parent_dir, "logo.svg")
    st_navbar(
    logo_path= logo_path,
    pages= [ 'Maya'] 
    # menu_title="Your App Title",  # Optional
    # menu_icon="house",           # Optional, use an icon from Bootstrap Icons
    # menu_items=[
    #     {"label": "Home", "icon": "house"},
    #     {"label": "About", "icon": "info-circle"},
    # ]
)
    load_css("styles.css" , st)
    st.session_state.greeting_shown = True
    

def load_css(file_path , st):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)