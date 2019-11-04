from typing import Optional, Callable

from rx3 import to_async
from rx3.core import Observable
from rx3.core.typing import Scheduler

def _start(func: Callable, scheduler: Optional[Scheduler] = None) -> Observable:
    """Invokes the specified function asynchronously on the specified
    scheduler, surfacing the result through an observable sequence.

    Example:
        >>> res = rx3.start(lambda: pprint('hello'))
        >>> res = rx3.start(lambda: pprint('hello'), rx3.Scheduler.timeout)

    Args:
        func: Function to run asynchronously.
        scheduler: [Optional] Scheduler to run the function on. If
            not specified, defaults to Scheduler.timeout.

    Remarks:
        The function is called immediately, not during the subscription
        of the resulting sequence. Multiple subscriptions to the
        resulting sequence can observe the function's result.

    Returns:
        An observable sequence exposing the function's result value,
        or an exception.
    """

    return to_async(func, scheduler)()
