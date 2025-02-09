import os
import pandas as pd

# 定义函数，检查指定目录中是否存在指定名称的图像文件
def check_image_existence(image_folder, slide_id):
    image_name = f"{slide_id}.pt"
    image_path = os.path.join(image_folder, image_name)
    return os.path.exists(image_path), f"{slide_id}"

# 读取 CSV 文件
def process_csv(csv_file, image_folder):
    # 读取 CSV 文件
    df = pd.read_csv(csv_file)
    
    # 存储结果的列表
    result_rows = []
    
    # 遍历每一行
    for index, row in df.iterrows():
        # 获取 slide_id
        slide_id = row['slide_id']
        
        # 检查图像是否存在
        image_exists, new_slide_id = check_image_existence(image_folder, slide_id)
        
        # 如果图像存在，则更新 slide_id，并将行添加到结果列表中
        if image_exists:
            row['slide_id'] = new_slide_id
            result_rows.append(row)
    
    # 将结果列表转换为 DataFrame
    result_df = pd.DataFrame(result_rows)
    
    return result_df

# 定义文件和文件夹路径
csv_file = '/home/wuyou/workspace/out_data.csv'  # 替换为你的 CSV 文件路径
image_folder = '/home/wuyou/workspace/DATA_ROOT_DIR/data_out/pt_files'  # 替换为存储图像的文件夹路径

# 处理 CSV 文件
result_df = process_csv(csv_file, image_folder)

# 输出结果
print(result_df)

result_df.to_csv('/home/wuyou/workspace/Step3_out.csv')