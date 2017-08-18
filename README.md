# Antsy2d

in-browser point cloud annotation tool for instance-level segmentation using 2d projection. Original written by [kyamagu](https://github.com/kyamagu/js-segment-annotator) with lightweight 3d point cloud adaptations by [Alvin Wan](http://alvinwan.com).

 * Label image regions with mouse.
 * Written in vanilla Javascript, with require.js dependency (packaged).
 * Pure client-side implementation of image segmentation.
 * *Fork introduces ability to label point cloud using 2d projection*

A browser must support HTML canvas to use this tool.

Importing data
--------------

Prepare a JSON file that looks like the following. The required fields are
`labels` and `imageURLs`. The `annotationURLs` are for existing data and can
be omitted. Place the JSON file inside the `data/` directory.

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
`index.html`.

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
