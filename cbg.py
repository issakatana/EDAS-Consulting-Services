from PIL import Image

def remove_background(input_path, output_path):
    # Open the image
    image = Image.open(input_path)

    # Convert the image to RGBA mode (if not already)
    image = image.convert('RGBA')

    # Create a mask using the alpha channel
    mask = Image.new('L', image.size, 0)
    mask.putalpha(image.split()[3])

    # Create a new image with a transparent background
    new_image = Image.new('RGBA', image.size, (0, 0, 0, 0))

    # Paste the original image using the mask
    new_image.paste(image, (0, 0), mask)

    # Save the result as a PNG image
    new_image.save(output_path, format='PNG')

if __name__ == "__main__":
    input_image_path = "static/media/teamImages/paula.jpeg"  # Replace with the path to your input image
    output_image_path = "image.jpg"  # Replace with the desired output pah

    remove_background(input_image_path, output_image_path)



