# This code converts a 16bit uint TIFF image (that can not be displayed by normal monitors) to a Visualizable TIFF image

import PIL.Image as pil_image
import io
import numpy as np
path='path to the TIFF image'
save_path='path to save the Visualizable image'
with open(path, 'rb') as f:
    tif = pil_image.open(io.BytesIO(f.read()))
array=np.array(tif)
max_val=np.amax(array)
normalized=(array/max_val)
im = pil_image.fromarray(normalized)
im.save(save_path) 