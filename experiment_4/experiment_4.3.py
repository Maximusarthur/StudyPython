class Animal:
    def sound(self):
        """基类Animal的叫声方法"""
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        """派生类Dog的叫声方法"""
        print("Dog sound")


class Cat(Animal):
    def sound(self):
        """派生类Cat的叫声方法"""
        print("Cat sound")


class DogCat(Dog, Cat):
    pass


dog_cat = DogCat()
dog_cat.sound()  # 输出：Dog sound
