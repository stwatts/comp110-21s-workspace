"""Utility functions for wrangling data."""

__author__ = "720332576"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], x: str) -> list[str]:
    """Creates a list of strs of all the values in a column."""
    columns: list[str] = []
    for row in table:
        for a in row:
            if a == x:
                columns.append(row[x])
    return columns


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Creates a column based table from row based."""
    columns: dict[str, list[str]] = {}
    for row in table:
        for a in row:
            if a not in columns:
                columns[a] = column_values(table, a)
    return columns


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Head function to display first N rows."""
    if rows >= len(table):
        return table
    else:
        newdict: dict[str, list[str]] = {}
        keys: list[str] = table.keys()
        for key in keys:
            values: list[str] = []
            i: int = 0
            while i < rows:
                values.append(table[key][i])
                i += 1
            newdict[key] = values
        return newdict
        

def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Selects certain columns from table."""
    newdict: dict[str, list[str]] = {}
    for key in names:
        newdict[key] = table[key]
    return newdict


def count(data: list[str]) -> dict[str, int]:
    """Counts the number of times each unique value is in a list."""
    newdict: dict[str, int] = {}
    length: int = len(data)
    i: int = 0
    while i < length:
        if data[i] in newdict:
            newdict[data[i]] += 1
            i += 1
        else:
            newdict[data[i]] = 1
            i += 1
    return newdict
