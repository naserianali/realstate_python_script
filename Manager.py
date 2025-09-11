class Manager:
    _class = None

    def __init__(self, _class=None):
        self._class = _class

    def search(self, *args, **kwargs):
        results = list()
        for key, value in kwargs.items():
            if key.endswith('__min'):
                compare = "min"
                key = key[:-5]
            elif key.endswith('__max'):
                compare = "max"
                key = key[:-5]
            else:
                compare = "equal"
            for obj in self._class.object_list:
                if hasattr(obj, key):
                    if compare == "max":
                        res = bool(getattr(obj, key) >= value)
                    elif compare == "min":
                        res = bool(getattr(obj, key) <= value)
                    else:
                        res = bool(getattr(obj, key) == value)
                    if res:
                        results.append(obj)
        return results
