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
                    /* 형이 준 배경 이미지를 기본 베이스로 설정 */
                    background: url('https://unsplash.com') no-repeat center center fixed;
                    background-size: cover;
                    color: #ffffff;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    position: relative;
                    overflow: hidden;
                }

                /* guns.lol 특유의 전체 배경 블러(흐림) 및 어두운 오버레이 필터 효과 */
                body::before {
                    content: '';
                    position: absolute;
                    top: 0; left: 0; width: 100%; height: 100%;
                    background: rgba(0, 0, 0, 0.2);
                    backdrop-filter: blur(25px);
                    -webkit-backdrop-filter: blur(25px);
                    z-index: 1;
                }

                /* 진입용 [ Click Here ] 팝업 (브금 재생 필수 장치) */
                .enter-overlay {
                    position: fixed;
                    top: 0; left: 0; width: 100%; height: 100%;
                    background: rgba(10, 10, 12, 0.98);
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
                    text-shadow: 0 0 15px rgba(255, 51, 68, 0.6);
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

                /* 🚨 캡처 화면과 똑같은 둥근 라운드 반투명 프로필 카드 🚨 */
                .profile-card {
                    background: rgba(255, 255, 255, 0.07);
                    border: 1px solid rgba(255, 255, 255, 0.05);
                    border-radius: 24px;
                    width: 90%;
                    max-width: 350px;
                    padding: 35px 25px;
                    text-align: center;
                    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
                    z-index: 2;
                    position: relative;
                }

                /* 캡처본 속 가시관 백발 캐릭터 이미지 크기와 일치화 */
                .avatar-img {
                    width: 110px;
                    height: 110px;
                    border-radius: 50%;
                    object-fit: cover;
                    background: #111;
                    margin: 0 auto 18px auto;
                    display: block;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
                }

                /* guns.lol 유저네임 폰트 스타일 */
                .username {
                    font-size: 2.1rem;
                    font-weight: 600;
                    color: #ffffff;
                    margin-bottom: 6px;
                    letter-spacing: -0.5px;
                }

                /* Designer 서브타이틀 텍스트 */
                .subtitle {
                    font-size: 1.05rem;
                    color: rgba(255, 255, 255, 0.85);
                    margin-bottom: 20px;
                    font-weight: 400;
                }

                /* 👁️ 조회수 아이콘 레이아웃 생성 */
                .views-container {
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                    gap: 6px;
                    color: rgba(255, 255, 255, 0.8);
                    font-size: 0.85rem;
                    padding-left: 5px;
                    margin-top: 15px;
                }

                .views-icon {
                    width: 16px;
                    height: 16px;
                    fill: currentColor;
                }

                /* 소셜 이동 링크 히든 컴포넌트 처리 */
                .social-box {
                    display: flex;
                    justify-content: center;
                    gap: 15px;
                    margin-top: 10px;
                }

                .social-link {
                    color: rgba(255,255,255,0.6);
                    text-decoration: none;
                    font-size: 0.85rem;
                    transition: color 0.2s;
                }
                .social-link:hover {
                    color: #ff3344;
                }
            </style>
        </head>
        <body>

            <!-- 입장 브릿지 오버레이 장치 -->
            <div class="enter-overlay" id="overlay" onclick="startSite()">
                <div class="enter-btn">[ Click Here ]</div>
            </div>

            <!-- 오리지널 클론 카드 -->
            <div class="profile-card">
                <!-- 형이 세팅하고 싶어 한 백발 가시관 캐릭터 애니메이션 인장 링크 연동 -->
                <img class="avatar-img" src="https://pinimg.com" alt="profile">
                
                <div class="username">mingyeol_prime</div>
                <div class="subtitle">Designer</div>
                
                <div class="social-box">
                    <a href="https://tiktok.com" target="_blank" class="social-link">TikTok</a>
                    <a href="https://discord.gg" target="_blank" class="social-link">Discord(y.eun)</a>
                </div>

                <!-- 👁️ 캡처본에 있던 조회수 마크 구현 -->
                <div class="views-container">
                    <svg class="views-icon" viewBox="0 0 24 24">
                        <path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/>
                    </svg>
                    <span>5</span>
                </div>

                <!-- DAY6 - 한 페이지가 될 수 있게 인라인 오디오 백엔드 스트리밍 엔진 -->
                <audio id="bgm" loop preload="auto">
                    <source src="https://archive.org" type="audio/mpeg">
                </audio>
            </div>

            <script>
                function startSite() {
                    var overlay = document.getElementById('overlay');
                    var audio = document.getElementById('bgm');
                    
                    overlay.classList.add('fade-out');
                    
                    // 사운드 액티베이션 우회 구동
                    audio.volume = 0.7;
                    audio.play().catch(function(e) {
                        console.log("스트리밍 재연동 시도");
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
