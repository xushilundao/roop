import threading
import numpy
# import opennsfw2   # 已禁用
from PIL import Image
from keras import Model

from roop.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 0.85


def get_predictor() -> Model:
    """
    原本返回 opennsfw2 模型，现在直接返回 None。
    """
    return None


def clear_predictor() -> None:
    """
    清空 predictor，这里什么也不做。
    """
    global PREDICTOR
    PREDICTOR = None


def predict_frame(target_frame: Frame) -> bool:
    """
    原本检测单帧是否 NSFW。
    现在始终返回 False（即不过滤）。
    """
    return False


def predict_image(target_path: str) -> bool:
    """
    原本检测单张图片。
    现在始终返回 False。
    """
    return False


def predict_video(target_path: str) -> bool:
    """
    原本检测视频。
    现在始终返回 False。
    """
    return False
