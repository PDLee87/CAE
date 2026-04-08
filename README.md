**CAM-CAPE Similarity Analysis**

**Overview**
This project calculates text similarity between SAP (Significant Accounting Matters) and CAE (Critical Accounting Policies and Estiamte) using two methods:
1. Cosine Similarity via TF-IDF
2. Semantic Similarity via Sentence Transformers (all-MiniLM-L6-v2)
The script reads an Excel file containing CIK_fical year (in column A); SAP texts (in columns B to Q, depending on how long SAP description is due to the text limit in a cell in Excel); and CAE text (in columns R-T), computes similarity scores, and saves the results in a new Excel file.


**Installation & Dependencies**
This project requires Python and the following libraries:
pandas
scikit-learn
sentence-transformers
tqdm
openpyxl

To install the required dependencies, run:
```pip install pandas scikit-learn sentence-transformers tqdm openpyxl```

**Usage**
1. Place your input Excel file in the specified directory.
2. Update the input_dir and input_file variables in the script.
3. Run the script:
```python similarity_analysis.py```
4. The output Excel file will be saved with similarity scores.

**Output**
The resulting file includes:
1. Cosine_Similarity: A score based on TF-IDF vectorization.
2. Semantic_Similarity: A score based on Sentence Transformers.
