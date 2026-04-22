# 评估训练好的模型
from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO(r"runs\detect\train\weights\best.pt")
    model.val(data="data.yaml",
              split="test")
