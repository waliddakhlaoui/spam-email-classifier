import streamlit as st
from prediction import predict_email

st.title("--------SPAMGUARD--------")
st.write("Enter an email below and the model will classify it as spam or ham")
email = st.text_area(
    "Email:",
    height=200,
    placeholder="Paste your email here...",
    key="email_input"
)
if st.button("Classify email"):

    if email.strip() == "":
        st.warning("Please enter an email.")
    else:
        prediction = predict_email(email)
        if prediction == "SPAM":
            st.error("🚨 SPAM")
        else:
            st.success("✅ LEGITIMATE")
def clear_email():
    st.session_state.email_input = ""

if st.button("Clear", on_click=clear_email):
    pass
