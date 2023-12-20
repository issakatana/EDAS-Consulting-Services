from PIL import Image, ImageDraw

def draw_rectangle(image, rectangle_coords, outline_color="red", outline_width=2):
    draw = ImageDraw.Draw(image)
    draw.rectangle(rectangle_coords, outline=outline_color, width=outline_width)
    return image

def preview_crop(input_image_path, crop_box):
    try:
        image = Image.open('static/media/teamImages/silasNobg.png')
        image_with_preview = draw_rectangle(image.copy(), crop_box)
        image_with_preview.show()  
    except Exception as e:
        print("Error:", e)

input_image_path = "edas.png"
crop_box = (2, 10, 404, 410)
preview_crop(input_image_path, crop_box)

# crop_box = (left, top, right, bottom)