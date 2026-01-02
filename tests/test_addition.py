"""
简单的加法函数测试模块
"""

import pytest


def add(a, b):
    """
    加法函数

    Args:
        a: 第一个加数
        b: 第二个加数

    Returns:
        两个数的和
    """
    return a + b


def test_add_positive_numbers():
    """测试两个正数相加"""
    assert add(1, 2) == 3
    assert add(10, 20) == 30


def test_add_negative_numbers():
    """测试负数相加"""
    assert add(-1, -2) == -3
    assert add(-5, 3) == -2


def test_add_zero():
    """测试加零的情况"""
    assert add(5, 0) == 5
    assert add(0, 0) == 0


def test_add_floats():
    """测试浮点数相加"""
    assert add(1.5, 2.5) == 4.0
    assert add(0.1, 0.2) == pytest.approx(0.3, rel=1e-9)
