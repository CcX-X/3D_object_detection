from ultralytics import YOLO
import os
os.environ['CUDA_LAUNCH_BLOCKING'] = '1'

if __name__ == "__main__":
    model = YOLO(r"yolo11s.pt")
    model.train(data="data.yaml",
                epochs=50,     # 训练多少轮，每一轮指的是让模型看一遍所有的训练集
                batch=8,       # 每次让模型看到多少个样本，电脑性能差的记得降低此数值
                workers=0,      # 数据处理线程数，电脑性能差的记得降低此数值，写0也可以，表示不用多线程
                seed=42,
                amp=True)       # 保持开启，可节省显存
