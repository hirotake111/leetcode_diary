class Class:
    def func(self):
        foo: int = 10

        def inner():
            print(f"foo: {foo}")

        inner()


if __name__ == "__main__":
    c = Class()
    c.func()
