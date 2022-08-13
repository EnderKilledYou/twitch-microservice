from pyee.base import EventEmitter

overwatch_event = EventEmitter()

from Ocr.frame import Frame


@overwatch_event.on('elim')
def on_elim_event(frame: Frame, count: int, duration: int, last_death):
    print("{4} Kill count: {0} seconds in: {1} last death: {2} , Duration: {3}  ".format(count, str(frame.ts_second),
                                                                                         last_death,
                                                                                         duration, frame.source_name))
    # ocr: TwitchVideoFrameBuffer = get_frame_buffer(frame.source_name)
    # config = get_streamer_config(frame.source_name)
    # clip_time_stamp = ClipTimeStamp()
    # clip_time_stamp.start = frame.ts_second
    # clip_time_stamp.end = frame.ts_second + duration + 1
    # clip_time_stamp.duration = duration
    # clip_time_stamp.type = 'elim'
    # clip_time_stamp.start_buffer = config.buffer_elim_clip_before
    # clip_time_stamp.end_buffer = config.buffer_elim_clip_after
    # ocr.stream_clipper.clip_request(clip_time_stamp)




@overwatch_event.on('elimed')
def on_elimed_event(frame: Frame):  # you can save the frame data for a screen cap
    print("Streamer Died")



@overwatch_event.on('healing')
def on_healing_event(frame: Frame, duration: int):
    print("Streamer " + frame.source_name + " healing " + str(duration))




@overwatch_event.on('queue_start')
def on_queue_start_event(frame: Frame):
    print("Streamer " + frame.source_name + " queue_start ")


@overwatch_event.on('assist')
def on_assist_event(frame: Frame, duration: int):
    print("Streamer " + frame.source_name + " assist " + str(duration))



@overwatch_event.on('defense')
def on_defense_event(frame: Frame, duration: int):
    print("Streamer " + frame.source_name + " defense " + str(duration))



@overwatch_event.on('orbed')
def on_orbed_event(frame: Frame):
    print("Streamer " + frame.source_name + " orbed")



@overwatch_event.on('slept')
def on_orbed_event(frame: Frame):
    print("Streamer " + frame.source_name + " slepting")



@overwatch_event.on('blocking')
def on_blocking_event(frame: Frame, duration: int):
    print("Streamer " + frame.source_name + " blocking " + str(duration))



@overwatch_event.on('spawn_room')
def on_spawn_room_event(frame: Frame):

    print("Streamer " + frame.source_name + " Spawning")
    # ocr: TwitchVideoFrameBuffer = get_frame_buffer(frame.source_name)
    # clip_time_stamp = ClipTimeStamp()
    # clip_time_stamp.start = frame.ts_second
    # clip_time_stamp.end = frame.ts_second   + 3
    # clip_time_stamp.duration = 3
    # clip_time_stamp.type = 'elim'
    # clip_time_stamp.start_buffer = 5
    # clip_time_stamp.end_buffer = 5
   # ocr.stream_clipper.clip_request(clip_time_stamp)



@overwatch_event.on('game_start')
def on_game_start_event(frame: Frame):
    print("Streamer " + frame.source_name + " Game started")


@overwatch_event.on('game_end')
def on_game_end_event(frame: Frame):
    print("Streamer " + frame.source_name + " Game started")

