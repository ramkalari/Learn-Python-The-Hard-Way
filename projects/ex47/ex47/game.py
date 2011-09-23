class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.dirty = False

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


    def clean(self):
        self.dirty = False

    def dump_trash(self):
        self.dirty = True
