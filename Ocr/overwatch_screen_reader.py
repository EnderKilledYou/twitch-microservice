import cv2
from PIL import Image

from Ocr.frame import Frame
from Ocr.frame_aggregator import FrameAggregator
from Ocr.overwatch_action_screen_region import OverwatchActionScreenRegion
from Ocr.screen_reader import ScreenReader
from Ocr.video_frame_buffer import VideoFrameBuffer


class OverwatchScreenReader(ScreenReader):
    def __init__(self, framebuffer: VideoFrameBuffer, frame_watcher: FrameAggregator):
        super(OverwatchScreenReader, self).__init__(framebuffer)
        self.skip_frames = 0
        self.last_queue_check = 0
        self.Show = False
        self.last_action_second = 0
        self.ActionTextCropper = OverwatchActionScreenRegion()
        self.frame_watcher = frame_watcher

    def ocr(self, frame: Frame) -> None:
        try:
            gray = cv2.cvtColor(frame.image, cv2.COLOR_RGB2GRAY)
        #    ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
         #   dst = cv2.fastNlMeansDenoising(th2, 10, 10, 7)
            pil_grey = Image.fromarray(gray)
            self.ActionTextCropper.process(pil_grey, frame, self.frame_watcher,
                                            self.Show)

        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()
