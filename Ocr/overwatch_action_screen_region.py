import os

import cv2
import numpy
from PIL import Image

from Ocr.frame import Frame
from Ocr.frame_aggregator import FrameAggregator
from Ocr.image_to_string import image_to_string
from Ocr.screen_region import ScreenRegion


class OverwatchActionScreenRegion(ScreenRegion):
    def process(self, pil: Image, frame: Frame, frame_watcher: FrameAggregator,    show: bool = False):
        img_crop = self.crop(pil)
        ocrMatch = image_to_string(img_crop)
        if len(ocrMatch.matches) == 0:
            return
        self._process_amtches(frame, frame_watcher, ocrMatch)

    def _process_amtches(self, frame, frame_watcher, ocrMatch):
        if 'elim' in ocrMatch.matches:
            frame_watcher.add_elim_frame(frame)
            frame.empty = False
        if 'healing' in ocrMatch.matches:
            frame_watcher.add_healing_frame(frame)
            frame.empty = False
        if 'hero_select' in ocrMatch.matches:
            frame_watcher.add_spawn_room_frame(frame)
            frame.empty = False
        if 'defense' in ocrMatch.matches:
            frame_watcher.add_defense_frame(frame)
            frame.empty = False
        if 'orbed' in ocrMatch.matches:
            frame_watcher.add_orb_gained_frame(frame)
            frame.empty = False
        if 'slept' in ocrMatch.matches:
            frame_watcher.add_slepting_frame(frame)
            frame.empty = False
        if 'block' in ocrMatch.matches:
            frame_watcher.add_blocking_frame(frame)
            frame.empty = False
        if 'death' in ocrMatch.matches:
            frame_watcher.add_elimed_frame(frame)
            frame.empty = False
        if 'assist' in ocrMatch.matches:
            frame_watcher.add_assist_frame(frame)
            frame.empty = False

    def crop(self, img):
        right = img.width - (img.width * .25)
        left = (img.width * .27)
        upper = img.height / 2
        lower = img.height - (img.height * .18)
        im_crop = img.crop(  # (left, upper, right, lower)-
            (left,
             upper,  # crop the part where it tells you where shit happens.
             right,
             lower)
        )

        return im_crop
