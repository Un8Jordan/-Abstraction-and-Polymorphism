from abc import ABC, abstractmethod

class Animal(ABC):
    #abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")
