import PyTexturePacker.Packer
import xml.etree.ElementTree as ET
import os
import util.logger as logger

png_paths = []

def map_xywh_uv(x, y, w, h, canvas_w, canvas_h):
    # sprite
    x = x
    y = y
    xmax = x+w
    ymax = y+h

    ATLAS_PIXEL_THRESHOLD = 0.5
    u_margin = ATLAS_PIXEL_THRESHOLD / canvas_w
    v_margin = ATLAS_PIXEL_THRESHOLD / canvas_h
    u_factor = 1 / canvas_w
    v_factor = 1 / canvas_h

    u1 = x * u_factor + u_margin
    v1 = ymax * v_factor - v_margin
    u2 = xmax * u_factor - u_margin
    v2 = y * v_factor + v_margin

    return u1, v1, u2, v2

def xml_atlas_handler(atlasinfo, filepath):
    # file path given comes with a .txt at the end, so replace that with xml
    filepath_base = os.path.splitext(filepath)[0]
    filepath_atlas = filepath_base + ".xml"
    filepath_png = filepath_base + ".png"
    filepath_tex = filepath_base + ".tex"
    logger.info2(f"Packed image: {filepath_png}")
    logger.info2(f"Generating atlas: {filepath_atlas}")

    sprite_list = []
    frames = atlasinfo["frames"]
    for texture in frames:
        logger.info2(f"Texture: {texture}", 1)
        sprite_list.append({
            "name":texture,
            "data":frames[texture]["frame"]
        })

    # convert pixel coords to uv coords
    tex_size = atlasinfo["meta"]["size"]
    canvas_w = tex_size["w"]
    canvas_h = tex_size["h"]
    for sprite in sprite_list:
        u1, v1, u2, v2 = map_xywh_uv(
            sprite["data"]["x"], sprite["data"]["y"],
            sprite["data"]["w"], sprite["data"]["h"],
            canvas_w, canvas_h,
        )
        sprite["data"]["u1"] = u1
        sprite["data"]["v1"] = v1
        sprite["data"]["u2"] = u2
        sprite["data"]["v2"] = v2

    # XML structure
    root = ET.Element("Atlas")
    texture = ET.SubElement(root, "Texture")
    texture.set("filename", os.path.basename(filepath_tex))
    elements = ET.SubElement(root, "Elements")
    for sprite in sprite_list:
        sprite_element = ET.SubElement(elements, "Element")
        # replace sprite name extension with .tex because thats what
        # we are going to read off later (after png->tex conversion)
        sprite_element.set("name", os.path.splitext(sprite["name"])[0] + ".tex")
        sprite_element.set("u1", str(sprite["data"]["u1"]))
        sprite_element.set("v1", str(sprite["data"]["v1"]))
        sprite_element.set("u2", str(sprite["data"]["u2"]))
        sprite_element.set("v2", str(sprite["data"]["v2"]))

    # write to XML atlas
    xml_str = ET.tostring(root)
    with open(filepath_atlas, "wb") as xml_out:
        xml_out.write(xml_str)

    png_paths.append(filepath_png)

def pack(source_dir):
    packer = PyTexturePacker.Packer.create(
        texture_format=".png",
        atlas_format=xml_atlas_handler,
        max_width=2048,
        max_height=2048,
        force_square=False,
        bg_color=0x00000000,
        enable_rotated=False,
        trim_mode=0,
        border_padding=0,
        shape_padding=0,
        inner_padding=0
    ).pack(source_dir+"/", source_dir+"_%d")

    return png_paths
