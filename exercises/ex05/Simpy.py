"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "720332576"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Construct a simpy class."""
        self.values = values

    def __repr__(self) -> str:
        """Used to print as a string."""
        return f"Simpy({self.values})"
   
    def fill(self, value: float, repeat: int) -> None:
        """Fills values list with value repeated."""
        self.values = []
        i: int = 0
        while i < repeat:
            self.values.append(value)
            i += 1
        return self

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Filles values list with list of numbers."""
        assert step != 0.0
        self.values = []
        self.values.append(start)
        i: float = start
        if step > 0:
            while i < (stop - step):
                self.values.append(i + step)
                i += step
            return self
        else:
            while i > (stop - step):
                self.values.append(i + step)
                i += step
            return self

    def sum(self) -> float:
        """Adds all numbers in an object together."""
        return sum(self.values)

    def __add__(self, rhs: (Union[float, Simpy])) -> Simpy:
        """Addition overloading."""
        result: list[float] = []
        if isinstance(rhs, float):
            for each in self.values:
                result.append(each + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, rhs: (Union[float, Simpy])) -> Simpy:
        """Exponent overloading."""
        result: list[float] = []
        if isinstance(rhs, float):
            for each in self.values:
                result.append(each ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __mod__(self, rhs: (Union[float, Simpy])) -> Simpy:
        """Mod overloading."""
        result: list[float] = []
        if isinstance(rhs, float):
            for each in self.values:
                result.append(each % rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: (Union[float, Simpy])) -> list[bool]:
        """Equality operator overload."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for each in self.values:
                result.append(each == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: (Union[float, Simpy])) -> list[bool]:
        """Greater than overload."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for each in self.values:
                result.append(each > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: (Union[int, list[bool]])) -> Union[float, Simpy]:
        """Get item subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            result: list[float] = []
            for i in range(len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)
