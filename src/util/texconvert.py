import os
import PIL.Image
import xml.etree.ElementTree as ET

MAGIC = b"KTEX\x02\x00\x08\x00\x08"

def png_to_tex(png_path): # .png input file
    filepath_base = os.path.splitext(png_path)[0]
    filepath_dds = filepath_base + ".dds"
    filepath_tex = filepath_base + ".tex"

    try:
        # apply dxt5 compression to png save to a temp file,
        # then write the image data from said temp file to .tex
        # and remove the temp file
        with PIL.Image.open(png_path) as png:
            png.compression = 'dxt5'
            png.save(filepath_dds)
        img_dds = open(filepath_dds, "rb")
        img_tex = open(filepath_tex, "wb")
        image_data = img_dds.read()
        img_tex.write(MAGIC + image_data)
        img_dds.close()
        img_tex.close()
    except:
        print("failed: invalid image data?")
    finally:
        # clean up temp dds image
        os.remove(filepath_dds)

def tex_to_png(tex_path, atlas_path=None): # .tex input file
    filepath_base = os.path.splitext(tex_path)[0]
    filepath_dds = filepath_base + ".dds"
    filepath_png = filepath_base + ".png"

    try:
        # extract dxt5 compressed image data from tex
        # and write to a temp file, then convert that file
        # back to png, and remove said temp file
        img_tex = open(tex_path, 'rb')
        img_dds = open(filepath_dds, 'wb')
        img_tex.seek(len(MAGIC))
        image_data = img_tex.read()
        img_dds.write(image_data)
        img_tex.close()
        img_dds.close()
        with PIL.Image.open(filepath_dds) as dds:
            dds.compression = "no"
            dds.save(filepath_png)
    except:
        print("failed: invalid image data?")
    finally:
        # clean up temp dds image
        os.remove(filepath_dds)

    if atlas_path != None:
        png = PIL.Image.open(filepath_png)
        w, h = png.size

        os.makedirs(filepath_base, exist_ok=True)
        tree = ET.parse(atlas_path)
        elements = tree.getroot().find("Elements")
        for element in elements:
            name = element.attrib["name"]
            name_base = os.path.splitext(name)[0]
            u1 = float(element.attrib["u1"])
            v1 = float(element.attrib["v1"])
            u2 = float(element.attrib["u2"])
            v2 = float(element.attrib["v2"])
            box = (u1*w, v2*h, u2*w, v1*h)
            png.crop(box).save(filepath_base+"/"+name_base+".png")

        png.close()

