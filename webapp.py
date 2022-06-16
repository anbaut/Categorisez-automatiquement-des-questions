import streamlit as st

def main():
    
    st.title("Tags prediction")
    menu = ["Content Based prediction"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Content Based prediction":
        st.subheader("Content Based prediction")
        title = st.text_area("Title")
        body = ("Body")
        if st.button("Predict Tags"):
            full_text = title + " " + body
            st.write(full_text)
    else:
        st.subheader("About")


if __name__ == '__main__':
    main()