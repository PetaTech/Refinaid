# -*- coding: utf-8 -*-
'''
Create Date: 2024/01/07
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

from typing import Any

def auth_admin(
    username: str,
    password: str,
    *args: Any, 
    **kwargs: Any,
) -> bool:
    if username == "admin" and password == "admin":
        return True
    else:
        return False
