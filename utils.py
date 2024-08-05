from streamlit_navigation_bar import st_navbar
import os
def set_front_page(st):
    st.set_page_config(initial_sidebar_state="collapsed")
    # st.logo('logo.jpg')
    # st.set_page_config(page_title="Maya", page_icon= "logo.png")
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(parent_dir, "logo.svg")
    styles = {
    "nav": {
        "background-color": "rgb(250,250,250)",
        "height": '2.875rem',
        "justify-content": "flex-start",
    },
    "div": {
        "max-width": "32rem",
    },
    "ul" :{
        "display":"flex",
        "justify-content": "flex-start",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
        # "height": '2.5rem',
    },
    "img" :{
        "height": '2.875rem',
        "border-radius": "15%",
    },
}
    # style = {
    #     "nav" : {
    #               "align-items": "center";
    #               "display": "flex-start";
    #               "height": '2.875rem';
    #               "background-color": "rgb(250, 250, 250)";
    #     }
    # }0
    st_navbar(
    logo_path= logo_path,
    styles= styles,
    pages = ['Maya']
    )
    # st.write(page )
    # menu_title="Your App Title",  # Optional
    # menu_0icon="house",           # Optional, use an icon from Bootstrap Icons
    # menu_items=[
    #     {"label": "Home", "icon": "house"},
    #     {"label": "About", "icon": "info-circle"},
    # ]
    # st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">' ,unsafe_allow_html = True )
    # st.markdown(
    #     """<nav class="navbar bg-body-tertiary">
    #             <div class="container-fluid">
    #                 <a class="navbar-brand" href="#">
    #                 <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
    #                 </a>
    #             </div>
    #         </nav>""" , unsafe_allow_html = True
    # )
    load_css("style.css" , st)
    st.session_state.greeting_shown = True
    

def load_css(file_path , st):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)