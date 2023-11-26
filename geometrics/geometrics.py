from common import *


class Rect():
    def Surface(self):
        return self.x_length*self.y_length

    def Diagonal(self):
        return math.sqrt(self.x_length*self.x_length+self.y_length+self.y_length)

    def __init__(self, x, y):
        malloc()
        self.x_length = x
        self.y_length = y
        self.surface = self.Surface()
        self.diagonal = self.Diagonal()
