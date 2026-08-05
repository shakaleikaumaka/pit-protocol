# TRACK B — ZK ACCESS TO PRIVATE TRANSMISSIONS
*Privy 🔒🕳️ · PIT Research Cycle №1 "The Consensual Pit" · CC0 · ✅ COMPLETE 2026-08-05 UTC (~3,200 words; skeleton filed ~03:45 UTC, sections written one-at-a-time against session death)*

> **One-line thesis (draft):** A static pit can't *hide* bytes — anything served is public. So private transmissions must be **encrypted at rest in the repo/CDN**, and the ZK question becomes a *key-release* question: who can reconstruct the decryption key, under what conditions, and how do we revoke. The pit's answer should be: client-side encryption always; threshold key-release (Lit-style) where on-chain conditions make sense; pure-ZK membership (Semaphore) where anonymity is the point; and a signed-JSON revocation registry that works even when the chain is unreachable on playa.

## Canon this builds on (internal sources)
- Tokyo WorldID consent hack seed 4: ENS × World ID, revocations.json as derived data, "doorbell-not-library" (internal: `/shared/kb/tokyo-worldid-consent-hack.md`)
- Consent taxonomy: pending→assumed→explicit, revoked; collective consensus w/ order_ref (CRUSTY, canon 2026-08-01)
- ShellPit census finding (Privy, 2026-08-05): client-side-only gates = honor system; gated content in a public repo is *served*, not sealed. The taxonomy may need a `gate_strength` honesty field.
- Pit soul: static sites, ~$0, forkable by any village, radical honesty in UI.

## THE HARD PROBLEM (framing)
A pit is a static site: HTML, JSON, media on GitHub Pages/IPFS/any dumb host. There is no server to say "no." Three consequences:
1. **Anything served is public.** A "locked" page whose bytes are in the repo is hidden, not sealed — `curl` defeats every JS gate (confirmed live in the 2026-08-05 census: consent-gated lanes served HTTP 200 to a stranger).
2. **Therefore privacy = encryption at rest.** Sealed transmissions must be ciphertext in the repo. The access question collapses to a **key-release question**: who can obtain/reconstruct the decryption key, under what conditions, checked by whom.
3. **Revocation is the hard half.** You cannot un-serve ciphertext already mirrored, but you *can* refuse future key release — and you can keep plaintext-derived artifacts (search-index, digests, og-images) out of the public layers from day one. ZK enters twice: proving *membership/eligibility* without revealing identity, and proving *personhood* for self-serve revocation without doxing the revoker.

Design axes used throughout: **forkability** (can a 30-person camp run it?), **cost** ($0 lanes win), **privacy strength** (what does an observer/learn? what does the infra learn?), **playa-resilience** (what breaks when the chain/ISP is unreachable in the desert?).

## 1. CLIENT-SIDE ENCRYPTION + LIT PROTOCOL (threshold key-release)
**What it is:** Lit is a decentralized threshold-cryptography network. You encrypt content client-side; the symmetric key is split across Lit nodes; nodes release key shares only when a caller satisfies **Access Control Conditions (ACCs)** — on-chain tests (holds token/NFT, is a specific wallet, signed something, timestamp windows) evaluated by the node set. No single node or operator can decrypt alone. This is *the* canonical answer to "gate static content with on-chain logic": encrypt once, store the ciphertext anywhere (repo, IPFS, Arweave), and the network — not your server — enforces the door. ([Lit docs — Encryption & Access Control](https://developer.litprotocol.com/sdk/access-control/intro), accessed 2026-08-05)

**Current state (Aug 2026):** ⚑ Mixed maturity — verify before committing.
- The production network is **Datil ("mainnet beta")**; usage requires prepaid **Capacity Credits** minted with the LPX token — i.e. NOT $0 for production use, though `datil-dev` is free for development. ([Paying for Lit](https://developer.litprotocol.com/paying-for-lit/overview), [Capacity Credits](https://developer.litprotocol.com/concepts/capacity-credits-concept), accessed 2026-08-05)
- Lit is mid-generational-shift: **Naga testnet** is live as the official successor to Datil (faster threshold ECDSA, more curves, key migration path from Datil v0), with Naga mainnet announced as "getting up right now" per Lit's own blog; a further ground-up rebuild **"Chipotle" (v3)** is announced for the "agent era." ([What's next for Lit / Naga](https://spark.litprotocol.com/whats-next-for-lit-protocol/), [Naga Test](https://spark.litprotocol.com/naga-test/), [Chipotle v3](https://spark.litprotocol.com/introducing-lit-protocol-v3-chipotle/), all accessed 2026-08-05)
- ⚑ UNVERIFIED: exact Capacity Credit pricing per decryption request in USD terms; Naga mainnet launch status as of today; long-term support horizon for Datil once Naga/Chipotle lands. Three network generations in flight = real migration risk for a fork that embeds Lit deeply.

**Fit for pits:** Strong conceptual fit (static ciphertext + on-chain conditions = token-gated transmissions with no backend). Weaknesses for *our* canon: (a) not $0 at production scale; (b) wallet UX for every viewer is heavy for a camp; (c) **playa failure mode is total** — if the viewer can't reach Lit nodes + the chain RPC, nothing decrypts (mitigation: pre-fetch/decrypt-before-you-leave, or an organizer-held offline key escrow); (d) ACCs are public — the *condition list* itself can leak who the inner circle is (privacy of the gate, if not the content).

**Verdict:** best-in-class for "wallet-holding community unlocks sealed drops," overkill for per-speaker consent gating. Recommend as an OPTIONAL fork module, not the core seal.

## 2. SEMAPHORE (ZK group membership)
**What it is:** Semaphore (Privacy & Scaling Explorations) lets someone prove "I am a member of this group" and broadcast a signal (vote, endorsement, request) **without revealing which member** — plus scoped **nullifiers** that prevent double-signaling without linking actions to identity. Groups are Merkle trees of identity commitments; proofs are zk-SNARKs verifiable on-chain or off-chain. ([Semaphore docs](https://docs.semaphore.pse.dev/), [ethereum.org tools page](https://ethereum.org/developers/tools/semaphore/), accessed 2026-08-05) World ID is built on Semaphore — proof that the primitive scales to millions of members in production. ([World: Semaphore in World ID](https://world.org/blog/world/intro-zero-knowledge-proofs-semaphore-application-world-id), accessed 2026-08-05)

**Fit for pits — three concrete uses:**
1. **Anonymous consent-cleared membership.** At a camp, the organizer adds each consenting participant's identity commitment to the pit's group (one ceremony, can be offline: collect commitments on paper/QR, publish the root later). A member can then prove "I am a consent-cleared member of *this* pit" — the missing proof behind "the inner circle may listen."
2. **Self-serve, dox-free revocation (seed 4's spine).** A speaker's nullifier scoped to `pit-slug + session-id` lets them signal "revoke" exactly once, verifiably a real member, without revealing who they are — Sybil-safe takedown that survives the organizer being unreachable. This is the strongest ZK fit in the whole track: revocation wants anonymity + uniqueness, which is precisely what nullifiers provide.
3. **Rate-limited "talk to the pit" doorbell** — membership proof as humanity/uniqueness check for interactive lanes, per the Dispatch learning: verification on the doorbell, not the library.

**Limits (radical honesty):** Semaphore proves membership, **not decryption** — it doesn't release keys by itself; it must pair with a key-release layer (Lit, a worker, or social escrow). Group membership is only as fresh as the last published Merkle root — adding/removing members means a new root, so revocation-of-membership has propagation lag (fine for camps, wrong for high-churn). On-chain verification costs gas; off-chain verification is free but then *whoever verifies* is a server you must run. And Semaphore anonymity sets are per-pit: a 30-person camp is a 30-person anonymity set — unlinkable, but small.

**Verdict:** core pit primitive for the revocation + membership-proof lanes. Not a gate for bytes — the *identity* layer the gates consult.

## 3. MACI (private voting — camp consent votes?)
**What it is:** Minimal Anti-Collusion Infrastructure (PSE) — on-chain voting where individual ballots stay **private** (encrypted to a coordinator) while the *tally* is ZK-proven correct. Designed to resist bribery/collusion: voters can change keys, and nobody can cryptographically prove to a briber how they voted. ([MACI site](https://maci.pse.dev/), [privacy-ethereum/maci repo](https://github.com/privacy-ethereum/maci), accessed 2026-08-05) Battle-tested lineage in quadratic funding rounds; still live in 2026 — Gitcoin Grants 24 ran a Privacy Round on MACI + Privote ([announcement/discussion](https://www.reddit.com/r/ethereum/comments/1odcd4y/), accessed 2026-08-05), and Vitalik highlighted "Interfold" as bringing MACI-style private voting closer to Ethereum mainline ([report](https://cryptoadventure.com/vitalik-says-interfold-brings-maci-style-private-voting-closer-to-ethereum/), accessed 2026-08-05 — ⚑ UNVERIFIED single-source news item).

**Fit for pits:** The question Track C owns is *how a camp decides*; MACI is the answer when the decision must be **coercion-resistant and secret-ballot**. Concretely: a ShellPit-style consent consensus ("do we publish the folder?") taken as a MACI vote means no camper can be pressured into revealing their yes/no — important precisely because consent votes have social stakes inside a camp that lives together. MACI's known centralization caveat applies with full force: the **coordinator** can censor (not forge) and learns nothing about individual votes but operates the tally — for a camp, the coordinator is the organizer, which is socially acceptable but must be *declared* in the ledger (radical honesty: "coordinator = Terri, could have censored, could not have forged").

**Limits:** heavy machinery — contracts, a coordinator service, ZK circuits, key-management UX for every voter. For a 30-person camp this is a weekend hack project, not a Tuesday tool. Completely chain-dependent at vote time (playa-unfriendly unless the vote happens before/after the desert — which consent votes usually do). ⚑ UNVERIFIED: current MACI v3+ operator costs and whether a no-code hosted coordinator exists in 2026 that a non-dev camp could use.

**Verdict:** the right tool for *contentious* consent votes and for pit-fork governance with money attached (grant rounds, blessing-pool allocations). Wrong tool for routine per-session consent — that's stamps + ledger (Track C). Recommend: reference architecture, not default kit.

## 4. ZK ATTESTATIONS / EAS+ZK PATTERNS
**What it is:** The Ethereum Attestation Service is two contracts — a schema registry + an attestation registry — running on every major EVM chain, with attestations made **on-chain** (public, gas-costing) or **off-chain** (signed EIP-712 payloads, free, stored anywhere — IPFS, a repo, a URL fragment) while remaining independently verifiable. ([EAS docs](https://docs.attest.org/), [QuickNode guide](https://www.quicknode.com/guides/ethereum-development/smart-contracts/what-is-ethereum-attestation-service-and-how-to-use-it), accessed 2026-08-05) The ZK pattern that matters for pits: EAS's own **ZK playbook** — sign off-chain attestations, then generate ZK proofs *about* them (SP1 → WASM verification; the zkAttestify toolkit) so a party can prove "I hold a valid attestation with property X" without revealing the attestation's contents. ([EAS ZK playbook quickstart](https://docs.attest.org/docs/zk--playbook/quickstart), [EAS on zkAttestify flow](https://x.com/eas_eth), accessed 2026-08-05 ⚑ UNVERIFIED: playbook maturity, pinned toolkit versions.)

**Fit for pits — this is where Track B meets Track C:**
- **Consent grants as attestations.** CRUSTY's ledger entries (grant/revoke, order_ref, timestamps) map 1:1 onto an EAS schema (`pit-consent/1`: pit, asset-id, state, order_ref, attester). Off-chain attestations keep it $0 and keep *personal data off the chain* — the ledger remembers decisions, not identities (consent-ledger-schema privacy rule, honored cryptographically).
- **ZK over the ledger.** A fork could prove "asset X has a valid explicit-grant attestation from the pit's consent authority" to a downstream mirror *without shipping the whole ledger* — useful when the ledger contains sensitive framing notes.
- **Anchoring, not consensus** (Track C's thesis, confirmed from this side): an occasional on-chain anchor (Merkle root of the off-chain attestation set, one cheap tx) gives tamper-evidence while daily consent work stays off-chain and free.
- **Revocation propagation:** EAS has native revocation for on-chain attestations; off-chain, revocation = a second signed attestation + the derived-data regeneration our canon already mandates ("regenerate, don't hand-merge").

**Limits:** EAS proves *statements*, not *keys* — like Semaphore, it doesn't decrypt anything; it's the notary layer the key-release layer consults. Off-chain attestations are only as discoverable as where you publish them (a repo JSON works — static-site native). ZK-over-EAS today means running prover tooling (SP1) — dev-tier, not camp-tier, in 2026. ⚑

**Verdict:** adopt the *pattern* now (consent ledger ↔ EAS-shaped schema, off-chain first, anchor later), adopt the *ZK prover* later. Cheapest credible path from JSON ledger to cryptographic anchoring.

## 5. PRAGMATIC MIDDLE: token-gated decryption, wallet-auth Cloudflare Workers
**What it is:** Keep the pit static, add ONE tiny edge function as the *only* server-side component: a Cloudflare Worker that (a) verifies a wallet signature (SIWE — Sign-In With Ethereum — or a plain EIP-191 personal-sign challenge), (b) checks the caller against the consent/membership list (a JSON the pit already generates), and (c) returns the content key (or proxies the decrypted asset) only on pass. Workers run Web Crypto natively and JWT/signature validation at the edge is a documented standard pattern. ([Cloudflare Workers Web Crypto](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/), [JWT validation Worker](https://developers.cloudflare.com/api-shield/security/jwt-validation/jwt-worker/), accessed 2026-08-05) ⚑ UNVERIFIED: current free-tier request limits (historically 100k req/day — ample for a camp) — confirm before publishing numbers.

**Why this is the pragmatic champion for pits:**
- **Canon precedent exists:** the family already ships `ops/publicinform-worker.js` in the pit-protocol repo (census 2026-08-05) — the pattern is in our own DNA, not an import.
- **Cost:** free tier ≈ $0 at camp scale; no token purchases (unlike Lit Capacity Credits).
- **Forkability:** one JS file + `wrangler deploy`. A village can run it. It also degrades honestly: worker down = sealed lane closed, public lane untouched (fail-closed, the correct direction for a privacy gate).
- **The gate is REAL:** unlike client-side JS locks (census finding: honor-system gates), the key never ships to the browser until the worker says yes. An attacker curling the repo gets ciphertext.
- **ZK-compatible upgrade path:** step (a) can later accept a Semaphore proof instead of a wallet signature ("prove membership, don't name yourself") — same worker, stronger privacy. The middle lane is the on-ramp, not the ceiling.

**Weaknesses (honest):** it's a trusted server — the operator *could* log who asked for what (mitigate: open-source the worker, log nothing, say so in the UI); key custody is centralized (the worker holds content keys — mitigate: keys in Workers secrets/KV, rotatable); and it's a live dependency — playa-dead unless you pre-decrypt before departure. Cloudflare's 2026 push into agent wallets/x402 ([Cloudflare Wallets announcement](https://blog.cloudflare.com/wallets/), accessed 2026-08-05) suggests the wallet-auth-at-edge lane will keep improving — tailwind, not dependency.

**Verdict:** the recommended DEFAULT seal for private transmissions today. Real gate, $0, forkable, honest failure mode, upgrade path to full ZK.

## 6. REVOCATION REGISTRIES (extends tokyo-worldid-consent-hack.md seed 4)
Seed 4 sketched: speaker ZK-proves personhood → binds a scoped nullifier to their sessions → revokes by signed signal → `revocations.json` regenerates → the constellation flags forks. This track's research fills in the implementation spectrum, cheapest to strongest:

**Tier 0 — Social (today, canon, WORKS):** one word `remove` → consent@publicinform.com → human stamps the ledger → regenerate site + search-index + manifests. This is the living door and it must remain the default: zero crypto, zero UX, works for your grandmother. Every tier below ADDS self-sovereignty; none may remove this lane.

**Tier 1 — Signed JSON registry (static-native, $0):** `revocations.json` becomes a *signed* document — the consent authority's key (camp multisig or organizer key) signs each revocation event; forks verify the signature chain before honoring it. No chain needed. Tamper-evident, propagates through pits.json like any derived data. The 2026-08-05 census adds one hard requirement: **regeneration must purge backups and caches too** — preconsensus backup snapshots were found publicly served; a revocation that doesn't reach `backups/`, search-index, og-images and CDN caches is theater. Takedown propagation checklist: site → search-index → manifests → backups → caches → downstream-fork flag. (This tier is buildable this week with tooling the fam already has.)

**Tier 2 — Semaphore nullifier self-serve (the ZK tier):** per §2 — the speaker's scoped nullifier signs the revocation; uniqueness without identity; the registry accepts it without knowing who. Solves "organizer is gone, speaker wants out" — the pit outlives the gathering. Requires the membership ceremony at consent time (collect identity commitments when consent is granted — one extra QR scan at the same moment, same social touchpoint).

**Tier 3 — On-chain anchor (tamper-proof, optional):** publish the Merkle root of the revocation set on a cheap EVM chain (Base-class), or as an EAS revocation attestation (§4). Now no operator — not even the pit fam — can silently drop a revocation from history. Append-only enforced by math, matching CRUSTY's "corrections get new lines, never erasures." Cost: one tx per anchor batch, not per revocation.

**What breaks on playa:** Tier 0 nothing (email when you're back; SLA clock should be honest about desert time). Tier 1 nothing (regeneration is a build step, runs anywhere). Tier 2 proof *verification* needs the group root — bundle roots into the static site so verification works offline; *submission* queues until connectivity. Tier 3 anchoring waits for connectivity — fine, anchoring is asynchronous by design.

**Design rule across all tiers:** revocation targets *future access* (key release stops, indexes purge) and *derived layers* — ciphertext already mirrored cannot be unserved, and the UI must say so plainly. Radical honesty about the limits of deletion IS the privacy policy.

## 7. RANKED ARCHITECTURES FOR THE PIT (scored)
Scores: 🟢 strong · 🟡 workable · 🔴 weak. Criteria from the brief: forkability (any village can run it), cost, privacy strength, playa-resilience.

### 🥇 ARCH 1 — "SEALED AT REST + WORKER DOOR" (default, build now)
Client-side-encrypt sealed transmissions (per-asset symmetric keys, ciphertext in repo) → one Cloudflare Worker verifies wallet-signature (later: Semaphore proof) against the generated consent/membership JSON → releases keys → revocation = regenerate the JSON + purge indexes/backups/caches (Tier 1 signed revocations.json).
| forkability | cost | privacy | playa |
|---|---|---|---|
| 🟢 one JS file + build step | 🟢 $0 (free tier) | 🟡 real gate, trusted operator, no anonymity yet | 🟡 pre-decrypt before departure; fails closed |
**Why first:** every weakness has a declared mitigation and an upgrade path; every strength is canon ($0, forkable, honest UI). Census finding addressed directly: JS-honor-gates become real gates.

### 🥈 ARCH 2 — "SEMAPHORE INNER CIRCLE" (the ZK upgrade, build second)
Arch 1 + Semaphore: consent-time commitment ceremony → viewers/members prove membership anonymously → worker (or pure client-side verification against bundled roots) accepts proofs → speaker self-serve revocation via scoped nullifiers (Tier 2).
| forkability | cost | privacy | playa |
|---|---|---|---|
| 🟡 ceremony + circuits; needs one dev per fork | 🟢 off-chain verification $0 | 🟢 anonymity + unlinkability + dox-free revocation | 🟢 roots bundled in the static site; submissions queue offline |
**Why second:** it's the strongest *privacy* architecture, but it stands on Arch 1's key-release bones and adds a ceremony camps must actually perform. Sequence matters.

### 🥉 ARCH 3 — "LIT THRESHOLD DROPS" (optional module for token-gated releases)
Encrypt to Lit ACCs (holds camp NFT / on consent-registry list) → Lit nodes release key shares on condition pass → ciphertext hosted anywhere.
| forkability | cost | privacy | playa |
|---|---|---|---|
| 🟡 SDK integration + wallet UX for every viewer | 🟡 Capacity Credits, not $0 (dev net free) | 🟢 no trusted operator; 🟡 ACC list is public metadata | 🔴 no Lit + no RPC = no decrypt; pre-decrypt required |
**Why third:** excellent for "community owns the key" drops, wrong as the default seal — cost, UX weight, three network generations in flight (Datil/Naga/Chipotle = migration risk ⚑), and the worst playa failure mode.

### 🏅 ARCH 4 — "MACI CONSENT BALLOT" (special teams only)
MACI vote for contentious camp-consent decisions; result feeds the ledger as order_ref; content gating itself stays on Arch 1/2.
| forkability | cost | privacy | playa |
|---|---|---|---|
| 🔴 coordinator + contracts + circuits | 🟡 gas + coordinator ops | 🟢 coercion-resistant secret ballot (declare the coordinator's censorship power) | 🔴 vote before/after the desert, never during |
**Why fourth:** solves a governance problem, not an access problem — include it so forks know where private *voting* lives when they need it.

### The synthesis in one breath
**Encrypt at rest (always) → worker-released keys (now) → Semaphore anonymity + nullifier revocation (next) → EAS-anchored append-only ledger (when cheap) → MACI only when the vote itself needs armor → and the email door stays open forever, because your grandmother is a consent authority too.**

## Sources
- Lit Protocol — Encryption & Access Control: https://developer.litprotocol.com/sdk/access-control/intro (accessed 2026-08-05)
- Lit Protocol — Paying for usage / Capacity Credits: https://developer.litprotocol.com/paying-for-lit/overview · https://developer.litprotocol.com/concepts/capacity-credits-concept (accessed 2026-08-05)
- Lit — Naga & roadmap: https://spark.litprotocol.com/whats-next-for-lit-protocol/ · https://spark.litprotocol.com/naga-test/ · https://spark.litprotocol.com/introducing-lit-protocol-v3-chipotle/ (accessed 2026-08-05)
- Semaphore docs: https://docs.semaphore.pse.dev/ · https://semaphore.pse.dev/ (accessed 2026-08-05)
- ethereum.org — Semaphore: https://ethereum.org/developers/tools/semaphore/ (accessed 2026-08-05)
- World — Semaphore in World ID: https://world.org/blog/world/intro-zero-knowledge-proofs-semaphore-application-world-id (accessed 2026-08-05)
- MACI: https://maci.pse.dev/ · https://github.com/privacy-ethereum/maci (accessed 2026-08-05)
- Gitcoin Grants 24 MACI+Privote round (community report ⚑): https://www.reddit.com/r/ethereum/comments/1odcd4y/ (accessed 2026-08-05)
- Vitalik/Interfold MACI-style voting (news report ⚑ UNVERIFIED): https://cryptoadventure.com/vitalik-says-interfold-brings-maci-style-private-voting-closer-to-ethereum/ (accessed 2026-08-05)
- EAS docs + ZK playbook: https://docs.attest.org/ · https://docs.attest.org/docs/zk--playbook/quickstart · https://attest.org/ (accessed 2026-08-05)
- QuickNode — What is EAS: https://www.quicknode.com/guides/ethereum-development/smart-contracts/what-is-ethereum-attestation-service-and-how-to-use-it (accessed 2026-08-05)
- Cloudflare Workers Web Crypto + JWT validation: https://developers.cloudflare.com/workers/runtime-apis/web-crypto/ · https://developers.cloudflare.com/api-shield/security/jwt-validation/jwt-worker/ (accessed 2026-08-05)
- Cloudflare Wallets (x402/agent wallets): https://blog.cloudflare.com/wallets/ (accessed 2026-08-05)
- Internal: /shared/kb/tokyo-worldid-consent-hack.md (seed 4) · /shared/handoff/consent/consent-ledger-schema.md · /shared/kb/private-pits.md (Privy census 2026-08-05) · /shared/privacy-reports/PRIVY-REPORT.md

*The privy provides... NOTHING to strangers — and now we know exactly how to keep that promise in math. Sealed with a pit. 🔒🕳️ — Privy, Track B complete 2026-08-05 UTC*

## Sources
*[accumulating]*
- Lit Protocol docs — Encryption & Access Control: https://developer.litprotocol.com/sdk/access-control/intro (accessed 2026-08-05)
