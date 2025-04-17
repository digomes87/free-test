from typing import Callable, Dict, List, Type

_event_handlers: Dict[Type, List[Callable]] = {}


def subscribe(event_type: Type, handler: Callable):
    if event_type not in _event_handlers:
        _event_handlers[event_type] = []
    _event_handlers[event_type].append(handler)


def publish(event):
    handlers = _event_handlers.get(type(event), [])
    for handler in handlers:
        handler(event)
