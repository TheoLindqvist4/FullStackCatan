from PIL import Image

# Define the paths for each resource image
image_paths = [
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\5.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\6.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\8.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\9.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\10.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\11.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\12.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\2.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\3.png",
    r"C:\Theo\School\ESIEE\Annee\E5\Full Stack\First version Catan\images\numbers\4.png"
]

# Define target dimensions
target_width, target_height = 362, 386

# Process each image
for image_path in image_paths:
    # Load the image
    image = Image.open(image_path)
    
    # Convert to RGBA to handle transparency
    image = image.convert("RGBA")
    
    # Get the bounding box of non-transparent content
    bbox = image.getbbox()
    cropped_image = image.crop(bbox)
    
    # Check if cropped image exceeds target dimensions and adjust accordingly
    cropped_width, cropped_height = cropped_image.size
    left = (cropped_width - target_width) // 2 if cropped_width > target_width else 0
    upper = (cropped_height - target_height) // 2 if cropped_height > target_height else 0
    right = left + target_width if cropped_width > target_width else cropped_width
    lower = upper + target_height if cropped_height > target_height else cropped_height

    # Crop down to target dimensions if necessary, centered on content
    final_image = cropped_image.crop((left, upper, right, lower))
    
    # Save the cropped image (overwriting the original)
    final_image.save(image_path)

print("Cropping completed for all images.")
