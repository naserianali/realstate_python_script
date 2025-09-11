class Manager:
    _class = None

    def __init__(self, _class=None):
        self._class = _class

    def search(self, *args, **kwargs):
        results = list()
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    results.append(obj)
        return results
