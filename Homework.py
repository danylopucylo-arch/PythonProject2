from os import name


class Animal:
        def __init__(self, name, age, furcolor):
            self.name = name
            self.age = age
            self.furcolor = furcolor

class Dog(Animal):
        def __init__(self,name ,age ,furcolor , tail, eyes_color):
            self.furcolor = furcolor
            self.tail = tail
            self.eyes_color = eyes_color
            self.name = name
            self.age = age
        def look_at_Puppy(self):
            print(f"Look at him {self.name} he is {self.age} years old")
class Cat(Animal):
        def __init__(self,age,name ,furcolor, tail, height):
            self.age = age
            self.furcolor = furcolor
            self.tail = tail
            self.height = height
            self.name = name

        def Look_at_Kitty(self):
            print(f"Look at her {self.name} she is {self.age} years old and she is {self.furcolor} her tail is {self.tail} her height is {self.height}")

sphinks = Cat(3,"Betty", "without fur", "long-middle","DarkBlue")
Buldog = Dog("Jax", 5, "BrightBrown", "short","BrightGreen" )
sphinks.Look_at_Kitty()
Buldog.look_at_Puppy()
