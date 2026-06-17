from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1470, 1102
BG = (22, 17, 27)
PRIMARY = (250, 236, 255)
TERTIARY = (132, 226, 246)
CORAL = (255, 109, 109)
AMBER = (210, 153, 34)
GREEN = (63, 185, 80)
GRAY = (150, 142, 152)
CONTAINER = (35, 29, 40)

font_dir = os.path.expanduser("~/Library/Fonts")
plex_bold   = ImageFont.truetype(os.path.join(font_dir, "IBMPlexMono-Bold.ttf"), 80)
plex_sbold  = ImageFont.truetype(os.path.join(font_dir, "IBMPlexMono-SemiBold.ttf"), 52)
plex_reg    = ImageFont.truetype(os.path.join(font_dir, "IBMPlexMono-Regular.ttf"), 36)
plex_sm     = ImageFont.truetype(os.path.join(font_dir, "IBMPlexMono-Regular.ttf"), 28)
plex_xs     = ImageFont.truetype(os.path.join(font_dir, "IBMPlexMono-Regular.ttf"), 22)
plex_title  = ImageFont.truetype(os.path.join(font_dir, "IBMPlexMono-Bold.ttf"), 64)
plex_sub    = ImageFont.truetype(os.path.join(font_dir, "IBMPlexMono-SemiBold.ttf"), 40)

def draw_cambio_frame(draw):
    box_margin, corner_len = 40, 30
    lc = TERTIARY
    draw.line([(box_margin, box_margin), (box_margin + corner_len, box_margin)], fill=lc, width=3)
    draw.line([(box_margin, box_margin), (box_margin, box_margin + corner_len)], fill=lc, width=3)
    draw.line([(W - box_margin, box_margin), (W - box_margin - corner_len, box_margin)], fill=lc, width=3)
    draw.line([(W - box_margin, box_margin), (W - box_margin, box_margin + corner_len)], fill=lc, width=3)
    draw.line([(box_margin, H - box_margin), (box_margin + corner_len, H - box_margin)], fill=lc, width=3)
    draw.line([(box_margin, H - box_margin), (box_margin, H - box_margin - corner_len)], fill=lc, width=3)
    draw.line([(W - box_margin, H - box_margin), (W - box_margin - corner_len, H - box_margin)], fill=lc, width=3)
    draw.line([(W - box_margin, H - box_margin), (W - box_margin, H - box_margin - corner_len)], fill=lc, width=3)
    sep_y = box_margin + 70
    draw.line([(box_margin + 10, sep_y), (W - box_margin - 10, sep_y)], fill=GRAY, width=1)
    draw.text((box_margin + 20, box_margin + 16), "CAMBIO_LABS_V1.0", fill=TERTIARY, font=plex_xs)
    draw.text((W - box_margin - 20, box_margin + 16), "IFE 2026", fill=GRAY, font=plex_xs, anchor="rt")
    draw.text((box_margin + 20, H - box_margin - 30), "AI LITERACY TRACK 2026", fill=CORAL, font=plex_sm)
    draw.text((W - box_margin - 20, H - box_margin - 30), "DAY 1", fill=GRAY, font=plex_sm, anchor="rt")
    draw.line([(box_margin + 10, H - box_margin - 55), (W - box_margin - 10, H - box_margin - 55)], fill=GRAY, width=1)

def make_slide(filename, lines, placeholder=False):
    """lines: list of (text, font, color, y_offset) tuples"""
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_cambio_frame(draw)
    for text, font, color, y in lines:
        draw.text((W // 2, y), text, fill=color, font=font, anchor="mm")
    if placeholder:
        draw.rectangle([(W//2 - 300, 600), (W//2 + 300, 660)], fill=CONTAINER, outline=GRAY, width=2)
        draw.text((W // 2, 630), "[ INSTRUCTOR: INSERT CONTENT HERE ]", fill=GRAY, font=plex_sm, anchor="mm")
    out = os.path.join("/Users/eolivera/Documents/Clients/Cambio Labs/IFE/Day1", filename)
    img.save(out)
    print(f"  {out}  {img.size}")

print("Generating slides...")

# S01 — Agenda overview
make_slide("s01_agenda.png", [
    ("AGENDA", plex_title, PRIMARY, 200),
    ("Welcome & overview", plex_reg, PRIMARY, 340),
    ("Journey login walkthrough", plex_reg, PRIMARY, 400),
    ("Terminal readiness check", plex_reg, PRIMARY, 460),
    ("WSL mini-lab (Windows)", plex_reg, PRIMARY, 520),
    ("Core terminal fun", plex_reg, TERTIARY, 600),
    ("Share-out", plex_reg, PRIMARY, 660),
    ("Journey reflection & wrap", plex_reg, PRIMARY, 720),
])

# S02 — Welcome
make_slide("s02_welcome.png", [
    ("WELCOME", plex_title, PRIMARY, 240),
    ("Today is about", plex_reg, GRAY, 360),
    ("first contact with the terminal", plex_reg, GREEN, 430),
    ("", plex_reg, GRAY, 500),
    ("No experience needed.", plex_reg, PRIMARY, 560),
    ("Low risk, high fun.", plex_reg, PRIMARY, 620),
    ("Every command is a win.", plex_reg, PRIMARY, 680),
])

# S03 — Journey login (PLACEHOLDER — needs screenshots)
make_slide("s03_journey_login.png", [
    ("JOURNEY LOGIN", plex_title, TERTIARY, 210),
    ("1. Navigate to Journey URL", plex_reg, PRIMARY, 350),
    ("2. Log in with your credentials", plex_reg, PRIMARY, 420),
    ("3. Find the Day 1 reflection area", plex_reg, PRIMARY, 490),
    ("", plex_reg, GRAY, 560),
    ("[ INSTRUCTOR: Insert Journey URL ]", plex_sm, GRAY, 640),
    ("[ INSTRUCTOR: Insert login screenshot ]", plex_sm, GRAY, 700),
], placeholder=True)

# S04 — Terminal readiness check
make_slide("s04_terminal_check.png", [
    ("TERMINAL CHECK", plex_title, GREEN, 200),
    ("Raise your hand if:", plex_sbold, PRIMARY, 340),
    ("You can see a terminal / command prompt", plex_reg, PRIMARY, 440),
    ("You have used a terminal before", plex_reg, PRIMARY, 510),
    ("", plex_reg, GRAY, 590),
    ("Goal: know which pods need WSL support", plex_reg, AMBER, 670),
])

# S05 — WSL mini-lab (PLACEHOLDER)
make_slide("s05_wsl_minilab.png", [
    ("WSL MINI-LAB", plex_title, AMBER, 200),
    ("Windows students only", plex_sbold, CORAL, 300),
    ("", plex_reg, GRAY, 380),
    ("[ INSTRUCTOR: Insert WSL install /", plex_sm, GRAY, 480),
    ("    terminal setup instructions ]", plex_sm, GRAY, 530),
    ("", plex_reg, GRAY, 620),
    ("macOS / Linux students: your terminal is ready", plex_reg, PRIMARY, 700),
], placeholder=True)

# S06 — Transition
make_slide("s06_transition.png", [
    ("TRANSITION", plex_title, TERTIARY, 220),
    ("Every pod has a working shell?", plex_sbold, PRIMARY, 360),
    ("", plex_reg, GRAY, 440),
    ("TAs: scan your pod zone", plex_reg, GRAY, 520),
    ("If stuck > 3 min → cloud fallback", plex_reg, CORAL, 590),
    ("", plex_reg, GRAY, 660),
    ("Ready? Let's go.", plex_sbold, GREEN, 750),
])

# S07 — Core terminal fun: Hello World
make_slide("s07_hello_world.png", [
    ("YOUR FIRST COMMAND", plex_title, PRIMARY, 200),
    ("Type this in your terminal:", plex_reg, GRAY, 340),
    ("echo \"Hello, world!\"", plex_sbold, TERTIARY, 440),
    ("", plex_reg, GRAY, 530),
    ("Hit Enter.", plex_reg, PRIMARY, 600),
    ("You just ran your first terminal command.", plex_reg, GREEN, 680),
])

# S08 — Fun commands
make_slide("s08_fun_commands.png", [
    ("FUN COMMANDS", plex_title, CORAL, 160),
    ("Try one (or all):", plex_reg, GRAY, 280),
    ("figlet -f slant \"Hello\"", plex_sbold, TERTIARY, 370),
    ("cowsay \"Hello, world!\"", plex_sbold, TERTIARY, 440),
    ("toilet --gay \"Hello\"", plex_sbold, TERTIARY, 510),
    ("echo \"Hello\" | lolcat", plex_sbold, TERTIARY, 580),
    ("", plex_reg, GRAY, 660),
    ("Not all may be installed — that's fine.", plex_sm, AMBER, 730),
])

# S09 — Personalized greeting
make_slide("s09_personalized_greeting.png", [
    ("YOUR GREETING", plex_title, PRIMARY, 200),
    ("echo \"Hello, world!", plex_sbold, TERTIARY, 350),
    ("My name is [YOUR NAME].\"", plex_sbold, TERTIARY, 420),
    ("", plex_reg, GRAY, 510),
    ("This is your deliverable.", plex_reg, GREEN, 600),
    ("Screenshot or copy-paste", plex_reg, PRIMARY, 670),
    ("→ submit in Journey", plex_reg, PRIMARY, 740),
])

# S10 — Share-out
make_slide("s10_shareout.png", [
    ("SHARE-OUT", plex_title, AMBER, 200),
    ("Show us your favorite output!", plex_sbold, PRIMARY, 360),
    ("", plex_reg, GRAY, 460),
    ("What did figlet make?", plex_reg, GRAY, 540),
    ("Did cowsay say something funny?", plex_reg, GRAY, 610),
    ("How did lolcat change the colors?", plex_reg, GRAY, 680),
    ("", plex_reg, GRAY, 760),
    ("Volunteers? TAs pick one per pod.", plex_sm, TERTIARY, 830),
])

# S11 — Exit line / Journey reflection
make_slide("s11_exit_line.png", [
    ("EXIT LINE", plex_title, PRIMARY, 180),
    ("Submit in Journey:", plex_reg, GRAY, 300),
    ("Quick Reflection", plex_sbold, CORAL, 400),
    ("1. How did it feel to use the terminal?", plex_reg, PRIMARY, 500),
    ("2. Had you used a terminal before?", plex_reg, PRIMARY, 570),
    ("3. How will AI through the terminal", plex_reg, PRIMARY, 640),
    ("   change how you see AI?", plex_reg, PRIMARY, 700),
    ("", plex_reg, GRAY, 780),
    ("[ INSTRUCTOR: Insert Journey link / QR code ]", plex_sm, GRAY, 870),
], placeholder=True)

# S12 — Q&A / buffer
make_slide("s12_qa_buffer.png", [
    ("Q & A", plex_title, TERTIARY, 240),
    ("", plex_reg, GRAY, 360),
    ("Catch stragglers", plex_reg, GRAY, 440),
    ("Help with submissions", plex_reg, GRAY, 510),
    ("Preview next session", plex_reg, GRAY, 580),
    ("", plex_reg, GRAY, 660),
    ("You survived Day 1.", plex_sbold, GREEN, 770),
    ("", plex_reg, GRAY, 840),
    ("Great job.", plex_sbold, PRIMARY, 910),
])

print("\nDone — 12 slides generated.")
