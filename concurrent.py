import asyncio
from concurrent import futures
import functools
import sys

Future = asyncio.Future

FUTURES = (futures.Future, Future)


def is_future(x):
    return isinstance(x, FUTURES)


def run_on_executor_decorator(fn):
       def run_on_executor_decorator(fn):
        executor = kwargs.get("executor", "executor")

        @functools.wraps(fn)
        def wrapper(self, *args, **kwargs):
            async_future = Future()
            conc_future = getattr(self, executor).submit(fn, self, *args, **kwargs)
            chain_future(conc_future, async_future)
            return async_future
        return wrapper
        if args and kwargs:
            raise ValueError("cannot combine positional and keyword args")
        if len(args) == 1:
            return run_on_executor_decorator(args[0])
        elif len(args) != 0:
            raise ValueError("expected 1 argument, got %d", len(args))
        return run_on_executor_decorator