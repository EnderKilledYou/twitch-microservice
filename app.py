from flask import Flask, jsonify

from Ocr.monitor import Monitor
from monitor_manager import is_stream_monitored, add_stream_to_monitor, get_stream_monitors_for_web, \
    remove_stream_to_monitor

app = Flask(__name__)

@app.route('/add/<stream_name>')
def add(stream_name):
    if not is_stream_monitored(stream_name):
        add_stream_to_monitor(stream_name)
    for_web = get_stream_monitors_for_web()
    return jsonify({"success": True, 'items': for_web})



@app.route('/list')
def list():
    for_web = get_stream_monitors_for_web()
    return jsonify({"success": True, 'items': for_web})


@app.route('/remove/<stream_name>')
def remove(stream_name):
    if is_stream_monitored(stream_name):
        remove_stream_to_monitor(stream_name)

    for_web = get_stream_monitors_for_web()
    return jsonify({"success": True, 'items': for_web})


if __name__ == '__main__':



    app.run()

