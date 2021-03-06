from scipy import integrate

from mobject.vectorized_mobject import VMobject

from helpers import *

class FunctionGraph(VMobject):
    CONFIG = {
        "color" : BLUE_D,
        "x_min" : -SPACE_WIDTH,
        "x_max" : SPACE_WIDTH,
        "num_steps" : 20,
    }
    def __init__(self, function, **kwargs):
        self.function = function
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        self.set_anchor_points([
            x*RIGHT + self.function(x)*UP
            for x in np.linspace(self.x_min, self.x_max, self.num_steps)
        ], mode = "smooth")

    def get_function(self):
        return self.function


class ParametricFunction(VMobject):
    CONFIG = {
        "t_min" : 0,
        "t_max" : 1,
        "num_anchor_points" : 10,
    }
    def __init__(self, function, **kwargs):
        self.function = function
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        self.set_anchor_points([
            self.function(t)
            for t in np.linspace(
                self.t_min, 
                self.t_max,
                self.num_anchor_points
            )
        ], mode = "smooth")



        