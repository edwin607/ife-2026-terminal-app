"""
PDF Generator — IFE Facilitator Reference

Uses md2pdf to convert markdown files to production-ready PDFs.
Usage: python generate-pdfs.py [--all | --file path/to/file.md]
"""

import os, sys, glob
from md2pdf.core import md2pdf

SKILLS_DIR = os.path.dirname(os.path.abspath(__file__))

CSS_FILE = os.path.join(SKILLS_DIR, "pdf-theme.css")

def convert_md_to_pdf(md_path):
    name = os.path.splitext(os.path.basename(md_path))[0]
    pdf_path = os.path.join(os.path.dirname(md_path), f"{name}.pdf")
    print(f"  Converting {os.path.basename(md_path)} -> {name}.pdf ...", end=" ")
    import pathlib
    md2pdf(pathlib.Path(pdf_path), raw=None, md=pathlib.Path(md_path), css=pathlib.Path(CSS_FILE))
    size = os.path.getsize(pdf_path)
    print(f"OK ({size/1024:.0f} KB)")

if __name__ == "__main__":
    if "--file" in sys.argv:
        files = [sys.argv[sys.argv.index("--file") + 1]]
    else:
        files = sorted(glob.glob(os.path.join(SKILLS_DIR, "*.md")))

    if not files:
        print("No markdown files found.")
        sys.exit(1)

    for f in files:
        convert_md_to_pdf(f)

    print(f"\nDone. Generated {len(files)} PDF(s).")
