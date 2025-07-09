class Iterator:
    def __init__(self):
        self.container = []
        self.__current_index = 0

    def __len__(self):
        return len(self.container)

    def __iter__(self):
        self.__current_index = 0

        return self

    def __next__(self):
        if self.__current_index >= len(self):
            raise StopIteration
        else:
            self.__current_index += 1

        return self.container[self.__current_index - 1]