from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('input_dir', type=str, help='Path to image file/folder')
parser.add_argument('output_path', type=str, help='Output path')

args = parser.parse_args()
if args.output_path[-1] != '/':
    args.output_path += '/'


def save(file):
    if not file.endswith('.webp'):
        return

    image = Image.open(os.path.join(file))
    image = image.convert('RGB')

    file = file[:(len(file) - len('.webp'))]
    outputDir = os.path.join(args.output_path, file)
    outputDir += '.png'

    print(f'- {file}.webp converted')
    image.save(outputDir)


if os.path.isdir(args.input_dir):
    for file in os.listdir(args.input_dir):
        save(os.path.join(args.input_dir, file))

    print(f'\n{len(os.listdir(args.input_dir))} Files converted')
else:
    save(args.input_dir)
