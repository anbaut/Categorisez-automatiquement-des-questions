import streamlit as st

def main():
    
    st.title("Tags prediction")
    menu = ["Content Based prediction"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Summerization")
        raw_text = st.text_area("Enter Text Here")
        if st.button("Summarize"):
            st.write(raw_text)
    else:
        st.subheader("About")


if __name__ == '__main__':
    main()