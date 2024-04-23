import streamlit as st
import os

def main():
    if "logged_in" not in st.session_state:
        login_page()
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
            st.experimental_rerun()
        else:
            st.error("Tài khoản hoặc mật khẩu không đúng. Vui lòng thử lại.")

def upload_file_page():
    st.title("Trang tải lên và danh sách tệp")

    uploaded_file = st.file_uploader("Tải lên tệp", type=['csv', 'docx', 'pptx'])
    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)

    file_categories = st.multiselect("Chọn loại file", ['csv', 'docx', 'pptx'], default=['csv', 'docx', 'pptx'])
    list_uploaded_files(file_categories)

def save_uploaded_file(uploaded_file):
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Đã lưu tệp {uploaded_file.name} thành công!")

def list_uploaded_files(file_categories):
    st.title("Danh sách tệp đã tải lên")
    if os.path.exists("uploads"):
        files = os.listdir("uploads")
        for file in files:
            file_extension = file.split(".")[-1].lower()
            if file_extension in file_categories:
                st.write(file)
                download_button = download_file(file)
    else:
        st.write("Chưa có tệp nào được tải lên.")

def download_file(file_name):
    file_path = os.path.join("uploads", file_name)
    with open(file_path, "rb") as f:
        file_contents = f.read()
    st.download_button(label="download file", data=file_contents, file_name=file_name)

if __name__ == "__main__":
    main()
