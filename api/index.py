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
            <title>Mingyeol_Prime</title>
            <style>
                * { box-sizing: border-box; margin: 0; padding: 0; }
                
                body {
                    background-color: #0a0a0c;
                    color: #ffffff;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    position: relative;
                    overflow: hidden;
                }

                /* 🌧️ 화면 전체에 실시간으로 비가 내리는 레이어 효과 */
                .rain-container {
                    position: absolute;
                    top: 0; left: 0; width: 100%; height: 100%;
                    z-index: 2;
                    pointer-events: none;
                }

                .drop {
                    position: absolute;
                    background: linear-gradient(transparent, rgba(255, 255, 255, 0.4));
                    width: 1px;
                    height: 85px;
                    animation: fall linear infinite;
                }

                @keyframes fall {
                    0% { transform: translateY(-100px); }
                    100% { transform: translateY(100vh); }
                }

                /* 진입용 [ Click Here! ] 락 스크린 */
                .enter-overlay {
                    position: fixed;
                    top: 0; left: 0; width: 100%; height: 100%;
                    background: #050507;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    z-index: 9999;
                    cursor: pointer;
                    transition: opacity 0.5s ease, visibility 0.5s ease;
                }

                .enter-btn {
                    font-size: 1.8rem;
                    font-weight: 700;
                    color: #ff3344;
                    letter-spacing: 2px;
                    text-transform: uppercase;
                    text-shadow: 0 0 15px rgba(255, 51, 68, 0.6);
                    animation: pulse 1.2s infinite alternate;
                }

                @keyframes pulse {
                    0% { transform: scale(0.96); opacity: 0.5; }
                    100% { transform: scale(1.04); opacity: 1; }
                }

                .enter-overlay.fade-out {
                    opacity: 0;
                    visibility: hidden;
                }

                /* 중앙 캐릭터 카드 프로필 레이아웃 크기 조정 */
                .profile-card {
                    text-align: center;
                    z-index: 5;
                    width: 90%;
                    max-width: 340px;
                    padding: 20px;
                }

                /* 형이 보내준 가시관 백발 캐릭터 이미지 최적화 맵핑 */
                .avatar-img {
                    width: 155px;
                    height: 155px;
                    border-radius: 50%;
                    object-fit: cover;
                    border: 2px solid rgba(255, 255, 255, 0.05);
                    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
                    margin: 0 auto 22px auto;
                    display: block;
                }

                /* 이름 스타일링 지정 */
                .username {
                    font-size: 2.2rem;
                    font-weight: 600;
                    color: #ffffff;
                    margin-bottom: 6px;
                    letter-spacing: -0.5px;
                }

                /* Designer 서브타이틀 영어 일치화 */
                .subtitle {
                    font-size: 1.1rem;
                    color: rgba(255, 255, 255, 0.7);
                    font-weight: 400;
                }
            </style>
        </head>
        <body>

            <!-- 브라우저 보안 오디오 락 패스 오버레이 -->
            <div class="enter-overlay" id="overlay" onclick="startSite()">
                <div class="enter-btn">[ Click Here! ]</div>
            </div>

            <!-- 비 내리는 애니메이션 컨테이너 스크립트 대응 영역 -->
            <div class="rain-container" id="rain"></div>

            <!-- 중앙 단독 프로필 카드 구조 메인 바인딩 -->
            <div class="profile-card">
                <img class="avatar-img" src="https://pinimg.com" alt="Mingyeol_Prime">
                <div class="username">Mingyeol_Prime</div>
                <div class="subtitle">Designer</div>
            </div>

            <!-- 🎧 DAY6 - 한 페이지가 될 수 있게 오피셜 무손실 다이렉트 오디오 엔진 스트리밍 주소 연동 -->
            <audio id="bgm" loop preload="auto">
                <source src="https://archive.org" type="audio/mpeg">
            </audio>

            <script>
                // 🌧️ 파이썬 짬바 스타일의 실시간 동적 비 내리는 알고리즘 스크립트 생성
                const rainContainer = document.getElementById('rain');
                const dropCount = 45; // 화면에 동시에 내릴 빗방울 개수 조절

                for (let i = 0; i < dropCount; i++) {
                    const drop = document.createElement('div');
                    drop.classList.add('drop');
                    drop.style.left = Math.random() * 100 + '%';
                    drop.style.top = Math.random() * -50 + 'px';
                    drop.style.animationDuration = (Math.random() * 0.5 + 0.6) + 's'; // 떨어지는 속도 무작위 처리
                    drop.style.animationDelay = Math.random() * 2 + 's';
                    drop.style.opacity = Math.random() * 0.4 + 0.1;
                    rainContainer.appendChild(drop);
                }

                function startSite() {
                    const overlay = document.getElementById('overlay');
                    const audio = document.getElementById('bgm');
                    
                    overlay.classList.add('fade-out');
                    
                    // 사운드 볼륨 밸런싱 및 구동 트리거
                    audio.volume = 0.65;
                    audio.play().catch(function(e) {
                        console.log("사운드 엔진 리로드 재구동");
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
