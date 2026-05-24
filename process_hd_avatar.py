import os
import sys

input_path = r"C:\Users\SAI MANI\.gemini\antigravity\brain\0d813287-5606-4326-8a3d-2817767569d4\media__1779540879681.png"
output_path = r"C:\Users\SAI MANI\.gemini\antigravity\scratch\pixel-portfolio\avatar.png"

try:
    from PIL import Image
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
    
    # Crop tightly around the head/shoulders in full high resolution
    left = int(0.24 * w)
    right = int(0.76 * w)
    top = int(0.22 * h)
    bottom = top + (right - left)
    
    # Ensure boundary safety
    if bottom > h:
        diff = bottom - h
        top = max(0, top - diff)
        bottom = h
        
    print(f"Cropping tight headshot in high-res: left={left}, top={top}, right={right}, bottom={bottom}")
    img_cropped = img.crop((left, top, right, bottom))
    
    # Save as PNG directly without downscaling or color quantization to preserve full high-definition details
    print(f"Saving high-res cropped avatar to {output_path}")
    img_cropped.save(output_path, "PNG")
    print("SUCCESS")
    
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(3)
