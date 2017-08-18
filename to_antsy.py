"""Converts 3d point cloud to 2d projection."""

import os
import numpy as np
import glob
import shutil
import json
import argparse

from thirdparty.calib import Calib


images_dir = 'data/images'
projected_dir = 'data/projected'
annotation_dir = 'data/annotations'


def main():
    parser = argparse.ArgumentParser(description='Converter')
    parser.add_argument('--kitti', type=str, help='Path to KITTI root directory, use if importing KITTI data')
    args = parser.parse_args()

    if args.kitti:
        images = load_kitti_pointclouds(args.kitti)
    else:
        raise NotImplementedError()

    with open('data/example.json') as f:
        data = json.load(f)
        data['projectedURLs'] = data.get('projectedURLs', [])
    for image in images:
        filename = image['filename']
        new_lidar_path = os.path.join(projected_dir, filename + '.npy')
        new_image_path = os.path.join(images_dir, filename + '.png')
        annotation_path = os.path.join(annotation_dir, filename + '.png')
        shutil.copy(image['path'], new_image_path)
        cloud = image['cloud'].reshape((-1, 3))
        projected_cloud = image['calib'].velo2img(cloud, 2)
        np.save(new_lidar_path, np.hstack((cloud, projected_cloud)))
        if new_image_path not in data['imageURLs']:
            data['imageURLs'].append(new_image_path)
        if annotation_path not in data['annotationURLs']:
            data['annotationURLs'].append(annotation_path)
        if new_lidar_path not in data['projectedURLs']:
            data['projectedURLs'].append(new_lidar_path)
    with open('data/example.json', 'w') as f:
        json.dump(data, f)


def load_kitti_pointclouds(kitti_dir):
    images = []
    for date in glob.iglob(os.path.join(kitti_dir, '2011_*')):
        calib = Calib(date)
        for drive in glob.iglob(os.path.join(date, '*_sync')):
            lidar_dir = os.path.join(drive, 'lidar_2d', 'data')
            image_dir = os.path.join(drive, 'image_02', 'data')
            for image in os.listdir(lidar_dir):
                image_path = os.path.join(image_dir, image.replace('.npy', '.png'))
                cloud_path = os.path.join(lidar_dir, image)
                images.append({
                    'path': image_path,
                    'cloud': np.load(cloud_path)[:, :, :3],
                    'calib': calib,
                    'filename': '__'.join((
                        os.path.basename(date),
                        os.path.basename(drive),
                        image.replace('.npy', '')))
                })
    return images


if __name__ == '__main__':
    main()