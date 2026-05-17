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
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
            <title>Dev-hub.kr | MINGYEOL_PRIME</title>
            <style>
                * { box-sizing: border-box; margin: 0; padding: 0; }
                
                body {
                    /* 형이 보내준 붉은 달 실루엣 사진으로 배경 지정 */
                    background: url('https://pinimg.com') no-repeat center center fixed;
                    background-size: cover;
                    color: #ffffff;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
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
                    background: rgba(0, 0, 0, 0.5);
                    z-index: 1;
                }

                /* [ Click Here ] 가림막 팝업 */
                .enter-overlay {
                    position: fixed;
                    top: 0; left: 0; width: 100%; height: 100%;
                    background: rgba(5, 5, 8, 0.98);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    z-index: 999;
                    cursor: pointer;
                    transition: opacity 0.4s ease, visibility 0.4s ease;
                }

                .enter-btn {
                    font-size: 1.6rem;
                    font-weight: 700;
                    color: #ff3344;
                    letter-spacing: 2px;
                    text-transform: uppercase;
                    text-shadow: 0 0 15px rgba(255, 51, 68, 0.8);
                    animation: pulse 1.2s infinite alternate;
                }

                @keyframes pulse {
                    0% { transform: scale(0.97); opacity: 0.5; }
                    100% { transform: scale(1.03); opacity: 1; }
                }

                .enter-overlay.fade-out {
                    opacity: 0;
                    visibility: hidden;
                }

                /* 디스코드 프로필 카드 디자인 */
                .profile-card {
                    background: rgba(15, 15, 22, 0.8);
                    backdrop-filter: blur(20px);
                    -webkit-backdrop-filter: blur(20px);
                    border: 1px solid rgba(255, 255, 255, 0.08);
                    border-radius: 16px;
                    width: 92%;
                    max-width: 360px;
                    overflow: hidden;
                    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.85);
                    z-index: 2;
                    position: relative;
                }

                .discord-banner {
                    width: 100%;
                    height: 105px;
                    background: linear-gradient(135deg, #ff3344, #151516);
                    position: relative;
                }

                /* 프로필 사진 컨테이너 */
                .avatar-container {
                    position: absolute;
                    top: 55px;
                    left: 20px;
                    width: 90px;
                    height: 90px;
                    border-radius: 50%;
                    background: #0f0f14;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                /* 엑스박스 완벽 해결: 아바타 이미지도 붉은 달 원본으로 일치 유도 */
                .avatar-img {
                    width: 78px;
                    height: 78px;
                    border-radius: 50%;
                    background: url('https://pinimg.com') no-repeat center center;
                    background-size: cover;
                    border: 2px solid #ff3344;
                    box-shadow: 0 0 15px rgba(255, 51, 68, 0.6);
                }

                .card-body {
                    padding: 55px 20px 25px 20px;
                }

                .username {
                    font-size: 1.5rem;
                    font-weight: 700;
                    color: #ffffff;
                    margin-bottom: 2px;
                }

                .tag {
                    font-size: 0.85rem;
                    color: #b5bac1;
                    margin-bottom: 12px;
                }

                .discord-nick-box {
                    font-size: 0.8rem;
                    background: rgba(255, 51, 68, 0.12);
                    border: 1px solid rgba(255, 51, 68, 0.25);
                    padding: 6px 12px;
                    border-radius: 6px;
                    color: #ff5566;
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
                    font-size: 0.7rem;
                    text-transform: uppercase;
                    color: #949ba4;
                    letter-spacing: 0.5px;
                    margin-bottom: 6px;
                }

                .bio-text {
                    font-size: 0.9rem;
                    color: #dbdee1;
                    line-height: 1.5;
                }

                .highlight {
                    color: #ff3344;
                    font-weight: 600;
                    text-shadow: 0 0 10px rgba(255, 51, 68, 0.3);
                }

                .links-container {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    margin-top: 15px;
                }

                .link-btn {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: rgba(255, 255, 255, 0.03);
                    border: 1px solid rgba(255, 255, 255, 0.06);
                    color: #f2f3f5;
                    padding: 12px;
                    border-radius: 8px;
                    text-decoration: none;
                    font-size: 0.9rem;
                    font-weight: 500;
                    transition: all 0.2s ease;
                }

                .link-btn:hover {
                    background: rgba(255, 51, 68, 0.08);
                    border-color: #ff3344;
                    color: #ff3344;
                    transform: translateY(-1px);
                    box-shadow: 0 5px 15px rgba(255, 51, 68, 0.1);
                }

                .music-status {
                    text-align: center;
                    font-size: 0.75rem;
                    color: #949ba4;
                    margin-top: 20px;
                }

                /* 백엔드 브금 재생 전용 유튜브 가상 프레임 (화면에 안 보임) */
                #youtube-player {
                    position: absolute;
                    width: 1px; height: 1px;
                    opacity: 0; top: -10px; left: -10px;
                }
            </style>
        </head>
        <body>

            <!-- [ Click Here ] 오버레이 가림막 -->
            <div class="enter-overlay" id="overlay" onclick="startSite()">
                <div class="enter-btn">[ Click Here ]</div>
            </div>

            <!-- 🚨 우회 차단 성공용 유튜브 임베드 플레이어 엔진 (DAY6 - 한 페이지가 될 수 있게 자동 재생 제어) -->
            <div id="youtube-player"></div>

            <div class="profile-card">
                <div class="discord-banner">
                    <div class="avatar-container">
                        <!-- 엑스박스 완벽 제거: CSS 전용 프로필 이미지 탑재 -->
                        <div class="avatar-img"></div>
                    </div>
                </div>
                
                <div class="card-body">
                    <div class="username">mingyeol_prime</div>
                    <div class="tag">@mingyeol_prime</div>
                    
                    <div class="discord-nick-box">🆔 Discord ID: y.eun</div>
                    
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
                </div>
            </div>

            <script>
                // 유튜브 공식 API 비동기 로드 실행
                var tag = document.createElement('script');
                tag.src = "https://youtube.com";
                var firstScriptTag = document.getElementsByTagName('script')[0];
                firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

                var player;
                function onYouTubeIframeAPIReady() {
                    // DAY6 - 한 페이지가 될 수 있게 음원 공식 ID 연동 매핑
                    player = new YT.Player('youtube-player', {
                        height: '1',
                        width: '1',
                        videoId: 'd7M97b4fWpA',
                        playerVars: {
                            'autoplay': 0,
                            'controls': 0,
                            'loop': 1,
                            'playlist': 'd7M97b4fWpA'
                        }
                    });
                }

                function startSite() {
                    var overlay = document.getElementById('overlay');
                    overlay.classList.add('fade-out');
                    
                    // 유저 클릭 허가 확인 후 유튜브 스트리밍 오디오 강제 플레이 가동
                    if (player && typeof player.playVideo === 'function') {
                        player.setVolume(60);
                        player.playVideo();
                    }
                }
            </script>

        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode('utf-8'))
        return
