import argparse
import util.logger as logger
parser = argparse.ArgumentParser(
    description="Packs a directory of PNG images into Rotwood Klei TEX textures and atlases.",
)
parser.add_argument('source_path', help="Directory of PNG files")
parser.add_argument('-v', '--verbose', help="Output verbosity level (can stack) (warnings, info, all info)", action="count", default=0)
args = parser.parse_args()
logger.verbosity = args.verbose
logger.indent_spaces = 4 # already initialized in logger, but write it here
#                         again so it's clear that this parameter exists.

# ---

import sys
import os.path
import util.texture_packer as texture_packer
import util.texconvert as texconvert

source_path = args.source_path
if not os.path.exists(source_path):
    logger.error("Directory does not exist")
    exit(1)
# remove trailing slashes
source_path = str(source_path).removesuffix("/")
source_path = str(source_path).removesuffix("\\")

logger.info(f"Packing images: {source_path}")
png_files = texture_packer.pack(source_path)
logger.info(f"Output PNGs: {png_files}")
for png in png_files:
    texconvert.png_to_tex(png)
