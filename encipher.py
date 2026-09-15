# -*- coding: utf-8 -*-
"""加密参数生成代码（外部加载）

DouK-Downloader 自 V5.8 起内置了纯 Python 的签名实现：
    - 抖音：`src/encrypt/douyin_params.py`（a_bogus + x-secsdk-web-signature）
    - TikTok：`src/encrypt/tiktok_params.py`（X-Bogus / X-Gnarly）

本文件保留“外部加密参数代码”机制：默认直接复用内置实现。
如需接入自行维护的算法，请把 DouYinParams / TikTokParams 替换为你自己的实现。
"""

from src.encrypt import DouYinParams, TikTokParams

__all__ = [
    "DouYinParams",
    "TikTokParams",
]

