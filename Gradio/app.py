import numpy as np
import cv2
import gradio as gr
from matplotlib import pyplot as plt

title = "Sky Identification with Classical Computer Vision Techniques"

def sky_detector(image):
    if image is None:
        return
    img = image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blur the image to reduce unnecessary details
    img_blur = cv2.blur(img_gray,ksize=(7, 7))
    # find edges with both thresholds equal to 127
    edges = cv2.Canny(img_gray, threshold1=127,threshold2=127)
    # set the median value for pixels
    median_pixel = np.median(img)
    # set upper and lower threshold for better edge detection
    lower = int(max(0, 0.7 * median_pixel))
    upper = int(min(255, 1.3 * median_pixel))
    edges_by_median = cv2.Canny(image=img_gray, threshold1=lower, threshold2=upper)
    # use Ostu's thresholding to verify sky portion
    ret,th = cv2.threshold(img_blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # combine the inverse of otsu thresholding and the edges to mask to the image
    otsu_inverse = cv2.bitwise_not(th)
    combined_mask = cv2.bitwise_or(edges_by_median, otsu_inverse)

    # use dilation and closing to refine edges
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(combined_mask,kernel,iterations = 2)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    masked_image = img.copy()
    masked_image[closing == 255] = [0, 0, 0]

    return masked_image

iface = gr.Interface(fn=sky_detector,inputs="image", outputs="image", title=title, live=True)
iface.launch(share=True, debug=True)