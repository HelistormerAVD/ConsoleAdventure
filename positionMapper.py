

class PositionMapper:
    def __init__(self):
        self.number_of_points = 0
        self.startpoint_X = 0
        self.startpoint_Y = 0
        self.current_X = 0
        self.current_Y = 0

    def get_Position(self):
        return self.current_X, self.current_Y

    def set_Position(self, x, y):
        self.current_X = x
        self.current_Y = y

    def checkIfInBoundry(self, x, y, boundry):
        for bound in boundry:
            if bound[0] <= x <= bound[1] and bound[0] <= y <= bound[1]:
                return True
            else:
                return False
