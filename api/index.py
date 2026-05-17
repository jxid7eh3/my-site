from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # 아까 짠 guns.lol 스타일의 힙한 바이오 화면 HTML
        html_content = """
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dev-hub.kr | MINGYEOL_PRIME</title>
            <style>
                * { box-sizing: border-box; margin: 0; padding: 0; }
                body {
                    background-color: #08080a;
                    color: #ffffff;
                    font-family: 'Helvetica Neue', sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    overflow: hidden;
                }
                .background-glow {
                    position: absolute;
                    width: 300px;
                    height: 300px;
                    background: radial-gradient(circle, rgba(0,255,102,0.15) 0%, rgba(0,0,0,0) 70%);
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    z-index: 1;
                }
                .profile-card {
                    background: rgba(15, 15, 20, 0.6);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-radius: 20px;
                    padding: 40px 30px;
                    width: 90%;
                    max-width: 400px;
                    text-align: center;
                    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
                    z-index: 2;
                }
                .username {
                    font-size: 1.8rem;
                    font-weight: 700;
                    letter-spacing: -0.5px;
                    margin-bottom: 8px;
                    text-shadow: 0 0 15px rgba(255,255,255,0.3);
                }
                .bio {
                    font-size: 0.95rem;
                    color: #a0a0ab;
                    margin-bottom: 25px;
                    line-height: 1.5;
                }
                .highlight {
                    color: #00ff66;
                    font-weight: bold;
                    text-shadow: 0 0 10px rgba(0,255,102,0.4);
                }
                .links-container {
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                }
                .link-btn {
                    background: rgba(255, 255, 255, 0.03);
                    border: 1px solid rgba(255, 255, 255, 0.08);
                    color: #e4e4e7;
                    padding: 14px;
                    border-radius: 12px;
                    text-decoration: none;
                    font-size: 0.95rem;
                    font-weight: 500;
                    transition: all 0.25s ease;
                }
                .link-btn:hover {
                    background: rgba(0, 255, 102, 0.1);
                    border-color: #00ff66;
                    color: #00ff66;
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(0, 255, 102, 0.1);
                }
            </style>
        </head>
        <body>
            <div class="background-glow"></div>
            <div class="profile-card">
                <div class="username">mingyeol_prime</div>
                <div class="bio">
                    <span class="highlight">Python Developer</span> (8 yrs exp) 🐍<br>
                    Co-founder of Jangan Song-family
                </div>
                <div class="links-container">
                    <a href="https://github.com" target="_blank" class="link-btn">💻 GitHub 포트폴리오</a>
                    <a href="https://guns.lol" target="_blank" class="link-btn">🔫 오리지널 Guns.lol</a>
                </div>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode('utf-8'))
        return
