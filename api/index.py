from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # guns.lol 보안 시스템을 우회하는 강력한 영구 리다이렉트(301) 헤더 전송
        self.send_response(301)
        self.send_header('Location', 'https://guns.lol')
        self.end_headers()
        return
