from PIL import Image
import os

def generate_icons(base_image_path, output_dir, sizes):
    base_img = Image.open(base_image_path)
    
    images_dir = os.path.join(output_dir, 'images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    for size, prefix in sizes:
        img = base_img.copy()
        img.thumbnail(size, Image.ANTIALIAS)
        
        if prefix == 'android':
            filename = f'android-chrome-{size[0]}x{size[1]}.png'
        elif prefix == 'favicon':
            filename = f'favicon-{size[0]}x{size[1]}.png'
        else:
            filename = f'apple-touch-icon-{size[0]}x{size[1]}.png'
            
        output_path = os.path.join(images_dir, filename)
        
        img.save(output_path, 'PNG')

base_image_path = 'base.png'
output_dir = './'

sizes = [
    ((57, 57), 'apple'),
    ((60, 60), 'apple'),
    ((72, 72), 'apple'),
    ((76, 76), 'apple'),
    ((114, 114), 'apple'),
    ((120, 120), 'apple'),
    ((144, 144), 'apple'),
    ((152, 152), 'apple'),
    ((180, 180), 'apple'),
    ((32, 32), 'favicon'),
    ((192, 192), 'android'),
    ((96, 96), 'favicon'),
    ((16, 16), 'favicon')
]

generate_icons(base_image_path, output_dir, sizes)