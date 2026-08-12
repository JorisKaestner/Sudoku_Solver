# grid_detector.py
# https://medium.com/@shiodev/analyzing-and-processing-grid-images-with-opencv-part-1-d5c42ab0703c
import cv2
import matplotlib.pyplot as plt
import numpy as np

def load_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def display_image(image, title):
    plt.figure(figsize=(8, 8))
    plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def detect_edges(gray_image, threshold1=50, threshold2=150):
    edges = cv2.Canny(gray_image, threshold1, threshold2, apertureSize=3)
    return edges

def detect_lines(edges, threshold=100, min_line_length=100, max_line_gap=10):
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=threshold, minLineLength=min_line_length, maxLineGap=max_line_gap)
    return lines

def merge_nearest_lines(lines, threshold=50):
    horizontal_lines = []
    vertical_lines = []

    for line in lines:
        x1, y1, x2, y2 = line[0]
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

def count_unit_squares(horizontal_lines, vertical_lines):
    square_count = (len(horizontal_lines) - 1) * (len(vertical_lines) - 1)
    return square_count

def extract_squares(image):
    horizontal_lines, vertical_lines = merge_nearest_lines(detect_lines(detect_edges(image)))
    squares = []
    padding = 3
    for i in range(len(horizontal_lines) - 1):
        for j in range(len(vertical_lines) - 1):
            squares.append(image[horizontal_lines[i]+padding:horizontal_lines[i+1]-padding, vertical_lines[j]+padding:vertical_lines[j+1]-padding])
    return squares

def resize_cells(cells, cell_size:int=28):
    resized = []
    for cell in cells:
        resized.append(cv2.resize(cell, (cell_size, cell_size), interpolation=cv2.INTER_AREA))
    return resized