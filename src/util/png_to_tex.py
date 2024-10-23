from wand import image
import os

def png_to_tex(filepath):
    filepath_base = os.path.splitext(filepath)[0]
    filepath_dds = filepath_base + ".dds"
    filepath_tex = filepath_base + ".tex"
    HEADER = b"KTEX\x02\x00\x08\x00\x08"
   
    with image.Image(filename=filepath) as dds_out:
        dds_out.compression = 'dxt5'
        dds_out.save(filename=filepath_dds)

    img_dds = open(filepath_dds, "rb")
    img_tex = open(filepath_tex, "wb")
    image_data = img_dds.read()
    img_tex.write(HEADER + image_data)
    img_dds.close()
    img_tex.close()
    # clean up temp dds image
    os.remove(filepath_dds)
