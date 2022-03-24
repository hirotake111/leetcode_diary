from typing import List


class User:
    name: str
    age: int
    hasChild: bool

    def __init__(self: any, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.hasChild = True

    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.hasChild}"


def func(arr: List[int]):
    arr.append(1)
    return


def func2(u: User):
    u.age = 1
    u.name = "b"
    u.hasChild = False


if __name__ == "__main__":
    a = []
    func(a)
    print(f"result: {a}")
    b = User("hiro", 39)
    func2(b)
    print(b)
