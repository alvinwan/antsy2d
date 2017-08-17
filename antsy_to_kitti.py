"""Converts labelled 2d projection to labelled point cloud."""

import cv2
import json
import numpy as np


def main():
    with open('data/example.json') as f:
        data = json.load(f)
    for imageURL, annotationURL, projectedURL in zip(
            data['imageURLs'], data['annotationURLs'], data['projectedURLs']):
        annotation = cv2.imread(imageURL)
        projected = np.load(projectedURL)
        labelled_cloud = []
        for point in projected:
            x = int(np.round(point[3]))
            y = int(np.round(point[4]))
            label = annotation[y, x]
            labelled_cloud.append(np.hstack((point[:3], label)))


if __name__ == '__main__':
    main()