# Antsy2d

in-browser point cloud annotation tool for instance-level segmentation using 2d projection. Original written by [kyamagu](https://github.com/kyamagu/js-segment-annotator) with lightweight 3d point cloud adaptations by [Alvin Wan](http://alvinwan.com).

 * Label image regions with mouse.
 * Written in vanilla Javascript, with require.js dependency (packaged).
 * Pure client-side implementation of image segmentation.
 * *Fork introduces ability to label point cloud using 2d projection*
 * Includes support for KITTI dataset

A browser must support HTML canvas to use this tool.

# Importing Data

You can use the automated script if you are using the KITTI dataset.

```
python to_antsy.py --kitti=path/to/KITTI
```

Otherwise, prepare a JSON file that looks like the following. The 
required fields are `labels` and `imageURLs`. The `annotationURLs` are 
for existing data and can be omitted. Place the JSON file inside the 
`data/` directory.

    {
      "labels": [
        "not drivable",
        "drivable"
      ],
      "imageURLs": [
        "data/images/test.png"
      ],
      "annotationURLs": [
        "data/annotations/test.png"
      ],
      "projectedURLs": [
        "data/projected/test.npy"
      ]
    }

Then edit `main.js` to point to this JSON file. Open a Web browser and visit
`index.html`. Once you're done annotating, click "save" to export. Drag
the image into `data/annotations`. Once you're done, convert this data
into labelled point clouds:

```
python from_antsy.py
```

Citation
--------

The original author asks that future users cite the following:

```
@article{tangseng2017looking,
Author        = {Pongsate Tangseng and Zhipeng Wu and Kota Yamaguchi},
Title         = {Looking at Outfit to Parse Clothing},
Eprint        = {1703.01386v1},
ArchivePrefix = {arXiv},
PrimaryClass  = {cs.CV},
Year          = {2017},
Month         = {Mar},
Url           = {http://arxiv.org/abs/1703.01386v1}
}
```
