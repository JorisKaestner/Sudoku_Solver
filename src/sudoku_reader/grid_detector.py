# grid_detector.py
# https://medium.com/@shiodev/analyzing-and-processing-grid-images-with-opencv-part-1-d5c42ab0703c
import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_image(image_path:str) -> list[int]:
    """Loads image from path and returns a grayscale image."""
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def display_image(image:np.array, title:str="Figure") -> None:
    """Display image with matplotlib"""
    plt.figure(figsize=(8, 8))
    plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def detect_edges(gray_image:np.array, threshold1:int=50, threshold2:int=150):
    """Returns edges in image with canny edge detection.

    :param int gray_image: matrix grayscale representation of image
    :param int threshold1: Lower threshold value in Hysteresis Thresholding
    :param int threshold2: Upper threshold value in Hysteresis Thresholding 
    """
    edges = cv2.Canny(gray_image, threshold1, threshold2, apertureSize=3)
    return edges

def detect_lines(edges, threshold:int=100, min_line_length:int=100, max_line_gap:int=10):
    """Detects lines from edges with Hough Line Transformation"""
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=threshold, minLineLength=min_line_length, maxLineGap=max_line_gap)
    return lines

def merge_nearest_lines(lines, threshold=50):
    """Merges nearest lines and separates by horizontal and vertical lines.
       Returns tuple of horizontal_lines, vertical_lines.
    """
    horizontal_lines = []
    vertical_lines = []

    lines = lines.reshape(-1, 4)  # normalize to (N, 4) for different opencv versions

    for line in lines:
        x1, y1, x2, y2 = line
        if abs(y1 - y2) < 10:  # Horizontal line
            horizontal_lines.append(y1)
        elif abs(x1 - x2) < 10:  # Vertical line
            vertical_lines.append(x1)

    horizontal_lines = sorted(set(horizontal_lines))
    vertical_lines = sorted(set(vertical_lines))

    def merge_lines(line_positions, threshold):
        merged_lines = []
        current_line = line_positions[0]

        for line in line_positions[1:]:
            if line - current_line <= threshold:
                continue
            else:
                merged_lines.append(current_line)
                current_line = line

        merged_lines.append(current_line)
        return merged_lines

    merged_horizontal_lines = merge_lines(horizontal_lines, threshold)
    merged_vertical_lines = merge_lines(vertical_lines, threshold)

    return merged_horizontal_lines, merged_vertical_lines

def count_unit_squares(horizontal_lines:list, vertical_lines:list) -> int:
    """Calculates squares by number of lines. Considers border lines."""
    square_count = (len(horizontal_lines) - 1) * (len(vertical_lines) - 1)
    return square_count

def extract_squares(image:np.array, padding_percentage:float=0.1) -> list[np.array]:
    """Detects lines in image and slices it into squares. Returns extracted cells in a list."""
    horizontal_lines, vertical_lines = merge_nearest_lines(detect_lines(detect_edges(image)))
    squares = []
    for i in range(len(horizontal_lines) - 1):
        row_padding = int((horizontal_lines[i+1]-horizontal_lines[i])*padding_percentage)
        for j in range(len(vertical_lines) - 1):
            col_padding = int((vertical_lines[j+1]-vertical_lines[j])*padding_percentage)
            squares.append(image[horizontal_lines[i]+row_padding:horizontal_lines[i+1]-row_padding, 
                                 vertical_lines[j]+col_padding:vertical_lines[j+1]-col_padding])
    return squares
