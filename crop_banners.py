from PIL import Image

def crop_to_banner(image_path):
    try:
        img = Image.open(image_path)
        width, height = img.size
        # Target aspect ratio 4:1
        target_height = width // 4
        
        # Calculate cropping box
        left = 0
        top = (height - target_height) // 2
        right = width
        bottom = (height + target_height) // 2
        
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(image_path)
        print(f"Successfully cropped {image_path} to {width}x{target_height}")
    except Exception as e:
        print(f"Failed to crop {image_path}: {e}")

crop_to_banner('assets/cyberpunk_banner.png')
crop_to_banner('assets/anime_footer_banner.png')
