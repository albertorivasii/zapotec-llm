from pdf2image import convert_from_path
import os
from tqdm import tqdm

os.chdir(r"C:\Users\thesm\Documents\Personal Website\zapotec-llm\data")

texts= ["pdfs/zav_Interlinear_texts_I.pdf", "pdfs/zav_Interlinear_texts_II.pdf", "pdfs/zav_Interlinear_texts_III.pdf", "pdfs/zav_Interlinear_texts_IV.pdf"]

for i, pdf in enumerate(tqdm(texts, desc="PDFs"), start=1):
    pages= convert_from_path(pdf)
    for j, page in enumerate(tqdm(pages, desc=f"Pages in text {i}", leave=False), start=1):
        img_path= f"images/text_{i}_page_{j}.png"
        page.save(img_path, "PNG")