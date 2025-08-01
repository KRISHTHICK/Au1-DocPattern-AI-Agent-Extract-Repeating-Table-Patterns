from docx import Document
from utils import detect_value_type

def extract_table_patterns(doc_path):
    doc = Document(doc_path)
    table_data = []

    for table_idx, table in enumerate(doc.tables):
        pattern = []
        table_json = {
            "table_index": table_idx,
            "rows": []
        }

        for row_idx, row in enumerate(table.rows):
            row_content = []
            for cell in row.cells:
                text = cell.text.strip()
                value_type = detect_value_type(text)
                row_content.append({
                    "text": text,
                    "type": value_type
                })
            table_json["rows"].append(row_content)
            if row_idx == 0:
                pattern = [cell["type"] for cell in row_content]

        table_json["pattern"] = pattern
        table_data.append(table_json)

    return table_data
