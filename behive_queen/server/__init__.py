import tornado.ioloop
import tornado.web
import tornado.websocket

from server.log import logger


class WebSocketServer(tornado.websocket.WebSocketHandler):
    def open(self):
        logger.info("WebSocket opened")

    def on_message(self, message):
        logger.info("Message received!")
        self.write_message("You said: " + message)

    def on_close(self):
        logger.info("WebSocket closed")


def main():
    # Create a web app whose only endpoint is a WebSocket, and start the web
    # app on port 8888.
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],
        websocket_ping_interval=10,
        websocket_ping_timeout=30,
    )
    app.listen(8888)

    # Create an event loop (what Tornado calls an IOLoop).
    io_loop = tornado.ioloop.IOLoop.current()

    # Start the event loop.
    io_loop.start()

