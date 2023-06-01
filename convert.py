from PIL import Image, ImageDraw, ImageFont
from zipfile import ZipFile
import os

uploaded_file = os.path.join(os.environ['TMPDIR'], os.environ['HTTP_FILENAME'])

with open(uploaded_file, 'r') as f:
    lines = f.read().splitlines()

zip_filename = 'images.zip'
zip_file = ZipFile(zip_filename, 'w')

for index, line in enumerate(lines):
    image = Image.new('RGB', (100, 100), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=14)
    draw.text((10, 40), line, fill='black', font=font)
    image_filename = f'image{index}.png'
    image.save(image_filename)
    zip_file.write(image_filename)

zip_file.close()

with open(zip_filename, 'rb') as f:
    zip_data = f.read()

print('Content-Type: application/zip')
print(f'Content-Disposition: attachment; filename="{zip_filename}"')
print()
print(zip_data)
