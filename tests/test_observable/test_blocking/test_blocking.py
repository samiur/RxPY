import unittest
import pytest

import rx3
from rx3.internal.exceptions import SequenceContainsNoElementsError
from rx3 import operators as ops
from rx3.testing import ReactiveTest

on_next = ReactiveTest.on_next
on_completed = ReactiveTest.on_completed
on_error = ReactiveTest.on_error
subscribe = ReactiveTest.subscribe
subscribed = ReactiveTest.subscribed
disposed = ReactiveTest.disposed
created = ReactiveTest.created


class RxException(Exception):
    pass


# Helper function for raising exceptions within lambdas
def _raise(ex):
    raise RxException(ex)


class TestBlocking(unittest.TestCase):

    def test_run_empty(self):
        with pytest.raises(SequenceContainsNoElementsError):
            rx3.empty().run()

    def test_run_error(self):
        with pytest.raises(RxException):
            rx3.throw(RxException()).run()

    def test_run_just(self):
        result = rx3.just(42).run()
        assert result == 42

    def test_run_range(self):
        result = rx3.range(42).run()
        assert result == 41

    def test_run_range_to_iterable(self):
        result = rx3.range(42).pipe(ops.to_iterable()).run()
        assert list(result) == list(range(42))

    def test_run_from(self):
        result = rx3.from_([1, 2, 3]).run()
        assert result == 3

    def test_run_from_first(self):
        result = rx3.from_([1, 2, 3]).pipe(ops.first()).run()
        assert result == 1

    def test_run_of(self):
        result = rx3.of(1, 2, 3).run()
        assert result == 3
