from http.server import BaseHTTPRequestHandler
import urllib.request
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. 오리지널 guns.lol 가상 브라우저 헤더 설정 (우회 핵심)
        url = "https://guns.lol"
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        )
        
        try:
            # 2. guns.lol 서비스 자체 소스코드를 백엔드에서 통째로 다운로드
            with urllib.request.urlopen(req) as response:
                guns_html = response.read().decode('utf-8')
            
            # 3. guns.lol 소스코드 내부에 박힌 주소 경로들을 내 사이트와 호환되도록 자동 파싱 매핑
            guns_html = guns_html.replace('href="/', 'href="https://guns.lol')
            guns_html = guns_html.replace('src="/', 'src="https://guns.lol')
            
            # 4. 브라우저 보안 잠금 헤더를 무력화하고 출력 데이터 전송
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            # 기존 X-Frame 차단 헤더를 보내지 않아 브라우저 락을 완벽 우회
            self.end_headers()
            
            self.wfile.write(guns_html.encode('utf-8'))
            
        except Exception as e:
            # 에러 발생 시 디버깅용 텍스트 출력
            self.send_response(500)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(f"서버 파싱 에러 발생: {str(e)}".encode('utf-8'))
        return
