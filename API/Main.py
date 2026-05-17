import re
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

# Vercel 서버리스 호환용 아키텍처 인스턴스 생성
app = FastAPI(title="Guns Clone Core Engine")

# 인메모리 가상 데이터베이스 구조 고도화
USER_DB = {
    "mingyeol_prime": {
        "username": "mingyeol_prime",
        "bio": "Python Developer (8 yrs exp) 🐍 | Co-founder of Jangan Song-family",
        "neon_color": "#00ff66",
        "discord_tag": "mingyeol_prime#0000",
        "discord_status": "Coding...",
        "banner_url": "https://unsplash.com",
        "badges": ["👑", "💻", "🐍"],
        "youtube_url": "https://youtube.com",
        "links": [{"title": "💻 GitHub", "url": "https://github.com"}]
    }
}

def convert_youtube_to_embed(url: str) -> str:
    """일반 유튜브 링크를 백그라운드 자동재생 전용 임베드 URL로 변환하는 정규식 엔지니어링"""
    if not url:
        return ""
    video_id_match = re.search(r'(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([\w-]{11})', url)
    if video_id_match:
        video_id = video_id_match.group(1)
        return f"https://youtube.com{video_id}?autoplay=1&mute=0&loop=1&playlist={video_id}&controls=0&showinfo=0&rel=0"
    return ""

# --- 1. 메인 가입 창설 폼 마크업 ---
REGISTER_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Dev-Hub 플랫폼 창설</title>
    <style>
        body { background-color: #08080a; color: #fff; font-family: monospace; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px 0; }
        .box { background: #121216; padding: 40px; border-radius: 15px; width: 100%; max-width: 450px; border: 1px solid #222; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        h1 { color: #00ff66; margin-bottom: 5px; }
        .desc { color: #888; font-size: 0.9rem; margin-bottom: 25px; }
        .section-title { font-size: 0.85rem; color: #00ff66; text-align: left; margin: 15px 0 5px 2px; text-transform: uppercase; letter-spacing: 1px; }
        input { width: 100%; padding: 12px; margin-bottom: 12px; background: #1c1c24; border: 1px solid #333; border-radius: 8px; color: #fff; box-sizing: border-box; font-family: monospace; }
        input:focus { border-color: #00ff66; outline: none; }
        button { width: 100%; padding: 14px; background: #00ff66; color: #000; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 15px; font-size: 1rem; }
        button:hover { background: #00cc55; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Dev-Hub.kr</h1>
        <p class="desc">오리지널 guns.lol 완벽 복제 프로필 빌더</p>
        <form action="/api/create" method="post">
            <div class="section-title">기본 정보</div>
            <input type="text" name="username" placeholder="유저네임 (영문 도메인 주소용)" required>
            <input type="text" name="bio" placeholder="한줄 소개 (HTML 태그 사용 가능)" required>
            <input type="text" name="neon_color" placeholder="글자 테두리 네온 색상코드 (기본: #00ff66)" value="#00ff66">
            
            <div class="section-title">디스코드 연동 데이터</div>
            <input type="text" name="discord_tag" placeholder="디스코드 닉네임 (예: mingyeol_prime)">
            <input type="text" name="discord_status" placeholder="디스코드 커스텀 상태메시지">
            <input type="text" name="discord_badges" placeholder="보유 뱃지 이모지 분리 (예: 👑,💻,🐍)">
            <input type="text" name="banner_url" placeholder="프로필 상단 배경 배너 이미지 URL">
            
            <div class="section-title">미디어 & 외부 링크</div>
            <input type="text" name="youtube_url" placeholder="배경음악 유튜브 링크 (일반/Shorts 모두 가능)">
            <input type="text" name="link_title" placeholder="첫 번째 버튼 이름 (예: GitHub)">
            <input type="text" name="link_url" placeholder="첫 번째 버튼 연결 URL">
            
            <button type="submit">나만의 프로필 최종 창설</button>
        </form>
    </div>
</body>
</html>
"""

# --- 2. 동적 프로필 랜딩 마크업 (Jinna2 충돌 완전 우회형 패킹) ---
PROFILE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>__USERNAME__ | Dev-Hub</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background-color: #060608; color: #ffffff; font-family: -apple-system, BlinkMacSystemFont, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; overflow-x: hidden; }
        .profile-card { background: rgba(10, 10, 14, 0.75); border: 1px solid rgba(255,255,255,0.06); border-radius: 24px; width: 90%; max-width: 430px; text-align: center; box-shadow: 0 30px 60px rgba(0,0,0,0.8); overflow: hidden; backdrop-filter: blur(20px); position: relative; }
        .profile-banner { width: 100%; height: 120px; background-image: url('__BANNER_URL__'); background-size: cover; background-position: center; border-bottom: 1px solid rgba(255,255,255,0.05); }
        .card-body { padding: 35px 25px 25px 25px; position: relative; }
        .badge-container { display: flex; justify-content: center; gap: 6px; margin-bottom: 12px; }
        .badge-item { background: rgba(255,255,255,0.05); padding: 4px 8px; border-radius: 6px; font-size: 0.9rem; border: 1px solid rgba(255,255,255,0.03); }
        .username { font-size: 2rem; font-weight: 800; margin-bottom: 4px; letter-spacing: -0.5px; text-shadow: 0 0 20px __NEON_COLOR__; }
        .discord-info { font-size: 0.85rem; color: #71717a; margin-bottom: 18px; font-family: monospace; display: flex; justify-content: center; align-items: center; gap: 6px; }
        .status-dot { width: 8px; height: 8px; background-color: #23a55a; border-radius: 50%; display: inline-block; box-shadow: 0 0 8px #23a55a; }
        .bio { font-size: 0.95rem; color: #d4d4d8; margin-bottom: 28px; line-height: 1.6; text-align: center; word-break: break-word; }
        .links-container { display: flex; flex-direction: column; gap: 12px; }
        .link-btn { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); color: #f4f4f5; padding: 15px; border-radius: 14px; text-decoration: none; font-size: 0.95rem; font-weight: 500; transition: all 0.25s ease; display: flex; justify-content: center; align-items: center; }
        .link-btn:hover { border-color: __NEON_COLOR__; color: __NEON_COLOR__; transform: translateY(-3px); background: __NEON_COLOR__05; box-shadow: 0 10px 20px __NEON_COLOR__15; }
        .make-yours { margin-top: 35px; display: inline-block; color: #3f3f46; font-size: 0.8rem; text-decoration: none; letter-spacing: 0.5px; font-family: monospace; }
        .make-yours:hover { color: __NEON_COLOR__; }
        .iframe-hidden { position: absolute; width: 1px; height: 1px; opacity: 0; pointer-events: none; }
    </style>
</head>
<body>
    <div class="profile-card">
        <div class="profile-banner"></div>
        <div class="card-body">
            <div class="badge-container">__BADGES_HTML__</div>
            <div class="username">__USERNAME__</div>
            <div class="discord-info"><span class="status-dot"></span> __DISCORD_TAG__ __DISCORD_STATUS__</div>
            <div class="bio">__BIO__</div>
            <div class="links-container">__LINKS_HTML__</div>
            <a href="/" class="make-yours">CREATE YOUR OWN PAGE ➔</a>
        </div>
    </div>
    __YOUTUBE_IFRAME__
</body>
</html>
"""

# --- 3. 라우팅 로직 처리 엔진 ---

@app.get("/", response_class=HTMLResponse)
async def home_page():
    """메인 회원가입 창설 폼 페이지 리턴"""
    return REGISTER_HTML

@app.post("/api/create")
async def create_profile(
    username: str = Form(...), 
    bio: str = Form(...), 
    neon_color: str = Form("#00ff66"),
    discord_tag: str = Form(""),
    discord_status: str = Form(""),
    discord_badges: str = Form(""),
    banner_url: str = Form(""),
    youtube_url: str = Form(""),
    link_title: str = Form(None),
    link_url: str = Form(None)
):
    cleaned_username = username.strip().lower()
    badge_list = [b.strip() for b in discord_badges.split(",") if b.strip()] if discord_badges else []
    final_banner = banner_url.strip() if banner_url.strip() else "https://unsplash.com"
    
    user_links = []
    if link_title and link_url:
        user_links.append({"title": link_title, "url": link_url})
        
    # 가상 DB 데이터 인젝션
    USER_DB[cleaned_username] = {
        "username": username,
        "bio": bio,
        "neon_color": neon_color,
        "discord_tag": discord_tag,
        "discord_status": f"({discord_status})" if discord_status else "",
        "banner_url": final_banner,
        "badges": badge_list,
        "youtube_url": youtube_url,
        "links": user_links
    }
    return RedirectResponse(url=f"/{cleaned_username}", status_code=303)

@app.get("/{username}", response_class=HTMLResponse)
async def get_user_profile(username: str):
    target_user = username.lower()
    if target_user in ["api", "favicon.ico"]:
        return HTMLResponse(status_code=404)
        
    user_data = USER_DB.get(target_user)
    if not user_data:
        return RedirectResponse(url="/")
        
    # HTML 조각 컴파일 생성
    badges_html = "".join([f'<span class="badge-item">{b}</span>' for b in user_data["badges"]])
    links_html = "".join([f'<a href="{l["url"]}" target="_blank" class="link-btn">🔗 {l["title"]}</a>' for l in user_data["links"]])
    
    embed_music_url = convert_youtube_to_embed(user_data["youtube_url"])
    youtube_iframe = f'<iframe class="iframe-hidden" src="{embed_music_url}" allow="autoplay"></iframe>' if embed_music_url else ""
        
    # 순수 파이썬 고속 대치 렌더링으로 프론트엔드 표출
    rendered = PROFILE_HTML_TEMPLATE
    rendered = rendered.replace("__USERNAME__", user_data["username"])
    rendered = rendered.replace("__BIO__", user_data["bio"])
    rendered = rendered.replace("__NEON_COLOR__", user_data["neon_color"])
    rendered = rendered.replace("__BANNER_URL__", user_data["banner_url"])
    rendered = rendered.replace("__DISCORD_TAG__", user_data["discord_tag"])
    rendered = rendered.replace("__DISCORD_STATUS__", user_data["discord_status"])
    rendered = rendered.replace("__BADGES_HTML__", badges_html)
    rendered = rendered.replace("__LINKS_HTML__", links_html)
    rendered = rendered.replace("__YOUTUBE_IFRAME__", youtube_iframe)
    
    return HTMLResponse(content=rendered)
