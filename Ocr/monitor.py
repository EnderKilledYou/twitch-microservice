import threading
from queue import Queue

from Ocr.frame_aggregator import FrameAggregator
from Ocr.frame_buffer import set_frame_buffer
from Ocr.ordered_frame_aggregator import OrderedFrameAggregator
from Ocr.overwatch_events import overwatch_event
from Ocr.overwatch_screen_reader import OverwatchScreenReader
from Ocr.screen_reader import ScreenReader
from Ocr.twitch_video_frame_buffer import TwitchVideoFrameBuffer
from Ocr.video_frame_buffer import VideoFrameBuffer


class Monitor:
    ocr: VideoFrameBuffer
    broadcaster: str
    agg: FrameAggregator
    matcher: ScreenReader

    def __init__(self, broadcaster: str, ):
        print("read starting " + broadcaster)
        self.broadcaster = broadcaster
        self.ocr = TwitchVideoFrameBuffer(broadcaster, 16)
        self.ocr.frame_streamer_name = broadcaster
        set_frame_buffer(broadcaster, self.ocr)

        self.agg = OrderedFrameAggregator(overwatch_event)
        self.matcher = OverwatchScreenReader(self.ocr, self.agg)
        self.producer_thread = threading.Thread(target=self.ocr.watch_streamer, args=[])

        self.consumer_threads = []
        for i in range(0, 10):
            consumer_thread = threading.Thread(target=self.matcher.consume_twitch_broadcast)
            self.consumer_threads.append(consumer_thread)
        self.producer_thread.start()

        for consumer_thread in self.consumer_threads:
            consumer_thread.start()

    def join(self):
        for consumer_thread in self.consumer_threads:
            consumer_thread.join()
        self.producer_thread.join()

    def dump(self):
        tmp = self.ocr.buffer
        self.ocr.buffer = Queue()
        while not tmp.empty():
            try:
                tmp.get(False)
            finally:
                return

    def stop(self):
        self.ocr.Active = False
        self.matcher.Active = False
