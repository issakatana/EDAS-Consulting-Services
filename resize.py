from PIL import Image

def crop_image(input_image_path, output_image_path, crop_box):
    try:
        image = Image.open('static/media/teamImages/silasNobg.png')
        cropped_image = image.crop(crop_box)
        cropped_image.save(output_image_path)
        print("Image cropped and saved successfully.")
    except Exception as e:
        print("Error:", e)

# Specify the input image path, output image path, and crop box (left, upper, right, lower)
input_image_path = "static/media/teamImages/silascropped.png"
output_image_path = "static/media/teamImages/silascropped.png"
crop_box = (2, 10, 404, 410)
# crop_box = (40, 70, 810, 395)  #HAMILOGO
crop_image(input_image_path, output_image_path, crop_box)