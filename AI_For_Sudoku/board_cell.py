import math

class board_cell:
    def __init__(self):
        self.domain = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.assignment = -1

    def remove_from_domain(self, elem):
        self.domain.remove(elem)

    def check_if_element_present(self, elem):
        return elem in self.domain
