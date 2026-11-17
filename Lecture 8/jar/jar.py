class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise ValueError("Only numbers are accepted.")
        elif capacity < 0:
            raise ValueError("The number of cookies can't be negative.")
        self._size = 0
        self._capacity = capacity

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("The number of cookies can't be negative.")
        elif n + self._size > self._capacity:
            raise ValueError("The deposite exceeds the capacity of the jar.")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("The number of cookies can't be negative.")
        elif n > self._size:
            raise ValueError("The withdraw number of cookies exceeds the size of the jar.")
        self._size -= n

    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return self._capacity


# def main():
#     n = input("Number of cookies: ")
#     jar = Jar()
#     jar.deposit(n)
#     print(jar.capacity)


# if __name__ == "__main__":
#     main()