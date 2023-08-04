Dataset **Water Meters** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/H/0/Ny/AOkNaQO9wQxKg1MdxJoIFsTNxeyPyK7FnxPOVnfQ75rUHCQ0w7EI6uCjyfJO9eW1H8drlWajhfY17rFSdPAM2pb6toyuKcZBwCvTFe5KiOwJMxPaW8D4KKmLJI6i.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Water Meters', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/tapakah68/yandextoloka-water-meters-dataset/download?datasetVersionNumber=2)