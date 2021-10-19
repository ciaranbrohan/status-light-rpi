#!/usr/bin/env python3
  
import json
from flask import Flask, request
from unicornhatmini import UnicornHATMini

app = Flask(__name__)

unicorn = UnicornHATMini()

def set_state(text):
    if text in config['statuses']:
        return set_color(config['statuses'][text])
    elif text == 'off':
        return set_color('off')
    elif text in config['colors']:
        return set_color(text)
    else: 
        return False
 
def set_color(color):
    if color == 'off':
        unicorn.clear()
        unicorn.show()
        return True
    elif color in config['colors']:
        unicorn.set_all(config['colors'][color][0],config['colors'][color][1],config['colors'][color][2])
        unicorn.show()
        
        return True
    else:
        return False
 
@app.route('/api/status/free', methods=['POST', 'GET'])
def set_free():
    if set_state('free'):
        return '200 - OK'
    else:
        return f"Unable to process request.", 400

@app.route('/api/status/busy', methods=['POST', 'GET'])
def set_busy():
    if set_state('busy'):
        return '200 - OK'
    else:
        return f"Unable to process request.", 400

@app.route('/api/status/away', methods=['POST', 'GET'])
def set_away():
    if set_state('away'):
        return '200 - OK'
    else:
        return f"Unable to process request.", 400

@app.route('/api/status/donotdisturb', methods=['POST', 'GET'])
def set_dnd():
    if set_state('donotdisturb'):
        return '200 - OK'
    else:
        return f"Unable to process request.", 400
 
if __name__ == '__main__':
    with open('config.json', 'r') as read_file:
        config = json.load(read_file)
    set_color('off')
    app.run(host='0.0.0.0')
