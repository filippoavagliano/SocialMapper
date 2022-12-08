import os


def logohunter_output(logohunter_output_path):
    print(logohunter_output_path)
    logo_dict = {}
    logo_output_path = os.path.join(logohunter_output_path, 'out.txt')
    data_array = [line.strip() for line in open(logo_output_path)]
    for picture in data_array:
        picture_data = picture.split(" ")[1:]
        picture_data = list(map(lambda x: x.split(',')[4].strip(), picture_data))
        picture_data = list(map(lambda x: x.partition('_')[0].strip(), picture_data))
        for logo in picture_data:
            key = logo
            count = picture_data.count(logo)
            logo_dict[key] = 1 if key not in logo_dict else logo_dict[key] + count
    return logo_dict
