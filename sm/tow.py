import random


class Tow:
    """    
    Tow Class represents a Tower of Watches (TOW) that keeps track of a block number
    within a specified range and allows you to create and retrieve block numbers.
    """

    def __init__(self, min_block, max_block):
        self.min_block = min_block
        self.max_block = max_block

        self.block_number = 0

    def choose_block_number_in_tow(self):
        self.block_number = random.randint(self.min_block, self.max_block)

    def create_a_block(self):
        self.block_number -= 1

    def get_current_block_number(self):
        return self.block_number
