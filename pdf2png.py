from pdf2image import convert_from_path
import argparse
import shutil
import sys
import os

# https://stackoverflow.com/a/56431948
def current_path(dir_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, dir_path)
    return os.path.join(".", dir_path)


parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('--no-name', action='store_true', help='Remove pdf name')
group.add_argument('--overwrite', action='store_true', help='Overwrite exists file')

parser.add_argument('input_pdf', type=str, help='Path to pdf file')
parser.add_argument('output_path', type=str, help='Output path')

args = parser.parse_args()
if args.output_path[-1] != '/':
    args.output_path += '/'

os.environ['PATH'] += os.pathsep + os.pathsep.join([current_path('poppler')])

images = convert_from_path(args.input_pdf)
fileName = ''
if not args.no_name:
    base=os.path.basename(args.input_pdf)
    fileName = os.path.splitext(base)[0]

if not os.path.isdir(args.output_path):
    os.makedirs(args.output_path)

isError = False
for i in range(len(images)):
    name = ''
    if args.no_name:
        name = str(i+1) +'.png'
    else:
        name = '{}-{}.png'.format(fileName, str(i+1))

    if (os.path.isfile(name)) and (not args.overwrite):
        print('Failed to convert {}, already exists'.format(name))
        isError = True
        break
    images[i].save(name, 'PNG')

    if (os.getcwd() != os.path.realpath(args.output_path)) and (os.path.isfile(os.path.join(args.output_path, name))) and (not args.overwrite):
        print('Failed to move {}, already exists'.format(name))
        isError = True
        break

    if(args.overwrite):
        shutil.move(os.path.join(os.getcwd(), name), os.path.join(args.output_path, name))
        continue

    if os.getcwd() != os.path.realpath(args.output_path):
        shutil.move(name, args.output_path)

if not isError:
    print('Converted {} files'.format(len(images)))
