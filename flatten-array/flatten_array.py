import collections

def deep_flatten(iterable):
    for el in iterable:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def flatten(iterable):
    return [x for x in deep_flatten(iterable) if x != None ]