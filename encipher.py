# -*- coding: utf-8 -*-
"""
加密参数生成代码（外部加载）

本文件会被 `src/config/parameter.py::check_objects_from_external_py` 动态加载，
用于覆盖程序内置（可能已过期）的加密参数算法。

接口签名必须与下方一致：
    ABogus.get_value(query, data, method, user_agent) -> str   # 抖音 a_bogus
    XBogus.get_x_bogus(query, data, method, user_agent) -> str # TikTok X-Bogus
    XGnarly.generate(query, data, method, user_agent) -> str   # TikTok X-Gnarly

当前实现为“临时占位实现”：直接复用项目内置算法，仅用于验证外部加载链路是否打通。
若抖音 / TikTok 升级签名算法后内置算法失效（例如返回 403），请将下方 get_value /
get_x_bogus / generate 替换为你自己的、与平台当前版本一致的实现（可调用
httpx / never_jscore / JavaScript 或自建参数生成服务）。
"""

from src.custom import USERAGENT
from src.encrypt import (
    ABogus as _ABogus,
    XBogus as _XBogus,
    XGnarly as _XGnarly,
)

__all__ = [
    "ABogus",
    "XBogus",
    "XGnarly",
]


class ABogus:
    """抖音接口加密参数（a_bogus）"""

    def __init__(self):
        ...

    def get_value(
        self,
        query: dict | str | None = None,
        data: dict | None = None,
        method: str | None = None,
        user_agent: str = "",
    ) -> str:
        return _ABogus(user_agent or USERAGENT).get_value(query, data, method)


class XBogus:
    """TikTok 接口加密参数（X-Bogus）"""

    def __init__(self):
        ...

    def get_x_bogus(
        self,
        query: dict | str | None = None,
        data: dict | None = None,
        method: str | None = None,
        user_agent: str = "",
    ) -> str:
        return _XBogus().get_x_bogus(
            query,
            data,
            method,
            user_agent=user_agent or USERAGENT,
        )


class XGnarly:
    """TikTok 接口加密参数（X-Gnarly）"""

    def __init__(self):
        ...

    def generate(
        self,
        query: dict | str | None = None,
        data: dict | None = None,
        method: str | None = None,
        user_agent: str = "",
    ) -> str:
        return _XGnarly().generate(
            query,
            data,
            method,
            user_agent=user_agent or USERAGENT,
        )
