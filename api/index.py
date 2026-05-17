import re
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

# 최신 Vercel 제로 세팅 인스턴스
app = FastAPI(title="Guns Clone New Engine")

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
    if not url: return ""
    v_match = re.search(r'(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([\w-]{11})', url)
    return f"https://youtube.com{v_match.group(1)}?autoplay=1&mute=0&loop=1&playlist={v_match.group(1)}&controls=0" if v_match else ""

REGISTER_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"><title>Dev-Hub 플랫폼</title>
    <style>
        body { background-color: #08080a; color: #fff; font-family: monospace; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .box { background: #121216; padding: 40px; border-radius: 15px; width: 100%; max-width: 450px; border: 1px solid #222; text-align: center; }
        h1 { color: #00ff66; }
        input { width: 100%; padding: 12px; margin-bottom: 12px; background: #1c1c24; border: 1px solid #333; border-radius: 8px; color: #fff; box-sizing: border-box; }
        button { width: 100%; padding: 14px; background: #00ff66; color: #000; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Dev-Hub.kr</h1>
        <form action="/api/create" method="post">
            <input type="text" name="username" placeholder="유저네임 (영문)" required>
            <input type="text" name="bio" placeholder="한줄 소개" required>
            <input type="text" name="neon_color" value="#00ff66">
            <input type="text" name="discord_tag" placeholder="디스코드 태그">
            <input type="text" name="discord_status" placeholder="상태메시지">
            <input type="text" name="discord_badges" placeholder="뱃지 이모지 (쉼표 분리)">
            <input type="text" name="banner_url" placeholder="배경 배너 URL">
            <input type="text" name="youtube_url" placeholder="BGM 유튜브 링크">
            <input type="text" name="link_title" placeholder="버튼 이름">
            <input type="text" name="link_url" placeholder="버튼 URL">
            <button type="submit">프로필 생성</button>
        </form>
    </div>
</body>
</html>
"""

PROFILE_HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"><title>__USERNAME__ | Dev-Hub</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background-color: #060608; color: #ffffff; font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .profile-card { background: rgba(10, 10, 14, 0.75); border: 1px solid rgba(255,255,255,0.06); border-radius: 24px; width: 90%; max-width: 430px; text-align: center; overflow: hidden; padding-bottom: 25px; }
        .profile-banner { width: 100%; height: 120px; background-image: url('__BANNER_URL__'); background-size: cover; background-position: center; }
        .badge-container { display: flex; justify-content: center; gap: 6px; margin: 20px 0 10px 0; }
        .badge-item { background: rgba(255,255,255,0.05); padding: 4px 8px; border-radius: 6px; font-size: 0.9rem; }
        .username { font-size: 2rem; font-weight: 800; margin-bottom: 4px; text-shadow: 0 0 20px __NEON_COLOR__; }
        .discord-info { font-size: 0.85rem; color: #71717a; margin-bottom: 18px; }
        .bio { font-size: 0.95rem; color: #d4d4d8; margin-bottom: 28px; }
        .links-container { display: flex; flex-direction: column; gap: 12px; padding: 0 25px; }
        .link-btn { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); color: #f4f4f5; padding: 15px; border-radius: 14px; text-decoration: none; }
        .link-btn:hover { border-color: __NEON_COLOR__; color: __NEON_COLOR__; }
        .iframe-hidden { position: absolute; width: 1px; height: 1px; opacity: 0; }
    </style>
</head>
<body>
    <div class="profile-card">
        <div class="profile-banner"></div>
        <div class="badge-container">__BADGES_HTML__</div>
        <div class="username">__USERNAME__</div>
        <div class="discord-info">__DISCORD_TAG__ __DISCORD_STATUS__</div>
        <div class="bio">__BIO__</div>
        <div class="links-container">__LINKS_HTML__</div>
    </div>
    __YOUTUBE_IFRAME__
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home_page(): return REGISTER_HTML

@app.post("/api/create")
async def create_profile(
    username: str = Form(...), bio: str = Form(...), neon_color: str = Form("#00ff66"),
    discord_tag: str = Form(""), discord_status: str = Form(""), discord_badges: str = Form(""),
    banner_url: str = Form(""), youtube_url: str = Form(""), link_title: str = Form(None), link_url: str = Form(None)
):
    cleaned_username = username.strip().lower()
    badge_list = [b.strip() for b in discord_badges.split(",") if b.strip()] if discord_badges else []
    final_banner = banner_url.strip() if banner_url.strip() else "https://unsplash.com"
    user_links = [{"title": link_title, "url": link_url}] if link_title and link_url else []
    
    USER_DB[cleaned_username] = {
        "username": username, "bio": bio, "neon_color": neon_color, "discord_tag": discord_tag,
        "discord_status": f"({discord_status})" if discord_status else "", "banner_url": final_banner,
        "badges": badge_list, "youtube_url": youtube_url, "links": user_links
    }
    return RedirectResponse(url=f"/{cleaned_username}", status_code=303)

@app.get("/{username}", response_class=HTMLResponse)
async def get_user_profile(username: str):
    target_user = username.lower()
    if target_user in ["api", "favicon.ico"]: return HTMLResponse(status_code=404)
    user_data = USER_DB.get(target_user)
    if not user_data: return RedirectResponse(url="/")
    
    b_html = "".join([f'<span class="badge-item">{b}</span>' for b in user_data["badges"]])
    l_html = "".join([f'<a href="{l["url"]}" target="_blank" class="link-btn">🔗 {l["title"]}</a>' for l in user_data["links"]])
    embed_url = convert_youtube_to_embed(user_data["youtube_url"])
    yt_iframe = f'<iframe class="iframe-hidden" src="{embed_url}" allow="autoplay"></iframe>' if embed_url else ""
    
    rendered = PROFILE_HTML_TEMPLATE.replace("__USERNAME__", user_data["username"]).replace("__BIO__", user_data["bio"]).replace("__NEON_COLOR__", user_data["neon_color"]).replace("__BANNER_URL__", user_data["banner_url"]).replace("__DISCORD_TAG__", user_data["discord_tag"]).replace("__DISCORD_STATUS__", user_data["discord_status"]).replace("__BADGES_HTML__", b_html).replace("__LINKS_HTML__", l_html).replace("__YOUTUBE_IFRAME__", yt_iframe)
    return HTMLResponse(content=rendered)
