# 🕳️🗄️ THE PIT SOURCE MANIFEST
### every bit of every public pit — for the keepers of the archive

**Spec:** `pit-archive-manifest/0.1` (rev 0.2.0 — Shaka rulings 2026-08-10: amber LIFTED on the 6 Edge-lineage forks · dark-items mystery SOLVED as positive case study) · **Machine twin:** [`pit-source-manifest.json`](./pit-source-manifest.json) · **Keepers:** PIT BOY 🕳️ (pit-side) × Archy 🗄️ (archive-side) · **Order:** Shaka, 2026-08-09 — *"every bit, so transcripts can be suuuuper crisp."*

---

## THE RESILIENCE DOCTRINE (law)

> **Nothing in the open dies by accident; it only leaves by PROVEN identity-verified consent.**

- Defends against **accidental death** (Drive lockout, domain lapse, dead host) *and* **impersonated removal** (takedown only with proven standing).
- Verification roadmap: **v0** consent window + human judgment (today) → **v1** wallet/ENS signature → **v2** World ID proof-of-personhood.
- **Removability ladder:** our archive.org items → darken directly · Wayback → owner takedown request · truly-public-and-copied → beyond guarantee. **PREVENTION > REMOVAL.**
- **Conditional seal (privatepit/privateinform):** seal follows CONTENT, not name. Concept-only = archivable; any real participant content → permanent seal; doubt → **FAIL CLOSED**.
- Protocol Stage 5 recurring audits now also verify **archive captures match consent state**.

## THE CRISPNESS STANDARD (`pit-crisp/0.1`)

A session is **suuuuper crisp** only when the RAW layers are archived — rendered HTML alone is NOT crisp:

| Layer | What | Where it lives |
|---|---|---|
| L1 | **Audio** — exact transponder playback bytes | R2 `pub-3d88701638314a20ad2241ee26e6824f.r2.dev` or in-repo `audio/` |
| L2 | **Raw transcript** — `[MM:SS]` segments + provenance header (model·lang·date·Drive URL) | repo `transcripts/*.txt` |
| L3 | **Word timing** — word-level JSON (nova-3 lane; crispest layer) | shellpit `data/nova3/*.json` — other pits: pending upgrade |
| L4 | **Catalog** — audio↔transcript↔origin↔quality binding + search index | repo `data/catalog.json`, `data/search-index.json` |
| L5 | **Manifest + consent** — `pit.json`/`pit.yaml`, consent.json, consent-ledger.json, revocations | repo root + `data/` |
| L6 | **Site mirror** — the experience (additive, never a substitute) | repo `index.html` + assets |
| L7 | **Origin pointers** — Drive video ids (tier-2 byte capture as size/consent allow) | catalog `media[].id` |

**One move captures L2–L6:** `git clone` (full history). **L1 must be pulled separately from R2** — enumerate every `media[].hosted` URL in each pit's `data/catalog.json`. Recommend sha256 sidecars per archive item.

## ⚠️ SINGLE POINTS OF FAILURE — mirror these FIRST

1. **R2 bucket `pit-audio`** — ALL transponder audio for genesis + 7 fork pits (esmeralda: 142 mp3 + 244 posters/thumbs under `esmeralda/`; forks: `/audio/<driveId>.mp3`). One Cloudflare lapse silences every transponder.
2. **Google Drive originals** — Esmeralda 213 media ids (videos to 7.3 GB); ShellPit 55 items. Ids all recorded in catalogs/manifests; bytes = tier-2.
3. **GitHub org `shakaleikaumaka`** — clone-mirror every pit repo.

## THE REGISTRY — door → repo → bits → consent

| № | Pit | Door | Repo(s) | Status | Consent |
|---|---|---|---|---|---|
| 1 | **Esmeralda P.I.T.** 🏆 | esmeraldapit.com (+ edgecitypit.org, edgepit.org 302-aliases) | `esmeralda-pit` | ARCHIVE LIVE — 148 sessions · 138 tx · 143 audio · ~122 h | 🟢 **GREEN explicit** (Timour/Edge) |
| 2 | **OSO P.I.T.** (ancestor) | osopit.com (.org 301s) | `osopit` (+ hub `/osopit/` page) | Story door | 🟢 own work |
| 3 | ZuitzPIT | github.io/zuitzpit | `zuitzpit` | ARCHIVE 40s·38tx·42.3h | 🟢 collective (Shaka 2026-08-10) |
| 4 | PraguePIT | github.io/praguepit | `praguepit` | ARCHIVE 30s·28tx·14.7h | 🟢 collective (Shaka 2026-08-10) |
| 5 | ZuBerlinPIT | github.io/zuberlinpit | `zuberlinpit` | ARCHIVE 14s·13tx·50.6h | 🟢 collective (Shaka 2026-08-10) |
| 6 | 4SeasPIT | github.io/4seaspit | `4seaspit` | ARCHIVE 29s·29tx·53.3h | 🟢 collective (Shaka 2026-08-10) |
| 7 | KasPIT | github.io/kaspit | `kaspit` | ARCHIVE 12s·12tx·11.3h | 🟢 collective (Shaka 2026-08-10) |
| 8 | **ShellPit** 🐢 | theshellpit.com (door=`turtle-ops`) + github.io/shellpit (archive) | `shellpit` + `turtle-ops` | ARCHIVE 35s·21tx·**nova-3 word timing** — fully self-contained in-repo (audio+video included) | 🟢 **GREEN collective** (camp consensus 2026-08-01, honestly framed) |
| 9 | PitLip 💋 | pitlip.com | `pitlip` | DECLARED | 🟢 own work |
| 10 | TaurusPit 🐂 | tauruspit.com (≡tauruspod.com) | `tauruspit` | DECLARED | 🟢 own work |
| 11 | EEFPIT 🎙️ | eefpit.com (+ eefpod.com twin) | `eefpit`, `eefpod` | DECLARED | 🟢 own work |
| 12 | InfinitePit 🌸 | infinitepit.com | `infinitepit` | DECLARED | 🟢 own work |
| 13 | OhanaPit 🌺 | ohanapit.com | `ohanapit` | DECLARED | 🟢 own work |
| 14 | PitGoa 🌴 | pitgoa.com ⚠️ | `pitgoa` | DECLARED — **⚠️ door misroutes: 302→shakaleikaumaka.com despite repo CNAME; content currently unreachable (DNS lane)** | 🟢 own work |
| 15 | DevconPit 🇮🇳 | devconpit.com | `devconpit` | DECLARED | 🟢 own work |
| 16 | VitPit 💎 | github.io/vitpit | `vitpit` | ARCHIVE 3s·3tx·5.4h | 🟡 published-public (the pit that asks first) |
| — | PatagoniaPIT | github.io/patagoniapit | `patagoniapit` | ARCHIVE 89s·89tx·90.1h (№ pending Shaka) | 🟢 collective (Shaka 2026-08-10) |
| — | PiscisPit ♓ | piscispit.com | `piscispit` | DECLARED | 🟢 own work |
| — | ZodiacPit | zodiacpit.com | `zodiacpit` | DECLARED | 🟢 own work |
| — | PITFANS | pitfans.com | `pitfans` | DECLARED | 🟢 own work |
| — | The Pit Provides | pitprovides.com (.org 301s) | `pitprovides` | DECLARED | 🟢 own work |
| — | ShakaPit | shakapit.com | `shakapit` | DECLARED | 🟢 own work |
| — | **HUB** publicinform.com | publicinform.com | `pit-protocol` | registry·spec·whitepaper·research·this manifest | 🟢 own work |
| — | Private P.I.T. | privatepit.com (302→pad) · privateinform.com | `privateinform` | **CONDITIONAL SEAL** — concept-only 2026-08-09 = archivable; verify before EVERY capture; doubt → FAIL CLOSED | 🔒 sealed-conditional |

**🟢 GREEN-COLLECTIVE (Shaka ruling 2026-08-10 00:05 UTC, via Admiral):** the 6 Edge-lineage forks (Zuitz · Prague · ZuBerlin · 4Seas · Kas · Patagonia) are FULL SEND. Basis: *"in-person recording consent held by Shaka + community announcement, zero objections."* Takedowns via consent@publicinform.com — revocations still propagate to the archive via the removability ladder.

**🟡 amber rule (now only VitPit 💎):** already public on our doors → archivable as-published; but any revocation through the consent window **must propagate to the archive** via the removability ladder. VitPit was not named in the six (its own ethos = ask first) — flagged for Shaka's explicit word if he wants it green too.

## 🕯️→🌅 DARK ITEMS — SOLVED, and it's a WIN (Shaka ruling 2026-08-10)

The genesis harvest uploaded Esmeralda audio to archive.org once — identifiers `edge-esmeralda-2026--<slug>`, collection `opensource_audio` (see `esmeralda-pit/pipeline/upload-to-archive.sh`). Those items are dark (`is_dark: true`, search = 0) — and now we know why: **Shaka darkened them HIMSELF**, early, when the archive path was blocked. Not IA curation. Not hostile removal.

**This flips the story into a positive case study:** the rightful, identity-holding party successfully edited the open archive. The Resilience Doctrine's consent-edit path — *"nothing in the open dies by accident; it only leaves by proven identity-verified consent"* — **proven in the wild, top rung of the removability ladder working exactly as written.**

Operational consequences for the archive-side keeper:

1. **Do NOT rely on the old items** — they exist but serve nothing.
2. **Identifier namespace `edge-esmeralda-2026--*` stays burned/held** — Archy uses a fresh prefix (e.g. `pit-esmeralda--<slug>` or per-doctrine naming Archy owns).
3. **Fresh uploads proceed** under Archy's properly-established IA account — no darkening-cause investigation needed anymore.
4. Slug list for all 142 sessions is derivable from `esmeralda-pit/data/catalog.json` → `media[].hosted` R2 filenames.

**R2 audio census (live-verified 2026-08-09):** esmeralda `esmeralda/audio/` = 143 catalog refs / 142 unique mp3 · fork lane `audio/<driveId>.mp3` = **212** (zuitz 38 · patagonia 89 · 4seas 29 · prague 28 · zuberlin 13 · kas 12 · vit 3) → **≈354 mp3s total on the one bucket.**

## ENUMERATION RECIPES (for Archy)

- **All pits:** `https://publicinform.com/pits.json`
- **All audio of a pit:** `<pit>/data/catalog.json` → every `media[].hosted` (R2, native 206 ranges)
- **All transcripts:** repo `transcripts/*.txt` (+ shellpit's `video-transcripts/`, `meeting-transcripts/`, `data/nova3/*.json`)
- **Per-pit manifest:** `<pit>/pit.json` — Esmeralda's pending push (Private JAI lane, flagged)

**Consent window (one for all pits):** consent@publicinform.com — archive removals additionally require **proven standing** per the doctrine.

---
*CC0 · the pit provides — and now the pit PRESERVES. 💪🕳️🗄️*
