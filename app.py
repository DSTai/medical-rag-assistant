import os
import streamlit as st

from backend.rag_pipeline import MedicalRAG
from backend.build_index import build_index


st.set_page_config(
    page_title="Medical Research Assistant",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Medical Research Assistant")

st.markdown(
    "Ask questions about your medical research papers."
)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📄 Upload Papers")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF papers",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    os.makedirs("data", exist_ok=True)

    for file in uploaded_files:

        save_path = os.path.join(
            "data",
            file.name
        )

        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

    st.sidebar.success(
        f"{len(uploaded_files)} PDF(s) uploaded."
    )


if st.sidebar.button(
    "🔄 Build Knowledge Base"
):

    with st.spinner(
        "Building vector database..."
    ):

        build_index()

        st.session_state.rag = MedicalRAG()

    st.sidebar.success(
        "Knowledge base updated!"
    )
st.sidebar.markdown("---")

pdf_count = 0

if os.path.exists("data"):
    pdf_count = len(
        [
            f for f in os.listdir("data")
            if f.endswith(".pdf")
        ]
    )

st.sidebar.markdown("### 📚 Knowledge Base")

st.sidebar.metric(
    "Papers",
    pdf_count
)

st.sidebar.caption(
    "Embedding: BGE-small-en-v1.5"
)

st.sidebar.caption(
    "LLM: Gemini 2.5 Flash"
)

st.sidebar.caption(
    "Retriever: FAISS + Reranker"
)

st.sidebar.markdown("---")
# ==========================================
# SESSION
# ==========================================

if "rag" not in st.session_state:
    st.session_state.rag = MedicalRAG()

if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "selected_question" not in st.session_state:
    st.session_state.selected_question = None
# ==========================================
# CHAT HISTORY
# ==========================================

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.markdown(
            msg["content"]
        )

# ==========================================
# CHAT INPUT
# ==========================================

question = st.chat_input(
    "Ask a question..."
)

if st.session_state.selected_question:

    question = (
        st.session_state.selected_question
    )

    st.session_state.selected_question = None
st.markdown("### 💡 Example Questions")

if "selected_question" not in st.session_state:
    st.session_state.selected_question = None

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "What is asthma?",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "What is asthma?"
        )
        st.rerun()

    if st.button(
        "What sensors are used for lung sound analysis?",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "What sensors are used for lung sound analysis?"
        )
        st.rerun()

with col2:

    if st.button(
        "How is wheeze detected?",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "How is wheeze detected?"
        )
        st.rerun()

    if st.button(
        "What machine learning models are proposed?",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "What machine learning models are proposed?"
        )
        st.rerun()
if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching papers..."
        ):

            result = (
                st.session_state.rag
                .ask_with_contexts(question)
            )

        answer = result["answer"]
        docs = result["docs"]

        st.markdown(answer)

        st.markdown("---")
        st.markdown("### Sources")

        for i, doc in enumerate(docs):

            page = (
                doc.metadata.get(
                    "page",
                    0
                ) + 1
            )

            source = doc.metadata.get(
                "source",
                "Unknown PDF"
            )

            with st.expander(
                f"[{i+1}] {source} - Page {page}"
            ):

                st.write(
                    doc.page_content[:1000]
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )