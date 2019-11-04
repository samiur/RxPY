from typing import Callable, Optional
from rx3 import operators
from rx3.core import Observable
from rx3.core.typing import Predicate

from .lastordefault import last_or_default_async


def _last(predicate: Optional[Predicate] = None) -> Callable[[Observable], Observable]:
    def last(source: Observable) -> Observable:
        """Partially applied last operator.

        Returns the last element of an observable sequence that
        satisfies the condition in the predicate if specified, else
        the last element.

        Examples:
            >>> res = last(source)

        Args:
            source: Source observable to get last item from.

        Returns:
            An observable sequence containing the last element in the
            observable sequence that satisfies the condition in the
            predicate.
        """

        if predicate:
            return source.pipe(
                operators.filter(predicate),
                operators.last()
            )

        return last_or_default_async(source, False)
    return last
