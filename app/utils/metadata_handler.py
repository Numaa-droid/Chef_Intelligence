# utils/metadata_handler.py
from typing import List, Dict, Any
import pandas as pd

def df_to_docs(df: pd.DataFrame, text_col: str, meta_cols: List[str]) -> List[Dict[str, Any]]:
    docs = []
    for _, row in df.iterrows():
        text = str(row[text_col]) if pd.notna(row[text_col]) else ""
        if not text.strip():
            continue
        md = {c: (row[c] if c in row and pd.notna(row[c]) else "") for c in meta_cols}
        docs.append({"text": text, "metadata": md})
    return docs

