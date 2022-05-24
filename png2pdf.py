from PIL import Image
import argparse
import os

OPTIMIZE_DPI = 144

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('--optimize', action='store_true', help='Optimize image quality')

parser.add_argument('--quality', type=int, help='Image quality, on a scale from 1 (worst) to 95 (best).', default=75)
parser.add_argument('input_folder', type=str, help='Path to image folder')
parser.add_argument('output_path', type=str, help='Output path')

args = parser.parse_args()
if args.output_path[-1] != '/':
    args.output_path += '/'

validFileExtension = ['.png', '.jpg']
def checkFileExtension(file):
    valid = False
    for ext in validFileExtension:
        if file.endswith(ext):
            valid = True
    return valid

imagesList = []
if os.path.isdir(args.input_folder):
    for file in sorted(os.listdir(args.input_folder)):
        if checkFileExtension(file):
            image = Image.open(os.path.join(args.input_folder, file))
            image = image.convert('RGB')

            if args.optimize:
                dpiX, dpiY = image.info['dpi']
                width, height = image.size

                newSize = (round(width*OPTIMIZE_DPI/dpiX), round(height*OPTIMIZE_DPI/dpiY))
                image = image.resize(newSize, resample=Image.Resampling.LANCZOS)
            imagesList.append(image)

optimize = False
resolutionX, resolutionY = imagesList[0].info['dpi']
if args.optimize:
    optimize = True
    resolutionX = OPTIMIZE_DPI
imagesList[0].save('{}.pdf'.format(os.path.join(args.output_path, os.path.dirname(args.input_folder))), save_all=True, append_images=imagesList[1:], optimize=optimize, resolution=resolutionX, quality=args.quality)