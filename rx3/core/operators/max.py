from typing import Callable, Optional

from rx3 import operators as ops
from rx3.core import Observable, pipe
from rx3.core.typing import Comparer
from rx3.internal.basic import identity

from .min import first_only


def _max(comparer: Optional[Comparer] = None) -> Callable[[Observable], Observable]:
    """Returns the maximum value in an observable sequence according to
    the specified comparer.

    Examples:
        >>> op = max()
        >>> op = max(lambda x, y:  x.value - y.value)

    Args:
        comparer: [Optional] Comparer used to compare elements.

    Returns:
        An operator function that takes an observable source and returns
        an observable sequence containing a single element with the
        maximum element in the source sequence.
    """

    return pipe(
        ops.max_by(identity, comparer),
        ops.map(first_only)
    )
