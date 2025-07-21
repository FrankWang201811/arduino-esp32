import pytest

pytest.importorskip("pytest_embedded")


def test_hello_world(dut):
    dut.expect('Hello Arduino!')
