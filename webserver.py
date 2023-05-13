import socketpool
import wifi
import digitalio
import board
from adafruit_httpserver.mime_type import MIMEType
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.server import HTTPServer

MODE_TOP = 0
MODE_ON = 1
MODE_OFF = 2

ssid = "your_ssid"
password = "your_pass"

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

wifi.radio.connect(ssid, password)
print("Connected to", wifi.radio.ipv4_address)

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool, "/static")

def sendResp(request, mode):
    resp = HTTPResponse(request, content_type = MIMEType.TYPE_HTML)
    html = f"""
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Web</title>
    </head>
    <body>
    """
    if mode == MODE_ON:
        html += "<p>Onにしました</p>"
    elif mode == MODE_OFF:
        html += "<p>Offにしました</p>"
    html += f"""
        <ul>
            <li><a href="/on">on</a></li>
            <li><a href="/off">off</a></li>
        </ul>
        </ul>
    </body>
</html>
    """
    resp.send(html)

@server.route("/")
def base(request: HTTPRequest):
    sendResp(request, MODE_TOP)

@server.route("/on")
def led_on(request: HTTPRequest):
    led.value = True
    sendResp(request, MODE_ON)

@server.route("/off")
def led_on(request: HTTPRequest):
    led.value = False
    sendResp(request, MODE_OFF)

server.serve_forever(str(wifi.radio.ipv4_address), port = 80)
