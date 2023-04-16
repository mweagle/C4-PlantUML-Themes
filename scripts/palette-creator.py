import os
from pathlib import Path
import json
import re
from urllib.request import urlopen
from string import Template
from datetime import datetime, timezone
import seaborn as sns
import matplotlib.pyplot as plt
import logging

################################################################################
# logger
logger = logging.getLogger("palette-creator")
logger.setLevel(logging.INFO)
ConsoleOutputHandler = logging.StreamHandler()
logger.addHandler(ConsoleOutputHandler)

################################################################################
# constants
logger = logging.getLogger("palette-creator")

URL_COLORBREWER_SOURCE_JSON = "https://colorbrewer2.org/export/colorbrewer.json"
CURRENT_UTC_TIME = datetime.now(timezone.utc)
THEME_OUTPUT_COMMON = f"""' Metadata
' Created: {CURRENT_UTC_TIME}
"""

THEME_OUTPUT_TEMPLATE_09 = (
    THEME_OUTPUT_COMMON + Path("./theme_template_9.puml").read_text()
)

THEME_OUTPUT_TEMPLATE_11 = (
    THEME_OUTPUT_COMMON + Path("./theme_template_11.puml").read_text()
)

# Template expressions for 9 and 11 colors
theme_template_09 = Template(THEME_OUTPUT_TEMPLATE_09)
theme_template_11 = Template(THEME_OUTPUT_TEMPLATE_11)

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
    output_data = ""
    if len(hex_colors) == 9:
        # Great - take the name, create a file with the template content, call it good
        output_data = theme_template_09.substitute(
            palette=palette_name,
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
        output_data = theme_template_11.substitute(
            palette=palette_name,
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

    if output_data == "":
        raise RuntimeError("Invalid output template created")

    output_basename = "./palettes/puml-theme-{0}".format(palette_name)
    output_puml_filename = "{0}.puml".format(output_basename)
    output_png_filename = "{0}.png".format(output_basename)
    with open(output_puml_filename, "w") as theme_file_output:
        theme_file_output.write(output_data)
    logger.info("Created theme: %s", output_puml_filename)

    # Create a color palette example
    seaborn_pallete = sns.color_palette(hex_colors)
    sns.palplot(seaborn_pallete)
    plt.savefig(output_png_filename)
    plt.close("all")

    logger.info("Created thumbnail: %s", output_png_filename)


################################################################################
# main
url_parts = URL_COLORBREWER_SOURCE_JSON.split("/")
colorbrewer_filename = url_parts[-1]
dir_path = os.path.dirname(os.path.realpath(__file__))
colorbrewer_path = os.path.join(dir_path, colorbrewer_filename)

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
