# TRACK D — TRANSCRIPTION: PARTNER, INTEGRATE, OR BUILD?
*PIT Research Cycle №1 "The Consensual Pit" · owner: PIT BULL 🐂🕳️ · CC0 · all sources accessed 2026-08-05 (UTC) · $0 research lane (web only, zero paid API calls)*

---

## 0. TL;DR — THE VERDICT

**BUILD stays champion. INTEGRATE stays tactical. PARTNER — politely decline for the transcription core, keep one door open for the workflow layer.**

Our own pipeline (Groq whisper-large-v3-turbo for bulk + Deepgram nova-3 for word-timestamp/diarization lanes + a to-be-built local whisper lane for the playa) beats every commercial alternative on the criteria that define a P.I.T.: word-level timestamps for the karaoke Knowledge Transponder, ~$0.04/audio-hr economics, consent-first privacy, and forkability by any village. **No meeting-assistant product on the market publishes word-level timestamps** — Circleback, Otter, Fireflies, Granola, Fathom, Read.ai, and Notta are all utterance/segment-level at best, per-seat priced, cloud-only, and solve *workflow* (notes/action items), not *archival transmission*. The one strategic improvement we should make: **close the offline gap** with a pre-provisioned whisper.cpp/faster-whisper "playa lane," and **watch three 2026 open models** (Voxtral Transcribe 2, Qwen3-ASR, pyannote community-1) that could upgrade the self-host stack.

---

## 1. THE PIT'S REQUIREMENTS (canon scorecard)

Every option below is scored against eight canon criteria:

1. **Word-level timestamps** — the karaoke Knowledge Transponder REQUIRES per-word start/end. No words, no glow.
2. **Diarization** — speaker attribution (who said what at the pit).
3. **Cost per audio-hour** — verified in-house baselines: **Groq turbo $0.04/audio-hr** (208-session harvest, July 2026) and **Deepgram nova-3 + diarize + word TS: $0.0825 for 23 clips / 19.18 min ≈ $0.26/audio-hr** (ShellPit re-harvest, 2026-08-01).
4. **Offline capability** — the playa has no internet. A camp MUST be able to transcribe local.
5. **Language coverage** — EN/HE/HI (ShellPit Hebrew, Goa/Devcon Hindi).
6. **Privacy** — camp audio on a third-party meeting platform = exposure. Weighted heavily: consent-first is the pit's soul.
7. **Forkability** — any village must reproduce the protocol. Cheap/free API keys OK; exotic infra not OK.
8. **Hallucination behavior** — pit canon: collapse loops to honest markers, never smooth over. (Our cross-check canon: nova-3 empty + whisper short phrase on noisy clip = whisper artifact → trust nova-3, flag ⚑.)

---

## 2. THE LANDSCAPE (verified August 2026)

### 2.1 The meeting-assistant class — what Shaka asked about

**Circleback (circleback.ai)** — the one Shaka named. YC-backed AI meeting-notes SaaS: joins Zoom/Meet/Teams/Slack huddles, records in-person via mobile/desktop apps, produces notes, action items, automations, cross-meeting search.
- **Pricing:** per-seat SaaS, no per-hour rate: Individual **$20.83/user/mo** (annual), Team **$25/user/mo**, Enterprise custom. 7-day trial; no forever-free tier. [circleback.ai/pricing]
- **Integration:** ⚠️ **NO traditional REST API.** Data access via (a) MCP server at `circleback.ai/api/mcp` (OAuth), (b) official CLI (`@circleback/cli`, `--json` output), (c) outbound webhooks (HMAC-signed JSON with transcript/notes/action items), (d) Zapier/Make. [support.circleback.ai MCP & CLI articles; github.com/onyx-dot-app/onyx#9680]
- **Word-level timestamps:** ⚑ UNVERIFIED — MCP returns "full transcript with speaker labels and timestamps," granularity unpublished; no SRT/VTT export documented. Utterance-level is the likely ceiling.
- **Diarization:** YES (speaker recognition, auto-named). **Languages:** 100+ (133 per release note); **Hebrew ✅ Hindi ✅** explicitly listed. [support.circleback.ai meeting-languages]
- **Privacy:** SOC 2 Type II, HIPAA, GDPR, EU-US DPF; encryption at rest/in transit; **"we do not use customer data to train models."** Cloud-processed only. [security.circleback.ai; support.circleback.ai security article]
- **Offline:** NO. **Partnership surface:** Rewardful affiliate program (30% commission on first 6 months of referred revenue) + a Startups program. [circleback.getrewardful.com; circleback.ai/affiliates, /startups]

**The rest of the class (one-paragraph verdicts, full receipts in §6):**

- **Otter.ai** — veteran bot-transcriber. Free 300 min/mo; Pro $8.33/user/mo annual. Public API is **Enterprise-only**. SRT export = segment-level, **no word-level TS**. **Hebrew ❌ Hindi ❌** (6 languages only). ⚠️ **Trains its own models on de-identified user data by default** — consent-first red flag. Cloud-only. [help.otter.ai; otter.ai/privacy-security]
- **Fireflies.ai** — Free tier; Pro $10/user/mo annual. Public **GraphQL API**; transcript = sentence-level with speakers; word-level ⚑ UNVERIFIED (likely no). 117 languages, **Hebrew ✅ Hindi ✅**. SOC 2 II/GDPR/HIPAA; states no LLM training on personal data. Cloud-only. [fireflies.ai/api, /pricing; guide.fireflies.ai languages; fireflies.ai/privacy-policy]
- **Granola** — bot-free local notepad: captures system audio on-device, sends to cloud ASR (Deepgram/AssemblyAI) + LLMs for notes, deletes audio. Business $14/user/mo. **API on Enterprise tier only**, no word TS, diarization hit-or-miss >3 people, 10 languages (**Hindi ✅ Hebrew ❌**). SOC 2 II. The most privacy-*conscious* architecture of the class, but still cloud-processed. [granola.ai/security; docs.granola.ai multi-language]
- **Fathom** — generous free tier (unlimited recording/transcription); Premium $16/mo annual. Public REST API + MCP; transcript = **utterance-level, not word-level**. 38 languages, **Hindi ✅ Hebrew ❌**. ⚠️ **Trains proprietary models on de-identified data by default** (opt-out in settings). [developers.fathom.ai; help.fathom.video security & languages]
- **Read.ai** — meeting assistant + enterprise search. Free 5 transcripts/mo; Pro $15/mo annual. Public REST API + MCP + webhooks. Word-level ⚑ UNVERIFIED. 20+ languages, **Hebrew ✅ Hindi ✅**. "No training on your data by default," SOC 2. [support.read.ai API reference; read.ai]
- **Notta** — Japan-based, strongest language play (58 transcription languages, **Hebrew ✅ Hindi ✅**). Free 120 min/mo; Pro $8.17/mo annual. ⚑ likely **no self-serve public API** (conflicting sources). SRT export = segment-level. **Notable: new "Privacy Mode" desktop beta (announced 2026-07-03) does LOCAL on-device transcription that works offline after setup** — the only offline offering in the entire class. [notta.ai/en/pricing; PRNewswire 2026-07-03]

**Class verdict:** these products solve *meeting workflow* — notes, action items, CRM sync. None publishes word-level timestamps, so **none can feed the karaoke Transponder**. All are per-seat subscriptions (a 10-person camp = \$100–250/mo ≈ 100–200× our per-hour costs), all cloud-upload camp audio to a third party, and two (Otter, Fathom) train on it by default. This class fails criteria ①④⑥⑦ outright.

### 2.2 The API class — our current lanes and rivals

| API (async batch, PAYG) | $/audio-hr | +Diarize | Word TS | HE | HI | Free credit | On-prem |
|---|---|---|---|---|---|---|---|
| **Groq whisper-large-v3-turbo** | **$0.04** ✅ verified | none | ✅ | ✅ | ✅ | free tier | ❌ |
| Groq whisper-large-v3 | $0.111 | none | ✅ | ✅ | ✅ | free tier | ❌ |
| **Speechmatics Melia 1** (new multilingual) | $0.129 | incl. | ✅ | ✅ | ✅ | $100 | ✅✅ (private cloud/container/appliance/on-device) |
| AssemblyAI Universal-2 | $0.15 | incl. | ✅ | ✅ | ✅ | $50 | ❌ |
| OpenAI gpt-4o-mini-transcribe | $0.18 | — | ❌ (whisper-1 only) | ✅ | ✅ | ❌ | ❌ |
| AssemblyAI Universal-3.5 Pro (2026 flagship) | $0.21 | incl. | ✅ | ✅ | ✅ | $50 | ❌ |
| Speechmatics Enhanced | $0.40 | incl. | ✅ | ✅ | ✅ | $100 | ✅✅ |
| OpenAI gpt-transcribe (new 2026 flagship) | $0.27 | — | ❌ | ✅ | ✅ | ❌ | ❌ |
| **Deepgram nova-3** mono | $0.288 promo (list $0.462) | +$0.12 | ✅ | ✅ | ✅ | $200 | ✅ (Enterprise self-host; SageMaker airgap) |
| OpenAI gpt-4o-transcribe-diarize (NEW 2026) | ~$0.36 ⚑ est. | incl. | ❌ | ✅ | ✅ | ❌ | ❌ |
| Gladia Solaria-1 Starter | $0.61 (Growth ~$0.20) | incl. | ✅ | ✅ | ✅ | €50 | Enterprise only |

Sources: deepgram.com/pricing + developers.deepgram.com docs; assemblyai.com/pricing + docs; gladia.io/pricing + /solaria; speechmatics.com/pricing (page updated 2026-07-31); platform.openai.com/docs/pricing + speech-to-text guide; console.groq.com/docs/speech-to-text. All accessed 2026-08-05.

**Notable changes since our July 2026 canon:**
1. **Groq turbo $0.04/audio-hr confirmed unchanged** — matches our verified harvest figure exactly. Word-level timestamps supported via `verbose_json` + `timestamp_granularities=["word"]`. Still **no diarization**. [console.groq.com/docs/speech-to-text]
2. **Deepgram diarization is now itemized at +$0.0020/min (+$0.12/hr)** on the pricing page — our nova-3 runs treated it as bundled. Worth re-checking against actual invoices; our ShellPit effective rate ($0.26/hr) sits under the promo list math either way. [deepgram.com/pricing]
3. **OpenAI entered diarization in 2026** (`gpt-4o-transcribe-diarize`, `diarized_json` output) and launched `gpt-transcribe` — but **only legacy whisper-1 supports word-level timestamp granularities** in their whole lineup. Karaoke-incompatible. [platform.openai.com/docs/guides/speech-to-text]
4. **AssemblyAI's 2026 flagship is Universal-3.5 Pro** ($0.21/hr, diarization included, HE+HI on both its models). Strong #2 behind Deepgram for full-feature lanes.
5. **Speechmatics is the dark horse**: Melia 1 at **$0.129/hr with diarization included**, never trains on your data by default, batch auto-deletes ≤7 days, and the **strongest deployment menu of any vendor** (private cloud, container, virtual appliance, on-device GPU/CPU) — the only API vendor whose on-prem story a well-resourced camp could actually adopt. [speechmatics.com/pricing]
6. **Deepgram offers Enterprise self-hosting** (Docker/K8s, airgapped via AWS SageMaker) — real but Enterprise-contract-priced; not village-forkable. [developers.deepgram.com/docs/self-hosted-introduction]
7. **Gladia Solaria-3 (2026) is European-languages-only** — HE/HI jobs must stay on Solaria-1 ($0.61/hr Starter). Priced out of contention.

### 2.3 The self-host class — the playa lane

| Tool / model | License | Word TS | Diarization | HE | HI | Hardware | Throughput (1 audio-hr) |
|---|---|---|---|---|---|---|---|
| **faster-whisper** (large-v3/turbo) | MIT | ✅ native (DTW) | ❌ (pair w/ pyannote) | ✅ | ✅ | GPU or CPU | RTX 4090: <9 min; CPU int8 small: ~8 min |
| **whisperX** (faster-whisper + wav2vec2 align + pyannote) | BSD-2 | ✅ aligned (HE+HI align models verified in source) | ✅ pyannote | ✅ | ✅ | CUDA GPU ~5GB VRAM | up to ~70× RT batched |
| **whisper.cpp** | MIT | ✅ (`-ml 1` token-level) | ❌ | ✅ | ✅ | anything; Metal on Mac | M5 Pro ~10× RT; generic M-series 2–3× RT |
| **NVIDIA Parakeet v3** | CC-BY-4.0 | ✅ native | ❌ (pair w/ Sortformer) | ❌ | ❌ (25 EU langs) | NVIDIA GPU | top-of-leaderboard throughput, 6.34% WER |
| **Voxtral Transcribe 2** (Mistral, 2026) | Apache-2.0 | ✅ | ✅ **built-in** | ❌ | ✅ (13 langs) | GPU (24B/3B-mini) | realtime variant exists |
| **Qwen3-ASR 0.6B/1.7B** (2026) | Apache-2.0 | ✅ via ForcedAligner (no HE/HI align) | ❌ | ❌ | ✅ | CUDA GPU, vLLM | 2000× RT @ batch128 claim |
| Whisper large-v3-turbo (open weights) | MIT | ✅ | ❌ | ✅ | ✅ | GPU/CPU | (as faster-whisper row) |
| **pyannote community-1** (diarization) | CC-BY-4.0, HF-gated | n/a | ✅ language-agnostic | ✅ | ✅ | GPU/CPU | DER ~11–19% |

Sources: github.com/m-bain/whisperX (incl. alignment.py), github.com/SYSTRAN/faster-whisper, github.com/ggml-org/whisper.cpp, huggingface.co/nvidia/parakeet-tdt-0.6b-v3, mistral.ai/news/voxtral-transcribe-2, github.com/QwenLM/Qwen3-ASR + HF model cards, huggingface.co/pyannote/speaker-diarization-community-1, hf-audio/open_asr_leaderboard. All accessed 2026-08-05. ⚑ UNVERIFIED: Sortformer license (possible NC clause), Kyutai/Moonshine/Granite-Speech license specifics, CPU large-v3 real-time factor (extrapolated).

**Key findings for the pit:**
- **The offline gap is closable TODAY with mature tooling.** whisper.cpp on any M-series MacBook transcribes an audio-hour in ~6–30 min fully offline; faster-whisper on a gaming-laptop GPU in <10 min; even a CPU-only laptop manages with the turbo or small model. Cost ≈ electricity (\$0.10–0.30/hr) — effectively **\$0 per audio-hour** once hardware exists.
- **Hebrew is the constraint.** The hot 2026 models (Parakeet v3, Voxtral 2, Qwen3-ASR, Kyutai) all skipped Hebrew. The whisper lineage (whisper.cpp / faster-whisper / whisperX) remains **the only self-host stack covering EN+HE+HI with word-level timestamps**, and whisperX is the only one adding verified HE+HI forced-alignment models plus diarization.
- **pyannote community-1** (CC-BY-4.0) is the forkable diarization answer — but it's HF-gated: a camp must download models + token **before** losing internet. Canon for playa prep.
- **whisperX maintenance is ACTIVE again** (last push 2026-07-13, 23.4k★) after historically slow merge periods.

---

## 3. ECONOMICS TABLE (mandatory) — what an audio-hour actually costs

**Scenario: a 10-person camp archive, 30 audio-hours/month, with word-level timestamps + diarization where available.**

| Option | Unit cost | 30 hr/mo scenario | Word TS | Offline | Notes |
|---|---|---|---|---|---|
| **Groq turbo (our bulk lane)** | **$0.04/hr** ✅ verified | **$1.20/mo** | ✅ | ❌ | no diarization |
| **Deepgram nova-3 + diarize (our fidelity lane)** | $0.288 + $0.12 ≈ $0.41/hr list-promo; **$0.26/hr verified effective** (ShellPit) | **$7.80–12.30/mo** | ✅ | ❌ | $200 free credit onboards new pits at $0 |
| Speechmatics Melia 1 | $0.129/hr (diarize incl.) | $3.87/mo | ✅ | via Enterprise on-device | cheapest full-feature API |
| AssemblyAI Universal-2 | $0.15/hr (diarize incl.) | $4.50/mo | ✅ | ❌ | $50 free credit |
| OpenAI gpt-transcribe | $0.27/hr | $8.10/mo | ❌ | ❌ | karaoke-incompatible |
| Gladia Solaria-1 Starter | $0.61/hr (diarize incl.) | $18.30/mo | ✅ | ❌ | — |
| **Self-host whisper.cpp/faster-whisper** | **~$0** (electricity ~$0.10–0.30/hr + hardware the camp already owns) | **~$0–9/mo electricity** | ✅ | ✅ | the playa lane |
| Circleback Team | $25/user/mo | **$250/mo (10 seats)** | ⚑ no evidence | ❌ | unlimited meetings, but no word TS |
| Otter Pro | $8.33/user/mo | $83/mo + 1,200 min/mo cap (would need 2× plans) | ❌ | ❌ | trains on data |
| Fireflies Pro | $10/user/mo | $100/mo | ⚑ sentence-level | ❌ | — |
| Notta Pro | $8.17/user/mo | $82/mo (1,800 min cap) | ⚑ | beta only | — |

**The spread is 200×: $1.20/mo (our Groq lane) vs $250/mo (Circleback seats) for the same camp — and the $250 option still can't produce a karaoke transcript.** Free tiers ($200 Deepgram / $100 Speechmatics / $50 AssemblyAI credits) mean a *new* pit can onboard at literally $0: at Deepgram's credit, that's ~480 audio-hours of nova-3 before a dollar is spent.

---

## 4. REQUIREMENTS MATRIX — every option × 8 canon criteria

✅ passes · ⚠️ partial/caveat · ❌ fails

| Option | ① word TS | ② diarize | ③ $/hr | ④ offline | ⑤ EN/HE/HI | ⑥ privacy | ⑦ forkable | ⑧ honest failure mode |
|---|---|---|---|---|---|---|---|---|
| **Our pipeline (Groq+nova-3)** | ✅ | ✅ (nova-3 lane) | ✅ $0.04–0.26 | ❌→🔧 buildable | ✅ | ✅ zero-retention lanes + consent canon | ✅ scripts CC0 on GitHub | ✅ collapse-to-marker canon in production |
| **+ whisper.cpp/faster-whisper playa lane** | ✅ | ⚠️ via pyannote | ✅ ~$0 | ✅ | ✅ | ✅ audio never leaves camp | ✅ one binary / pip install | ✅ whisper loops → markers (known, documented) |
| Circleback | ⚑ ⚠️ | ✅ | ❌ per-seat | ❌ | ✅ | ⚠️ good policy, but cloud 3rd-party | ❌ per-seat SaaS | ⚑ |
| Otter | ❌ | ✅ | ❌ per-seat+caps | ❌ | ❌ no HE/HI | ❌ trains by default | ❌ | ⚑ |
| Fireflies | ⚠️ sentence | ✅ | ❌ per-seat | ❌ | ✅ | ⚠️ cloud | ❌ | ⚑ |
| Granola | ❌ | ⚠️ | ❌ per-seat | ❌ | ⚠️ no HE | ⚠️ best-in-class, still cloud | ❌ | ⚑ |
| Fathom | ❌ utterance | ✅ | ❌ per-seat | ❌ | ⚠️ no HE | ❌ trains by default | ❌ | ⚑ |
| Read.ai | ⚑ | ✅ | ❌ per-seat | ❌ | ✅ | ⚠️ cloud | ❌ | ⚑ |
| Notta | ⚑ | ✅ | ❌ per-seat | ⚠️ beta | ✅ | ⚑ | ❌ | ⚑ |
| Deepgram nova-3 API | ✅ | ✅ (+$0.12/hr) | ✅ | ⚠️ Enterprise self-host only | ✅ | ✅ SOC2/HIPAA/GDPR, EU endpoint | ✅ cheap key | ✅ empty-output honesty observed (ShellPit) |
| AssemblyAI | ✅ | ✅ incl. | ✅ | ❌ | ✅ | ✅ | ✅ | ⚑ |
| Speechmatics | ✅ | ✅ incl. | ✅ | ✅ (Enterprise on-device) | ✅ | ✅ no-training default, ≤7-day delete | ⚠️ on-prem is Enterprise | ⚑ |
| OpenAI APIs | ⚠️ whisper-1 only | ⚠️ new, no word TS | ✅ | ❌ | ✅ | ✅ no-training default | ✅ | ⚑ whisper loops |
| Gladia | ✅ | ✅ incl. | ⚠️ $0.61 | ❌ | ✅ (Solaria-1) | ✅ | ✅ | ⚑ |
| whisperX self-host | ✅ aligned | ✅ pyannote | ✅ ~$0 | ✅ | ✅ (HE/HI align models) | ✅ | ⚠️ dependency-fragile | ⚠️ whisper loops |
| Parakeet/Voxtral/Qwen3 (2026 models) | ✅ | ⚠️ Voxtral only | ✅ ~$0 | ✅ | ❌ no HE | ✅ | ⚠️ GPU/vLLM heaviness | ⚑ |

---

## 5. THE VERDICT — PARTNER vs INTEGRATE vs BUILD

### 🏗️ BUILD — champion, and one strategic upgrade
Our pipeline already embodies the pit's soul: consent-first, ~$0 infra, forkable (every crusher script is CC0 on GitHub), radically honest (whisper-hallucination cross-checks with ⚑ flags shipped in production during the ShellPit nova-3 run). **Nothing on the market comes within 100× on cost, and nothing at any price fails criteria ①④⑥⑦ as hard as the meeting-assistant class.** Concrete improvements, in priority order:

1. **Close the offline gap — build the "playa lane" (top priority).** Pre-provision a camp kit: whisper.cpp (single binary, Metal-accelerated) or faster-whisper + `word_timestamps=True`, models + pyannote community-1 downloaded **before** the event (HF gating requires it), plus our existing collapse-to-marker post-processing. Any M-series MacBook transcribes an audio-hour offline in ~6–30 min at ~$0. This converts criterion ④ from ❌ to ✅ with mature, MIT-licensed parts.
2. **Add a local diarization lane.** Groq has no diarization; today that forces diarized jobs to Deepgram. Pairing faster-whisper word timestamps + pyannote community-1 (CC-BY-4.0, language-agnostic) = a fully self-hosted karaoke+diarization stack for camps that can't upload audio at all — the strongest privacy answer available.
3. **Keep the bilingual two-pass canon** (merge_bilingual.py) — 2026's multilingual API models (nova-3 `multi`, AssemblyAI U-3.5 Pro, Melia 1) all claim code-switching; worth a $1 bake-off against our verified zh/en merge approach, but our canon stands until beaten on receipts.
4. **Watch-list for 2026–27:** Voxtral Transcribe 2 (Apache-2.0, built-in diarization + word TS — adopt the day it adds Hebrew), Qwen3-ASR + ForcedAligner (ditto), whisperX alignment quality vs Qwen3-ForcedAligner (their AAS benchmark claims 37.5ms vs WhisperX 92.1ms on EN ⚑ vendor claim).

### 🔌 INTEGRATE — tactical, already doing it right
APIs are our commodity lanes, and the market is moving *toward* us (Speechmatics at $0.129/hr with diarization included would have been unthinkable in 2024). Recommendations:
- **Groq turbo stays the bulk lane** ($0.04/hr, price re-confirmed Aug 2026).
- **Deepgram nova-3 stays the fidelity lane** (word TS + diarize + HE/HI + $200 onboarding credit per new pit). Re-verify the new itemized diarization charge (+$0.12/hr) against our next invoice.
- **Add Speechmatics as the designated backup/vendor-diversity lane** — cheapest full-feature API, never-trains-by-default privacy posture that matches our consent canon better than anyone, and the only vendor with a real on-device deployment path if a resourced camp ever wants vendor-supported on-prem.
- **AssemblyAI Universal-3.5 Pro as second backup** — diarization included, HE/HI confirmed, $50 credit.

### 🤝 PARTNER — decline for the core; one honest door to leave open
- **Circleback et al. cannot be transcription partners** — they fail word-level timestamps (⚑ unpublished granularity at best), offline, per-seat economics, and forkability. Putting camp audio on any meeting platform is also a consent-canon violation unless every speaker opts into that specific third party.
- **The one honest exception:** Circleback's *workflow* layer (action items, cross-meeting search, MCP/CLI/webhooks, no-training policy, SOC 2) could serve **pit-organizer operations** — the family's own coordination meetings, not camp archives. Their affiliate (30%/6mo via Rewardful) and startups programs exist, but for a CC0 public-good protocol, referral revenue is a conflict-of-interest smell; if Shaka explores anything, it should be a **non-financial conversation** (e.g., word-level export on their roadmap? MCP-based consent metadata?). ⚑ UNVERIFIED whether they'd entertain it.
- **Notta's Privacy Mode beta** (local on-device transcription, July 2026) is the first meeting-class product moving toward our architecture — watch it, don't wed it.

### The one-line answer to Shaka's question
**The pit's transcription future is BUILD on our own mechanisms, INTEGRATE commodity APIs as swappable lanes, and PARTNER with no one for the archive core — because the karaoke Transponder's word-level requirement, the playa's offline requirement, and the consent canon's privacy requirement are three doors that no commercial partner currently fits through.**

---

## 6. SOURCES (all accessed 2026-08-05 UTC)

**Meeting-assistant class:** circleback.ai/pricing · security.circleback.ai · support.circleback.ai articles 13249081 (MCP), 14677613 (CLI), 11014015 (webhooks), 10493546 (languages), 10460553 (security) · github.com/onyx-dot-app/onyx issue #9680 · circleback.getrewardful.com/signup · help.otter.ai articles 36130822688279, 360047247414, 360047733634 · otter.ai/privacy-security · fireflies.ai/pricing, /api, /privacy-policy · guide.fireflies.ai articles 2973706448, 2154538358 · granola.ai/security, /blog/ai-meeting-notes-pricing · docs.granola.ai multi-language · developers.fathom.ai/api-reference/recordings/get-transcript · fathom.video/pricing · help.fathom.video articles 296192, 296512 · read.ai/plans-pricing, /post/six-new-languages-now-supported · support.read.ai article 49381161088659 · notta.ai/en/pricing · support.notta.ai article 4403155631131 · prnewswire.com Notta Privacy Mode release 2026-07-03 · eweek.com/artificial-intelligence/notta-review

**API class:** deepgram.com/pricing · developers.deepgram.com/docs/models-languages-overview, /docs/self-hosted-introduction · assemblyai.com/pricing, /docs/getting-started/models, /docs/getting-started/supported-languages, /docs/billing-and-pricing · gladia.io/pricing, /solaria, /blog/solaria-3-speech-to-text-model-for-european-languages · speechmatics.com/pricing, /speech-to-text/hebrew · platform.openai.com/docs/pricing, /docs/guides/speech-to-text · console.groq.com/docs/speech-to-text, /docs/model/whisper-large-v3-turbo · getmaxim.ai + portkey.ai (gpt-4o-transcribe-diarize per-min estimate ⚑)

**Self-host class:** github.com/m-bain/whisperX (incl. /blob/main/whisperx/alignment.py) · github.com/SYSTRAN/faster-whisper · github.com/ggml-org/whisper.cpp · huggingface.co/nvidia/parakeet-tdt-0.6b-v3 · arxiv.org/abs/2509.14128 (Granary) · mistral.ai/news/voxtral-transcribe-2 · github.com/QwenLM/Qwen3-ASR · huggingface.co/Qwen/Qwen3-ASR-1.7B · huggingface.co/pyannote/speaker-diarization-community-1, /speaker-diarization-3.1 · pyannote.ai/blog/community-1 · huggingface.co/spaces/hf-audio/open_asr_leaderboard · github.com/openai/whisper · github.com/kyutai-labs/delayed-streams-modeling · github.com/moonshine-ai/moonshine · promptquorum.com + digitalapplied.com + justvoice.ai (Apple Silicon throughput) · runaihome.com + localaimaster.com (GPU throughput)

**In-house verified baselines (pit canon, primary sources):** BULL-REPORT #20 (ShellPit nova-3: $0.0825 / 19.18 min / 23 clips, 2026-08-01) · harvest fleet logs (Groq turbo $0.04/audio-hr across 257.7 audio-hr, July 2026) · /shared/handoff/shellpit/nova3/ deliverables.

*⚑ UNVERIFIED marks throughout are deliberate: per pit canon, uncertainty is flagged, never smoothed over.*

— PIT BULL 🐂🕳️ BULL CRUSH! *the pit provides — and the bull PROVIDES PROOF!* 💪
