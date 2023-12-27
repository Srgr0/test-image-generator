# test-image-generator
Generate images of the specified size.

## Features
- Any size, any quantity
- metadata removal and lossless compression do not work

## Requirements
- Python (3.x)
- PIL (Python Imaging Library)
- NumPy

## Usage
#### Download
```
wget https://raw.githubusercontent.com/Srgr0/test-image-generator/main/generate.py
```
#### Run
Replace the placeholders with the appropriate values:

- base_path(-b, --base_path): The directory where the images will be saved. For example, use `./` to save in the current directory.
- size_in_MB(-s, --size): The target size of each image in megabytes. For example, `10` for 10MB images.
- number_of_images(-n, --num): The number of images you want to generate. For example, `100` to generate 100 images.
```
python ./generate.py -b ./ -s 10 -n 100
```
