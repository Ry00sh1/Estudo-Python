import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

def save_images_from_pdf(pdf_file_name, output_dir, images):
    # Convert PDF to images

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for i, image in enumerate(images):
        # Save each image with a unique name
        image_path = os.path.join(output_dir, f"page_{i + 1}.png")
        image.save(image_path, 'PNG')
        print(f"Saved: {image_path}")

def extract_region_from_pdf(pdf_file_name, output_txt_file_name, region, save_images=False):
    # Convert PDF to images
    images = convert_from_path(pdf_file_name)

    # Optionally save images
    if save_images:
        save_images_from_pdf(pdf_file_name, 'extracted_images', images)

    # Open a file to write the extracted text
    with open(output_txt_file_name, 'w', encoding='utf-8') as txt_file:
        # Loop through each image (page)
        for i, image in enumerate(images):
            # Crop to region (x, y, width, height)
            x, y, width, height = region
            cropped_image = image.crop((x, y, x + width, y + height))
            
            # Perform OCR on the cropped region
            text = pytesseract.image_to_string(cropped_image)

            # Write the extracted text to the file
            txt_file.write(f"Page {i + 1}:\n")
            txt_file.write(text)
            txt_file.write("\n" + "-"*80 + "\n")

# Specify file names and the region coordinates
pdf_path = 'document.pdf'
output_txt_path = 'textfile.txt'
region = (0, 0, 1656, 480)  # Define the region you want to extract text from

extract_region_from_pdf(pdf_path, output_txt_path, region, save_images=True)

