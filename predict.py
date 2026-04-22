from ultralytics import YOLO

model = YOLO(r"runs\detect\train\weights\best.pt")
# 对图片进行推理（将 test.jpg 替换为你自己的图片）
results = model.predict(
    source=r"4.mp4",
    conf=0.25,  # 置信度阈值，低于此值的检测框会被过滤
    iou=0.45,  # NMS 去重阈值
    save=True,  # 保存标注结果图
    device=0,
    show=True
)
