# 基于 YOLOv11 的行人与车辆识别工程

本项目基于 [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) 搭建，面向两类目标检测任务：

- `person`：行人
- `car`：车辆

## 项目简介

本工程使用 YOLOv11 目标检测模型对交通场景中的行人与车辆进行识别。
项目包含：
- 原始数据集与划分后的训练/验证/测试集
- 训练脚本 `train.py`
- 测试脚本 `test.py`
- 推理脚本 `predict.py`
- 数据集划分脚本 `data_split.py`
- 图像尺寸预处理脚本 `change_img.py`
- 已训练权重与训练/验证结果输出

## 工程目录结构

```text
pythonProject/
│
├─ dataset_org/                   # 原始数据集
│  ├─ images/                     # 原始图片
│  └─ labels/                     # 原始标注（YOLO 格式）
├─ dataset/                       # 划分后的数据集
│  ├─ train/
│  │  ├─ images/
│  │  └─ labels/
│  ├─ valid/
│  │  ├─ images/
│  │  └─ labels/
│  └─ test/
│     ├─ images/
│     └─ labels/
├─ runs/
│   └─ detect/
│     ├─ train/                   # 训练结果目录
│     │  ├─ weights/
│     │  │  ├─ best.pt            # 最优权重
│     │  │  └─ last.pt            # 最后一轮权重
│     │  ├─ results.csv           # 训练日志
│     │  ├─ results.png           # 训练曲线
│     │  └─ confusion_matrix.png  # 混淆矩阵等图表
│     ├─ val/                     # 测试集评估结果
│     ├─ predict/                 # 批量图片推理结果
│     ├─ predict2/                # 单张图片推理结果
│     ├─ predict3/                # 单张图片推理结果
│     └─ predict4/                # 视频推理结果
├─ 1.jpg                          # 示例图片
├─ 2.jpg                          # 示例图片
├─ 3.jpg                          # 示例图片
├─ 4.mp4                          # 示例视频
├─ README.md                      # 项目说明文档
├─ change_img.py                  # 图片尺寸缩放脚本
├─ data.yaml                      # YOLO 数据集配置文件
├─ data_split.py                  # 数据集划分脚本
├─ predict.py                     # 推理脚本
├─ test.py                        # 测试/评估脚本
├─ train.py                       # 训练脚本
├─ yolo11n.pt                     # YOLOv11 预训练权重
├─ yolo11s.pt                     # YOLOv11 预训练权重
└─ yolo26n.pt                     # 备用模型权重文件
```

## 环境配置

使用 Anaconda 创建 Python 虚拟环境运行本项目。

### 创建方式
```
conda create -n yolo11 python=3.8 -y
conda activate yolo11

pip install ultralytics
```

如果需要使用 GPU，请确保：

- 已正确安装 NVIDIA 显卡驱动
- 已安装与当前 PyTorch 版本匹配的 CUDA 环境

## 数据集说明

`data.yaml` 中当前配置如下：

```yaml
train: H:\szu\ai_test\pythonProject\dataset\train\images
val: H:\szu\ai_test\pythonProject\dataset\valid\images
test: H:\szu\ai_test\pythonProject\dataset\test\images

nc: 2
names: ["person", "car"]
```

注意：
- 下载数据集后需要同步修改 `data.yaml` 中的路径配置

## 数据预处理与划分

脚本：`data_split.py`

作用：
- 从 `dataset_org/images` 和 `dataset_org/labels` 读取原始数据
- 按比例划分为训练集、验证集、测试集
- 生成新的 `dataset/` 目录结构

当前脚本中的划分比例为：

- 训练集：`0.7`
- 验证集：`0.2`
- 测试集：`0.1`

## 模型训练

脚本：`train.py`

核心代码逻辑：

- 加载预训练模型 `yolo11s.pt`
- 使用 `data.yaml` 中定义的数据集进行训练
- 训练结束后自动保存结果到 `runs/detect/`

当前默认训练参数如下：

- 模型：`yolo11s.pt`
- 训练轮数：`50`
- 批大小：`8`
- 数据加载线程：`0`
- 随机种子：`42`
- 混合精度：`amp=True`

## 模型测试与评估

脚本：`test.py`

作用：

- 加载训练得到的最优模型 `best.pt`
- 在 `data.yaml` 中定义的 `test` 集上执行评估

评估结果会输出到：

- `runs/detect/val/`

其中通常包括：

- PR 曲线
- F1 曲线
- 混淆矩阵
- 测试集预测可视化结果

## 图片与视频推理

脚本：`predict.py`

当前默认配置：

- 权重文件：`runs\detect\train\weights\best.pt`
- 输入源：`4.mp4`
- 置信度阈值：`0.25`
- NMS IoU 阈值：`0.45`
- 保存结果：`save=True`
- 显示结果：`show=True`
- 推理设备：`device=0`

`source` 可以替换为：
- 单张图片，如 `1.jpg`
- 文件夹，如 `dataset/test/images`
- 视频文件，如 `4.mp4`

推理结果会自动保存在 `runs/detect/predict*` 目录中，例如：

- `predict/`：批量图片推理结果
- `predict2/`、`predict3/`：单图推理结果
- `predict4/`：视频推理结果

## 当前结果说明

验证集指标大致为：

- Precision：`0.7227`
- Recall：`0.5933`
- mAP50：`0.6464`
- mAP50-95：`0.3717`

这些结果说明模型已经具备一定的行人与车辆检测能力，能够完成基础识别任务。若希望进一步提升效果，可以从以下几个方面优化：

- 增加训练数据量
- 提高标注质量
- 尝试更大的模型版本
- 增加训练轮数
- 调整图像分辨率、批大小和数据增强策略
