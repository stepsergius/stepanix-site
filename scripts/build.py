#!/usr/bin/env python3
"""Builds stepanix.com (English at the root, Ukrainian in uk/) from one template.

    python3 scripts/build.py

To add an app: put its icon (384 px PNG) and a dark screenshot per language (WebP) in assets/,
add an entry to APPS below, run the script and push.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "https://stepanix.com"
EMAIL = "stepsergius@gmail.com"

# Each app: its site, colours for its glow, screenshot size per language, and texts.
APPS = [
    dict(id="klavko", name="Klavko", url="https://klavko.stepanix.com/", glow="#3d7bff", warm="#ffc23d",
         shot={"en": (1185, 402), "uk": (1185, 402)},
         en=dict(kind="Typing assistant", line="Just type. Klavko fixes the rest.",
                 text="Typed a word in the wrong layout? Klavko switches it as you type. It also fixes typos, types what you say, translates and reads text from the screen.",
                 points=["Fixes the wrong keyboard layout on the fly", "Typos and tidy text", "Voice input and translation", "Text from the screen, clipboard history"],
                 meta="Free · Pro $9.99 once · Mac, Windows in beta", alt="Klavko's layout settings"),
         uk=dict(kind="Помічник для набору", line="Просто друкуйте. Решту виправить Klavko.",
                 text="Набрали слово не тією розкладкою? Klavko перемкне її просто під час набору. А ще виправить помилки, запише сказане, перекладе й прочитає текст з екрана.",
                 points=["Виправляє неправильну розкладку на льоту", "Помилки й охайний текст", "Голосовий ввід і переклад", "Текст з екрана, історія буфера"],
                 meta="Безкоштовно · Pro $9.99 один раз · Mac, Windows у беті", alt="Налаштування розкладки в Klavko")),
    dict(id="tapko", name="Tapko", url="https://tapko.stepanix.com/", glow="#7a5cff", warm="#ff9a3d",
         shot={"en": (1410, 660), "uk": (1410, 698)},
         en=dict(kind="Trackpad gestures", line="Your trackpad can do more.",
                 text="Tapko turns taps, swipes, pinches and holds into the things you do all day. Middle click, close a window, open Telegram. In every app.",
                 points=["Taps, swipes, pinches and holds", "Ready-made gesture sets", "Rules for each app", "Record your own gesture"],
                 meta="Free · Pro $9.99 once · 7 days of Pro free", alt="Tapko's gestures with their actions"),
         uk=dict(kind="Жести трекпада", line="Ваш трекпад уміє більше.",
                 text="Tapko перетворює тапи, свайпи, щипки й утримання на дії, які ви робите щодня. Клік середньою кнопкою, закрити вікно, відкрити Telegram. У будь-якій програмі.",
                 points=["Тапи, свайпи, щипки й утримання", "Готові набори жестів", "Правила для кожної програми", "Запис власного жесту"],
                 meta="Безкоштовно · Pro $9.99 один раз · 7 днів Pro у подарунок", alt="Жести Tapko та їхні дії")),
    dict(id="duesko", name="Duesko", url="https://duesko.stepanix.com/", glow="#2f6bff", warm="#ffb020",
         shot={"en": (1800, 1200), "uk": (1800, 1200)},
         en=dict(kind="Subscription tracker", line="Every subscription, on time.",
                 text="Duesko keeps track of what you pay for, reminds you before every charge and shows where the money goes. No account, no bank login.",
                 points=["Reminders before every charge", "Calendar, menu bar and widgets", "Any currency, with conversion", "Analytics and a monthly budget"],
                 meta="Free up to 5 subscriptions · Pro $9.99 once", alt="Duesko's overview: this month's charges and the budget"),
         uk=dict(kind="Облік підписок", line="Кожна підписка — вчасно.",
                 text="Duesko пам'ятає, за що ви платите, нагадує перед кожним списанням і показує, куди йдуть гроші. Без акаунта й без входу в банк.",
                 points=["Нагадування перед кожним списанням", "Календар, рядок меню й віджети", "Будь-яка валюта з перерахунком", "Аналітика й бюджет на місяць"],
                 meta="Безкоштовно до 5 підписок · Pro $9.99 один раз", alt="Огляд у Duesko: списання цього місяця й бюджет")),
]

T = {
    "en": dict(
        title="Stepanix · Small, careful apps for Mac",
        description="Stepanix makes small Mac apps that do one thing well: Klavko for typing, Tapko for trackpad gestures, Duesko for subscriptions. No accounts, pay once.",
        nav=("Apps", "How we work", "Contact"), language="Language",
        pill_new="New", pill="Duesko keeps your subscriptions on time",
        h1='Small apps for Mac.<br><span class="glow-text">Done with care.</span>',
        lead="Three tools that each do one thing well: fix what you type, give your trackpad more gestures, and keep your subscriptions on time.",
        cta="See the apps", cta2="Write to us",
        apps_h="Our apps", apps_p="Each one is free to start. Pro is a one-time purchase, not another subscription.",
        visit="Visit {name}",
        how_h="How we make them",
        how=[("lock", "Private by design", "No accounts and no tracking. What you type, tap and pay for stays on your Mac."),
             ("once", "Pay once", "Free to start. Pro costs $9.99 once and includes updates. No subscriptions."),
             ("feather", "Light and native", "Small apps built for macOS that start fast and stay out of your way."),
             ("globe", "In your language", "English, Ukrainian and many more languages in every app.")],
        contact_h="Questions or ideas?", contact_p="Write anytime. Every email is read and answered.",
        rights="© 2026 Stepanix",
    ),
    "uk": dict(
        title="Stepanix · Невеликі, ретельно зроблені програми для Mac",
        description="Stepanix робить невеликі програми для Mac, які добре виконують свою справу: Klavko для набору, Tapko для жестів трекпада, Duesko для підписок. Без акаунтів, оплата один раз.",
        nav=("Програми", "Як ми працюємо", "Контакти"), language="Мова",
        pill_new="Нове", pill="Duesko нагадає про кожну підписку",
        h1='Невеликі програми для Mac.<br><span class="glow-text">Зроблені з турботою.</span>',
        lead="Три інструменти, і кожен добре робить свою справу: виправляє набраний текст, дає трекпаду більше жестів і стежить, щоб підписки не заставали зненацька.",
        cta="Переглянути програми", cta2="Написати нам",
        apps_h="Наші програми", apps_p="Кожною можна користуватися безкоштовно. Pro купується один раз, а не стає ще однією підпискою.",
        visit="Сайт {name}",
        how_h="Як ми їх робимо",
        how=[("lock", "Приватно від початку", "Без акаунтів і стеження. Те, що ви друкуєте, натискаєте й оплачуєте, лишається на вашому Mac."),
             ("once", "Оплата один раз", "Почати можна безкоштовно. Pro коштує $9.99 один раз, оновлення включено. Жодних підписок."),
             ("feather", "Легкі й рідні для Mac", "Невеликі програми для macOS, які швидко запускаються й не заважають працювати."),
             ("globe", "Вашою мовою", "Українська, англійська й ще багато мов у кожній програмі.")],
        contact_h="Питання чи ідеї?", contact_p="Пишіть будь-коли. Кожен лист прочитаємо й відповімо.",
        rights="© 2026 Stepanix",
    ),
}

ICONS = {
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "once": '<circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>',
    "feather": '<path d="M20.2 3.8a6 6 0 0 0-8.5 0L5 10.5V19h8.5l6.7-6.7a6 6 0 0 0 0-8.5z"/><path d="M16 8 2 22M17.5 15H9"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
}

def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

# The Stepanix mark: a sun rising over a horizon, the motif of the whole site.
LOGO = '''<svg class="mark" viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffd27a"/><stop offset="1" stop-color="#ff8a3d"/></linearGradient></defs><rect width="32" height="32" rx="8" fill="#141a2e"/><circle cx="16" cy="21" r="8" fill="url(#lg)"/><rect x="4" y="21" width="24" height="7" fill="#141a2e"/><path d="M6 21.5h20" stroke="#ffd9a0" stroke-width="1.6" stroke-linecap="round"/></svg>'''

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffd27a"/><stop offset="1" stop-color="#ff8a3d"/></linearGradient></defs><rect width="32" height="32" rx="8" fill="#141a2e"/><circle cx="16" cy="21" r="8" fill="url(#lg)"/><rect x="4" y="21" width="24" height="7" fill="#141a2e"/><path d="M6 21.5h20" stroke="#ffd9a0" stroke-width="1.6" stroke-linecap="round"/></svg>'''

CSS = """
:root {
  color-scheme: dark;
  --bg: #07090f; --bg-2: #0c1020; --fg: #f1f3fa; --muted: #9aa3b8; --dim: #6c748a;
  --line: rgb(255 255 255 / .09); --glass: rgb(255 255 255 / .035);
  --sun: #ffb347; --sun-2: #ff7a2f; --blue: #4f7dff;
  --display: "Plus Jakarta Sans", "Inter", system-ui, -apple-system, sans-serif;
  --body: "Inter", system-ui, -apple-system, sans-serif;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; background: var(--bg); }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
body { margin: 0; background: var(--bg); color: var(--fg); font: 400 17px/1.6 var(--body); -webkit-font-smoothing: antialiased; overflow-x: clip; }
a { color: inherit; }
img { max-width: 100%; display: block; }
.wrap { max-width: 1120px; margin: 0 auto; padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); }
h1, h2, h3 { font-family: var(--display); margin: 0; letter-spacing: -0.025em; text-wrap: balance; }
p { margin: 0; }
svg { flex: none; }

/* Buttons: a glowing warm one and a glass one. */
.btn { display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px; border-radius: 999px; font: 600 15px/1 var(--body); text-decoration: none; transition: transform .2s ease, box-shadow .2s ease, background .2s ease; }
.btn svg { width: 16px; height: 16px; }
.btn:hover { transform: translateY(-1px); }
.btn:focus-visible { outline: 2px solid var(--sun); outline-offset: 3px; }
.btn.warm { color: #1b0f02; background: linear-gradient(180deg, #ffc56a, #ff8f3a); box-shadow: 0 0 0 1px rgb(255 200 140 / .5) inset, 0 8px 30px -6px rgb(255 140 50 / .6); }
.btn.warm:hover { box-shadow: 0 0 0 1px rgb(255 210 160 / .6) inset, 0 10px 40px -4px rgb(255 140 50 / .75); }
.btn.glass { color: var(--fg); background: var(--glass); border: 1px solid var(--line); backdrop-filter: blur(10px); }
.btn.glass:hover { background: rgb(255 255 255 / .07); }

/* Navigation */
header.nav { position: sticky; top: 0; z-index: 10; background: rgb(7 9 15 / .72); backdrop-filter: saturate(1.4) blur(14px); border-bottom: 1px solid var(--line); }
.nav .wrap { display: flex; align-items: center; gap: 28px; height: 66px; }
.brand { display: flex; align-items: center; gap: 10px; font: 800 20px var(--display); letter-spacing: -0.02em; text-decoration: none; }
.brand .mark { width: 30px; height: 30px; }
.nav nav { display: flex; gap: 26px; margin-left: auto; font-size: 15px; color: var(--muted); }
.nav nav a { text-decoration: none; transition: color .2s; }
.nav nav a:hover { color: var(--fg); }
.lang { display: flex; padding: 3px; border: 1px solid var(--line); border-radius: 999px; font: 600 13px/1 var(--body); }
.lang a { padding: 6px 10px; border-radius: 999px; text-decoration: none; color: var(--muted); }
.lang a:hover { color: var(--fg); }
.lang a[aria-current] { background: rgb(255 179 71 / .14); color: var(--sun); }
.lang a:focus-visible { outline: 2px solid var(--sun); outline-offset: 2px; }
@media (max-width: 720px) { .nav nav { display: none; } .nav .lang { margin-left: auto; } }

/* Hero: the headline, then a sun rising over the horizon with the three app icons on it. */
.hero { position: relative; text-align: center; padding-top: 88px; isolation: isolate; }
.hero::before { content: ""; position: absolute; inset: -66px 0 auto; height: 720px; z-index: -1; pointer-events: none;
  background: radial-gradient(600px 380px at 22% 0%, rgb(79 125 255 / .16), transparent 70%), radial-gradient(520px 340px at 85% 10%, rgb(255 140 60 / .10), transparent 70%); }
.pill { display: inline-flex; align-items: center; gap: 10px; padding: 4px 14px 4px 4px; border-radius: 999px; border: 1px solid var(--line); background: var(--glass); font-size: 14px; color: var(--muted); text-decoration: none; transition: border-color .2s; }
.pill:hover { border-color: rgb(255 179 71 / .4); color: var(--fg); }
.pill b { padding: 4px 10px; border-radius: 999px; color: #1b0f02; font-weight: 600; background: linear-gradient(180deg, #ffc56a, #ff8f3a); }
.pill svg { width: 14px; height: 14px; }
.hero h1 { font-size: clamp(42px, 7.2vw, 84px); font-weight: 700; line-height: 1.04; margin-top: 26px; }
.glow-text { background: linear-gradient(90deg, #ffd690, #ff9a4a 55%, #ff7a2f); -webkit-background-clip: text; background-clip: text; color: transparent; }
.hero .lead { color: var(--muted); font-size: clamp(17px, 2vw, 20px); max-width: 46ch; margin: 22px auto 0; }
.hero .ctas { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-top: 32px; }

.horizon { position: relative; height: 400px; margin-top: -4px; overflow: hidden; -webkit-mask-image: linear-gradient(to bottom, transparent, #000 40px, #000 74%, transparent); mask-image: linear-gradient(to bottom, transparent, #000 40px, #000 74%, transparent); }
.horizon .sun { position: absolute; left: 50%; top: 236px; width: max(2600px, 220vw); aspect-ratio: 1; transform: translateX(-50%); border-radius: 50%;
  background: radial-gradient(closest-side, var(--bg) 99.2%, transparent 100%);
  box-shadow: 0 -1px 0 rgb(255 230 190 / .95), 0 -6px 24px rgb(255 190 110 / .6), 0 -30px 90px rgb(255 130 50 / .42), 0 -110px 240px rgb(79 125 255 / .26); }
.horizon .flare { position: absolute; left: 50%; top: 136px; width: 640px; height: 220px; transform: translateX(-50%); background: radial-gradient(closest-side, rgb(255 180 100 / .28), transparent); filter: blur(12px); pointer-events: none; }
.horizon .icons { position: absolute; left: 0; right: 0; top: 236px; transform: translateY(-100%); padding-bottom: 14px; display: flex; justify-content: center; align-items: flex-end; gap: clamp(18px, 4vw, 44px); }
.horizon .icons a { display: block; width: clamp(88px, 11vw, 128px); transition: transform .3s ease; filter: drop-shadow(0 18px 30px rgb(0 0 0 / .55)); }
.horizon .icons a:nth-child(2) { transform: translateY(-26px); }
.horizon .icons a:hover { transform: translateY(-6px); }
.horizon .icons a:nth-child(2):hover { transform: translateY(-32px); }
.horizon .icons a:focus-visible { outline: 2px solid var(--sun); outline-offset: 4px; border-radius: 24%; }
@media (max-width: 640px) {
  .horizon { height: 290px; }
  .horizon .sun, .horizon .icons { top: 196px; }
  .horizon .flare { top: 96px; }
}

section { padding-block: 100px; }
.head { text-align: center; display: grid; gap: 14px; justify-items: center; margin-bottom: 56px; }
.head h2 { font-size: clamp(32px, 4.6vw, 52px); font-weight: 700; line-height: 1.08; }
.head p { color: var(--muted); max-width: 52ch; font-size: 18px; }

/* One block per app. */
.apps { display: grid; gap: 28px; }
.app { position: relative; display: grid; grid-template-columns: 0.95fr 1.25fr; gap: 48px; align-items: center; padding: 44px; border-radius: 32px; border: 1px solid var(--line); overflow: hidden; isolation: isolate;
  background: linear-gradient(180deg, rgb(255 255 255 / .045), rgb(255 255 255 / .015)); }
.app::before { content: ""; position: absolute; z-index: -1; inset: auto auto -40% -20%; width: 70%; aspect-ratio: 1; border-radius: 50%; background: radial-gradient(closest-side, var(--glow), transparent); opacity: .30; filter: blur(30px); }
.app::after { content: ""; position: absolute; z-index: -1; inset: -35% -15% auto auto; width: 55%; aspect-ratio: 1; border-radius: 50%; background: radial-gradient(closest-side, var(--warm), transparent); opacity: .14; filter: blur(30px); }
.app.flip { grid-template-columns: 1.25fr 0.95fr; }
.app.flip .text { order: 2; }
.app .text { display: grid; gap: 18px; align-content: start; }
.app .title { display: flex; align-items: center; gap: 16px; }
.app .title img { width: 68px; height: 68px; }
.app .kind { font-size: 13px; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: var(--warm); }
.app h3 { font-size: 34px; font-weight: 800; line-height: 1.05; }
.app .line { font: 600 21px/1.3 var(--display); letter-spacing: -0.01em; }
.app .desc { color: var(--muted); font-size: 16px; }
.app ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 9px; font-size: 15px; }
.app li { display: flex; gap: 10px; align-items: baseline; }
.app li::before { content: ""; width: 6px; height: 6px; border-radius: 50%; flex: none; transform: translateY(-2px); background: var(--warm); box-shadow: 0 0 10px var(--warm); }
.app .meta { color: var(--dim); font-size: 14px; }
.app .btn { justify-self: start; }
.app .shot { border-radius: 16px; overflow: hidden; border: 1px solid rgb(255 255 255 / .12); box-shadow: 0 40px 80px -30px rgb(0 0 0 / .8), 0 0 60px -20px var(--glow); background: #1d1d20; }
.app .shot img { width: 100%; height: auto; }
@media (max-width: 900px) {
  .app, .app.flip { grid-template-columns: 1fr; gap: 32px; padding: 28px 22px; border-radius: 26px; }
  .app.flip .text { order: 0; }
}

/* How we work */
.how { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
@media (max-width: 960px) { .how { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 540px) { .how { grid-template-columns: 1fr; } }
.how div { padding: 26px; border-radius: 22px; border: 1px solid var(--line); background: var(--glass); display: grid; gap: 10px; align-content: start; }
.how .ic { width: 46px; height: 46px; border-radius: 14px; display: grid; place-items: center; color: var(--sun); background: radial-gradient(circle at 50% 120%, rgb(255 140 50 / .35), rgb(255 255 255 / .04)); border: 1px solid rgb(255 179 71 / .25); box-shadow: 0 0 24px -6px rgb(255 140 50 / .5); }
.how .ic svg { width: 22px; height: 22px; }
.how h3 { font-size: 18px; font-weight: 700; margin-top: 6px; }
.how p { color: var(--muted); font-size: 15px; }

/* Contact */
.contact { position: relative; text-align: center; padding: 64px 28px; border-radius: 32px; border: 1px solid var(--line); overflow: hidden; isolation: isolate; display: grid; gap: 16px; justify-items: center;
  background: linear-gradient(180deg, rgb(255 255 255 / .04), transparent); }
.contact::before { content: ""; position: absolute; z-index: -1; left: 50%; bottom: calc(80px - 2200px); width: 2200px; aspect-ratio: 1; transform: translateX(-50%); border-radius: 50%; background: var(--bg);
  box-shadow: 0 -1px 0 rgb(255 220 170 / .75), 0 -14px 50px rgb(255 140 60 / .35), 0 -60px 140px rgb(79 125 255 / .18); }
.contact { padding-bottom: 104px; }
.contact h2 { font-size: clamp(30px, 4vw, 44px); font-weight: 700; }
.contact p { color: var(--muted); font-size: 18px; }
.contact .btn { margin-top: 8px; }

footer { padding-block: 40px; color: var(--dim); font-size: 14px; }
footer .wrap { display: flex; flex-wrap: wrap; gap: 12px 24px; align-items: center; }
footer .links { display: flex; flex-wrap: wrap; gap: 20px; margin-left: auto; }
footer a { text-decoration: none; } footer a:hover { color: var(--fg); }

/* Blocks rise into view as you scroll. Without JavaScript, or with reduced motion, everything is simply shown. */
.js .reveal { opacity: 0; transform: translateY(28px); transition: opacity .8s ease, transform .8s cubic-bezier(.2,.7,.2,1); }
.js .reveal.in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { .js .reveal { opacity: 1; transform: none; transition: none; } }
"""

SCRIPT = """<script>
document.documentElement.classList.add("js");
(function () {
  /* Remembers the chosen language and opens that version on later visits. English is the default. */
  try {
    var root = document.documentElement, saved = localStorage.getItem("stepanix-lang");
    if (saved && saved !== root.lang && root.dataset.alt) location.replace(root.dataset.alt + location.hash);
    document.addEventListener("click", function (e) {
      var link = e.target.closest && e.target.closest("[data-set-lang]");
      if (link) localStorage.setItem("stepanix-lang", link.getAttribute("data-set-lang"));
    });
  } catch (e) {}
  document.addEventListener("DOMContentLoaded", function () {
    var items = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window)) { items.forEach(function (el) { el.classList.add("in"); }); return; }
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); seen.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    items.forEach(function (el) { seen.observe(el); });
  });
})();
</script>"""


def page(lang):
    t = T[lang]
    p = "" if lang == "en" else "../"
    alt = "uk/" if lang == "en" else "../"
    en_href = "./" if lang == "en" else "../"
    uk_href = "uk/" if lang == "en" else "./"
    cur = lambda l: ' aria-current="true"' if l == lang else f' hreflang="{l}"'
    nav_links = "".join(f'<a href="#{a}">{n}</a>' for a, n in zip(("apps", "how", "contact"), t["nav"]))
    site = lambda a: a["url"] + ("" if lang == "en" else "uk/")

    icons = "".join(f'<a href="#{a["id"]}" aria-label="{a["name"]}"><img src="{p}assets/{a["id"]}.png" alt="" width="128" height="128"></a>' for a in APPS)

    blocks = []
    for i, a in enumerate(APPS):
        x = a[lang]
        w, h = a["shot"][lang]
        pts = "".join(f"<li>{s}</li>" for s in x["points"])
        blocks.append(f"""
      <article class="app reveal{' flip' if i % 2 else ''}" id="{a['id']}" style="--glow: {a['glow']}; --warm: {a['warm']}">
        <div class="text">
          <div class="title"><img src="{p}assets/{a['id']}.png" alt="" width="68" height="68"><div><div class="kind">{x['kind']}</div><h3>{a['name']}</h3></div></div>
          <p class="line">{x['line']}</p>
          <p class="desc">{x['text']}</p>
          <ul>{pts}</ul>
          <p class="meta">{x['meta']}</p>
          <a class="btn glass" href="{site(a)}">{t['visit'].format(name=a['name'])} {icon('arrow')}</a>
        </div>
        <div class="shot"><img src="{p}assets/{a['id']}-{lang}.webp" alt="{x['alt']}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>
      </article>""")

    how = "".join(f'<div class="reveal"><span class="ic">{icon(i)}</span><h3>{h}</h3><p>{d}</p></div>' for i, h, d in t["how"])
    app_links = "".join(f'<a href="{site(a)}">{a["name"]}</a>' for a in APPS)

    return f"""<!doctype html>
<html lang="{lang}" data-alt="{alt}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#07090f">
<title>{t['title']}</title>
<meta name="description" content="{t['description']}">
<link rel="alternate" hreflang="en" href="{HOST}/">
<link rel="alternate" hreflang="uk" href="{HOST}/uk/">
<link rel="alternate" hreflang="x-default" href="{HOST}/">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['description']}">
<meta property="og:image" content="{HOST}/assets/duesko-{lang}.webp">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Inter:wght@400;500;600&display=swap">
<style>{CSS}</style>
{SCRIPT}
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="#top">{LOGO}Stepanix</a>
    <nav aria-label="Sections">{nav_links}</nav>
    <div class="lang" role="group" aria-label="{t['language']}">
      <a href="{en_href}"{cur('en')} lang="en" data-set-lang="en">EN</a>
      <a href="{uk_href}"{cur('uk')} lang="uk" data-set-lang="uk" title="Українська">UA</a>
    </div>
  </div>
</header>

<main id="top">
  <div class="hero">
    <div class="wrap">
      <a class="pill" href="#duesko"><b>{t['pill_new']}</b>{t['pill']} {icon('arrow')}</a>
      <h1>{t['h1']}</h1>
      <p class="lead">{t['lead']}</p>
      <div class="ctas">
        <a class="btn warm" href="#apps">{t['cta']} {icon('arrow')}</a>
        <a class="btn glass" href="#contact">{t['cta2']}</a>
      </div>
    </div>
    <div class="horizon" aria-hidden="false">
      <div class="flare"></div>
      <div class="sun"></div>
      <div class="icons">{icons}</div>
    </div>
  </div>

  <section id="apps" style="padding-top: 24px">
    <div class="wrap">
      <div class="head reveal"><h2>{t['apps_h']}</h2><p>{t['apps_p']}</p></div>
      <div class="apps">{''.join(blocks)}
      </div>
    </div>
  </section>

  <section id="how" style="padding-top: 20px">
    <div class="wrap">
      <div class="head reveal"><h2>{t['how_h']}</h2></div>
      <div class="how">{how}</div>
    </div>
  </section>

  <section id="contact" style="padding-top: 20px">
    <div class="wrap">
      <div class="contact reveal">
        <h2>{t['contact_h']}</h2>
        <p>{t['contact_p']}</p>
        <a class="btn warm" href="mailto:{EMAIL}">{icon('mail')} {EMAIL}</a>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <span>{t['rights']}</span>
    <div class="links">{app_links}<a href="mailto:{EMAIL}">{EMAIL}</a></div>
  </div>
</footer>
</body>
</html>
"""


def main():
    (ROOT / "index.html").write_text(page("en"), encoding="utf-8")
    (ROOT / "uk").mkdir(exist_ok=True)
    (ROOT / "uk" / "index.html").write_text(page("uk"), encoding="utf-8")
    (ROOT / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (ROOT / "CNAME").write_text("stepanix.com", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("Built", ROOT)


if __name__ == "__main__":
    main()
