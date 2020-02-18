class BooleanData:

    def __init__(self, objects):
        self.objects = list(objects)

    @ property
    def head(self):
        return(self.objects[0])

    @ property
    def tail(self):
        if len(self.objects) > 1:
            return self.objects[1:]
        else:
            return []

class BooleanUnion(BooleanData):
    def get_distance(self, pt):
        loc_diss = []
        for loc_obj in self.objects:
            loc_diss.append(loc_obj.get_distance(pt))

        return min(loc_diss)

class BooleanDifference(BooleanData):
    def get_distance(self, pt):
        loc_diss = [self.head.get_distance(pt)]
        for loc_obj in self.tail:
            loc_diss.append(- loc_obj.get_distance(pt))

        return max(loc_diss)

class BooleanIntersection(BooleanData):
    def get_distance(self, pt):
        loc_diss = []
        for loc_obj in self.objects:
            loc_diss.append(loc_obj.get_distance(pt))

        return max(loc_diss)