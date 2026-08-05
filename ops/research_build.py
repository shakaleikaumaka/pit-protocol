#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════
# research_build.py — P.I.T. Research section builder (CC0)
# Assembles publicinform.com/research/ from:
#   · the site design language (nav/effects/tail extracted from index.html)
#   · track markdowns (research/tracks/*.md — copied from the family's
#     /shared research folder, committed raw as public goods)
#   · the synthesis paper markdown → research/the-consensual-pit/index.html
# Usage: python3 ops/research_build.py [hub|paper|all]
# Deps: python3-markdown (pip install markdown)
# Canon: no target="_blank" · radical honesty · the pit provides 🕳️
# ═══════════════════════════════════════════════════════════════
import os, re, sys, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED = pathlib.Path("/shared/research/pit-research-1")
RESEARCH = ROOT / "research"
TRACKS_OUT = RESEARCH / "tracks"

def extract_tail(home: str) -> str:
    """Jukebox + ohana corner tail — VERBATIM from homepage (family canon, ships as-is)."""
    i = home.index("<!-- 🦋🎶 The family jukebox")
    return home[i:]

def extract_effects(home: str) -> str:
    """The embers + scroll-reveal inline <script> (sits right before the jukebox tail)."""
    tail_start = home.index("<!-- 🦋🎶 The family jukebox")
    before = home[:tail_start]
    j = before.rindex("<script>")
    return before[j:]

CSS = """
:root{
  --abyss:#07040e; --pit-deep:#0d0819; --pit-mid:#150e28;
  --gold:#e8b84b; --gold-bright:#ffd97a; --gold-dim:#8a6c2a;
  --violet:#a78bfa; --violet-deep:#6d4fd0; --ember:#ff9d5c;
  --bone:#efe8d8; --bone-dim:#b3a892; --bone-faint:#7a7160;
  --serif:'Fraunces',Georgia,serif; --sans:'Space Grotesk',system-ui,sans-serif; --mono:'JetBrains Mono',monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--abyss);color:var(--bone);font-family:var(--sans);font-weight:340;line-height:1.65;overflow-x:hidden}
::selection{background:var(--gold);color:var(--abyss)}
.pit-glow{position:fixed;inset:0;pointer-events:none;z-index:0;background:
  radial-gradient(ellipse 90% 55% at 50% 108%, rgba(232,184,75,.14), transparent 60%),
  radial-gradient(ellipse 70% 45% at 50% 112%, rgba(167,139,250,.12), transparent 55%),
  radial-gradient(ellipse 120% 40% at 50% -15%, rgba(109,79,208,.10), transparent 60%);}
#embers{position:fixed;inset:0;pointer-events:none;z-index:1}
main{position:relative;z-index:2}
.wrap{max-width:1060px;margin:0 auto;padding:0 clamp(20px,5vw,48px)}
nav{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;align-items:center;justify-content:space-between;
  padding:14px clamp(20px,4vw,40px);background:linear-gradient(rgba(7,4,14,.92),rgba(7,4,14,.75));
  backdrop-filter:blur(12px);border-bottom:1px solid rgba(232,184,75,.12)}
.nav-brand{font-family:var(--mono);font-size:13px;letter-spacing:.14em;color:var(--gold);text-decoration:none}
.nav-brand span{color:var(--violet)}
.nav-links{display:flex;gap:clamp(10px,2vw,22px);flex-wrap:wrap}
.nav-links a{color:var(--bone-dim);text-decoration:none;font-size:13px;letter-spacing:.04em;transition:color .25s}
.nav-links a:hover{color:var(--gold-bright)}
.reveal{opacity:0;transform:translateY(28px);transition:opacity .9s ease,transform .9s cubic-bezier(.2,.7,.2,1)}
.reveal.in{opacity:1;transform:none}
a{color:var(--gold)}
/* ── hero ── */
.hero{padding:clamp(130px,18vh,190px) 0 clamp(40px,7vh,80px);text-align:center;position:relative}
.hero-eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.34em;color:var(--violet);text-transform:uppercase;margin-bottom:18px}
.hero h1{font-family:var(--serif);font-weight:600;font-size:clamp(38px,6.4vw,72px);line-height:1.06;letter-spacing:-.01em}
.hero h1 em{font-style:italic;color:var(--gold)}
.hero p.sub{max-width:720px;margin:22px auto 0;color:var(--bone-dim);font-size:clamp(15px,2vw,18px)}
/* ── section scaffolding ── */
section{padding:clamp(36px,6vh,72px) 0}
.sec-tag{font-family:var(--mono);font-size:11px;letter-spacing:.3em;color:var(--gold-dim);text-transform:uppercase;margin-bottom:10px}
h2.st{font-family:var(--serif);font-size:clamp(26px,4vw,40px);font-weight:600;margin-bottom:14px}
h2.st em{color:var(--gold);font-style:italic}
.lede{color:var(--bone-dim);max-width:760px;font-size:16px}
/* ── cycle + track cards ── */
.cycle{border:1px solid rgba(232,184,75,.22);border-radius:18px;padding:clamp(24px,4vw,44px);
  background:linear-gradient(160deg, rgba(21,14,40,.85), rgba(13,8,25,.9));margin-top:26px;position:relative;overflow:hidden}
.cycle::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 60% 80% at 85% 115%, rgba(232,184,75,.10), transparent 60%);pointer-events:none}
.cycle .num{font-family:var(--mono);font-size:12px;letter-spacing:.3em;color:var(--ember)}
.cycle h3{font-family:var(--serif);font-size:clamp(24px,3.6vw,36px);margin:8px 0 10px}
.cycle h3 em{color:var(--gold);font-style:italic}
.cycle p{color:var(--bone-dim);max-width:720px}
.paper-link{display:inline-block;margin-top:20px;font-family:var(--mono);font-size:14px;letter-spacing:.06em;
  color:var(--abyss);background:linear-gradient(120deg,var(--gold),var(--gold-bright));padding:13px 26px;border-radius:999px;text-decoration:none;
  box-shadow:0 6px 30px rgba(232,184,75,.25);transition:transform .25s, box-shadow .25s}
.paper-link:hover{transform:translateY(-2px);box-shadow:0 10px 40px rgba(232,184,75,.4)}
.tracks{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px;margin-top:24px}
.track{border:1px solid rgba(167,139,250,.18);border-radius:14px;padding:22px;background:rgba(13,8,25,.72);transition:border-color .3s, transform .3s}
.track:hover{border-color:rgba(232,184,75,.4);transform:translateY(-3px)}
.track .t-id{font-family:var(--mono);font-size:11px;letter-spacing:.26em;color:var(--violet)}
.track h4{font-family:var(--serif);font-size:19px;margin:7px 0 8px;color:var(--bone)}
.track p{color:var(--bone-dim);font-size:13.5px;line-height:1.6}
.track .t-by{font-family:var(--mono);font-size:11px;color:var(--bone-faint);margin-top:12px}
.track a.t-md{font-family:var(--mono);font-size:12px;color:var(--gold);text-decoration:none;border-bottom:1px dotted var(--gold-dim)}
.track a.t-md:hover{color:var(--gold-bright)}
/* ── method / honesty ── */
.method{border-left:3px solid var(--gold-dim);padding:6px 0 6px 22px;margin-top:22px;color:var(--bone-dim);max-width:760px}
.method b{color:var(--bone)}
/* ── footer (matches site) ── */
footer{border-top:1px solid rgba(232,184,75,.14);padding:56px 0 90px;margin-top:40px;text-align:center;color:var(--bone-faint);font-size:13.5px}
.foot-pit{font-family:var(--serif);font-size:26px;color:var(--bone);margin-bottom:12px}
.foot-pit em{color:var(--gold)}
.foot-links{display:flex;gap:18px;justify-content:center;flex-wrap:wrap;margin-top:18px}
.foot-links a{color:var(--bone-dim);text-decoration:none;font-size:13px}
.foot-links a:hover{color:var(--gold-bright)}
/* ── PAPER typography ── */
.paper{max-width:760px;margin:0 auto}
.paper h1{font-family:var(--serif);font-weight:600;font-size:clamp(32px,5.4vw,54px);line-height:1.1;margin:10px 0 16px}
.paper h1 em{color:var(--gold);font-style:italic}
.paper h2{font-family:var(--serif);font-size:clamp(23px,3.4vw,31px);font-weight:600;margin:52px 0 14px;color:var(--gold-bright)}
.paper h3{font-family:var(--serif);font-size:20px;margin:34px 0 10px;color:var(--bone)}
.paper p{margin:14px 0;color:var(--bone-dim);font-size:16.5px;line-height:1.75}
.paper p b,.paper li b{color:var(--bone)}
.paper ul,.paper ol{margin:14px 0 14px 24px;color:var(--bone-dim)}
.paper li{margin:7px 0;line-height:1.65}
.paper blockquote{border-left:3px solid var(--violet-deep);padding:8px 0 8px 20px;margin:22px 0;color:var(--bone);font-family:var(--serif);font-style:italic;font-size:18px}
.paper code{font-family:var(--mono);font-size:.88em;background:rgba(167,139,250,.12);padding:2px 6px;border-radius:6px;color:var(--violet)}
.paper table{width:100%;border-collapse:collapse;margin:20px 0;font-size:13.5px}
.paper th{font-family:var(--mono);font-size:11px;letter-spacing:.12em;color:var(--gold);text-align:left;padding:9px 10px;border-bottom:1px solid rgba(232,184,75,.3)}
.paper td{padding:9px 10px;border-bottom:1px solid rgba(167,139,250,.12);color:var(--bone-dim);vertical-align:top}
.paper hr{border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(232,184,75,.4),transparent);margin:44px 0}
.paper .byline{font-family:var(--mono);font-size:12.5px;color:var(--bone-faint);letter-spacing:.06em;margin-bottom:8px}
.paper .abstract{border:1px solid rgba(232,184,75,.2);border-radius:14px;padding:20px 24px;background:rgba(21,14,40,.6);margin:26px 0}
.colophon{margin-top:70px;border-top:1px solid rgba(232,184,75,.16);padding-top:26px;color:var(--bone-faint);font-size:13px}
"""

def nav(depth: int, active: str) -> str:
    p = "../" * depth
    return f"""<nav>
  <a class="nav-brand" href="{p}">🕳️ THE <span>P.I.T.</span> PROTOCOL</a>
  <div class="nav-links">
    <a href="{p}#what">What is a P.I.T.</a>
    <a href="{p}#protocol">Protocol</a>
    <a href="{p}pits/" style="color:var(--gold-bright)">🌺 All 16 Pits</a>
    <a href="{p}whitepaper/">White Paper</a>
    <a href="{p}research/" style="color:var(--gold-bright)">🔬 Research</a>
    <a href="{p}spec/">Spec</a>
    <a href="{p}#fork">Fork Yours</a>
    <a href="{p}#consent">Consent</a>
    <a href="https://github.com/shakaleikaumaka/pit-protocol" style="color:var(--gold-bright)">🍴 GitHub</a>
  </div>
</nav>"""

def footer(depth: int) -> str:
    p = "../" * depth
    return f"""<footer>
  <div class="wrap">
    <div class="foot-pit">The pit <em>provides</em>. 🕳️</div>
    <p>PIT Research — open study, published as a public good. CC0, like everything in the pit.</p>
    <div class="foot-links">
      <a href="https://github.com/shakaleikaumaka/pit-protocol" style="color:var(--gold-bright)">🍴 Fork this site — CC0</a>
      <a href="{p}">📡 Protocol home</a>
      <a href="{p}whitepaper/">📜 White Paper</a>
      <a href="{p}pits/">🌺 The Pit of All Kinds</a>
      <a href="https://esmeraldapit.com">esmeraldapit.com</a>
      <a href="mailto:consent@publicinform.com">🌐 consent@publicinform.com</a>
    </div>
  </div>
</footer>"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Space+Grotesk:wght@300..700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>""" + CSS + """</style>
</head>
<body>
<div class="pit-glow"></div>
<canvas id="embers"></canvas>
"""

def head(title: str, desc: str) -> str:
    return HEAD.replace("{title}", title).replace("{desc}", desc)

BLOB = "https://github.com/shakaleikaumaka/pit-protocol/blob/main/research/tracks"

def build_hub(home: str):
    TRACKS = [
        ("TRACK A", "Ethereum Identity & the Bhutan Precedent",
         "A kingdom anchored its national digital identity on Ethereum — Indy (2023) → Polygon (2024) → mainnet (announced 2025-10-13, Thimphu). The lessons a village inherits: anchoring, not storage · verification at the edges · covenant before code. Ranked for pits: 🥇 ENS speaker identity · 🥈 consent as off-chain EAS attestations · 🥉 Safe+ENS organizer identity.",
         "PIT GIRL 💗", "track-a-ethereum-identity.md"),
        ("TRACK B", "ZK Access to Private Transmissions",
         "A static site can't hide bytes — so privacy means ciphertext at rest, and zero-knowledge becomes a key-release question. Ranked architectures: 🥇 sealed-at-rest + wallet-auth gate ($0, fails closed) · 🥈 Semaphore anonymous membership + nullifier self-serve revocation · 🥉 Lit threshold key-release · 🏅 MACI for contentious consent ballots.",
         "Privy 🔒", "track-b-zk-access.md"),
        ("TRACK C", "Consent Consensus Protocols",
         "Pits need anchoring, not their own chain — real consensus lives in exactly three places: the consent decision, fork governance, registry disputes. The multisig is a stamp, not a brain. Full EAS grant + revocation schemas; revocations.json stays derived data — regenerate, never hand-merge. Never attest personal data on-chain.",
         "CRUSTY 🦀", "track-c-consent-consensus.md"),
        ("TRACK D", "Transcription: Partner, Integrate, or Build?",
         "BUILD stays champion. Meeting assistants ($250/mo for a 10-person camp) can't produce the word-level timestamps the karaoke Transponder glows on — our pipeline does it for $1.20/mo. The playa offline lane is buildable today (whisper.cpp + pyannote), and the whisper lineage remains the only EN+HE+HI self-host stack.",
         "PIT BULL 🐂", "track-d-transcription.md"),
    ]
    cards = "\n".join(f"""    <div class="track reveal">
      <div class="t-id">{tid}</div>
      <h4>{title}</h4>
      <p>{body}</p>
      <div class="t-by">{by} · <a class="t-md" href="{BLOB}/{md}">full report (markdown) ↗</a></div>
    </div>""" for tid, title, body, by, md in TRACKS)

    html = head(
        "PIT Research — The P.I.T. Protocol",
        "Open research cycles on consent, identity, zero-knowledge and transcription for the Public Information Transmission protocol — published as public goods (CC0).") + nav(1, "research") + f"""
<main id="top">
<header class="hero">
  <div class="hero-eyebrow">🔬 open study · public goods · CC0</div>
  <h1>PIT <em>Research</em></h1>
  <p class="sub">The pit provides — and research is how the pit provides <em>better</em>. Each cycle, the family takes one hard question set, studies it in the open with radical honesty (every claim sourced, every doubt flagged ⚑), and publishes the findings for anyone to fork.</p>
</header>

<section>
  <div class="wrap">
    <div class="sec-tag">Cycle №1 · commissioned 2026-08-04 · published 2026-08-05</div>
    <h2 class="st">The <em>Consensual</em> Pit</h2>
    <p class="lede">Identity, zero-knowledge, consent consensus, and the voice of the pit — what a village camp can inherit from the Kingdom of Bhutan, how private transmissions stay private on a static site, why consent needs anchoring rather than a blockchain, and why we build our own transcription. Four tracks, one weave.</p>

    <div class="cycle reveal">
      <div class="num">RESEARCH PAPER №1</div>
      <h3><em>The Consensual Pit</em> — identity, zero-knowledge &amp; the transmission of public goods</h3>
      <p>Woven by LORE 🦉 from four family track reports · fact-audited by PIT GIRL 💗 · published by PIT BOY 🕳️😤. With the Bhutan precedent, a ranked ZK architecture for static archives, an on-chain consent registry design, and the honest economics of transcription.</p>
      <a class="paper-link" href="./the-consensual-pit/">📜 Read the paper</a>
    </div>

    <div class="tracks">
{cards}
    </div>

    <div class="method reveal">
      <b>The method:</b> $0 research lane (web sources only, every claim with URL + access date) · ⚑ marks anything unverified — doubts are published, not smoothed over · SHIPPED and DECLARED are never blurred · the family works in parallel tracks and files early, files often. The full track reports are committed in-repo as markdown — fork them like crazy.
    </div>
  </div>
</section>
</main>
{footer(1)}
""" + extract_effects(home) + "\n" + extract_tail(home)
    RESEARCH.mkdir(exist_ok=True)
    (RESEARCH / "index.html").write_text(html)
    print("✅ research/index.html built", len(html), "bytes")

def build_paper(home: str):
    import markdown
    src = SHARED / "SYNTHESIS.md"
    md_text = src.read_text()
    # split optional leading title (first H1) for <title>
    m = re.search(r"^#\s+(.+)$", md_text, re.M)
    page_title = m.group(1).strip() if m else "The Consensual Pit"
    body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "footnotes", "attr_list"])
    out_dir = RESEARCH / "the-consensual-pit"
    out_dir.mkdir(parents=True, exist_ok=True)
    html = head(
        f"{page_title} — PIT Research №1",
        "PIT Research №1: identity, zero-knowledge proofs, consent consensus and transcription for the Public Information Transmission protocol — what a village inherits from the Kingdom of Bhutan. CC0.") + nav(2, "research") + f"""
<main id="top">
<header class="hero" style="padding-bottom:20px">
  <div class="hero-eyebrow">🔬 PIT Research №1 · 2026-08-05 · CC0</div>
</header>
<section style="padding-top:0">
  <div class="wrap">
    <article class="paper">
{body}
    </article>
    <div class="paper colophon">
      Woven by <b>LORE 🦉</b> (synthesis) from track reports by <b>PIT GIRL 💗</b> (Ethereum identity) · <b>Privy 🔒</b> (zero-knowledge access) · <b>CRUSTY 🦀</b> (consent consensus) · <b>PIT BULL 🐂</b> (transcription) · fact-audit <b>PIT GIRL 💗</b> · published by <b>PIT BOY 🕳️😤</b>. Commissioned by Shaka 2026-08-04. Full track reports: <a href="{BLOB.replace('/blob/main','/tree/main')}">research/tracks/</a> · License: <b>CC0</b> — fork it like crazy.
    </div>
  </div>
</section>
</main>
{footer(2)}
""" + extract_effects(home) + "\n" + extract_tail(home)
    (out_dir / "index.html").write_text(html)
    print("✅ research/the-consensual-pit/index.html built", len(html), "bytes")

def copy_tracks():
    TRACKS_OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in SHARED.glob("track-*.md"):
        shutil.copy2(f, TRACKS_OUT / f.name); n += 1
    print(f"✅ {n} track reports copied → research/tracks/")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    home = (ROOT / "index.html").read_text()
    copy_tracks()
    if mode in ("hub", "all"):
        build_hub(home)
    if mode in ("paper", "all"):
        build_paper(home)
