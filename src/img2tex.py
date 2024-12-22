import sys
import os.path
import argparse
from util.texture_packer import pack
from util.texconvert import png_to_tex

parser = argparse.ArgumentParser(
    description="Packs a directory of PNG images into Rotwood Klei TEX textures and atlases.",
)
parser.add_argument('source_path', help="Directory of PNG files")
args = parser.parse_args()

source_path = args.source_path

if not os.path.exists(source_path):
    print("directory does not exist")
    exit(1)

png_files = pack(source_path)
for png in png_files:
    png_to_tex(png)
