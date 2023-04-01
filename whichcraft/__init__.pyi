# -*- coding: utf-8 -*-

__author__: str
__email__: str
__version__: str

import os
from typing import Optional

try:
    from shutil import which
except ImportError:
    def which(
        cmd: str, mode: int = ..., path: Optional[str] = ...
    ) -> Optional[str]: ...
