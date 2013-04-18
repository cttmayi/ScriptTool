

from Basic.Module import module

class moduleFrame(module):
    def onCreate(self):
        self.createStatic("Name:", 0, 0)
        self.createTable(-1, 2, 60, 10, ['A','B','C'])
        pass