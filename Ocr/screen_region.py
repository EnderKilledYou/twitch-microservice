from PIL import Image

from Ocr.frame import Frame
from Ocr.frame_aggregator import FrameAggregator


class ScreenRegion:
    def crop(self, img):
        """crops this specific screen region."""
        pass

    def process(self, pil: Image, frame: Frame, frame_watcher: FrameAggregator,   show:bool = False):
        """Runs the region analysis and return sends the result to the frame watcher."""
        pass
