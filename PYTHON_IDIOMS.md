# Python Idioms
## Multiplication Instead of a Loop
Something like that:
```
class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        cookies = []
        for i in range(self._size):
            cookies.append("🍪")
        emoji_cookies = "".join(cookies)
        return f"{emoji_cookies}"
```
Can be replaced with this:
```
class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        return "🍪" * self._size
```