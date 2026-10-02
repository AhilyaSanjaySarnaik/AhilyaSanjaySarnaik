#!/usr/bin/env python3
"""
crawler.py - a little web crawler that walks across your profile text and grabs
the [[links]] with its legs. Outputs a self-animating SVG (SMIL, no JavaScript),
which GitHub renders inside a README.

  python crawler.py                         # writes crawler-dark.svg + crawler-light.svg
  python crawler.py --frame 40 --out f.svg  # one static frame, for previewing

Edit TEXT below. Anything wrapped in [[double brackets]] becomes a link the
crawler can grab. Change SEED for a different walk.
"""
import argparse, html, math, random, re

# ------------------------------------------------------------------ edit me
TEXT = r"""
$ cat ~/about.txt                                                    @Ahi_Cyber
--------------------------------------------------------------------------------------
ahilya sarnaik :: [[security]] / [[ctf]] / [[web]] / [[AI]]
breaking things to learn how to defend them -> [[tryhackme]] rooms, notes, writeups
lately: [[web crawlers]], [[Common Crawl]] and how the [[open internet]] gets indexed
reading about [[AI security]] :: [[prompt injection]], [[data poisoning]], [[jailbreaks]]
toolbox :: [[python]] [[bash]] [[linux]] [[nmap]] [[burp suite]] [[wireshark]] [[git]]
ctf log :: [[picoCTF]] [[HackTheBox]] [[TryHackMe]] :: flags found > flags lost (mostly)
building -> [[YOUR_PROJECT]] :: [[YOUR_OTHER_PROJECT]]
reach me -> [[x.com/Ahi_Cyber]] / [[github.com/YOUR_USERNAME]] / [[YOUR_EMAIL]]
robots.txt ::  User-agent: *   Allow: [[/]]       crawlers welcome here
--------------------------------------------------------------------------------------
$ ./crawl --depth=1 --polite                                              [[200 OK]]
"""
SEED = 11
FPS = 15
DURATION = 16      # seconds per loop
STOPS = 8          # links visited per loop (the crawler pauses on each)
# -------------------------------------------------------------------------

FONT, LINE_H, CHAR_W = 13, 22, 7.8
PAD_X, PAD_TOP, PAD_BOTTOM = 30, 40, 26
SEG = 40                      # length of each of the two leg segments
REACH = 58                    # how far out the feet want to be
STEP_TRIGGER = 28
STEP_FRAMES = 4
LEG_ANGLES = [-38, -78, -116, -152, 38, 78, 116, 152]
GROUP_A = {0, 2, 5, 7}        # alternating gait: A steps, then B

THEMES = {
    "dark":  dict(bg="#0d1117", text="#5b636e", link="#8fc8ff", hl="#ff2e88",
                  leg="#3fd6ff", body="#f0f6fc", thread="#3fd6ff"),
    "light": dict(bg="#ffffff", text="#9aa3ad", link="#0550ae", hl="#e0207a",
                  leg="#0a84b0", body="#1f2328", thread="#0a84b0"),
}


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def ease(t):
    return t * t * (3 - 2 * t)


def layout(text):
    words, links = [], []
    lines = text.strip("\n").split("\n")
    maxlen = 0
    for row, raw in enumerate(lines):
        base = PAD_TOP + row * LINE_H
        plain, spans, pos = "", [], 0
        for m in re.finditer(r"\[\[(.+?)\]\]", raw):
            plain += raw[pos:m.start()]
            s = len(plain)
            plain += m.group(1)
            spans.append((s, len(plain), m.group(1)))
            pos = m.end()
        plain += raw[pos:]
        maxlen = max(maxlen, len(plain))
        owner = [None] * len(plain)
        for k, (a, b, _) in enumerate(spans):
            for i in range(a, b):
                owner[i] = len(links) + k
        i = 0
        while i < len(plain):
            if plain[i] == " ":
                i += 1
                continue
            j = i
            while j < len(plain) and plain[j] != " " and owner[j] == owner[i]:
                j += 1
            words.append(dict(x=PAD_X + i * CHAR_W, y=base, s=plain[i:j],
                              w=(j - i) * CHAR_W, link=owner[i] is not None))
            i = j
        for a, b, label in spans:
            x, w = PAD_X + a * CHAR_W, (b - a) * CHAR_W
            links.append(dict(x=x - 3, y=base - FONT + 1, w=w + 6, h=FONT + 6,
                              label=label, c=(x + w / 2, base - FONT / 2 + 2)))
    width = PAD_X * 2 + maxlen * CHAR_W
    height = PAD_TOP + (len(lines) - 1) * LINE_H + PAD_BOTTOM
    return words, links, width, height


def simulate(words, links, width, height, rng):
    n = round(FPS * DURATION)

    # --- route: hop between nearby links, then loop back to the start
    cur = rng.randrange(len(links))
    order, left = [cur], set(range(len(links))) - {cur}
    while len(order) < min(STOPS, len(links)):
        d = lambda k: dist(links[k]["c"], links[cur]["c"])
        mid = [k for k in left if 150 < d(k) < 420]
        cur = rng.choice(mid) if mid else min(left, key=d)
        order.append(cur)
        left.discard(cur)
    pts = [links[k]["c"] for k in order]
    m = len(pts)

    # --- timeline: [pause at stop i][travel to stop i+1], scaled to DURATION
    pause_w, segs = 0.9, []
    for i in range(m):
        segs.append((pause_w, 0.35 + dist(pts[i], pts[(i + 1) % m]) / 230))
    scale = DURATION / sum(p + t for p, t in segs)

    def cr(p0, p1, p2, p3, t):
        t2, t3 = t * t, t * t * t
        return tuple(0.5 * (2 * p1[k] + (p2[k] - p0[k]) * t
                            + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2
                            + (3 * p1[k] - p0[k] - 3 * p2[k] + p3[k]) * t3) for k in (0, 1))

    body, at_stop = [], []
    for f in range(n):
        t, acc = f / n * DURATION, 0.0
        for i, (p, tr) in enumerate(segs):
            p, tr = p * scale, tr * scale
            if t < acc + p:
                pos, stop = pts[i], order[i]
                break
            if t < acc + p + tr:
                u = ease((t - acc - p) / tr)
                pos = cr(pts[i - 1], pts[i], pts[(i + 1) % m], pts[(i + 2) % m], u)
                stop = None
                break
            acc += p + tr
        else:
            pos, stop = pts[0], order[0]
        wob = 2 * math.pi * f / n
        x = min(max(pos[0] + 2.0 * math.sin(wob * 5), 10), width - 10)
        y = min(max(pos[1] - 6 + 1.6 * math.cos(wob * 7), 10), height - 10)
        body.append((x, y))
        at_stop.append(stop)

    # --- legs: feet stick to words/links and step when they fall behind
    anchors = [(w["x"] + w["w"] / 2, w["y"] - 4, w["link"]) for w in words]

    def snap(p):
        best, score = p, 1e9
        for ax, ay, is_link in anchors:
            d = dist(p, (ax, ay))
            if d < 38:
                s = d - (14 if is_link else 0)
                if s < score:
                    best, score = (ax, ay), s
        return best

    heading = 0.0
    def ideal(f, leg):
        nonlocal heading
        a, b = body[(f - 1) % n], body[(f + 1) % n]
        vx, vy = (b[0] - a[0]) / 2, (b[1] - a[1]) / 2
        if math.hypot(vx, vy) > 0.35:
            heading = math.atan2(vy, vx)
        ang = heading + math.radians(LEG_ANGLES[leg])
        bx, by = body[f % n]
        return (bx + REACH * math.cos(ang) + vx * 4, by + REACH * math.sin(ang) + vy * 4)

    feet = [snap(ideal(0, i)) for i in range(8)]
    steps = [None] * 8                       # (from, to, k)
    glow = [0.0] * len(links)
    rec_feet, rec_glow = [], []
    for f in range(2 * n):                   # first loop is a warm-up
        targets = [ideal(f, i) for i in range(8)]
        for i in range(8):
            if steps[i]:
                a, b, k = steps[i]
                k += 1
                u = ease(k / STEP_FRAMES)
                feet[i] = (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)
                steps[i] = None if k >= STEP_FRAMES else (a, b, k)
        bpos = body[f % n]
        for i in sorted(range(8), key=lambda i: -dist(feet[i], targets[i])):
            if steps[i] or dist(feet[i], targets[i]) < STEP_TRIGGER:
                continue
            mine = (i in GROUP_A)
            blocked = any(steps[j] and ((j in GROUP_A) != mine) for j in range(8))
            if blocked and dist(feet[i], bpos) < SEG * 2 * 0.97:
                continue
            steps[i] = (feet[i], snap(targets[i]), 0)
        for k, L in enumerate(links):
            hit = any(L["x"] - 5 <= fx <= L["x"] + L["w"] + 5 and
                      L["y"] - 5 <= fy <= L["y"] + L["h"] + 5 for fx, fy in feet)
            hit = hit or at_stop[f % n] == k
            glow[k] = max(1.0 if hit else 0.0, glow[k] * 0.78)
        if f >= n:
            rec_feet.append(list(feet))
            rec_glow.append(list(glow))

    # smooth the seam so the loop restarts without a jump
    B = 6
    for f in range(n - B, n):
        u = ease((f - (n - B) + 1) / B)
        rec_feet[f] = [(a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)
                       for a, b in zip(rec_feet[f], rec_feet[0])]
        rec_glow[f] = [a + (b - a) * u for a, b in zip(rec_glow[f], rec_glow[0])]

    return dict(n=n, body=body, feet=rec_feet, glow=rec_glow, at_stop=at_stop, order=order)


def knee(b, foot, side):
    d = dist(b, foot)
    mx, my = (b[0] + foot[0]) / 2, (b[1] + foot[1]) / 2
    h = math.sqrt(max(0.0, SEG * SEG - (d / 2) ** 2))
    if d < 1e-6:
        return mx, my - SEG
    px, py = -(foot[1] - b[1]) / d, (foot[0] - b[0]) / d
    return mx + px * h * side, my + py * h * side


def render(theme, frame=None, text=TEXT, seed=SEED):
    c = THEMES[theme]
    words, links, W, H = layout(text)
    S = simulate(words, links, W, H, random.Random(seed))
    n = S["n"]
    F = list(range(n)) + [0]                       # close the loop
    sel = frame % n if frame is not None else 0
    dur = f"{DURATION}s"
    num = lambda v: f"{v:.1f}".rstrip("0").rstrip(".")

    def anim(attr, vals, extra=""):
        if frame is not None:
            return ""
        return (f'<animate attributeName="{attr}" dur="{dur}" repeatCount="indefinite" '
                f'calcMode="linear" values="{";".join(vals)}"{extra}/>')

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {num(W)} {num(H)}" '
           f'width="{num(W)}" height="{num(H)}" font-family="ui-monospace,SFMono-Regular,'
           f'Menlo,Consolas,\'Liberation Mono\',monospace" font-size="{FONT}">',
           f'<rect width="100%" height="100%" rx="10" fill="{c["bg"]}"/>']

    # link highlights
    for k, L in enumerate(links):
        g = [num(S["glow"][f][k] * 0.9) for f in F]
        out.append(f'<rect x="{num(L["x"])}" y="{num(L["y"])}" width="{num(L["w"])}" '
                   f'height="{num(L["h"])}" rx="2" fill="{c["hl"]}" fill-opacity="0.22" '
                   f'stroke="{c["hl"]}" stroke-width="1" opacity="{g[sel]}">{anim("opacity", g)}</rect>')

    # text
    for w in words:
        col = c["link"] if w["link"] else c["text"]
        out.append(f'<text x="{num(w["x"])}" y="{w["y"]}" fill="{col}" '
                   f'textLength="{num(w["w"])}" lengthAdjust="spacingAndGlyphs">'
                   f'{html.escape(w["s"])}</text>')

    # threads from the body to nearby links
    for k, L in enumerate(links):
        op = []
        for f in F:
            d = dist(S["body"][f], L["c"])
            op.append(num(0.5 * max(0.0, 1 - d / 165) ** 1.5) if d < 165 else "0")
        if all(o == "0" for o in op):
            continue
        bx = [num(S["body"][f][0]) for f in F]
        by = [num(S["body"][f][1]) for f in F]
        out.append(f'<line x1="{bx[sel]}" y1="{by[sel]}" x2="{num(L["c"][0])}" y2="{num(L["c"][1])}" '
                   f'stroke="{c["thread"]}" stroke-width="0.7" opacity="{op[sel]}">'
                   f'{anim("x1", bx)}{anim("y1", by)}{anim("opacity", op)}</line>')

    # legs
    for i in range(8):
        side = -1 if LEG_ANGLES[i] < 0 else 1
        pts, fx, fy = [], [], []
        for f in F:
            b, ft = S["body"][f], S["feet"][f][i]
            kx, ky = knee(b, ft, side)
            pts.append(f"{num(b[0])},{num(b[1])} {num(kx)},{num(ky)} {num(ft[0])},{num(ft[1])}")
            fx.append(num(ft[0]))
            fy.append(num(ft[1]))
        out.append(f'<polyline points="{pts[sel]}" fill="none" stroke="{c["leg"]}" '
                   f'stroke-width="1.4" stroke-linejoin="round">{anim("points", pts)}</polyline>')
        out.append(f'<circle cx="{fx[sel]}" cy="{fy[sel]}" r="2.4" fill="{c["leg"]}">'
                   f'{anim("cx", fx)}{anim("cy", fy)}</circle>')

    # body
    tr = [f"{num(S['body'][f][0])} {num(S['body'][f][1])}" for f in F]
    move = ("" if frame is not None else
            f'<animateTransform attributeName="transform" type="translate" dur="{dur}" '
            f'repeatCount="indefinite" values="{";".join(tr)}"/>')
    spin = ("" if frame is not None else
            '<animateTransform attributeName="transform" type="rotate" from="0" to="360" '
            'dur="5s" repeatCount="indefinite"/>')
    out.append(f'<g transform="translate({tr[sel]})">{move}'
               f'<g>{spin}<circle r="13" fill="none" stroke="{c["hl"]}" stroke-width="1" '
               f'stroke-dasharray="3 5" opacity="0.8"/></g>'
               f'<circle r="7.5" fill="{c["bg"]}" stroke="{c["leg"]}" stroke-width="1.2"/>'
               f'<circle r="3.6" fill="{c["body"]}"/></g>')

    # big label of the link being "fetched" at each stop
    for k in dict.fromkeys(S["order"]):
        L = links[k]
        raw = [1.0 if S["at_stop"][f] == k else 0.0 for f in range(n)]
        sm = [max(raw[(f + d) % n] * (1 - abs(d) / 4) for d in range(-3, 4)) for f in range(n)]
        op = [num(sm[f]) for f in F]
        x = min(L["c"][0] + 16, W - 12 - len(L["label"]) * 11)
        y = max(L["c"][1] - 22, 24)
        out.append(f'<text x="{num(x)}" y="{num(y)}" font-size="18" font-weight="700" '
                   f'fill="{c["hl"]}" stroke="{c["bg"]}" stroke-width="4" paint-order="stroke" '
                   f'opacity="{op[sel]}">{html.escape(L["label"])}{anim("opacity", op)}</text>')

    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--theme", choices=THEMES, default=None)
    ap.add_argument("--frame", type=int, default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--seed", type=int, default=SEED)
    a = ap.parse_args()
    themes = [a.theme] if a.theme else list(THEMES)
    for t in themes:
        path = a.out if (a.out and len(themes) == 1) else f"crawler-{t}.svg"
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(t, a.frame, seed=a.seed))
        print("wrote", path)
