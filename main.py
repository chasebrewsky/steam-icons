import os
import xml.etree.ElementTree as ET

from cairosvg import svg2png

if __name__ == '__main__':
    for path, subdirectories, names in os.walk('vectors'):
        subdirectory = path.lstrip('vectors/')

        if subdirectory and not os.path.exists(f'images/{subdirectory}'):
            os.makedirs(f'images/{subdirectory}')
        for name in names:
            if not name.endswith('.svg'):
                continue
            with open(f'{path}/{name}') as source:
                root = ET.parse(source)
                element = root.getroot()
                element.attrib['fill'] = '#ffffff'
                svg2png(
                    ET.tostring(element, encoding='utf8', method='xml'),
                    parent_width=512,
                    parent_height=512,
                    write_to=f'images/{subdirectory}/{name.replace(".svg", ".png")}',
                )

