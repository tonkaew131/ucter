# UCTER

Universal converter cli for me xD

## Features

```
- pdf2png
- png2pdf

*not working properly
```

## Usage

- pdf2png: Convert pdf file to png image

```
usage: pdf2png.py [-h] [--no-name | --overwrite] input_pdf output_path

positional arguments:
  input_pdf    Path to pdf file
  output_path  Output path

optional arguments:
  -h, --help   show this help message and exit
  --no-name    Remove pdf name
  --overwrite  Overwrite exists file
```

- png2pdf: Convert folder of images to pdf file

```
usage: png2pdf.py [-h] [--optimize] [--quality QUALITY]
                  input_folder output_path

positional arguments:
  input_folder       Path to image folder
  output_path        Output path

optional arguments:
  -h, --help         show this help message and exit
  --optimize         Optimize image quality
  --quality QUALITY  Image quality, on a scale from 1 (worst) to 95 (best).
```

## Executable

Create folder `poppler` inside project, then paste all poppler binary in it. When converting, use 

```
pyinstaller filename.py -F --add-data "./poppler/*;./poppler" --noupx
```

## Contributing

Feel free to fix my error.

## Authors

* **Athicha Leksansern** - *Initial work* - [Tonkaew](https://github.com/tonkaew131)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details