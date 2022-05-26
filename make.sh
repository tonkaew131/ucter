pyinstaller pdf2png.py -F --add-data "./poppler/*;./poppler" --noupx
pyinstaller png2pdf.py -F --noupx
pyinstaller webp2png.py -F --noupx