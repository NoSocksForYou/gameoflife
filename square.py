class Square:
    def __init__(self, pos_x, pos_y, alive, edges=(False, False, False, False)):
        #edges (left, right, up, bottom)
        self.__pos_x = pos_x
        self.__pos_y = pos_y

        self.alive = alive

        self.edges = edges

        self.neighbors = self.__getneighbors()

    def __getneighbors(self):
        neighbors = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if (x, y) == (0, 0):
                    continue
                if x < 0 and self.edges[0]:
                    continue
                if x > 0 and self.edges[1]:
                    continue
                if y < 0 and self.edges[2]:
                    continue
                if y > 0 and self.edges[3]:
                    continue

                print(x, y)

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, newval):
        raise Exception("No can do!")

    @property
    def pos_y(self):
        return self.__pos_y

    @pos_y.setter
    def pos_y(self, newval):
        raise Exception("No can do!")




