# CS 5330 Spring 2024 Lab 1 Sky Identification

## Overview
This project focuses on the identification of the sky in images using a combination of Canny edge detection and Otsu thresholding. The goal is to create an effective sky detection algorithm that works well under specific conditions.
The Gradio demo of this project can be found at https://huggingface.co/spaces/yzhong2/sky-identification-gradio-demo

## Features
Canny Edge Detection: Utilizes the Canny edge detection algorithm to identify edges in the image.
Otsu Thresholding: Applies Otsu's thresholding to enhance the detection of lighter and darker areas, especially effective when the sky is cloudless.

## Methodology
Applies Canny's edge detection algorithm to the grayscale image, determining thresholds based on the median value of pixel intensities.
Iteratively adjusts upper and lower limits for optimal edge detection.

Conducts Otsu's thresholding on the blurred grayscale image to identify lighter and darker areas.

Combines Canny's edge detection and Otsu's thresholding, masking them to the original image to detect the sky.

## Limitations
The assumption that the sky is always brighter among all areas may not hold true in certain lighting conditions.
Performance may be less effective in the presence of other light sources, such as streetlights.
Poor performance when distinguishing the sky from non-sky regions with similar color and brightness, especially in images with large cloud groups.

## Future Improvements
Incorporate advanced computer vision techniques to handle images with varying lighting conditions.
Enhance segmentation for better identification of the sky in complex scenarios.
