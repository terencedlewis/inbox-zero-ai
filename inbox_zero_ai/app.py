import streamlit as st

from ai import analyze_message

st.set_page_config(page_title="Inbox Zero AI")

st.title("Inbox Zero AI")

user_input = st.text_area("Paste your email or message:")

if st.button("Analyze"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = analyze_message(user_input)
        st.markdown(result)
    else:
        st.warning("Please enter some text.")
