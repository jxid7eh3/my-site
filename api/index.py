from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
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
                    background: url('https://pinimg.com') no-repeat center center fixed;
                    background-size: cover;
                    color: #ffffff;
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    position: relative;
                    overflow: hidden;
                }

                body::before {
                    content: '';
                    position: absolute;
                    top: 0; left: 0; width: 100%; height: 100%;
                    background: rgba(0, 0, 0, 0.45);
                    z-index: 1;
                }

                /* 🚨 진입할 때 무조건 뜨는 Click Here 오버레이 화면 🚨 */
                .enter-overlay {
                    position: fixed;
                    top: 0; left: 0; width: 100%; height: 100%;
                    background: rgba(5, 5, 8, 0.95);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    z-index: 999;
                    cursor: pointer;
                    transition: opacity 0.5s ease, visibility 0.5s ease;
                }

                .enter-btn {
                    font-size: 1.8rem;
                    font-weight: 700;
                    color: #ff3344; /* 붉은 달과 어울리는 다크 네온 레드 */
                    letter-spacing: 2px;
                    text-transform: uppercase;
                    text-shadow: 0 0 15px rgba(255, 51, 68, 0.7);
                    animation: pulse 1.5s infinite alternate;
                }

                @keyframes pulse {
                    0% { transform: scale(0.98); opacity: 0.6; }
                    100% { transform: scale(1.04); opacity: 1; }
                }

                /* 팝업 닫혔을 때 쓰는 클래스 */
                .enter-overlay.fade-out {
                    opacity: 0;
                    visibility: hidden;
                }

                /* 프로필 카드 디자인 */
                .profile-card {
                    background: rgba(20, 20, 28, 0.75);
                    backdrop-filter: blur(16px);
                    -webkit-backdrop-filter: blur(16px);
                    border: 1px solid rgba(255, 255, 255, 0.08);
                    border-radius: 16px;
                    width: 90%;
                    max-width: 380px;
                    overflow: hidden;
                    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.7);
                    z-index: 2;
                    position: relative;
                }

                .discord-banner {
                    width: 100%;
                    height: 105px;
                    background: linear-gradient(135deg, #7289da, #1a1a24);
                    position: relative;
                }

                .avatar-container {
                    position: absolute;
                    top: 60px;
                    left: 22px;
                    width: 86px;
                    height: 86px;
                    border-radius: 50%;
                    background: #14141c;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                .avatar-circle {
                    width: 76px;
                    height: 76px;
                    border-radius: 50%;
                    background: radial-gradient(circle, #00ff66 0%, #111 100%);
                    box-shadow: 0 0 15px rgba(0, 255, 102, 0.4);
                }

                .card-body {
                    padding: 55px 22px 25px 22px;
                }

                .username {
                    font-size: 1.6rem;
                    font-weight: 700;
                    color: #ffffff;
                    margin-bottom: 4px;
                }

                .tag {
                    font-size: 0.9rem;
                    color: #b5bac1;
                    margin-bottom: 15px;
                }

                .divider {
                    height: 1px;
                    background: rgba(255, 255, 255, 0.08);
                    margin: 15px 0;
                }

                .bio-section h3 {
                    font-size: 0.75rem;
                    text-transform: uppercase;
                    color: #b5bac1;
                    letter-spacing: 0.5px;
                    margin-bottom: 8px;
                }

                .bio-text {
                    font-size: 0.95rem;
                    color: #dbdee1;
                    line-height: 1.5;
                }

                .highlight {
                    color: #00ff66;
                    font-weight: 600;
                }

                .links-container {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    margin-top: 20px;
                }

                .link-btn {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                    background: rgba(255, 255, 255, 0.04);
                    border: 1px solid rgba(255, 255, 255, 0.08);
                    color: #f2f3f5;
                    padding: 12px;
                    border-radius: 8px;
                    text-decoration: none;
                    font-size: 0.95rem;
                    font-weight: 500;
                    transition: all 0.2s ease;
                }

                .link-btn:hover {
                    background: rgba(0, 255, 102, 0.12);
                    border-color: #00ff66;
                    color: #00ff66;
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(0, 255, 102, 0.15);
                }

                .music-status {
                    text-align: center;
                    font-size: 0.75rem;
                    color: #949ba4;
                    margin-top: 20px;
                    letter-spacing: 0.3px;
                }
            </style>
        </head>
        <body>

            <!-- 🚨 첫 진입 클릭 오버레이 장치 -->
            <div class="enter-overlay" id="overlay" onclick="startSite()">
                <div class="enter-btn">[ Click Here ]</div>
            </div>

            <div class="profile-card">
                <div class="discord-banner">
                    <div class="avatar-container">
                        <div class="avatar-circle"></div>
                    </div>
                </div>
                
                <div class="card-body">
                    <div class="username">mingyeol_prime</div>
                    <div class="tag">@mingyeol_prime</div>
                    
                    <div class="divider"></div>

                    <div class="bio-section">
                        <h3>소개글</h3>
                        <div class="bio-text">
                            <span class="highlight">Python Developer</span> (8 yrs exp) 🐍<br>
                            Co-founder of Jangan Song-family
                        </div>
                    </div>

                    <div class="divider"></div>

                    <div class="bio-section">
                        <h3>소셜 링크</h3>
                        <div class="links-container">
                            <a href="https://tiktok.com" target="_blank" class="link-btn">🎵 TikTok 바로가기</a>
                            <a href="https://discord.gg" target="_blank" class="link-btn">💬 Discord 친구추가</a>
                        </div>
                    </div>

                    <div class="music-status">
                        🎧 BGM: DAY6 - 한 페이지가 될 수 있게
                    </div>
                    
                    <!-- 오디오 소스 태그 -->
                    <audio id="bgm" loop>
                        <source src="https://r2.dev" type="audio/mpeg">
                    </audio>
                </div>
            </div>

            <!-- 자바스크립트로 음악 재생 강제 트리거 조절 -->
            <script>
                function startSite() {
                    var overlay = document.getElementById('overlay');
                    var audio = document.getElementById('bgm');
                    
                    // 팝업 제거
                    overlay.classList.add('fade-out');
                    
                    // 배경음악 강제 재생 (보안 뚫기 성공)
                    audio.play().catch(function(error) {
                        console.log("Audio play failed:", error);
                    });
                }
            </script>

        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode('utf-8'))
        return
