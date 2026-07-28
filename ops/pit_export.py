#!/usr/bin/env python3
"""
pit_export.py — P.I.T. Manifest Generator v0.1 🕳️
Public Information Transmission Protocol — CC0 (no rights reserved)

Generates pit.json + pit.yaml (PIT-MANIFEST/0.1) at a pit repo's root,
from its data/catalog.json. One manifest = one portable pit: identity,
sessions, transcript/audio/Drive pointers, consent metadata, LLM hints.
"Anyone can import a pit into their AI and talk to the pit." — Siri's seed

Usage:
  python3 pit_export.py --slug zuitzpit --repo /path/to/clone [--push]
  python3 pit_export.py --hub /path/to/pit-protocol   # emits pits.json registry
"""
import json, sys, os, argparse, datetime, subprocess

SPEC = "pit-manifest/0.1"
HUB = "https://publicinform.com"
R = "https://github.com/shakaleikaumaka"
P = "https://shakaleikaumaka.github.io"

# THE REGISTRY — single source of truth for the constellation.
# (hub pits.json + every per-pit manifest derive from this)
REGISTRY = {
  "esmeraldapit": dict(
    name="The Esmeralda P.I.T.", registry_number=1, generation=0,
    url="https://esmeraldapit.com", repo=f"{R}/esmeralda-pit", forked_from=None,
    event="Edge Esmeralda", location="Healdsburg, California", dates="2026 (28 days)",
    tagline="The genesis pit — 149 sessions, 122 hours, 138 synced transcripts",
    status="live", consent="consent-first · organizer-blessed demo archive",
    lane="private-jai"),
  "osopit": dict(
    name="OSO P.I.T.", registry_number=2, generation=0,
    url="https://publicinform.com/osopit/", repo="https://github.com/opensource-orchestra/osopit",
    forked_from=None, event="ETHGlobal Delhi hackathon", location="Delhi, India", dates="2025",
    tagline="The ancestor — where the pit first got its name (Most Creative Use of ENS)",
    status="ancestor", consent="historical exhibit", lane=None),
  "zuitzpit": dict(
    name="The ZuitzPIT", registry_number=3, generation=1,
    url=f"{P}/zuitzpit/", repo=f"{R}/zuitzpit", forked_from=f"{R}/esmeralda-pit",
    event="Zuitzerland residency", location="Swiss Alps", dates="May 2025",
    tagline="700 years of Swiss democracy, transmitted — the first fork",
    status="live", consent="demo · links to source Drive, nothing re-hosted beyond audio", lane="pit-crew"),
  "patagoniapit": dict(
    name="The PatagoniaPIT", registry_number=4, generation=2,
    url=f"{P}/patagoniapit/", repo=f"{R}/patagoniapit", forked_from=f"{R}/zuitzpit",
    event="Edge City Patagonia", location="Andes, Argentina", dates="Oct 18 – Nov 15, 2025",
    tagline="The second fork — four weeks on the lake", status="live",
    consent="demo · links to source Drive", lane="pit-crew"),
  "4seaspit": dict(
    name="The 4SeasPIT", registry_number=5, generation=2,
    url=f"{P}/4seaspit/", repo=f"{R}/4seaspit", forked_from=f"{R}/zuitzpit",
    event="ETHChiangmai × 4Seas", location="Chiang Mai, Thailand", dates="Dec 8, 2025 – Feb 3, 2026",
    tagline="The third fork — lanterns over the moat", status="live",
    consent="demo · links to source Drive", lane="pit-crew"),
  "praguepit": dict(
    name="The PraguePIT", registry_number=6, generation=2,
    url=f"{P}/praguepit/", repo=f"{R}/praguepit", forked_from=f"{R}/zuitzpit",
    event="ETHPrague 2026 · Masaryk Stage", location="Prague, Czechia", dates="2026",
    tagline="The fourth fork — recorded by Shaka himself", status="live",
    consent="demo · links to source Drive", lane="pit-crew"),
  "zuberlinpit": dict(
    name="The ZuBerPit", registry_number=7, generation=2,
    url=f"{P}/zuberlinpit/", repo=f"{R}/zuberlinpit", forked_from=f"{R}/zuitzpit",
    event="ZuBerlin 2025 · Futura Garden", location="Berlin, Germany (rooftop)", dates="2025",
    tagline="The fifth fork — über swagger, one legendary squirrel", status="live",
    consent="demo · links to source Drive", lane="pit-crew"),
  "kaspit": dict(
    name="The KasPIT", registry_number=8, generation=2,
    url=f"{P}/kaspit/", repo=f"{R}/kaspit", forked_from=f"{R}/zuitzpit",
    event="ZuKas 2025", location="Kaş, Türkiye", dates="2025",
    tagline="The sixth fork — Vitalik remote, Bauwens ×3, one sea turtle 🐢", status="live",
    consent="demo · links to source Drive", lane="pit-crew"),
  "vitpit": dict(
    name="The VitPit", registry_number=9, generation=3,
    url=f"{P}/vitpit/", repo=f"{R}/vitpit", forked_from=f"{R}/zuitzpit",
    event="Celebrating Vitalik Buterin", location="the ether", dates="ongoing",
    tagline="The seventh fork but the ninth P.I.T. — the pit that asks first", status="live",
    consent="consent-first made manifest · no further content without explicit consent", lane="pit-crew"),
  "goapit": dict(
    name="The Goa P.I.T.", registry_number=10, generation=None,
    url=None, repo=None, forked_from=None,
    event="Goa gathering", location="Goa, India", dates="Oct 2026 (declared)",
    tagline="Up next — forming", status="forming", consent="pending", lane=None),
  "devconpit": dict(
    name="The Devcon P.I.T.", registry_number=11, generation=None,
    url=None, repo=None, forked_from=None,
    event="Devcon 8", location="Jio World Centre, Mumbai, India", dates="Nov 3–6, 2026 (declared)",
    tagline="Declared — the pit of all kinds", status="declared", consent="pending", lane=None),
}

def parse_dur(d):
    """'HH:MM:SS' or 'MM:SS' -> seconds (int) or None"""
    if not d: return None
    try:
        p = [int(x) for x in str(d).split(":")]
        if len(p) == 3: return p[0]*3600 + p[1]*60 + p[2]
        if len(p) == 2: return p[0]*60 + p[1]
    except ValueError: pass
    return None

def session_entry(s, base):
    mid = s.get("id")
    m0 = (s.get("media") or [{}])[0]
    media = {}
    if m0.get("id"):
        media["drive"] = f"https://drive.google.com/file/d/{m0['id']}/view"
    if m0.get("hosted"):
        media["audio"] = m0["hosted"]
    if m0.get("kind"): media["kind"] = m0["kind"]
    if m0.get("size"): media["bytes"] = m0["size"]
    e = {
        "id": mid,
        "title": s.get("title"),
        "date": s.get("date"),
        "speakers": s.get("speakers") or [],
        "duration": s.get("duration"),
        "duration_seconds": parse_dur(s.get("duration")),
        "media": media or None,
        "transcript": f"{base}transcripts/{s['transcript']}.txt" if s.get("transcript") else None,
        "transcript_format": "pit-transcript/1 · plain text, [MM:SS] timestamps" if s.get("transcript") else None,
        "summary": s.get("summary"),      # digest layer lands here (seed 3)
        "digest": s.get("digest"),
        "note": s.get("note"),
    }
    return {k: v for k, v in e.items() if v not in (None, [], {})}

def build_manifest(slug, repo_path):
    meta = REGISTRY[slug]
    cat = json.load(open(os.path.join(repo_path, "data", "catalog.json")))
    base = meta["url"]
    sessions = [session_entry(s, base) for s in cat]
    n_tx = sum(1 for s in cat if s.get("transcript"))
    secs = sum(parse_dur(s.get("duration")) or 0 for s in cat)
    # source drive folders — best-effort from pipeline config / first media id provenance
    src = []
    for cand in ("pipeline/config.json", "data/source.json"):
        p = os.path.join(repo_path, cand)
        if os.path.exists(p):
            try:
                cfg = json.load(open(p))
                fid = cfg.get("folder_id") or cfg.get("drive_folder")
                if fid:
                    src.append({"type": "google-drive-folder", "id": fid,
                                "url": f"https://drive.google.com/drive/folders/{fid}"})
            except Exception: pass
    if not src:
        src.append({"type": "google-drive-folder",
                    "note": "source folder id recorded in the pit's pipeline — see repository"})
    return {
        "spec": SPEC,
        "pit": {
            "name": meta["name"], "slug": slug, "registry_number": meta["registry_number"],
            "url": base, "repository": meta["repo"], "forked_from": meta["forked_from"],
            "generation": meta["generation"], "event": meta["event"],
            "location": meta["location"], "dates": meta["dates"], "tagline": meta["tagline"],
            "status": meta["status"],
        },
        "license": "CC0-1.0 · no rights reserved · fork it",
        "consent": {
            "policy": "consent-first",
            "status": meta["consent"],
            "policy_url": f"{HUB}/whitepaper/#consent",
        },
        "source": src,
        "counts": {
            "sessions": len(cat), "transcripts": n_tx,
            "seconds": secs or None, "hours": round(secs/3600, 1) if secs else None,
        },
        "sessions": sessions,
        "llm": {
            "hint": ("To talk to this pit: read this manifest, then fetch any session's "
                     "'transcript' URL (plain text, [MM:SS] timestamps). Quote with timestamps. "
                     "Audio pointers are 64k mp3 on Cloudflare R2; 'drive' is the original video. "
                     "Honor the consent block — this knowledge is transmitted, not taken."),
            "transcript_search_index": f"{base}data/search-index.json",
            "catalog": f"{base}data/catalog.json",
        },
        "hub": HUB,
        "registry": f"{HUB}/pits.json",
        "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "pit_export.py v0.1 · PIT BOY 🕳️😤",
    }

# --- tiny YAML emitter (structure-known, dependency-free; container-safe) ---
def yaml_escape(s):
    if s is None: return "null"
    s = str(s)
    if s == "" or any(c in s for c in ":#{}[]&,*?|-<>=!%@`\"'") or s != s.strip() \
       or s.lower() in ("null","true","false","yes","no","on","off") or "\n" in s:
        return json.dumps(s, ensure_ascii=False)
    return s

def to_yaml(obj, ind=0):
    pad = "  " * ind
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and v:
                out.append(f"{pad}{k}:")
                out.append(to_yaml(v, ind+1))
            elif v == {} or v == []:
                out.append(f"{pad}{k}: {'{}' if v=={} else '[]'}")
            else:
                out.append(f"{pad}{k}: {yaml_escape(v)}")
    elif isinstance(obj, list):
        for v in obj:
            if isinstance(v, dict) and v:
                first = True
                for k, vv in v.items():
                    pre = f"{pad}- " if first else f"{pad}  "
                    if isinstance(vv, (dict, list)) and vv:
                        out.append(f"{pre}{k}:")
                        out.append(to_yaml(vv, ind+2))
                    else:
                        out.append(f"{pre}{k}: {yaml_escape(vv)}")
                    first = False
            elif isinstance(v, (dict, list)):
                out.append(f"{pad}-"); out.append(to_yaml(v, ind+1))
            else:
                out.append(f"{pad}- {yaml_escape(v)}")
    return "\n".join(out)

def hub_registry(out_dir):
    """pits.json — the constellation map. Finding one pit leads to all pits."""
    pits = []
    for slug, m in sorted(REGISTRY.items(), key=lambda kv: kv[1]["registry_number"]):
        e = {"slug": slug, "name": m["name"], "registry_number": m["registry_number"],
             "url": m["url"], "repository": m["repo"], "forked_from": m["forked_from"],
             "generation": m["generation"], "event": m["event"], "location": m["location"],
             "dates": m["dates"], "tagline": m["tagline"], "status": m["status"],
             "manifest": f"{m['url']}pit.json" if m["url"] and "github.io" in (m["url"] or "") else None}
        pits.append({k: v for k, v in e.items() if v is not None})
    reg = {"spec": "pit-registry/0.1", "hub": HUB,
           "hint": "The constellation of living pits. Fetch any pit's manifest (pit.json) to talk to it.",
           "pits": pits,
           "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    p = os.path.join(out_dir, "pits.json")
    json.dump(reg, open(p, "w"), indent=1, ensure_ascii=False)
    print(f"🕸️  wrote {p} ({len(pits)} pits)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug"); ap.add_argument("--repo"); ap.add_argument("--hub")
    a = ap.parse_args()
    if a.hub:
        hub_registry(a.hub); return
    if not (a.slug and a.repo): ap.error("--slug and --repo required (or --hub)")
    man = build_manifest(a.slug, a.repo)
    pj = os.path.join(a.repo, "pit.json"); py = os.path.join(a.repo, "pit.yaml")
    json.dump(man, open(pj, "w"), indent=1, ensure_ascii=False)
    open(py, "w").write("# 🕳️ P.I.T. MANIFEST — " + SPEC + "\n" + to_yaml(man) + "\n")
    c = man["counts"]
    print(f"🕳️ {man['pit']['name']}: {c['sessions']} sessions · {c['transcripts']} transcripts · {c.get('hours')} h")
    print(f"   wrote {pj} + {py}")

if __name__ == "__main__":
    main()
