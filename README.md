# UCTER

Universal converter cli for me Why? i hate cloud

## Features

```
- pdf2png
- png2pdf
- webp2png
```

## Usage

- **pdf2png**: Convert pdf file to png image

```
usage: pdf2png.py [-h] [--no-name | --overwrite] input_pdf output_path
```

- **png2pdf**: Convert folder of images to pdf file

```
usage: png2pdf.py [-h] [--optimize] [--quality QUALITY]
                  input_folder output_path

options:
  --quality QUALITY  Image quality, on a scale from 1 (worst) to 95 (best).
```

- **webp2png**: Convert wepb image(s) file/folder to png file

```
usage: webp2png.py [-h] input_dir output_path
```

## Executable

Compile all features into `.exe` for Windows

```
./make.sh
```

## Contributing

Feel free to fix my error.

## Authors

* **Athicha Leksansern** - *Initial work* - [Tonkaew](https://github.com/tonkaew131)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details