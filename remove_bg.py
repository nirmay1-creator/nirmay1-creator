import sys
import subprocess

try:
    import imageio
    from rembg import remove
    from PIL import Image
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "imageio", "rembg", "Pillow", "numpy"])
    import imageio
    from rembg import remove
    from PIL import Image
    import numpy as np

print("Dependencies loaded, starting processing...")

input_path = "assets/cat-laptop.gif"
output_path = "assets/cat-transparent.gif"

print(f"Reading {input_path}...")
reader = imageio.get_reader(input_path)
fps = reader.get_meta_data().get('fps', 10)
frames = []

for i, frame in enumerate(reader):
    print(f"Processing frame {i}...")
    # rembg requires PIL image or numpy array
    img = Image.fromarray(frame).convert("RGBA")
    
    # Remove background
    out = remove(img)
    
    # Convert back to numpy array
    frames.append(np.array(out))

print(f"Writing {output_path}...")
imageio.mimsave(output_path, frames, format='GIF', fps=fps, loop=0)
print("Done!")
