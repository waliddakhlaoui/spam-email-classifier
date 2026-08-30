import streamlit as st
from prediction import predict_email
st.title("--------SPAMGUARD--------")
st.write("enter an email below and the model will classify it as spam or ham")
email=st.text_area("email:",height=200,placeholder="paste your email here...")
if st.button("classify email"):
    if email.strip()=="":
        st.warning ("please enter an email.")
    else:
        prediction=predict_email(email)
        if prediction=="SPAM":
            st.error("SPAM")
        else:
            st.success("HAM")
            