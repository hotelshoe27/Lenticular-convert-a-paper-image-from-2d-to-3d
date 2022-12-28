from PIL import Image



image = Image.open('./data/sample_0.jpg')

resize_image = image.resize((560, 845))

resize_image.save('./data/resized_img_0.png')