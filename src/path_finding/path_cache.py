import pickle


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PathCache(metaclass=Singleton):

    # data:
    # (StartPoint, EndPoint) => WalkQueue

    def __init__(self):
        self.file_name = "path_cache.file"

        try:
            with open(self.file_name, "rb") as f:
                self.cache = pickle.load(f)
        except:
            self.cache = dict()

    def put(self, start_point, end_point, walk_queue):
        self.cache[(start_point, end_point)] = list(walk_queue)
        self.cache[(end_point, start_point)] = list(reversed(walk_queue))

        with open(self.file_name, "wb") as f:
            pickle.dump(self.cache, f, pickle.HIGHEST_PROTOCOL)

    def get(self, start_point, end_point):
        key = (start_point, end_point)
        if key in self.cache:
            return list(self.cache[key])
        else:
            raise PathNotInCacheException()

    def __str__(self):
        return str(self.cache)


class PathNotInCacheException(Exception):
    pass
