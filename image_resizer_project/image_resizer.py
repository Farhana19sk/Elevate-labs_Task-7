import os
from PIL import Image

# Input and Output folder paths
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"

# Resize dimensions
NEW_WIDTH = 800
NEW_HEIGHT = 600

# Create output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Supported image formats
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png")

print("Starting Image Resizing Process...\n")

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(SUPPORTED_FORMATS):
        try:
            input_path = os.path.join(INPUT_FOLDER, filename)
            output_path = os.path.join(OUTPUT_FOLDER, filename)

            # Open image
            with Image.open(input_path) as img:
                # Resize image
                resized_img = img.resize((NEW_WIDTH, NEW_HEIGHT))

                # Save resized image
                resized_img.save(output_path)

            print(f"Resized and saved: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("\nImage Resizing Completed Successfully!")
