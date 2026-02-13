import os
import sys
from file_loader import load_files_from_folder
from summarizer import summarize_text

def main(folder_path=None):

    if folder_path is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(current_dir, "data")

    print("Loading files...")
    content = load_files_from_folder(folder_path)

    print("Generating summary...")
    summary = summarize_text(content)

    print("\n===== SUMMARY =====\n")
    print(summary)

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else None
    main(folder)
