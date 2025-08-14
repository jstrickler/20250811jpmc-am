import typing as T

x: int
x = 5
# x = "abc"
print(x)

colors: list[str] = []
colors.append('red')
colors.append(5)

person1: tuple[str, ...]  # all elements must be str
person2: tuple[str, str]

counts: dict[str, int] = {}
counts['a'] = 5
counts['b'] = "abc"
counts[1] = 5

items: set[int|float] = set()
items.add(5)
items.add(10)
items.add(3.5)
items.add("abc")

def update(value: int|float) -> float:
    return 0.0

def make_upper(word_list: T.Iterable[str]) -> list[str]:
    return [w.upper() for w in word_list]

words = ['wombat', 'camel', 'moose']
print(make_upper(words))

more_words = 'winken', 'blinken', 'nod'
print(make_upper(more_words))

def spam(arg: T.Any) -> None:
    print("SPAM")


class Dog:
    pass

class Cat:
    pass

def go_walkies(dog: Dog) -> None:
    print("walking...")

d = Dog()
c = Cat()
go_walkies(d)
go_walkies(c)



class Spam:
    def __init__(self, ham: "Ham"):
        pass

class Ham:
    pass