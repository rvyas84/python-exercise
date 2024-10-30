class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def personTalk(self):
        print(f"Hi, I am {self.first_name} {self.last_name}.")


rv = Person("Rajan", "Vyas")
print(rv.first_name)
print(rv.last_name)
rv.personTalk()

mv = Person("Manisha", "Vyas")
print(mv.first_name)
print(mv.last_name)
mv.personTalk()