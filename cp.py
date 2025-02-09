import csv
import shutil
import os

# 定义要复制的标签
target_label = 'no_tumo'

# 读取CSV文件
csv_file_path = '/home/wuyou/workspace/Classification_pytorch/out_test.csv'

# 遍历CSV文件的每一行
with open(csv_file_path, mode='r') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)  # 跳过表头
    for row in reader:
        image_path = row[0]
        label = row[1]

        # 检查标签是否匹配目标标签
        if label == target_label:
            # 生成新的文件路径
            file_directory, file_name = os.path.split(image_path)
            file_base, file_extension = os.path.splitext(file_name)
            new_file_name = f"{file_base}_copy2{file_extension}"
            new_file_path = os.path.join(file_directory, new_file_name)

            # 复制文件
            # shutil.copy2(image_path, new_file_path)
            os.remove(image_path)
            print(f"del {image_path} to {new_file_path}")
            # print(f"Copied {image_path} to {new_file_path}")
        # else:
        #     os.remove(image_path)
