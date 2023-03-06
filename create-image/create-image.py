import sys
from pathlib import Path

from PIL import Image

if len(sys.argv) < 5:
    print("Missing mandatory inputs:\n\n\tcreate-image.exe <first-image-file> <second-image-file> <output-directory> <output-file-name>")
else:
    print("first-image-file: {}".format(sys.argv[1]))
    print("second-image-file: {}".format(sys.argv[2]))
    print("output-directory: {}".format(sys.argv[3]))
    print("output-file-name: {}".format(sys.argv[4]))

    images = [Image.open(x)
              for x in [sys.argv[1], sys.argv[2]]]

    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    Path(sys.argv[3]).mkdir(parents=True, exist_ok=True)
    new_im.save("{}\{}".format(sys.argv[3], sys.argv[4]))
