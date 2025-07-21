import pytest

pytest.importorskip("pytest_embedded")


def test_unity(dut):
    dut.expect_unity_test_output(timeout=240)
