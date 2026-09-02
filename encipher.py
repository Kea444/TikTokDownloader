# -*- coding: utf-8 -*-
"""
加密参数生成代码（外部加载）

本文件会被 `src/config/parameter.py::check_objects_from_external_py` 动态加载，
用于覆盖程序内置（可能已过期）的加密参数算法。

接口签名必须与下方一致：
    ABogus.get_value(query, data, method, user_agent) -> str   # 抖音 a_bogus
    XBogus.get_x_bogus(query, data, method, user_agent) -> str # TikTok X-Bogus
    XGnarly.generate(query, data, method, user_agent) -> str   # TikTok X-Gnarly

当前实现：
    - ABogus：通过 `never_jscore` 执行 `static/js/a_bogus.js` 的 `generate_a_bogus()`
      生成抖音 a_bogus。算法版本完全由该 JS 决定，若抖音升级算法，请同步替换
      `static/js/a_bogus.js` 为与抖音当前版本一致的实现。
    - XBogus / XGnarly：仍转发项目内置实现，如需可同样改为 JS/Node 或自建服务。
"""

from pathlib import Path
from urllib.parse import quote, urlencode

import never_jscore

from src.custom import USERAGENT
from src.encrypt import XBogus as _XBogus, XGnarly as _XGnarly

__all__ = [
    "ABogus",
    "XBogus",
    "XGnarly",
]

_ROOT = Path(__file__).resolve().parent
_JS_PATHS = (
    _ROOT / "static" / "js" / "a_bogus.js",
    _ROOT.parent / "static" / "js" / "a_bogus.js",
)
_ENGINE = None


def _get_engine():
    """懒加载并缓存 never_jscore 的 JS 引擎。"""
    global _ENGINE
    if _ENGINE is not None:
        return _ENGINE
    js_path = next((p for p in _JS_PATHS if p.is_file()), None)
    if js_path is None:
        raise FileNotFoundError(
            "未找到 static/js/a_bogus.js，请确认该文件存在"
            "（源码运行时位于项目根目录，打包运行时位于 _internal 目录）！"
        )
    _ENGINE = never_jscore.JSEngine(js_path.read_text(encoding="utf-8"))
    return _ENGINE


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
        if isinstance(query, dict):
            query = urlencode(query, safe="=", quote_via=quote)
        return _get_engine().call(
            "generate_a_bogus",
            [query or "", user_agent or USERAGENT],
        )


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

