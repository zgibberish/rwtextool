import sys
import os.path
import argparse
import util.texture_packer
import util.texconvert

parser = argparse.ArgumentParser(
    description="Packs a directory of PNG images into Rotwood Klei TEX textures and atlases.",
)
parser.add_argument('source_path', help="Directory of PNG files")
args = parser.parse_args()

source_path = args.source_path

if not os.path.exists(source_path):
    print("failed: directory does not exist")
    exit(1)

# remove trailing slashes
source_path = str(source_path).removesuffix("/")
source_path = str(source_path).removesuffix("\\")

png_files = util.texture_packer.pack(source_path)
for png in png_files:
    util.texconvert.png_to_tex(png)
