import os


def yolo_user_output(yolo_output_path):
    labels_path = os.path.join(yolo_output_path, 'labels')
    object_dict = {}
    for image_result in os.scandir(labels_path):
        data_array = [line.strip() for line in open(image_result.path)]
        data_array = data_array[:-1]
        map_output = set(map(lambda x: x.partition('-')[0].strip(), data_array))
        map_output = set(map(lambda x: x.partition('#'), map_output))
        for element in map_output:
            key = element[2].strip()
            count = int(element[0].strip())
            object_dict[key] = 1 if key not in object_dict else object_dict[key] + count
    return object_dict
