#Create the user interface for file upload and querying
import streamlit as st
from graph.workflow import workflow
from ingestions.document_loader import (
    load_pdf,
    load_txt,
    load_csv,
    load_excel
)
from ingestions.vector_store import create_vector_store

st.title("Agentic Banking Knowledge Assistant")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "txt", "csv", "xlsx"]
)

if uploaded_file:
    if uploaded_file.name.endswith("pdf"):
        text = load_pdf(uploaded_file)
    elif uploaded_file.name.endswith("txt"):
        text = load_txt(uploaded_file)
    elif uploaded_file.name.endswith("csv"):
        text = load_csv(uploaded_file)
    else:
        text = load_excel(uploaded_file)
    
    create_vector_store(text)
    st.success("Document indexed successfully")

question = st.text_input("Ask a question")

if st.button("Submit"):
    result = workflow.invoke(
        {"question": question}
    )
    st.subheader("Answer")
    st.write(result["answer"])
    st.subheader("Validation")
    st.write(result["validation"])