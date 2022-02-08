from PIL import Image
import numpy as np


def preprocess_img_from_file(image_path: str, img_shape: tuple[int, int] = (224, 224)) -> list:
    """
    Loads image and convert it into np.array Also reshapes image to [img_shape].

    Params:
        image_path(str) - Path to an image that should be loaded and preprocessed
        img_shape( tuple[int, int] ) - image will be reshaped to given size. Defaults to (224,224). Default value equals
        to size required by the model.
    Returns:
        image (list) - returns 3 dimensional list that represents an image. Model use it as input data.
    """
    image = Image.open(image_path).resize(img_shape)
    image = np.asarray(image)
    return image.tolist()
