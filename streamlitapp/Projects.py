import streamlit as st

st.set_page_config(page_title="Projects", page_icon="🚀", layout="centered")

st.header("Projects")

st.write("I’ll add detailed projects here soon, including: ")

projects = [
    "🌟 Brain MRI Segmentation",
    "🤖 Clinical RAG assistant pipelines",
    "📄 Protocol generation with LLMs",
    "🚗 Autonomous vehicle steering angle prediction",
    "👁️‍🗨️ Real-time vision proctoring system"
]

for project in projects:
    st.write(f"- {project}")

st.info("Detailed project cards with images & links will be added later.")
