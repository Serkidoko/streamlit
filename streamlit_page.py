import streamlit as st

def main():
    # Trang đăng nhập
    if "logged_in" not in st.session_state:
        login_page()
    # Trang tải lên tệp
    else:
        upload_file_page()

def login_page():
    st.title("Trang đăng nhập")
    username = st.text_input("Tài khoản")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if username == "admin" and password == "1234":
            st.success("Đăng nhập thành công!")
            st.session_state.logged_in = True
        else:
            st.error("Tài khoản hoặc mật khẩu không đúng. Vui lòng thử lại.")

def upload_file_page():
    st.title("Trang tải lên tệp")
    uploaded_file = st.file_uploader("Tải lên tệp CSV", type=['csv'])
    if uploaded_file is not None:
        st.write("Dữ liệu đã tải lên:")
        st.write(uploaded_file.getvalue().decode())

if __name__ == "__main__":
    main()
