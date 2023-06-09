import os
from pathlib import Path
import json
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from string import Template
from datetime import datetime, timezone
import seaborn as sns
import matplotlib.pyplot as plt
import logging
import zlib
import base64
import string

################################################################################
# logger
logger = logging.getLogger("palette-creator")
logger.setLevel(logging.INFO)
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)


################################################################################
# Excerpts from https://gist.github.com/ryardley/64816f5097003a35f9726aab676920d0
# to create the encoded PlantUML data to render as a PNG which
# we'll save locally
plantuml_alphabet = (
    string.digits + string.ascii_uppercase + string.ascii_lowercase + "-_"
)
base64_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
b64_to_plantuml = bytes.maketrans(
    base64_alphabet.encode("utf-8"), plantuml_alphabet.encode("utf-8")
)
plantuml_to_b64 = bytes.maketrans(
    plantuml_alphabet.encode("utf-8"), base64_alphabet.encode("utf-8")
)


def plantuml_encode(plantuml_text):
    """zlib compress the plantuml text and encode it for the plantuml server"""
    zlibbed_str = zlib.compress(plantuml_text.encode("utf-8"))
    compressed_string = zlibbed_str[2:-4]
    return (
        base64.b64encode(compressed_string).translate(b64_to_plantuml).decode("utf-8")
    )


################################################################################
# constants
logger = logging.getLogger("palette-creator")

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

URL_COLORBREWER_SOURCE_JSON = "https://colorbrewer2.org/export/colorbrewer.json"
URL_ALL_ELEMENTS_TEST = "https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/percy/TestAllElementsWithLegend.puml"
CURRENT_UTC_TIME = datetime.now(timezone.utc)


def theme_concat(*theme_filenames):
    content = ""
    for each_filename in theme_filenames:
        content += Path(os.path.join(SCRIPT_DIR, each_filename)).read_text()
        content += "\n"

    return content


THEME_OUTPUT_TEMPLATE_09 = theme_concat(
    "theme_template_common_header.puml",
    "theme_template_9.puml",
    "theme_template_common_footer.puml",
)

THEME_OUTPUT_TEMPLATE_11 = theme_concat(
    "theme_template_common_header.puml",
    "theme_template_11.puml",
    "theme_template_common_footer.puml",
)

ALL_ELEMENTS_THEMED_OUTPUT = theme_concat("theme_template_all_elements_example.puml")

# Template expressions for 9 and 11 colors
theme_template_09 = Template(THEME_OUTPUT_TEMPLATE_09)
theme_template_11 = Template(THEME_OUTPUT_TEMPLATE_11)
theme_template_example_output = Template(ALL_ELEMENTS_THEMED_OUTPUT)

SEABORN_PALETTES = [
    "deep",
    "husl",
    "gray",
    "vlag",
    "icefire",
    "rocket",
    "mako",
    "flare",
    "crest",
    "magma",
    "viridis",
    "Set1",
    "Set2",
    "Set3",
    "Paired",
    "Accent",
    "Pastel1",
    "Pastel2",
    "Dark2",
]


################################################################################
# utilities
def rgb_str_to_hex(r, g, b):
    return ("{:02X}" * 3).format(int(r), int(g), int(b))


def create_theme_from_colors(palette_name, hex_colors):
    theme_color_data = ""
    if len(hex_colors) == 9:
        # Great - take the name, create a file with the template content, call it good
        theme_color_data = theme_template_09.substitute(
            palette=palette_name,
            current_utc_time=CURRENT_UTC_TIME,
            color0=hex_colors[0],
            color1=hex_colors[1],
            color2=hex_colors[2],
            color3=hex_colors[3],
            color4=hex_colors[4],
            color5=hex_colors[5],
            color6=hex_colors[6],
            color7=hex_colors[7],
            color8=hex_colors[8],
        )
    elif len(hex_colors) == 11:
        # Great - take the name, create a file with the template content, call it good
        theme_color_data = theme_template_11.substitute(
            palette=palette_name,
            current_utc_time=CURRENT_UTC_TIME,
            color0=hex_colors[0],
            color1=hex_colors[1],
            color2=hex_colors[2],
            color3=hex_colors[3],
            color4=hex_colors[4],
            color5=hex_colors[5],
            color6=hex_colors[6],
            color7=hex_colors[7],
            color8=hex_colors[8],
            color9=hex_colors[9],
            color10=hex_colors[10],
        )
    else:
        logger.warn(
            "Unsupported color count %d for palette %s", len(hex_colors), palette_name
        )
        return

    if theme_color_data == "":
        raise RuntimeError("Invalid output template created")

    output_basename = "./palettes/puml-theme-{0}".format(palette_name)
    output_puml_filename = "{0}.puml".format(output_basename)
    output_png_filename = "{0}.png".format(output_basename)
    output_example_image_filename = "{0}-example.png".format(output_basename)

    with open(output_puml_filename, "w") as theme_file_output:
        theme_file_output.write(theme_color_data)
    logger.info("Created theme: %s", output_puml_filename)

    # Create a color palette example
    seaborn_pallete = sns.color_palette(hex_colors)
    sns.palplot(seaborn_pallete)
    plt.savefig(output_png_filename)
    plt.close("all")

    logger.info("Created thumbnail: %s", output_png_filename)

    # Create a sample output file
    logger.info("Creating PlantUML theme: {0}".format(palette_name))
    output_data = theme_template_example_output.substitute(
        palette=palette_name,
        theme_data=theme_color_data,
        plantuml_data=all_test_elements_plantuml,
    )
    logger.debug("Theme Data\n{0}\n".format(output_data))

    # write the output to a temp file, invoke the local render to create the file
    logger.info("Creating sample image for palette: {0}".format(palette_name))

    # Read the sample output file, turn it into a PlantUML encoded
    # url, then fetch the image and download it to the local preview image
    encoded_url_part = plantuml_encode(output_data)
    plant_uml_image_url = "https://www.plantuml.com/plantuml/png/{0}".format(
        encoded_url_part
    )
    logger.debug("Image URL: {0}".format(plant_uml_image_url))

    with open(output_example_image_filename, "wb") as local_png_file:
        try:
            with urlopen(plant_uml_image_url) as remote_png_response:
                local_png_file.write(remote_png_response.read())
        except HTTPError as err:
            logger.error("Failed to render\n{0}\n".format(output_data))
            logger.error("HTTP Status Code: {0}".format(err.code))
            logger.error("HTTP Headers: {0}".format(err.headers))
            raise err


################################################################################
# main
# Download the PlantUML resource that has all the test elements so that the
# server side render doesn't need to make another requests..
logger.info("Fetching latest PlantUML test elements content")
all_test_elements_plantuml = ""
with urlopen(URL_ALL_ELEMENTS_TEST) as puml_response:
    all_test_elements_plantuml = puml_response.read().decode()

# Fetch the latest palettes...
url_parts = URL_COLORBREWER_SOURCE_JSON.split("/")
colorbrewer_filename = url_parts[-1]
colorbrewer_path = os.path.join(SCRIPT_DIR, colorbrewer_filename)

# Download the latest colorbrewer file from the site
# https://colorbrewer2.org/#
logger.info("Creating ColorBrewer palettes")
logger.info("Downloading latest colorbrewer source: %s", URL_COLORBREWER_SOURCE_JSON)

with urlopen(URL_COLORBREWER_SOURCE_JSON) as json_response:
    json_data = json_response.read().decode()
    # Writing to file
    with open(colorbrewer_path, "w") as json_file:
        # Writing data to a file
        json_file.write(json_data)
        print("Downloaded JSON data: {0}".format(colorbrewer_path))

# Create the PUML themes and palette visualization
max_count = 0  # Set to non-zero to short-circuit creating all the palettes
theme_count = 0
total_entries = 0

# Colorbrewer themes...
with open(colorbrewer_path, "r") as file:
    jsonData = json.load(file)
    for each_key, each_map in jsonData.items():
        palette_type = each_map["type"]
        map_colors = {}
        for each_list_count_key, each_list_colors in each_map.items():
            total_entries += 1
            if each_list_count_key != "9" and each_list_count_key != "11":
                continue

            hex_colors = []
            for each_color in each_list_colors:
                re_result = re.search("rgb\((\d+)\w*,(\d+)\w*,(\d+)\w*\)", each_color)
                hex_color = rgb_str_to_hex(
                    re_result.group(1), re_result.group(2), re_result.group(3)
                )
                hex_colors.append("#{0}".format(hex_color))

            palette_name = "cb_{0}_{1}_{2}".format(
                palette_type, each_key, len(hex_colors)
            )
            create_theme_from_colors(palette_name, hex_colors)
            theme_count += 1

            if max_count > 0 and theme_count >= max_count:
                logger.info("Created maximum number of themes: {0}".format(max_count))
                quit()

# Seaborn palettes
logger.info("Creating Seaborn palettes")
for each_seaborn_palette in SEABORN_PALETTES:
    total_entries += 1
    hex_colors = sns.color_palette(each_seaborn_palette, 9).as_hex()
    palette_name = "{0}_{1}_{2}".format(
        "seaborn", each_seaborn_palette, len(hex_colors)
    )
    create_theme_from_colors(palette_name, hex_colors)
    theme_count += 1

logger.info("Created %d themes (total: %d)", theme_count, total_entries)
