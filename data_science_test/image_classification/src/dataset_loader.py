"""Module responsible for loading datasets."""
import glob
import os
from typing import List, Tuple

import cv2
import numpy as np


def load_images(image_dir: str) -> List[Tuple[np.array, str]]:
    """Load imagens from directory.

    Args:
        image_dir: path to directory.

    Returns:
        List[Tuple[np.array, str]]: Images and labels.
    """
    im_list = []
    image_types = ["day", "night"]

    for im_type in image_types:
        for file in glob.glob(os.path.join(image_dir, im_type, "*")):
            im = cv2.imread(file)

            if im is not None:
                im_list.append((im, im_type))

    return im_list
