"""Converts labelled 2d projection to labelled point cloud."""

import argparse
import cv2
import json
import numpy as np
import os


def main():
    parser = argparse.ArgumentParser(description='Converter')
    parser.add_argument('--kitti', type=str,
                        help='Path to KITTI root directory, use if importing KITTI data')
    args = parser.parse_args()

    with open('data/example.json') as f:
        data = json.load(f)
    for imageURL, annotationURL, projectedURL in zip(
            data['imageURLs'], data['annotationURLs'], data['projectedURLs']):
        annotation = cv2.imread(annotationURL)
        if annotation is None:
            continue
        projected = np.load(projectedURL)
        labelled_cloud = []
        for point in projected:
            x = int(np.round(point[3]))
            y = int(np.round(point[4]))
            if 0 < y + 1 < annotation.shape[0] and 0 < x + 1 < annotation.shape[1]:
                label = annotation[y, x, 2]
            else:
                label = 0
            labelled_cloud.append(np.hstack((point[:3], label)))
        new_cloud = np.vstack(labelled_cloud)
        np.save(os.path.join(args.kitti, imageURL.replace('__', '/')), new_cloud)


if __name__ == '__main__':
    main()