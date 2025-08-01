import streamlit as st
import json
from extract_tables import extract_table_patterns

st.set_page_config(page_title="DocPattern AI Agent", layout="wide")

st.title("📄 DocPattern AI Agent")
st.write("Upload a `.docx` file to extract repeating table patterns.")

uploaded_file = st.file_uploader("Upload Word Document (.docx)", type=["docx"])

if uploaded_file:
    with open("uploaded.docx", "wb") as f:
        f.write(uploaded_file.read())
    
    tables = extract_table_patterns("uploaded.docx")
    
    st.success(f"{len(tables)} tables found and processed.")

    for idx, tbl in enumerate(tables):
        st.subheader(f"🧩 Table {idx + 1} Pattern: {tbl['pattern']}")
        st.json(tbl["rows"])
    
    if st.button("Download JSON Output"):
        json_output = json.dumps(tables, indent=2)
        st.download_button("Download Table Data", json_output, file_name="table_patterns.json", mime="application/json")
