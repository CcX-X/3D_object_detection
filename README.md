# 基于 YOLOv11 的行人与车辆识别工程
<<<<<<< HEAD
# YOLOv11-based Pedestrian and Vehicle Detection Project

本项目基于 [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) 搭建，面向两类目标检测任务：
This project is built on top of [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) and focuses on two object detection classes:

- `person`：行人 / Pedestrian
- `car`：车辆 / Vehicle


## 示例视频 / Demo Video

点击下图查看示例视频：  
Click the image below to watch the demo video:

[![Demo Video](./demo-cover.jpg)](.runs/detect/predict4/4.avi)


## 项目简介 / Project Overview

本工程使用 YOLOv11 目标检测模型对交通场景中的行人与车辆进行识别。  
This project uses the YOLOv11 object detection model to detect pedestrians and vehicles in traffic scenes.

项目包含：  
The project includes:

- 原始数据集与划分后的训练/验证/测试集 / Original dataset and split train/validation/test sets
- 训练脚本 `train.py` / Training script `train.py`
- 测试脚本 `test.py` / Evaluation script `test.py`
- 推理脚本 `predict.py` / Inference script `predict.py`
- 数据集划分脚本 `data_split.py` / Dataset splitting script `data_split.py`
- 图像尺寸预处理脚本 `change_img.py` / Image resizing preprocessing script `change_img.py`
- 已训练权重与训练/验证结果输出 / Trained weights and training/validation outputs

## 工程目录结构 / Project Structure
=======

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
>>>>>>> c35b7c1b0b694d79f775a2bcf3761e1405ae3379

```text
pythonProject/
│
<<<<<<< HEAD
├─ dataset_org/                   # 原始数据集 / Original dataset
│  ├─ images/                     # 原始图片 / Original images
│  └─ labels/                     # 原始标注（YOLO 格式）/ Original YOLO-format labels
├─ dataset/                       # 划分后的数据集 / Split dataset
=======
├─ dataset_org/                   # 原始数据集
│  ├─ images/                     # 原始图片
│  └─ labels/                     # 原始标注（YOLO 格式）
├─ dataset/                       # 划分后的数据集
>>>>>>> c35b7c1b0b694d79f775a2bcf3761e1405ae3379
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
<<<<<<< HEAD
│     ├─ train/                   # 训练结果目录 / Training outputs
│     │  ├─ weights/
│     │  │  ├─ best.pt            # 最优权重 / Best checkpoint
│     │  │  └─ last.pt            # 最后一轮权重 / Last checkpoint
│     │  ├─ results.csv           # 训练日志 / Training log
│     │  ├─ results.png           # 训练曲线 / Training curves
│     │  └─ confusion_matrix.png  # 混淆矩阵等图表 / Confusion matrix and charts
│     ├─ val/                     # 测试集评估结果 / Evaluation outputs
│     ├─ predict/                 # 批量图片推理结果 / Batch image inference results
│     ├─ predict2/                # 单张图片推理结果 / Single image inference results
│     ├─ predict3/                # 单张图片推理结果 / Single image inference results
│     └─ predict4/                # 视频推理结果 / Video inference results
├─ 1.jpg                          # 示例图片 / Example image
├─ 2.jpg                          # 示例图片 / Example image
├─ 3.jpg                          # 示例图片 / Example image
├─ 4.mp4                          # 示例视频 / Example video
├─ README.md                      # 项目说明文档 / Project documentation
├─ change_img.py                  # 图片尺寸缩放脚本 / Image resize script
├─ data.yaml                      # YOLO 数据集配置文件 / YOLO dataset config
├─ data_split.py                  # 数据集划分脚本 / Dataset split script
├─ predict.py                     # 推理脚本 / Inference script
├─ test.py                        # 测试/评估脚本 / Test/evaluation script
├─ train.py                       # 训练脚本 / Training script
├─ yolo11n.pt                     # YOLOv11 预训练权重 / YOLOv11 pretrained weights
├─ yolo11s.pt                     # YOLOv11 预训练权重 / YOLOv11 pretrained weights
└─ yolo26n.pt                     # 备用模型权重文件 / Backup model weights
```

## 环境配置 / Environment Setup

使用 Anaconda 创建 Python 虚拟环境运行本项目。  
It is recommended to create a Python virtual environment with Anaconda before running this project.

### 创建方式 / Setup Commands

```bash
=======
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
>>>>>>> c35b7c1b0b694d79f775a2bcf3761e1405ae3379
conda create -n yolo11 python=3.8 -y
conda activate yolo11

pip install ultralytics
```

<<<<<<< HEAD
如果需要使用 GPU，请确保：  
If you want to use GPU acceleration, make sure that:

- 已正确安装 NVIDIA 显卡驱动 / NVIDIA GPU driver is installed correctly
- 已安装与当前 PyTorch 版本匹配的 CUDA 环境 / CUDA matches the installed PyTorch version

## 数据集说明 / Dataset Description

`data.yaml` 中当前配置如下：  
The current configuration in `data.yaml` is:
=======
如果需要使用 GPU，请确保：

- 已正确安装 NVIDIA 显卡驱动
- 已安装与当前 PyTorch 版本匹配的 CUDA 环境

## 数据集说明

`data.yaml` 中当前配置如下：
>>>>>>> c35b7c1b0b694d79f775a2bcf3761e1405ae3379

```yaml
train: H:\szu\ai_test\pythonProject\dataset\train\images
val: H:\szu\ai_test\pythonProject\dataset\valid\images
test: H:\szu\ai_test\pythonProject\dataset\test\images

nc: 2
names: ["person", "car"]
```

<<<<<<< HEAD
注意：  
Note:

- 下载数据集后需要同步修改 `data.yaml` 中的路径配置 / Update the paths in `data.yaml` after downloading or moving the dataset

## 数据预处理与划分 / Data Preprocessing and Split

脚本：`data_split.py`  
Script: `data_split.py`

作用：  
Functions:

- 从 `dataset_org/images` 和 `dataset_org/labels` 读取原始数据 / Read raw images and labels from `dataset_org/images` and `dataset_org/labels`
- 按比例划分为训练集、验证集、测试集 / Split data into train, validation, and test sets
- 生成新的 `dataset/` 目录结构 / Generate the new `dataset/` directory structure

当前脚本中的划分比例为：  
The current split ratios in the script are:

- 训练集：`0.7` / Train: `0.7`
- 验证集：`0.2` / Validation: `0.2`
- 测试集：`0.1` / Test: `0.1`

## 模型训练 / Model Training

脚本：`train.py`  
Script: `train.py`

核心代码逻辑：  
Core workflow:

- 加载预训练模型 `yolo11s.pt` / Load the pretrained model `yolo11s.pt`
- 使用 `data.yaml` 中定义的数据集进行训练 / Train on the dataset defined in `data.yaml`
- 训练结束后自动保存结果到 `runs/detect/` / Automatically save outputs to `runs/detect/`

当前默认训练参数如下：  
The default training parameters are:

- 模型：`yolo11s.pt` / Model: `yolo11s.pt`
- 训练轮数：`50` / Epochs: `50`
- 批大小：`8` / Batch size: `8`
- 数据加载线程：`0` / Data loader workers: `0`
- 随机种子：`42` / Random seed: `42`
- 混合精度：`amp=True` / Mixed precision: `amp=True`

## 模型测试与评估 / Model Testing and Evaluation

脚本：`test.py`  
Script: `test.py`

作用：  
Functions:

- 加载训练得到的最优模型 `best.pt` / Load the trained best model `best.pt`
- 在 `data.yaml` 中定义的 `test` 集上执行评估 / Evaluate on the `test` set defined in `data.yaml`

评估结果会输出到：  
Evaluation outputs are saved to:

- `runs/detect/val/`

其中通常包括：  
These results usually include:

- PR 曲线 / PR curve
- F1 曲线 / F1 curve
- 混淆矩阵 / Confusion matrix
- 测试集预测可视化结果 / Visualization results on the test set

## 图片与视频推理 / Image and Video Inference

脚本：`predict.py`  
Script: `predict.py`

当前默认配置：  
Current default configuration:

- 权重文件：`runs\detect\train\weights\best.pt` / Weights: `runs\detect\train\weights\best.pt`
- 输入源：`4.mp4` / Input source: `4.mp4`
- 置信度阈值：`0.25` / Confidence threshold: `0.25`
- NMS IoU 阈值：`0.45` / NMS IoU threshold: `0.45`
- 保存结果：`save=True` / Save results: `save=True`
- 显示结果：`show=True` / Show results: `show=True`
- 推理设备：`device=0` / Device: `device=0`

`source` 可以替换为：  
`source` can be replaced with:

- 单张图片，如 `1.jpg` / A single image such as `1.jpg`
- 文件夹，如 `dataset/test/images` / A folder such as `dataset/test/images`
- 视频文件，如 `4.mp4` / A video file such as `4.mp4`

推理结果会自动保存在 `runs/detect/predict*` 目录中，例如：  
Inference outputs will be automatically saved in `runs/detect/predict*`, for example:

- `predict/`：批量图片推理结果 / Batch image inference results
- `predict2/`、`predict3/`：单图推理结果 / Single image inference results
- `predict4/`：视频推理结果 / Video inference results

## 结果说明 / Results

验证集指标大致为：  
The validation metrics are approximately:
=======
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
>>>>>>> c35b7c1b0b694d79f775a2bcf3761e1405ae3379

- Precision：`0.7227`
- Recall：`0.5933`
- mAP50：`0.6464`
- mAP50-95：`0.3717`

<<<<<<< HEAD
这些结果说明模型已经具备一定的行人与车辆检测能力，能够完成基础识别任务。若希望进一步提升效果，可以从以下几个方面优化：  
These results indicate that the model already has basic pedestrian and vehicle detection capability. To further improve performance, you can optimize the project in the following ways:

- 增加训练数据量 / Increase the amount of training data
- 提高标注质量 / Improve annotation quality
- 尝试更大的模型版本 / Try a larger model version
- 增加训练轮数 / Increase the number of training epochs
- 调整图像分辨率、批大小和数据增强策略 / Tune image resolution, batch size, and data augmentation strategy
=======
这些结果说明模型已经具备一定的行人与车辆检测能力，能够完成基础识别任务。若希望进一步提升效果，可以从以下几个方面优化：

- 增加训练数据量
- 提高标注质量
- 尝试更大的模型版本
- 增加训练轮数
- 调整图像分辨率、批大小和数据增强策略
>>>>>>> c35b7c1b0b694d79f775a2bcf3761e1405ae3379
