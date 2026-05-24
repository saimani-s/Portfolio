import os
import sys

input_path = r"C:\Users\SAI MANI\.gemini\antigravity\brain\0d813287-5606-4326-8a3d-2817767569d4\media__1779540879681.png"
output_path = r"C:\Users\SAI MANI\.gemini\antigravity\scratch\pixel-portfolio\avatar.png"

try:
    from PIL import Image, ImageEnhance
except ImportError:
    print("PIL_MISSING")
    sys.exit(1)

try:
    if not os.path.exists(input_path):
        print(f"ERROR: Input image not found at {input_path}")
        sys.exit(2)
        
    print(f"Opening input image: {input_path}")
    img = Image.open(input_path)
    
    w, h = img.size
    print(f"Original dimensions: width={w}, height={h}")
    
    # Saimani's face in this new image is centered. Let's crop it tightly around the head/shoulders
    # to make it look like a real RPG dialogue sprite!
    # The head starts around y = 0.25*h to 0.8*h, and x = 0.25*w to 0.75*w.
    # Let's crop a square area: x from 0.25*w to 0.75*w, y from 0.25*h to 0.75*h.
    # Let's calculate exactly.
    left = int(0.24 * w)
    right = int(0.76 * w)
    top = int(0.22 * h)
    bottom = top + (right - left)
    
    # Ensure boundary safety
    if bottom > h:
        diff = bottom - h
        top = max(0, top - diff)
        bottom = h
        
    print(f"Cropping tight headshot: left={left}, top={top}, right={right}, bottom={bottom}")
    img_cropped = img.crop((left, top, right, bottom))
    
    # Enhance the contrast and color saturation slightly to fit the vibrant cyberpunk neon theme
    print("Enhancing image for cyberpunk aesthetics...")
    enhancer_color = ImageEnhance.Color(img_cropped)
    img_vibrant = enhancer_color.enhance(1.15) # Boost color saturation
    enhancer_contrast = ImageEnhance.Contrast(img_vibrant)
    img_contrasted = enhancer_contrast.enhance(1.1) # Boost contrast slightly for sharp pixel transitions
    
    # Resize down to 64x64 pixels to get crisp retro pixels
    print("Downscaling to 64x64 retro resolution...")
    img_small = img_contrasted.resize((64, 64), Image.Resampling.LANCZOS)
    
    # Quantize to a retro game 32-color adaptive palette to lock in the 8-bit styling
    print("Converting to 8-bit retro palette...")
    img_pixelated = img_small.convert('P', palette=Image.Palette.ADAPTIVE, colors=32)
    
    # Save as PNG
    print(f"Saving pixel-art avatar to {output_path}")
    img_pixelated.save(output_path, "PNG")
    print("SUCCESS")
    
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(3)
