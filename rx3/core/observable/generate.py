from typing import Any

from rx3.core import Observable
from rx3.core.typing import Mapper, Predicate
from rx3.scheduler import CurrentThreadScheduler
from rx3.disposable import MultipleAssignmentDisposable


def _generate(initial_state: Any,
              condition: Predicate,
              iterate: Mapper
              ) -> Observable:

    def subscribe(observer, scheduler=None):
        scheduler = scheduler or CurrentThreadScheduler.singleton()
        first = True
        state = initial_state
        mad = MultipleAssignmentDisposable()

        def action(scheduler, state1=None):
            nonlocal first
            nonlocal state

            has_result = False
            result = None

            try:
                if first:
                    first = False
                else:
                    state = iterate(state)

                has_result = condition(state)
                if has_result:
                    result = state

            except Exception as exception:  # pylint: disable=broad-except
                observer.on_error(exception)
                return

            if has_result:
                observer.on_next(result)
                mad.disposable = scheduler.schedule(action)
            else:
                observer.on_completed()

        mad.disposable = scheduler.schedule(action)
        return mad
    return Observable(subscribe)
