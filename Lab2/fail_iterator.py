import csv


class FailIterator:
    """iteration class"""
    def __init__(self, path_csv: str, number_of_star: int):
        """initialization of the iterated class, where data is read from a csv fail
         and the necessary data is written to an array"""
        self.__number_of_star: int = number_of_star
        self.__path_list: list = list()
        self.__count: int = 0
        with open(path_csv, "r",  encoding='utf-8') as fail:
            read = csv.reader(fail)
            for row in read:
                if row[2] == str(self.__number_of_star):
                    self.__path_list.append(row[0])

    def __iter__(self):
        return self

    def get_len(self):
        return len(self.__path_list)

    def __next__(self) -> str:
        """the __next__ method that iterates through the array elements"""
        if len(self.__path_list) != self.__count:
            elem: str = self.__path_list[self.__count]
            self.__count += 1
            return elem
        else:
            raise StopIteration
