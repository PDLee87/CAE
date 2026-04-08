import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

# --- Similarity Functions ---

def jaccard_similarity(text1, text2):
    if not text1 or not text2:
        return 0
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union) if union else 0

def tfidf_cosine_similarity(text1, text2):
    if not text1 or not text2:
        return 0
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

def semantic_similarity(text1, text2):
    if not text1 or not text2:
        return 0
    embeddings = model.encode([text1, text2])
    return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

# Load semantic model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# --- Main Processing Function ---
def process_excel_file(input_dir, file_name):
    file_path = os.path.join(input_dir, file_name)
    df = pd.read_excel(file_path)

    # Define column ranges
    sap_cols = df.columns[1:17]  # B to Q
    cae_cols = df.columns[17:20]  # R to T

    # Combine the text columns
    sap_texts = df[sap_cols].astype(str).fillna('').agg(' '.join, axis=1).str.strip()
    cae_texts = df[cae_cols].astype(str).fillna('').agg(' '.join, axis=1).str.strip()

    # Compute similarities
    tfidf_scores, semantic_scores, jaccard_scores = [], [], []

    for sap, cae in tqdm(zip(sap_texts, cae_texts), total=len(df), desc=file_name):
        tfidf_scores.append(tfidf_cosine_similarity(sap, cae))
        semantic_scores.append(semantic_similarity(sap, cae))
        jaccard_scores.append(jaccard_similarity(sap, cae))

    # Build result DataFrame
    result_df = pd.DataFrame({
        'Row': df.index,
        'SAP_Text': sap_texts,
        'CAE_Text': cae_texts,
        'TFIDF_Similarity': tfidf_scores,
        'Semantic_Similarity': semantic_scores,
        'Jaccard_Similarity': jaccard_scores
    })

    # Save new file
    base_name = os.path.splitext(file_name)[0]
    output_file = os.path.join(input_dir, f"14. {base_name}_similarity.xlsx")
    result_df.to_excel(output_file, index=False)
    print(f"✅ Saved similarity scores to: {output_file}")

# ---- USER INPUT HERE ----
if __name__ == "__main__":
    # ✅ CHANGE THESE TWO LINES BELOW:
    input_directory = r"INPUT YOUR FILE DIRECTORY"
    excel_file_name = "INPUT YOUR EXCEL FILE NAME.xlsx"

    process_excel_file(input_directory, excel_file_name)

