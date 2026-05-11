"""Stub portal_sdk до импорта agent.py.

В production portal_sdk инжектит сам портал при сборке. В тестах его
скачивать из приватного monorepo лишний геморрой — все наши unit-кейсы
проверяют чистые хелперы, реальный Agent не вызывают.
"""
from __future__ import annotations

import sys
from types import SimpleNamespace


class _StubAgent:
    """Stub: agent.py делает `from portal_sdk import Agent`, не более."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        self.params: dict = {}
        self.output_dir = None

    def log(self, *_a: object, **_k: object) -> None:
        pass

    def progress(self, *_a: object, **_k: object) -> None:
        pass

    def item_done(self, *_a: object, **_k: object) -> None:
        pass

    def failed(self, *_a: object, **_k: object) -> None:
        pass

    def result(self, *_a: object, **_k: object) -> None:
        pass

    def input_dir(self, _name: str):  # noqa: ANN201
        from pathlib import Path
        return Path("/tmp/stub")


sys.modules.setdefault("portal_sdk", SimpleNamespace(Agent=_StubAgent))
