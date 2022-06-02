total=3

printf '[1/'$total'] Compiling pdf2png.py ...\n'
python -m PyInstaller pdf2png.py -F --clean --noupx
printf '[1/'$total'] Done.\n\n\n\n\n'

printf '[2/'$total'] Compiling png2pdf.py...\n'
python -m PyInstaller png2pdf.py -F --clean --noupx
printf '[2/'$total'] Done.\n\n\n\n\n'

printf '[3/'$total'] Compiling webp2png.py...\n'
python -m PyInstaller webp2png.py -F --clean --noupx
printf '[3/'$total'] Done.\n\n\n\n\n'