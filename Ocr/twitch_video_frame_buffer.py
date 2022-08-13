import traceback

import cv2
import cv2 as cv
import streamlink
from streamlink import Streamlink

from Ocr.frame import Frame
from Ocr.get_unix_time import get_unix_time

from Ocr.video_frame_buffer import VideoFrameBuffer

sl_session = Streamlink()


class TwitchVideoFrameBuffer(VideoFrameBuffer):
    frame_streamer_name: str = ''
    file_name = ''

    def __init__(self, broadcaster: str, sample_rate: int):
        super(TwitchVideoFrameBuffer, self).__init__()

        self.broadcaster = broadcaster

        self.Active = True
        self.sample_rate = sample_rate

    def watch_streamer(self):
        self.buffer_twitch_broadcast()
        self.Active = False
        print("Exiting watch of " + self.broadcaster)

    def buffer_twitch_broadcast(self):

        try:
            streams = sl_session.streams('https://www.twitch.tv/{0}'.format(self.broadcaster))
        except BaseException as e:
            traceback.print_exc()
            return
        if 'best' not in streams:
            print("stream offline")
            self.Active = False
            return
        self.file_name = "{0}_{1}.ts".format(self.broadcaster, str(get_unix_time()))
        ocr_stream = streams['best']

        if '720p60' in streams:
            ocr_stream = streams['720p60']
            self.fps = 60
        else:
            for stream_res in streams:
                if not stream_res.endswith('p60'):
                    continue
                ocr_stream = streams[stream_res]
                self.fps = 60

        self._capture_stream(ocr_stream)

    def _capture_stream(self, stream):
        url = stream.url
        self.capture_url_or_file(url)

    def capture_url_or_file(self, url):
        video_capture = cv2.VideoCapture(url)
        if not video_capture:
            print("Capture could not open stream")
        #     return
        try:
            if self.fps == 0:
                self.fps = video_capture.get(cv2.cv.CV_CAP_PROP_FPS)
                if self.fps > 1000:
                    self.fps = 60
            frame_number = 0
            self.Capturing = True
            # sample_rate = (self.fps // self.sample_rate)
            sample_rate = 4
            while self.Active and video_capture.isOpened():
                ret, frame = video_capture.read()
                if not ret:
                    break
                frame_number += 1

                if frame_number % sample_rate != 0:
                    continue
                self.buffer.put(
                    Frame(frame_number, frame, frame_number // self.fps, self.frame_streamer_name, self.file_name))
            self.Capturing = False
        except Exception as e:

            print(e)

            traceback.print_exc()
        try:
            video_capture.release()
        except Exception as e:
            print("cap release failed")
            print(e)
            print(traceback.format_exc())

        print("Capture thread stopping")
