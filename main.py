class Shape:
    def init(self,w,h):
        self.w=w
        self.h=h
    @staticmethod
    def area(w,h):
        return w*h


w = int(input())
h = int(input())

print(Shape.area(w, h))