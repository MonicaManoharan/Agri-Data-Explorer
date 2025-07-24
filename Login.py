# import streamlit as st

# users = {
#     "farmer": {"password": "farmer123", "role": "Farmer"},
#     "policymaker": {"password": "policy123", "role": "Policymaker"},
#     "researcher": {"password": "research123", "role": "Researcher"}
# }

# # https://static.vecteezy.com/system/resources/previews/031/696/054/large_2x/sprawling-agricultural-farm-featuring-fields-of-crops-ai-generated-photo.jpg");
# def login():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-image: url("https://img.freepik.com/premium-photo/spring-grain-concept-agriculture-healthy-eating-organic-food-generative-ai_58409-32489.jpg");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }
        
#         h1 {
#             color: black !important;
#         }

#         /* Label color (Username, Password) */
#         label {
#             color: black !important;
#             font-weight: bold;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # st.image("assets/header_image.png", use_container_width=True)
#     st.title("AgriData Explorer - Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     if st.button("Login"):
#         user = users.get(username)
#         if user and user["password"] == password:
#             st.session_state["logged_in"] = True
#             st.session_state["role"] = user["role"]
#         else:
#             st.error("Invalid username or password")
import streamlit as st

users = {
    "farmer": {"password": "farmer123", "role": "Farmer"},
    "policymaker": {"password": "policy123", "role": "Policymaker"},
    "researcher": {"password": "research123", "role": "Researcher"}
}

def login():
    st.set_page_config(layout="wide", page_title="AgriData Explorer - Login", page_icon="🌾")

    # Custom CSS for background and styling
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background-image: url("https://img.freepik.com/premium-photo/spring-grain-concept-agriculture-healthy-eating-organic-food-generative-ai_58409-32489.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        

        label {
            color: black !important;
            font-weight: bold;
        }

        .stTextInput > div > div > input {
            background-color: white !important;
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Center the login form
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        # st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<h2 style="color:black; text-align:center;">AgriData Explorer - Login</h2>', unsafe_allow_html=True)

        # st.markdown("## AgriData Explorer - Login")
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")

        if login_button:
            user = users.get(username)
            if user and user["password"] == password:
                st.session_state.logged_in = True
                st.session_state.role = user["role"]
                st.success(f"Welcome, {user['role']}!")
                st.rerun()  # rerun to trigger dashboard
            else:
                st.error("Invalid username or password")
        st.markdown('</div>', unsafe_allow_html=True)
