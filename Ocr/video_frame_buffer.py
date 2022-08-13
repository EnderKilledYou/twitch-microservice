from queue import Queue
from typing import Any


class VideoFrameBuffer:
    Capturing: bool
    buffer: Queue
    Active: bool

    def __init__(self):
        self.Capturing = False
        self.buffer = Queue()
        self.Active = True
