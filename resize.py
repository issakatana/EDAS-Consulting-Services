from PIL import Image

def crop_image(input_image_path, output_image_path, crop_box):
    try:
        image = Image.open('static/media/bgImages/jobsearch.png')
        cropped_image = image.crop(crop_box)
        cropped_image.save(output_image_path)
        print("Image cropped and saved successfully.")
    except Exception as e:
        print("Error:", e)

# Specify the input image path, output image path, and crop box (left, upper, right, lower)
input_image_path = "edasNavLogoU.png"
output_image_path = "edasNavLogoU.png"
crop_box = (-400, 0, 0, 0)
# crop_box = (40, 70, 810, 395)  #HAMILOGO
crop_image(input_image_path, output_image_path, crop_box)