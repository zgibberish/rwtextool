import argparse
import util.logger as logger
parser = argparse.ArgumentParser(
    description="Unpacks a Rotwood Klei TEX file (and XML atlas) to PNG images.",
)
parser.add_argument('tex_path', help="TEX texture file")
parser.add_argument('-A', '--auto-atlas', help="Automatically find and use the XML atlas matching the texture file name", action="store_true", dest="auto_atlas")
parser.add_argument('-a', '--atlas', help="XML atlas file, the result unpacked images will be placed in a new directory", dest="atlas_path")
parser.add_argument('-v', '--verbose', help="Output verbosity level (can stack) (warnings, info, all info)", action="count", default=0)
args = parser.parse_args()
logger.verbosity = args.verbose

# ---

import sys
import os.path
import util.texconvert as texconvert

tex_path = args.tex_path
auto_atlas = args.auto_atlas
atlas_path = None
if auto_atlas:
    atlas_path = os.path.splitext(tex_path)[0]+".xml"
    logger.info(f"--auto-atlas used, using {atlas_path} as atlas")
else:
    atlas_path = args.atlas_path

failed = False
if (atlas_path != None) and (not os.path.isfile(atlas_path)):
    logger.warn("Atlas does not exist, not using atlas")
    atlas_path = None
if not os.path.isfile(tex_path):
    logger.error("TEX does not exist")
    failed = True
if failed: exit(1)

texconvert.tex_to_png(tex_path=tex_path, atlas_path=atlas_path)
