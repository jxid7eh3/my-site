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
                    /* 형이 보내준 붉은 달 고화질 이미지 CDN 원본으로 긴급 교체 */
                    background: url('https://unsplash.com') no-repeat center center fixed;
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
                    /* 배경 무드가 살도록 투명도 조절 */
                    background: rgba(0, 0, 0, 0.5);
                    z-index: 1;
                }

                /* 첫 진입 Click Here 팝업 */
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
                    color: #ff3344;
                    letter-spacing: 2px;
                    text-transform: uppercase;
                    text-shadow: 0 0 15px rgba(255, 51, 68, 0.7);
                    animation: pulse 1.5s infinite alternate;
                }

                @keyframes pulse {
                    0% { transform: scale(0.98); opacity: 0.6; }
                    100% { transform: scale(1.04); opacity: 1; }
                }

                .enter-overlay.fade-out {
                    opacity: 0;
                    visibility: hidden;
                }

                /* 프로필 카드 디자인 */
                .profile-card {
                    background: rgba(20, 20, 28, 0.85);
                    backdrop-filter: blur(20px);
                    -webkit-backdrop-filter: blur(20px);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 16px;
                    width: 90%;
                    max-width: 380px;
                    overflow: hidden;
                    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.8);
                    z-index: 2;
                    position: relative;
                }

                /* 🚨 디스코드 배너 영역을 y.eun 테마 붉은 달 미니 버전으로 매칭 */
                .discord-banner {
                    width: 100%;
                    height: 115px;
                    background: url('https://unsplash.com') no-repeat center center;
                    background-size: cover;
                    position: relative;
                }

                /* 프로필 아바타를 y.eun 네온 레드/그린 크로스 엠블럼으로 세팅 */
                .avatar-container {
                    position: absolute;
                    top: 65px;
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
                    background: radial-gradient(circle, #ff3344 0%, #111 100%);
                    box-shadow: 0 0 15px rgba(255, 51, 68, 0.5);
                }

                .card-body {
                    padding: 45px 22px 25px 22px;
                }

                .username {
                    font-size: 1.6rem;
                    font-weight: 700;
                    color: #ffffff;
                    margin-bottom: 2px;
                }

                .tag {
                    font-size: 0.9rem;
                    color: #ff5566;
                    font-weight: bold;
                    margin-bottom: 12px;
                    text-shadow: 0 0 8px rgba(255, 85, 102, 0.3);
                }

                .discord-nick-box {
                    font-size: 0.85rem;
                    background: rgba(255, 51, 68, 0.1);
                    border: 1px solid rgba(255, 51, 68, 0.25);
                    padding: 6px 12px;
                    border-radius: 6px;
                    color: #ff6677;
                    font-weight: bold;
                    display: inline-block;
                    margin-bottom: 5px;
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
                    background: rgba(255, 51, 68, 0.15);
                    border-color: #ff3344;
                    color: #ff3344;
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(255, 51, 68, 0.2);
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

            <!-- 입장 제어 패널 (BGM 브라우저 보안 우회용) -->
            <div class="enter-overlay" id="overlay" onclick="startSite()">
                <div class="enter-btn">[ Click Here ]</div>
            </div>

            <div class="profile-card">
                <!-- 붉은 달 연동 배너 -->
                <div class="discord-banner">
                    <div class="avatar-container">
                        <div class="avatar-circle"></div>
                    </div>
                </div>
                
                <div class="card-body">
                    <!-- 유저 정보 영역 y.eun 풀 세팅 -->
                    <div class="username">y.eun</div>
                    <div class="tag">@y.eun</div>
                    
                    <div class="discord-nick-box">🎯 Main Profile: y.eun</div>
                    
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
                    
                    <!-- 🚨 전 세계 공용 인터넷 아카이브 서버 우회용 순수 고정 오디오 스트리밍 주소 탑재 -->
                    <audio id="bgm" loop preload="auto">
                        <source src="https://archive.org" type="audio/mpeg">
                    </audio>
                </div>
            </div>

            <script>
                function startSite() {
                    var overlay = document.getElementById('overlay');
                    var audio = document.getElementById('bgm');
                    
                    overlay.classList.add('fade-out');
                    
                    // 강제 재생 메커니즘 가동
                    audio.volume = 0.7;
                    audio.play().then(function() {
                        console.log("DAY6 브금 스트리밍 성공");
                    }).catch(function(error) {
                        console.log("인증 실패 우회 재시도");
                        audio.load();
                        audio.play();
                    });
                }
            </script>

        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode('utf-8'))
        return
