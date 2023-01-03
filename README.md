# Steam Icons

This repository contains a list of publicly accessible icons that are formatted to be used as custom icons on steam deck virtual menus. These icons are pulled from different sets of free use web icons that are designed to be visually cohesive. The problem is that most of these images come as SVGs and the steam deck prefers PNGs, and the SVGs use black as a base icon color while the steam deck prefers white so that it can apply color styling.

SVG images are placed into the vectors directory, then the `main.py` file is ran in order to generated PNGs from those icons. These PNGs are given a 512px by 512px dimension as well as setting the default icon color to white.