class Cat:
    MEOWS = 5

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow  meow  meow meow  meow  "
                  "meow meow  meow  meow meow  "
                  "meow meow  meow meow  meow "
                  "meow  meow meow"
                  " meow")


cat = Cat()
cat.meow()

# type hint !!
# meow
