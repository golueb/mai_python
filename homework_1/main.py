class Animal:
    name = ''
    sound = ''
    def make_sound(self):
        print(self.sound)

cat = Animal()
cat.color = 'white'
cat.sound = 'meow'
dog = Animal()
dog.sound = 'woof'
dog.color = 'blue'

cat.make_sound()
dog.make_sound()