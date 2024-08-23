# Author: Raphael Senn

from prettytable import PrettyTable
from typing import Callable


def project(table: PrettyTable, cols: list[int], distinct: bool=False) -> PrettyTable:
    table_result = PrettyTable()
    table_result.field_names = [table.field_names[col_index] for col_index in cols]
    if not distinct:
        for row in table.rows:
            table_result.add_row([row[col_index] for col_index in cols])
        return table_result
    for row in table.rows:
        row_result = [row[col_index] for col_index in cols]
        if row_result not in table_result.rows:
            table_result.add_row(row_result)
    return table_result


def select(table: PrettyTable, phi: Callable[[list], bool]) -> PrettyTable:
    table_result = PrettyTable()
    table_result.field_names = table.field_names
    for row in table.rows: 
        if phi(row):
            table_result.add_row(row)
    return table_result


def cartesian_product(table_1: PrettyTable, table_2: PrettyTable) -> PrettyTable:
    table_result = PrettyTable()
    table_result.field_names = table_1.field_names + table_2.field_names
    for row1 in table_1.rows:
        for row2 in table_2.rows:
            new_row = row1 + row2
            table_result.add_row(new_row)
    return table_result


def join(table_1: PrettyTable, table_2: PrettyTable, j1: int, j2: int) -> PrettyTable:
    table_result = PrettyTable()
    table_result.field_names = table_1.field_names + table_2.field_names
    for row1 in table_1.rows:
        for row2 in table_2.rows:
            if row1[j1] == row2[j2]:
                new_row = row1 + row2
                table_result.add_row(new_row)
    return table_result 