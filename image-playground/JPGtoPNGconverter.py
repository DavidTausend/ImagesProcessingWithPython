import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check is new/ exists, if not create it
if not os.paht.exists(output_folder):
    os.makedirs(output_folder)

# loop through pokedex and convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{filename}.png', 'png')
    print('all done!')