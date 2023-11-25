import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import random  # NOQA

from sm.block_creation_status import BlockCreationStatus  # NOQA
from sm.tow import Tow  # NOQA


class TimeWindow:
    """
    TimeWindow Class represents a time window consisting of multiple Tower of Watches (TOWs).
    It tracks the creation status of blocks within the TOWs."""
        
    def __init__(self, tow_number, min_tow_block_number, max_tow_block_number):
        self.tow_number = tow_number

        self.min_tow_block_number = min_tow_block_number
        self.max_tow_block_number = max_tow_block_number

        self.tows = [Tow(min_tow_block_number, max_tow_block_number)
                     for _ in range(tow_number)]

        for tow in self.tows:
            tow.choose_block_number_in_tow()

        self.current_tow = 0

    def create_a_block(self):
        if self.current_tow < self.tow_number:
            self.tows[self.current_tow].create_a_block()
            if self.tows[self.current_tow].get_current_block_number() > 0:
                return BlockCreationStatus.Normal

            elif self.tows[self.current_tow].get_current_block_number() == 0:
                self.current_tow += 1
                return BlockCreationStatus.EndTow

        return BlockCreationStatus.EndTimeWindow

    def get_average_tow(self):
        return (self.min_tow_block_number + self.max_tow_block_number) / 2
