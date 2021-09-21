from b import B


class A:
    def __init__(self):
        self.bs = []

    def add_b(self, b: B):
        """As can hold references to Bs."""
        self.bs.append(b)
