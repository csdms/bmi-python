from __future__ import annotations

import inspect

import pytest

from bmipy import Bmi
from bmipy import BmiStub


def test_stub_implements_everything():
    assert isinstance(BmiStub(), Bmi)


@pytest.mark.parametrize("name", sorted(Bmi.__abstractmethods__))
def test_stub_raises_not_implemented(name):
    method = getattr(BmiStub(), name)
    signature = inspect.signature(method)

    kwds = dict.fromkeys(signature.parameters)

    with pytest.raises(NotImplementedError, match=name):
        method(**kwds)


@pytest.mark.parametrize("name", sorted(Bmi.__abstractmethods__))
def test_stub_matches_signatures(name):
    assert inspect.signature(getattr(BmiStub, name)) == inspect.signature(
        getattr(Bmi, name)
    )
