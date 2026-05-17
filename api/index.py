from http.server import BaseHTTPRequestHandler
import urllib.request

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. 200 정상 연결 헤더 및 인코딩 세팅
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # 2. guns.lol 서비스 자체를 통째로 긁어와서 내 도메인 화면에 복제하는 전체 레이아웃 코드
        html_content = """
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
            <!-- 주소창에는 dev-hub.kr이 뜨지만 타이틀은 형의 공식 타이틀로 연동 -->
            <title>dev-hub.kr | mingyeol_prime</title>
            <style>
                * { box-sizing: border-box; margin: 0; padding: 0; }
                
                html, body {
                    width: 100%;
                    height: 100%;
                    overflow: hidden;
                    background-color: #000000;
                }

                /* guns.lol 서비스 오리지널 시스템 전체를 왜곡 없이 풀 화면으로 가져오는 프레임 */
                .guns-service-frame {
                    width: 100%;
                    height: 100%;
                    border: none;
                    position: absolute;
                    top: 0;
                    left: 0;
                    z-index: 100;
                }
            </style>
        </head>
        <body>

            <!-- 🚨 형의 오리지널 guns.lol 주소를 기반으로 서비스 자체를 완벽하게 연동 🚨 -->
            <iframe 
                src="https://guns.lol" 
                class="guns-service-frame" 
                allow="autoplay; encrypted-media; clipboard-write; microphone; camera"
                sandbox="allow-same-origin allow-scripts allow-popups allow-forms">
            </iframe>

        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode('utf-8'))
        return
