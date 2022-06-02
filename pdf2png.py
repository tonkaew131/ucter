import fitz  # PyMuPDF
import argparse
import shutil
import os

DEFAULT_DPI = 300

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('--no-name', action='store_true', help='Remove pdf name')
group.add_argument('--overwrite', action='store_true',
                   help='Overwrite exists file')

parser.add_argument('input_pdf', type=str, help='Path to pdf file')
parser.add_argument('output_path', type=str, help='Output path')

args = parser.parse_args()
if args.output_path[-1] != '/':
    args.output_path += '/'

base = os.path.basename(args.input_pdf)
print(f'Opening {base} pdf file...')

document = fitz.open(args.input_pdf)
pageCount = document.page_count

fileName = ''
if not args.no_name:
    fileName = os.path.splitext(base)[0]

if not os.path.isdir(args.output_path):
    os.makedirs(args.output_path)

isError = False
for i in range(pageCount):
    name = ''
    if args.no_name:
        name = str(i+1) + '.png'
    else:
        name = '{}-{}.png'.format(fileName, str(i+1))

    if (os.path.isfile(name)) and (not args.overwrite):
        print(f'\nFailed to convert {name}, already exists')
        isError = True
        break

    page = document.load_page(0)
    image = page.get_pixmap(matrix=fitz.Matrix(DEFAULT_DPI/72, DEFAULT_DPI/72))
    image.save(name, 'PNG')
    print(f'{name} converted')

    if (os.getcwd() != os.path.realpath(args.output_path)) and (os.path.isfile(os.path.join(args.output_path, name))) and (not args.overwrite):
        print(f'\nFailed to move {name}, already exists')
        isError = True
        break

    if(args.overwrite):
        shutil.move(os.path.join(os.getcwd(), name),
                    os.path.join(args.output_path, name))
        continue

    if os.getcwd() != os.path.realpath(args.output_path):
        shutil.move(name, args.output_path)

if not isError:
    print(f'\n{pageCount} Files converted')
