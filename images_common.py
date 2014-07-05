import os
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage import measure

def plot_contours(img, dark, light, show=True):
    """Display the image and plot all contours found"""
    plt.imshow(img, cmap='gray')
    
    for n, contour in enumerate(dark):
        plt.plot(contour[:, 1], contour[:, 0], c='r', linewidth=1)
    
    for n, contour in enumerate(light):
        plt.plot(contour[:, 1], contour[:, 0], c='b', linewidth=1)

    plt.axis('image')
    plt.xticks([])
    plt.yticks([])
    if show:
        plt.show()

def find_contours(path, low=0.1, high=0.8):
    """Find contours in an image at path
    """
    img = imread(path, flatten=True)
    
    # Find contours at a constant value of 0.1 and 0.8
    dark = measure.find_contours(img, low)
    light = measure.find_contours(img, high)
    return img, dark, light

def get_contours_image(path):
    from IPython.core.pylabtools import print_figure
    
    img, dark, light = find_contours(path)
    plot_contours(img, dark, light, show=False)
    fig = plt.gcf()
    pngdata = print_figure(fig)
    plt.close(fig)
    return pngdata

def get_pictures(pictures_dir):
    """Return a list of picture files found in pictures_dir"""

    pictures = []
    for directory, subdirs, files in os.walk(pictures_dir):
        for fname in files:
            if fname.lower().endswith(('.jpg', '.png')):
                pictures.append(os.path.join(directory, fname))
    
    return pictures
