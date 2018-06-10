"""Implementation of the class TabularData"""
from copy import deepcopy
import json
class TabularData:
    def __init__(self, column_names):
        self.column_names=list(column_names) #nie musza sobie odpowiadac
        self._rows=[] #pole prywatne w pythonie - nikt poza instancjami nie ma do niego dostepu; podkreslnik na poczatku
        self._columns = {}
        for idx, name in enumerate(column_names):
            self._columns[name] = idx
            #ew. wyrazenie slownikowe: self._columns = {name: idx for idx, name in enumerate(column_names)}
        if len(column_names) > len(self._columns):
            raise ValueError("Column names has to be unique")

    def get_row(self, row_n):
        if row_n < 0 or row_n >= len(self._rows):
            raise ValueError ("invalid row number: ", row_n)
        return self._rows[row_n]


    def get_column(self, col_name):
        if col_name not in self._columns:
            raise KeyError("Unknown column name: ", col_name)
        idx = self._columns[col_name]
        values = []
        for row in self._rows:
            values.append((row[idx]))
        return values

    def append(self, new_row):
        if len(new_row) != len(self._columns):
            raise ValueError("Row should have size: ", len(self._columns))
        return self._rows.append(new_row)

    def rows_count(self):
        return len(self._rows)

    def __len__(self):
        return len(self._rows)

    def __str__(self):
        return str(self._rows)

    def to_json(self):
        slownik = {"columns": self.column_names, "rows": self._rows}
        return json.dumps(slownik)

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        for columns, rows in data:
            table = TabularData(data[columns])
            for row in data['rows']:
                table.append(row)
        return table

    def to_json_file(self, tab_json):
        slownik = {"columns": self.column_names, "rows": self._rows}
        json.dump(slownik, tab_json)

    @staticmethod
    def from_json_file(tab_json):
        data = json.load(tab_json)
        table = TabularData(data['columns'])
        for row in data['rows']:
            table.append(row)
        return table


xyz =TabularData(['name', 'surname', 'age'])
xyz.append(["John", "Doe", 12])
print(xyz.append)
xyz.append(["Anne", "Novak", 22])
print(xyz._rows)
xyz.get_row(0)
print(xyz.get_row(0))
xyz.rows_count()
print(xyz.rows_count())
xyz.get_column("age")
print(xyz.get_column("age"))
print(len(xyz)) #dzieki temu, że w def bylo __len__ mozna to tak printowac
print(str(xyz))
xyz.to_json()
print(xyz.to_json())
with open('tab.json', 'wt') as tab_json:
    xyz.to_json_file(tab_json)
with open('tab.json', 'rt') as tab_json:
    xyz2 = TabularData.from_json_file(tab_json)
print('to jest xyz2', xyz2)
