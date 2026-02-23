# Elevate-labs_Task-7
🖼 Image Resizer Tool (Python)
1.A simple Python-based Image Resizer Tool that resizes multiple images in batch and saves them to an output folder.
2.This project was developed as part of a Python Developer Internship Task.

🚀 Features
1.Batch image processing
2.Resizes images to fixed dimensions (800x600)
3.Supports JPG, JPEG, and PNG formats
4.Automatically creates output folder
5.Error handling included
6.Clean and simple folder structure

🛠 Technologies Used
1.Python 3
2.Pillow (PIL) Library
3.OS module

📂 Project Structure
image_resizer_project/
│
├── image_resizer.py
├── input_images/
│     ├── sample1.jpg
│     ├── sample2.png
│
└── output/images

⚙️ Installation
1Install the required package:
      pip install pillow

▶️ How to Run
1.Place images inside the input_images folder.
2.Run the script:
      python image_resizer.py
3.Resized images will be saved in output/images.

📌 Concepts Demonstrated
1.File handling with os
2.Working with directories
3.Image processing using Pillow
4.Batch processing
5.Exception handling
🎯 Output
All images from the input folder are resized to 800x600 pixels and saved in the output folder.
