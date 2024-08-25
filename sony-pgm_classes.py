class Shape:
    def create(self):
        print("A shape creation in progress")

    def printShapeCreated(self):
        print("A General shape is created successfully")

class Circle(Shape):
    def printShapeCreated(self):
        print("A circle is created successfully")

circleShape = Circle()
circleShape.create()
circleShape.printShapeCreated()
circleShape = Shape()
circleShape.create()
circleShape.printShapeCreated()

#OUTPUT
#A shape creation in progress
#A circle is created successfully
#A shape creation in progress
#A General shape is created successfully
