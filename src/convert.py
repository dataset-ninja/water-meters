import ast
import csv
import os

import supervisely as sly
from supervisely.io.fs import get_file_name, get_file_name_with_ext


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/iwatkot/Downloads/ninja-datasets/WaterMeters"
    download_polygons = False
    ds_name = "ds"

    batch_size = 30
    images_folder_name = "images"
    masks_folder_name = "masks"
    ann_poly = "data.csv"

    def get_water_meter_value(file_name):
        str_value = file_name.split("_value_")[1]
        value = str_value.replace("_", ".")
        return float(value)

    def create_ann(image_path):
        labels = []

        image_name = get_file_name_with_ext(image_path)
        mask_path = os.path.join(masks_path, image_name)
        mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
        img_height = mask_np.shape[0]
        img_wight = mask_np.shape[1]
        mask = mask_np > 200
        curr_bitmap = sly.Bitmap(mask)
        curr_label = sly.Label(curr_bitmap, obj_class)
        labels.append(curr_label)
        vater_value = get_water_meter_value(get_file_name(image_path))
        tag = sly.Tag(meta=tag_water_value, value=vater_value)

        if download_polygons:
            curr_poly = image_name_to_data[image_name]
            exterior = []
            for coords in curr_poly:
                x = int(coords["x"] * img_wight)
                y = int(coords["y"] * img_height)
                exterior.append([y, x])

            polygon = sly.Polygon(exterior=exterior)
            label_poly = sly.Label(polygon, obj_class_poly)
            labels.append(label_poly)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[tag])

    images_path = os.path.join(dataset_path, images_folder_name)
    images_names = os.listdir(images_path)
    masks_path = os.path.join(dataset_path, masks_folder_name)
    polygons_path = os.path.join(dataset_path, ann_poly)

    obj_class = sly.ObjClass("water meter data", sly.Bitmap)
    obj_classes = [obj_class]
    tag_water_value = sly.TagMeta(name="water meter value", value_type=sly.TagValueType.ANY_NUMBER)
    if download_polygons:
        obj_class_poly = sly.ObjClass("water meter data polygon", sly.Polygon)
        obj_classes.append(obj_class_poly)
        image_name_to_data = {}

        with open(polygons_path, "r") as file:
            csv_data = csv.reader(file)
            for row in list(csv_data)[1:]:
                data_str_dict = row[2]
                data_dict = ast.literal_eval(data_str_dict)
                image_name_to_data[row[0]] = data_dict["data"]

    obj_class_collection = sly.ObjClassCollection(obj_classes)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection, tag_metas=[tag_water_value])
    api.project.update_meta(project.id, meta.to_json())
    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in img_names_batch
        ]

        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(img_names_batch))

    return project
