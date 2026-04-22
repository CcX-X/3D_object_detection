from PIL import Image
import os

input_dir = "dataset/SourceImages"
output_dir = "dataset/SourceImages_change"
os.makedirs(output_dir, exist_ok=True)
for f in os.listdir(input_dir):
    if f.endswith(('.jpg', '.png')):
        img = Image.open(os.path.join(input_dir, f))
        img.thumbnail((1920, 1080))  # 限制最大尺寸
        img.save(os.path.join(output_dir, f))