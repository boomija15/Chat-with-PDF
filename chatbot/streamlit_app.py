import streamlit as st
from chatbot_core import build_qa_chain

st.set_page_config(page_title="📄 PDF-Chatbot", layout="wide")
st.title("📄 Chat with your PDF")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# Clear chat
if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = []

# Build QA chain after file upload
if uploaded_file is not None:
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.session_state.qa_chain = build_qa_chain("temp_uploaded.pdf")
    st.success("✅ PDF uploaded and processed!")

# Question input
question = st.text_input("What would you like to know?", key="input")

# If question is asked and qa_chain is ready
if question:
    if st.session_state.qa_chain is not None:
        result = st.session_state.qa_chain({
            "question": question,
            "chat_history": st.session_state.chat_history
        })

        st.session_state.chat_history.append((question, result["answer"]))

        for i, (q, a) in enumerate(st.session_state.chat_history[::-1]):
            st.markdown(f"**❓ Question {len(st.session_state.chat_history) - i}:** {q}")
            st.markdown(f"**🤖 Answer:** {a}")
            sources = result.get("source_documents", [])
            for doc in sources:
                page_num = doc.metadata.get("page", None)
                if page_num is not None:
                    st.markdown(f"📄 Source: Page {page_num + 1}")
        st.markdown(f"📈 **Total Questions Asked:** {len(st.session_state.chat_history)}")
    else:
        st.warning("⚠️ Please upload a PDF before asking questions.")
