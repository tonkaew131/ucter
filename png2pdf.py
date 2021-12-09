from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser()

# group = parser.add_mutually_exclusive_group()
# group.add_argument('--no-name', action='store_true', help='Remove pdf name')
# group.add_argument('--overwrite', action='store_true', help='Overwrite exists file')

parser.add_argument('input_folder', type=str, help='Path to image folder')
parser.add_argument('output_path', type=str, help='Output path')

args = parser.parse_args()
if args.output_path[-1] != '/':
    args.output_path += '/'

imagesList = []
if os.path.isdir(args.input_folder):
    for file in sorted(os.listdir(args.input_folder)):
        if file.endswith(".png"):
            image = Image.open(os.path.join(args.input_folder, file))
            image = image.convert('RGB')

            imagesList.append(image)

imagesList[0].save('{}.pdf'.format(os.path.join(args.output_path, os.path.dirname(args.input_folder))), save_all=True, append_images=imagesList[1:])