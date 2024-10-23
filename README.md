# Rotwood TEX Tool

A texture packer+converter for Rotwood (WIP)

## Requirements

Any of the newer versions of Python should work, and you'll need the `PyTexturePacker` and `Wand` modules

```shell
pip install PyTexturePacker Wand
```

## Usage

### Packing PNGs into TEX+XML

To pack a directory containing source .png images into .tex textures and .xml atlases:

```shell
python src/img2tex.py 'path'
```

Output will be created next to your source directory.

### Unpacking TEX+XML to PNGs

Feature not implemented yet, I will look into this later when I have time.
