# square image!
from torchvision.transforms.functional import center_crop

def squareImage(image):
    h, w = image.size[:2]

    if h > w:
        img = center_crop(image, (w, w))
    else:
        img = center_crop(image, (h, h))

    return img

