from util.png_to_tex import png_to_tex
from util.texture_packer import pack
import sys

args = sys.argv
if len(args) < 2:
    sys.exit("must provide a directory path")

source_dir = args[1]

png_files = pack(source_dir)
for png in png_files:
    png_to_tex(png)
