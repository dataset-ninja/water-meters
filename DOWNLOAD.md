Dataset **Water Meters** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/g/d/kM/kZJVm1JLYWUqNqHCsRD7NPhNS8VZVJui2vGVbcXBJBrIK9sUcpniGnYyFhA8BbSuVumNyNuM2REFWqJis9kj04ejuFmk54Et9WVMwqEfsl6KqM1OAYGUS3Za6O78.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Water Meters', dst_path='~/dtools/datasets/Water Meters.tar')
```
The data in original format can be 🔗[downloaded here.](https://www.kaggle.com/datasets/tapakah68/yandextoloka-water-meters-dataset/download?datasetVersionNumber=2)