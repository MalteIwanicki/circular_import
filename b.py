from a import A


class B:
    def __init__(self, a: A):
        print("B created.")
        self.a = a
