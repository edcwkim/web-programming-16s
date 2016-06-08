from io import BytesIO
from PIL import Image
from django.core.files import File
from django.utils import six


def pil_image(input_f, quality=80):
    if isinstance(input_f, six.string_types):
        filename = input_f
    elif hasattr(input_f, "name"):
        filename = input_f.name
    else:
        filename = "noname.png"

    extension = filename.rsplit(".")[-1]
    try:
        format = {
            '.jpg': 'jpeg',
            '.jpeg': 'jpeg',
            '.png': 'png',
            '.gif': 'gif',
        }[extension]
    except KeyError:
        format = 'png'

    image = Image.open(input_f)
    return image, format


def image_to_file(image, format, quality):
    output_f = BytesIO()
    image.save(output_f, format=format, quality=quality)
    output_f.seek(0)
    return output_f


def thumbnail(input_f, width, height, quality=80):
    image, format = pil_image(input_f, quality)
    image.thumbnail((width, height), Image.ANTIALIAS)
    return image_to_file(image, format, quality)


def thumbnailize_image(sender, instance, **kwargs):
    images = [instance.image1]
    if instance.image2:
        images += [instance.image2]
    if instance.image3:
        images += [instance.image3]
    for image in images:
        max_width = 1200
        max_height = 6000
        if image and (image.width > max_width or image.height > max_height):
            processed_file = thumbnail(image.file, max_width, max_height)
            image.save(image.name, File(processed_file))
