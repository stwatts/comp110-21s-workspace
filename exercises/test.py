from __future__ import annotations

from typing import Union

class Yikes:
    x: int = 0

    def __add__(self, rhs: Yikes) -> int:
        self.x += rhs.x
        return self.x

a: Yikes = Yikes()
a.x = 5
b: Yikes = Yikes()
b.x = 10
c: int = a + b

d: int = b + a

y: Yikes = Yikes()
y.x = 1
z: int = y.x + 1
print(z)