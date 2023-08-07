"""Module responsible for image preprocessing."""
from typing import List, Tuple

import cv2
import numpy as np


class ImagePreprocessing:
    """Class responsible for image preprocessing."""

    def __init__(self):
        pass

    def preprocess_image_list(
        self, list_image: List[Tuple[np.array, str]]
    ) -> List[Tuple[float, bool]]:
        """Normalize and extract brightness and encode label from image list.

        Args:
            list_image (List[np.array, str]): Image list and label.

        Returns:
            List[Tuple(float, bool)]: List with mean brightness and label from each image.

        """
        list_image_normalized = []
        for im in list_image:
            image = im[0]
            label = im[1]
            standardized_im = self.normalize_image(image)
            brightness = self.extract_brightness(standardized_im)
            binary_label = 1 if label == "day" else 0
            list_image_normalized.append((brightness, binary_label))
        return list_image_normalized

    def normalize_image(
        self, image: np.array, width: int = 1000, height: int = 600
    ) -> np.array:
        """Resize images to specific width and height.

        Args:
            image (np.array): Image.
            width (int): Target width.
            height (int): Target height.

        Returns:
            np.array: image resized to target dimentions.
        """
        dim = (width, height)
        return cv2.resize(image, dim)

    def extract_brightness(self, image: np.array) -> float:
        """Extract the mean brightness from an image.

        Args:
            image (np.array): Image.

        Returns:
            float: Image mean brightness.
        """

        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        sum_brightness = np.sum(hsv[:, :, 2])
        area = hsv.shape[0] * hsv.shape[1]
        return sum_brightness / area
