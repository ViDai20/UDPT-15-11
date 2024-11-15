import streamlit as st

# Initialize session state for user management
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'user_state' not in st.session_state:
    st.session_state.user_state = {
        'username': '',
        'logged_in': False
    }

# Page selection
page = st.sidebar.selectbox("Choose Action", ["Register", "Login"])

# Registration page
if page == "Register":
    st.title("User Registration")
    reg_username = st.text_input("Choose a Username")
    reg_password = st.text_input("Choose a Password", type="password")
    reg_confirm_password = st.text_input("Confirm Password", type="password")
    register_button = st.button("Register")

    if register_button:
        if reg_password != reg_confirm_password:
            st.error("Passwords do not match!")
        elif reg_username in st.session_state.user_data:
            st.error("Username already exists!")
        else:
            # Register the new user
            st.session_state.user_data[reg_username] = reg_password
            st.success("Registration successful! You can now log in.")

# Login page
if page == "Login":
    st.title("User Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        # Check credentials
        if (login_username in st.session_state.user_data and
                st.session_state.user_data[login_username] == login_password):
            st.session_state.user_state['username'] = login_username
            st.session_state.user_state['logged_in'] = True
            st.success(f"Welcome {login_username}!")
        else:
            st.error("Invalid username or password!")

# Logged-in state
if st.session_state.user_state['logged_in']:
    st.write("Welcome to the app!")
    st.write(f"You are logged in as: {st.session_state.user_state['username']}")
    logout_button = st.button("Logout")
    if logout_button:
        st.session_state.user_state['logged_in'] = False
        st.session_state.user_state['username'] = ''
        st.write("You have been logged out.")
