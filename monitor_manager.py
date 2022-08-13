import threading

from Ocr.monitor import Monitor

monitor_lock = threading.Lock()
monitors = []


def get_monitors():
    return monitors.copy()


def get_stream_monitors_for_web():
    return list(map(map_for_web, get_monitors()))


def map_for_web(monitor: Monitor):
    qsize = monitor.ocr.buffer.qsize()
    name = monitor.broadcaster
    seconds = qsize / 16

    return {
        'name': name,

        'seconds': seconds,
        'queue_size': qsize
    }


def add_stream_to_monitor(stream_name):
    monitor_lock.acquire(True, -1)
    try:
        monitors.append(Monitor(stream_name))
    finally:
        monitor_lock.release()


def is_stream_monitored(stream_name):
    for monitor in get_monitors():
        if monitor.broadcaster == stream_name:
            return True
    return False


def remove_stream_to_monitor(stream_name):
    tmp = []
    for monitor in get_monitors():
        if monitor.broadcaster == stream_name:
            monitor.stop()
        else:
            tmp.append(monitor.ocr)
    copy_tmp_to_monitors(tmp)


def copy_tmp_to_monitors(tmp):
    monitor_lock.acquire(True, -1)
    try:
        monitors.clear()
        for i in tmp:
            monitors.append(i)
    finally:
        monitor_lock.release()
