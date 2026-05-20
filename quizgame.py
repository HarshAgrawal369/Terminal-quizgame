import random
import time
import os
import json
from datetime import datetime

# ─────────────────────────────────────────────
#  ANSI COLOR PALETTE
# ─────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    MAGENTA = "\033[95m"
    BLUE    = "\033[94m"
    WHITE   = "\033[97m"
    GREY    = "\033[90m"
    BG_DARK = "\033[40m"

def clr(): os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""
{C.CYAN}{C.BOLD}
  ██████╗ ██╗   ██╗██╗███████╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
 ██╔═══██╗██║   ██║██║╚══███╔╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
 ██║   ██║██║   ██║██║  ███╔╝     ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
 ██║▄▄ ██║██║   ██║██║ ███╔╝      ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
 ╚██████╔╝╚██████╔╝██║███████╗    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
  ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{C.RESET}{C.GREY}                           — The Ultimate Knowledge Challenge —{C.RESET}
""")

def divider(char="─", color=C.GREY):
    print(f"{color}{char * 62}{C.RESET}")

def section(title, color=C.CYAN):
    divider("═", color)
    print(f"{color}{C.BOLD}  {title}{C.RESET}")
    divider("═", color)

# ─────────────────────────────────────────────
#  QUESTION BANK  (category → difficulty → list)
# ─────────────────────────────────────────────
QUESTIONS = {
    "🌍 Geography": {
        "Easy": [
            {"q": "What is the capital of France?",      "a": "paris",    "opts": ["paris","berlin","rome","madrid"]},
            {"q": "What is the capital of Germany?",     "a": "berlin",   "opts": ["lisbon","berlin","athens","rome"]},
            {"q": "What is the capital of Italy?",       "a": "rome",     "opts": ["madrid","paris","rome","berlin"]},
            {"q": "What is the capital of Spain?",       "a": "madrid",   "opts": ["athens","madrid","lisbon","paris"]},
            {"q": "What is the capital of Portugal?",    "a": "lisbon",   "opts": ["rome","berlin","madrid","lisbon"]},
            {"q": "What is the capital of Greece?",      "a": "athens",   "opts": ["paris","athens","berlin","madrid"]},
        ],
        "Hard": [
            {"q": "What is the capital of Kazakhstan?",  "a": "astana",   "opts": ["almaty","astana","bishkek","tashkent"]},
            {"q": "What is the capital of Myanmar?",     "a": "naypyidaw","opts": ["yangon","naypyidaw","mandalay","bagan"]},
            {"q": "What is the capital of Bhutan?",      "a": "thimphu",  "opts": ["paro","thimphu","punakha","bumthang"]},
            {"q": "What is the capital of Suriname?",    "a": "paramaribo","opts": ["cayenne","georgetown","paramaribo","bridgetown"]},
        ],
    },
    "🔬 Science": {
        "Easy": [
            {"q": "What planet is closest to the Sun?",          "a": "mercury",  "opts": ["venus","mercury","mars","earth"]},
            {"q": "What gas do plants absorb from air?",         "a": "co2",      "opts": ["oxygen","nitrogen","co2","hydrogen"]},
            {"q": "How many bones are in the adult human body?", "a": "206",      "opts": ["196","206","216","226"]},
            {"q": "What is the chemical symbol for gold?",       "a": "au",       "opts": ["go","gd","au","ag"]},
            {"q": "What force keeps us on the ground?",          "a": "gravity",  "opts": ["friction","gravity","magnetism","tension"]},
        ],
        "Hard": [
            {"q": "What is the speed of light (km/s)?",          "a": "299792",   "opts": ["199792","299792","399792","499792"]},
            {"q": "What particle has no electric charge?",       "a": "neutron",  "opts": ["proton","electron","neutron","positron"]},
            {"q": "What is the powerhouse of the cell?",         "a": "mitochondria","opts": ["nucleus","mitochondria","ribosome","golgi"]},
            {"q": "What element has atomic number 79?",          "a": "gold",     "opts": ["silver","platinum","gold","copper"]},
        ],
    },
    "💻 Technology": {
        "Easy": [
            {"q": "What does 'CPU' stand for?",                  "a": "central processing unit","opts": ["central processing unit","computer power unit","core program utility","central program unit"]},
            {"q": "Who founded Microsoft?",                      "a": "bill gates","opts": ["elon musk","steve jobs","bill gates","mark zuckerberg"]},
            {"q": "What does 'HTML' stand for?",                 "a": "hypertext markup language","opts": ["hypertext markup language","hyper transfer markup language","high text machine language","hypertext machine language"]},
            {"q": "What language runs in a web browser?",        "a": "javascript","opts": ["python","java","javascript","ruby"]},
        ],
        "Hard": [
            {"q": "What does 'API' stand for?",                  "a": "application programming interface","opts": ["application programming interface","automated protocol integration","advanced program interface","application process interaction"]},
            {"q": "Which sorting algorithm has O(n log n) avg?", "a": "merge sort","opts": ["bubble sort","merge sort","selection sort","insertion sort"]},
            {"q": "What is the base of hexadecimal?",            "a": "16",       "opts": ["8","10","16","32"]},
        ],
    },
    "🎬 Pop Culture": {
        "Easy": [
            {"q": "Which movie features the line 'Just keep swimming'?","a": "finding nemo","opts": ["finding nemo","finding dory","the little mermaid","moana"]},
            {"q": "Which band released 'Bohemian Rhapsody'?",    "a": "queen",    "opts": ["beatles","queen","led zeppelin","pink floyd"]},
            {"q": "What sport is played at Wimbledon?",          "a": "tennis",   "opts": ["cricket","tennis","golf","badminton"]},
        ],
        "Hard": [
            {"q": "Who directed the movie Inception (2010)?",    "a": "christopher nolan","opts": ["james cameron","christopher nolan","steven spielberg","ridley scott"]},
            {"q": "What year was the first iPhone released?",    "a": "2007",     "opts": ["2005","2006","2007","2008"]},
        ],
    },
}

HIGHSCORE_FILE = "quiz_highscores.json"

# ─────────────────────────────────────────────
#  HIGH SCORE  helpers
# ─────────────────────────────────────────────
def load_scores():
    try:
        with open(HIGHSCORE_FILE) as f:
            return json.load(f)
    except:
        return []

def save_score(name, score, total, category, difficulty, elapsed):
    scores = load_scores()
    scores.append({
        "name": name, "score": score, "total": total,
        "category": category, "difficulty": difficulty,
        "accuracy": round(score/total*100, 1),
        "time": round(elapsed, 1),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    scores.sort(key=lambda x: (-x["accuracy"], x["time"]))
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump(scores[:10], f, indent=2)

def show_leaderboard():
    scores = load_scores()
    section("🏆  LEADERBOARD  — TOP 10", C.YELLOW)
    if not scores:
        print(f"  {C.GREY}No scores yet. Be the first!{C.RESET}")
    else:
        print(f"  {C.BOLD}{'#':<4}{'Name':<15}{'Score':<10}{'Acc%':<9}{'Time(s)':<10}{'Category'}{C.RESET}")
        divider()
        for i, s in enumerate(scores, 1):
            bar_col = C.GREEN if s["accuracy"] >= 80 else C.YELLOW if s["accuracy"] >= 50 else C.RED
            print(f"  {C.CYAN}{i:<4}{C.WHITE}{s['name']:<15}{C.GREEN}{s['score']}/{s['total']:<8}"
                  f"{bar_col}{s['accuracy']:<9}{C.GREY}{s['time']:<10}{C.MAGENTA}{s['category']}{C.RESET}")
    divider()
    input(f"\n{C.GREY}Press Enter to continue...{C.RESET}")

# ─────────────────────────────────────────────
#  TIMER  bar
# ─────────────────────────────────────────────
def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        filled = int((remaining / seconds) * 20)
        bar = "█" * filled + "░" * (20 - filled)
        col = C.GREEN if remaining > seconds * 0.5 else C.YELLOW if remaining > seconds * 0.25 else C.RED
        print(f"  {col}⏱  [{bar}] {remaining:2d}s{C.RESET}", end="\r")
        time.sleep(1)
    print(" " * 50, end="\r")

# ─────────────────────────────────────────────
#  SINGLE QUESTION
# ─────────────────────────────────────────────
def ask_question(q_data, q_num, total, lives, difficulty):
    opts = q_data["opts"][:]
    random.shuffle(opts)
    time_limit = {"Easy": 20, "Hard": 12}[difficulty]

    print(f"\n  {C.CYAN}Question {q_num}/{total}{C.RESET}  "
          f"{C.GREY}│{C.RESET}  "
          f"{'❤️ ' * lives}  "
          f"{C.GREY}│  Difficulty: {C.YELLOW}{difficulty}{C.RESET}\n")

    print(f"  {C.WHITE}{C.BOLD}{q_data['q']}{C.RESET}\n")

    labels = ["A", "B", "C", "D"]
    for i, (label, opt) in enumerate(zip(labels, opts)):
        print(f"    {C.CYAN}[{label}]{C.RESET}  {opt.title()}")

    print()
    # Start timer in a thread-free way (blocking)
    import threading
    timer_done = [False]
    def run_timer():
        countdown_timer(time_limit)
        timer_done[0] = True

    t = threading.Thread(target=run_timer, daemon=True)
    t.start()

    start = time.time()
    raw = input(f"\n  {C.YELLOW}Your answer (A/B/C/D): {C.RESET}").strip().upper()
    elapsed = time.time() - start
    timer_done[0] = True  # stop visual timer

    if raw in labels:
        guess = opts[labels.index(raw)].lower()
    else:
        guess = ""

    timed_out = elapsed >= time_limit

    if timed_out or guess == "":
        print(f"\n  {C.RED}⏰  Time's up! The answer was: {C.BOLD}{q_data['a'].title()}{C.RESET}")
        return False, guess, elapsed

    correct = guess == q_data["a"]
    if correct:
        time_bonus = max(0, time_limit - int(elapsed))
        print(f"\n  {C.GREEN}✔  Correct!{C.RESET}  {C.GREY}+{time_bonus}s bonus{C.RESET}")
    else:
        print(f"\n  {C.RED}✘  Wrong!  The answer was: {C.BOLD}{q_data['a'].title()}{C.RESET}")

    time.sleep(1.2)
    return correct, guess, elapsed

# ─────────────────────────────────────────────
#  SCORE CARD
# ─────────────────────────────────────────────
def display_score(correct, total, elapsed, category, difficulty, player):
    acc = correct / total * 100
    section("📊  RESULTS", C.MAGENTA)
    print(f"  {C.WHITE}Player      : {C.CYAN}{C.BOLD}{player}{C.RESET}")
    print(f"  {C.WHITE}Category    : {C.MAGENTA}{category}{C.RESET}")
    print(f"  {C.WHITE}Difficulty  : {C.YELLOW}{difficulty}{C.RESET}")
    divider()
    print(f"  {C.GREEN}✔  Correct  : {correct}/{total}{C.RESET}")
    print(f"  {C.RED}✘  Wrong    : {total - correct}/{total}{C.RESET}")
    print(f"  {C.CYAN}📈 Accuracy  : {acc:.1f}%{C.RESET}")
    print(f"  {C.GREY}⏱  Time     : {elapsed:.1f}s{C.RESET}")
    divider()

    # Grade
    if acc == 100:
        grade, col = "S  — PERFECT! 🌟", C.GREEN
    elif acc >= 80:
        grade, col = "A  — Excellent!", C.GREEN
    elif acc >= 60:
        grade, col = "B  — Good Job!", C.CYAN
    elif acc >= 40:
        grade, col = "C  — Keep Practicing", C.YELLOW
    else:
        grade, col = "F  — Better luck next time", C.RED

    print(f"\n  {col}{C.BOLD}Grade: {grade}{C.RESET}\n")
    save_score(player, correct, total, category, difficulty, elapsed)

# ─────────────────────────────────────────────
#  MAIN GAME
# ─────────────────────────────────────────────
def new_game(player):
    clr()
    banner()

    # Choose category
    categories = list(QUESTIONS.keys())
    section("📚  CHOOSE CATEGORY", C.CYAN)
    for i, cat in enumerate(categories, 1):
        print(f"  {C.CYAN}[{i}]{C.RESET}  {cat}")
    print(f"  {C.CYAN}[{len(categories)+1}]{C.RESET}  🎲 Random Mix")

    while True:
        choice = input(f"\n  {C.YELLOW}Enter choice: {C.RESET}").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories) + 1:
            break
        print(f"  {C.RED}Invalid. Try again.{C.RESET}")

    choice = int(choice)
    random_mode = choice == len(categories) + 1
    category_name = "🎲 Random Mix" if random_mode else categories[choice - 1]

    # Choose difficulty
    section("⚡  CHOOSE DIFFICULTY", C.YELLOW)
    print(f"  {C.GREEN}[1]{C.RESET}  Easy   — 20s per question, 3 lives")
    print(f"  {C.RED}[2]{C.RESET}  Hard   — 12s per question, 2 lives")

    while True:
        diff = input(f"\n  {C.YELLOW}Enter choice: {C.RESET}").strip()
        if diff in ("1", "2"):
            break
        print(f"  {C.RED}Invalid. Try again.{C.RESET}")

    difficulty = "Easy" if diff == "1" else "Hard"
    lives = 3 if difficulty == "Easy" else 2

    # Build question pool
    if random_mode:
        pool = []
        for cat in QUESTIONS.values():
            pool.extend(cat.get(difficulty, []))
    else:
        pool = QUESTIONS[categories[choice - 1]].get(difficulty, [])

    random.shuffle(pool)
    pool = pool[:6]

    clr()
    banner()
    section(f"🚀  STARTING  |  {category_name}  |  {difficulty}", C.GREEN)
    print(f"\n  {C.WHITE}Get ready, {C.CYAN}{C.BOLD}{player}{C.RESET}{C.WHITE}! {len(pool)} questions ahead.{C.RESET}")
    time.sleep(1.5)

    correct = 0
    start_time = time.time()

    for i, q in enumerate(pool, 1):
        if lives <= 0:
            print(f"\n  {C.RED}{C.BOLD}💀  No lives left! Game Over.{C.RESET}")
            break
        clr()
        banner()
        result, guess, _ = ask_question(q, i, len(pool), lives, difficulty)
        if result:
            correct += 1
        else:
            lives -= 1

    elapsed = time.time() - start_time
    clr()
    banner()
    display_score(correct, len(pool), elapsed, category_name, difficulty, player)

# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────
def main():
    clr()
    banner()
    section("👤  WELCOME", C.CYAN)
    player = input(f"  {C.YELLOW}Enter your name: {C.RESET}").strip() or "Player"

    while True:
        clr()
        banner()
        section("📋  MAIN MENU", C.CYAN)
        print(f"  {C.GREEN}[1]{C.RESET}  🎮  Start New Game")
        print(f"  {C.YELLOW}[2]{C.RESET}  🏆  Leaderboard")
        print(f"  {C.RED}[3]{C.RESET}  🚪  Quit")
        divider()

        choice = input(f"\n  {C.YELLOW}Enter choice: {C.RESET}").strip()
        if choice == "1":
            new_game(player)
            input(f"\n  {C.GREY}Press Enter to return to menu...{C.RESET}")
        elif choice == "2":
            clr()
            banner()
            show_leaderboard()
        elif choice == "3":
            clr()
            print(f"\n  {C.CYAN}{C.BOLD}Thanks for playing, {player}! See you next time. 👋{C.RESET}\n")
            break
        else:
            print(f"  {C.RED}Invalid. Try again.{C.RESET}")
            time.sleep(0.8)

if __name__ == "__main__":
    main()
