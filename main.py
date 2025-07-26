import re
import json
from PyPDF2 import PdfReader

def extract_outline(pdf_path):
    reader = PdfReader(pdf_path)
    outline = []
    title = ""
    heading_patterns = {
        "H1": re.compile(r"^[A-Z][A-Za-z\s]{3,}$"),
        "H2": re.compile(r"^[A-Z][a-z]+\s[A-Z][a-z]+"),
        "H3": re.compile(r"^\d+(\.\d+)*\s.+")
    }

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not title and len(line.split()) > 3 and line.istitle():
                title = line
            elif heading_patterns["H1"].match(line):
                outline.append({"level": "H1", "text": line, "page": i + 1})
            elif heading_patterns["H2"].match(line):
                outline.append({"level": "H2", "text": line, "page": i + 1})
            elif heading_patterns["H3"].match(line):
                outline.append({"level": "H3", "text": line, "page": i + 1})

    return {
        "title": title,
        "outline": outline
    }

if __name__ == "__main__":
    import sys
    from pathlib import Path

    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in input_dir.glob("*.pdf"):
        output = extract_outline(str(pdf_file))
        output_file = output_dir / (pdf_file.stem + ".json")
        with open(output_file, "w") as f:
            json.dump(output, f, indent=2)
