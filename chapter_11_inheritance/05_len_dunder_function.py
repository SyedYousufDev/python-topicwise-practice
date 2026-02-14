#Details about the dunder

#In Python, __len__ is a special (dunder) method that defines what should be returned when the built-in len() function is called on an object. When you write len(obj), Python internally calls obj.__len__(). This method must return a non-negative integer representing the size or length of the object. By defining __len__ in a custom class, you can make your objects behave like built-in containers such as lists or strings.


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


# Example usage
v = Vector(7, 8, 10)
print(v)