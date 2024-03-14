import streamlit as st
from langchain_community.callbacks.streamlit import (
    StreamlitCallbackHandler,
)
from agent import agent

st.title("Agente AI con datos Excel o CSV")
st.subheader("Ventas supermercado")

st_callback = StreamlitCallbackHandler(st.container())


if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent.invoke(
            {"input": prompt}, {"callbacks": [st_callback]}
        )
        st.write(response["output"])