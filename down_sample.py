

import os
from PIL import Image

def downsample_image(image_path, output_path):
    # 打开图像
    with Image.open(image_path) as img:
        # 计算新的尺寸
        new_size = (img.width // 4, img.height // 4)
        # 下采样图像
        downsampled_img = img.resize(new_size, Image.LANCZOS)
        # 保存下采样后的图像
        downsampled_img.save(output_path)

def process_images(input_folder, output_folder):
    # 创建输出文件夹，如果它不存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            downsample_image(input_path, output_path)
            print(f"Processed {filename}")

if __name__ == "__main__":
    Image.MAX_IMAGE_PIXELS = 1000000000 
    input_folder = '/home/wuyou/workspace/deepslide2_balance/all_wsi_big/LGSC'  # 替换为你的输入文件夹路径
    output_folder = '/home/wuyou/workspace/deepslide2_balance/all_wsi/LGSC'  # 替换为你的输出文件夹路径

    process_images(input_folder, output_folder)
