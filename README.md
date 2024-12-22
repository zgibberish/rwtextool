# Rotwood TEX Tool

KTEX texture packer+converter for Rotwood

## Requirements

- Python
- `PyTexturePacker` and `pillow` Python modules

## Usage

### Packing PNGs into TEX+XML

```shell
usage: img2tex.py [-h] source_path

Packs a directory of PNG images into Rotwood Klei TEX textures and atlases.

positional arguments:
  source_path  Directory of PNG files

options:
  -h, --help   show this help message and exit
```

### Unpacking TEX+XML to PNGs

```shell
usage: tex2img.py [-h] [-A] [-a ATLAS_PATH] tex_path

Unpacks a Rotwood Klei TEX file (and XML atlas) to PNG images.

positional arguments:
  tex_path              TEX texture file

options:
  -h, --help            show this help message and exit
  -A, --auto-atlas      Automatically find and use the XML atlas matching the texture file name
  -a ATLAS_PATH, --atlas ATLAS_PATH
                        XML atlas file, the result unpacked images will be placed in a new directory
```
