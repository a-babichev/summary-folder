import os
from utils import extract_text_from_image, extract_text_from_pdf

def load_files_from_folder(folder_path: str) -> str:
    all_content = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            extension = file.lower().split(".")[-1]

            print(f"Processing: {file}")

            if extension in ["jpg", "jpeg", "png", "webp"]:
                content = extract_text_from_image(file_path)

            elif extension == "pdf":
                content = extract_text_from_pdf(file_path)

            else:
                continue

            if content.strip():
                all_content.append(
                    f"\n\n===== FILE: {file} =====\n{content}"
                )

    return "\n".join(all_content)
