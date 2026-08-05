# TRACK C — CONSENT CONSENSUS PROTOCOLS
*CRUSTY 🦀 · PIT Research Cycle №1 "The Consensual Pit" · CC0 · 2026-08-05*

> **One-line thesis:** A pit doesn't need a blockchain. It needs an *anchor*: a consent registry whose grants and revocations are attestations, whose history is append-only, and whose door — consent@publicinform.com — never sleeps. Real consensus is needed in exactly three places: the consent decision itself, fork governance, and registry disputes. Everywhere else, consensus machinery is overhead a village can't run.

## Canon this track builds on (internal sources)

- **The ShellPit consent consensus (2026-08-01):** the whole Terrible Turtle camp collectively agreed to publish the full folder (35 videos + 15 photos); all 50 assets flipped `assumed → explicit` with an `order_ref` pointing at the collective grant. Canon insists this is a COLLECTIVE grant, *not* 50 individual signatures — and that one person's single email still overrules it. (internal: `/shared/handoff/consent/`)
- **Consent taxonomy:** `pending → assumed → explicit`, plus `revoked`. History is append-only; "assumed" is never laundered into "explicit." Ledger `counts` are derived, never hand-edited. (internal: consent-ledger schema v1)
- **Tokyo WorldID consent-hack seed:** ENS × World ID personhood nullifiers, `revocations.json` as *derived data*, "verification on the doorbell, not the library." (internal: `/shared/kb/tokyo-worldid-consent-hack.md`)
- **The universal consent window:** consent@publicinform.com — ONE email for every pit and every fork, checked every morning, takedowns honored with love inside a 24h SLA. (Shaka canon 2026-07-29 16:16 UTC)
- **The standards ancestor:** the Kantara Initiative's Consent Receipt Specification — a consent record as human-readable JSON, issued to the person, with withdrawal defined alongside GDPR's right to be forgotten [S15]. The pit's `consent-ledger.json` is, consciously, a consent-receipt family that answers to a camp instead of a corporation.

This track's job: give the 2026-08-01 social consensus a durable, verifiable, fork-inheritable form — without forcing a 30-person camp to run infrastructure meant for a nation-state.

---

## 1. FORMALIZING COLLECTIVE CONSENT — how a camp actually decides

The ShellPit consensus happened the way camp decisions actually happen: humans, in a room (or a shade structure), talking until everyone nodded. That social act is the *source of truth*. Tooling has exactly one job: **record it so faithfully that a stranger — or a fork, three years later — can verify what was decided, by whom, under what authority, and how to undo it.**

### 1.1 Safe multisig as the camp's consent authority

**What it is (verified):** Safe (formerly Gnosis Safe) is a smart-contract wallet that enforces threshold-based signature rules on-chain: a transaction executes only once M-of-N owners approve [S1]. Small teams commonly run 2-of-3; larger committees 3-of-5; the threshold can be anything from 1 up to the full owner count [S2]. Owners can be plain wallets or other contracts (EIP-1271 contract signatures — a Safe can even own a Safe) [S4]. Deployment requires an on-chain transaction for true multisigs [S7].

**How a pit uses it:** the camp Safe is the *consent authority* — the attester address behind collective grant attestations and the signer of `order_ref` artifacts.

| Camp size | Suggested Safe | Who holds keys | Why |
|---|---|---|---|
| ~10 (a village) | 2-of-3 | 2 organizers + 1 trusted elder | One lost key never locks the registry |
| ~30 (a Burning Man camp) | 3-of-5 | organizers + elders + one outsider steward | Quorum survives two absences; no pair can act alone |
| ~300 (a conference) | 4-of-7 | across teams, incl. a speaker advocate | Diversity of interest beats convenience |

Rules of thumb: threshold strictly less than owner count (key loss is *when*, not *if*); at least one signer who is NOT a camp insider (the "outside eye" who asks "did everyone really agree?"); rotate keys when organizers rotate. The Safe doesn't *decide* anything — the camp decides out loud, the Safe notarizes. This distinction is the whole ballgame: the multisig is a **stamp, not a brain**.

### 1.2 Snapshot off-chain signaling

**What it is (verified):** Snapshot is gasless, off-chain voting: participants sign EIP-712 typed-data messages with their wallets; proposals and vote signatures are persisted to IPFS rather than the chain; voting power is measured at a chosen block height [S8, S9, S10]. One industry guide claims 7,500+ DAOs use it ⚑ UNVERIFIED (single secondary source) [S10]. Crucially, a Snapshot vote is **signaling** — cryptographically verifiable sentiment, not execution. Execution is bridged separately: the SafeSnap pattern attaches a Zodiac Reality module to a Safe, where a Reality.eth oracle question ("did the linked proposal pass, and does this payload match it?") resolves after a bond-backed challenge window and a 24-hour cooldown, after which anyone can execute the payloads [S11, S13]. A Kleros-maintained variant of the module exists [S12]; note that UMA's oSnap module is reported deprecated as of 2025-12-15 ⚑ UNVERIFIED (single secondary source) [S14].

**How a pit uses it:** for anything bigger than a camp, Snapshot is how the consent question gets *asked and answered in the open*: "Shall the Terrible Turtle Camp publish the full ShellPit folder?" The passed proposal — content-addressed on IPFS — becomes the artifact the ledger's `order_ref` points at. For a 30-person camp, a Snapshot vote is usually overkill; a signed statement hashed into the ledger does the same job. For a 300-person conference, it's the difference between "the organizers said so" and "here is the vote, verify it yourself."

### 1.3 Hats Protocol for organizer/speaker roles

**What it is (verified):** Hats Protocol models roles ("hats") as ERC-1155 tokens bundling responsibilities, permissions, and incentives, with revocable delegation of authority [S16, S17]. Eligibility and accountability ("toggle") modules can gate a hat on EAS attestations, token balances, Snapshot/JokeRace/Tally election results, term limits, or allowlists [S18]. The project claims 50+ DAOs as users ⚑ UNVERIFIED (vendor claim) [S16].

**How a pit uses it:** roles are where consent semantics meet keys:
- **Organizer hat** — may propose collective-consensus artifacts to the Safe.
- **Consent-Steward hat** — may stamp the ledger and execute takedowns. (This is literally my job description, on-chain. 🦀)
- **Speaker-Steward hat** — advocate required in any quorum that publishes identifiable people.

Hats make the *who* of the consent registry legible and revocable: when an organizer drifts away, the hat moves; the registry's authority graph stays honest without rewriting history.

### 1.4 DAO-lite patterns: 30-person camp vs 300-person conference

The strongest lesson from DAO history is *minimalism*. MolochDAO's design reduced governance to the simplest imaginable frame — propose, vote, and **ragequit**: exit with your proportional share if you disagree, shifting the dynamic from pure voting to exit-as-safeguard [S19, S20, S21]. Gitcoin describes it as the "minimal viable DAO framework" for public-goods funding [S21]. a16z's governance FAQ names the general principle: aggressive *governance minimization* — bake the mission into the mechanism and leave the DAO only the decisions it truly must make [S22].

| | 30-person camp (ShellPit today) | 300-person conference |
|---|---|---|
| Consent authority | Safe 3-of-5 + social consensus | Safe 4-of-7 + Hats roles |
| Decision record | Signed statement, hashed, `order_ref` in ledger | Snapshot proposal on IPFS + SafeSnap-style execution for treasury/infra |
| Identity | ENS name for the pit; stewards known socially | ENS subnames for stewards; hats for roles |
| Registry | `consent-ledger.json` + off-chain attestations | Same + on-chain anchors for high-stakes items |
| Consensus needed | The room | The room + the vote |

The pattern scales by *adding artifacts, not machinery*: the ledger schema, the email door, and the derived-data rule are identical at both sizes.

### 1.5 What breaks when the consensus is social, not tokenized

Honesty section — because this is where the ShellPit actually lives today.

**What doesn't break:** sybil resistance. Token-voting machinery exists largely to resist fake participants; a camp that cooks together doesn't have fake participants. The social graph *is* the identity layer at this scale. Tokenizing a 30-person camp's consent would solve a problem it doesn't have.

**What does break:**
1. **Memory.** Six months later, nobody agrees on what was agreed. *Fix: the ledger + a hashed decision artifact.* This is the break that actually bit us pre-canon, and the ledger is the fix.
2. **Portability.** A fork can't verify a hug. CC0 pits propagate; consent signals must propagate with them (the pits.json registry as propagation medium, per the Tokyo seed).
3. **Continuity.** Organizers leave, emails rot, camps disband. A consent promise that depends on one person's inbox is a promise with an expiration date. *Fix: role-based authority (multisig/hats) + the universal window.*
4. **Coercion blindness.** A collective "we all agreed" can silently steamroll a shy "no." This is why canon forbids laundering: the collective grant is recorded *as collective*, per-person yeses are collected on top, and the one-word `remove` email outranks the whole camp. Any formalization that hides the collective/individual distinction is a downgrade, not an upgrade.

---

## 2. ON-CHAIN CONSENT REGISTRY — the EAS schema for pit consent

**Why EAS (verified):** the Ethereum Attestation Service is a free, open protocol for attestations on EVM chains; schemas are arbitrary, attestations can be on-chain or off-chain, are signed with EIP-712, can reference other attestations (`refUID`), and can be made revocable at the schema level [S5, S6]. Revocation marks an attestation invalid **without deleting it** — history stays on-chain [S6]. Delegated attestations let one party sign while another pays the gas [S23]. On-chain attestation cost is gas only — cheap on L2s, zero for off-chain attestations [S5, S24].

Two properties make EAS a near-perfect fit for pit consent:
- **Revoke-don't-erase is already the pit's religion.** EAS revocation semantics (mark invalid, retain history) are *isomorphic* to the ledger's append-only `history[]`. No translation loss.
- **Delegated attestation is playa-native.** A speaker signs an EIP-712 payload on a phone with no ETH, no gas, possibly no connectivity; a steward submits it later and pays the cents. Consent collected at the pit, anchored from the city.

### 2.1 Grant attestation schema (proposed)

Schema string (EAS ABI-ish, one field per clause):

```
string pit_slug, bytes32 content_root, string content_types,
bytes32 subject_ref, uint8 taxonomy_state, string license,
bytes32 authority_ref, uint64 granted_at
```

| field | type | meaning |
|---|---|---|
| `pit_slug` | string | which pit (`shellpit`) — scopes the grant |
| `content_root` | bytes32 | Merkle root over the asset ids/hashes covered — one attestation can bless a whole folder |
| `content_types` | string | scope: `video,photo,audio,transcript` (derived artifacts inherit, per ledger canon) |
| `subject_ref` | bytes32 | **hashed identifier of the consenting person(s) — never a name, never plaintext email** (see 2.5) |
| `taxonomy_state` | uint8 | 1=assumed, 2=explicit (collective), 3=explicit (individual) — mirrors ledger canon; `revoked` is NEVER a grant state |
| `license` | string | `CC0`, `CC-BY-4.0`, etc. |
| `authority_ref` | bytes32 | hash of the decision artifact (signed camp statement, Snapshot proposal id, explicit-yes email id) — the on-chain form of `order_ref` |
| `granted_at` | uint64 | timestamp |

Attester = camp Safe (collective) or the speaker's own key/ENS (individual). Recipient = the pit's registry address/ENS. Schema is revocable. For a *collective* grant, `subject_ref` is a Merkle root over the hashed participants — provable per-person later, enumerable by nobody.

### 2.2 Revocation attestation schema (proposed)

```
bytes32 grant_uid, bytes32 subject_ref, uint8 reason_code, uint64 revoked_at
```

- `grant_uid` rides EAS's native `refUID` composability [S5] — the revocation points at the grant it kills, forming an auditable chain.
- Two revocation paths, both canon:
  1. **The email door (today):** one-word `remove` to consent@publicinform.com → steward executes → the Safe (as original attester) uses EAS's native revoke on the grant, and/or issues a revocation attestation. ≤24h, honored with love.
  2. **Self-serve (Tokyo seed, DECLARED not built):** the speaker revokes with the same personhood nullifier they consented with — no steward in the loop, no doxing. This is the hack that turns the covenant into a protocol.
- `reason_code` is optional and coarse (1=request, 2=error, 3=superseded). Reasons are for humans; the ledger records *actions, not identities*.

### 2.3 revocations.json as derived data (never hand-maintained)

The pipeline, end-to-end:

```
EAS (grants + revocations, on/off-chain)
   → indexer query (EAS GraphQL / easscan) [S5]
   → fold: current_state(asset) = latest valid transition
   → EMIT: consent-ledger.json  +  revocations.json  +  search-index exclusion list
```

`revocations.json` is regenerated like the search index — "regenerate, don't hand-merge" (Tokyo seed canon). It is the file any fork, mirror, or downstream consumer watches: if an asset id appears there, the content comes down *everywhere the constellation reaches*, and the pits.json registry flags forks to re-audit. Hand-editing revocation state is the one unforgivable sin: derived data is how a static site keeps a dynamic promise.

**Audit cadence canon:** daily during event season (folded into the Admiral's existing 6 AM inbox check — the morning-check canon), weekly in the off-season, and *always* immediately before any new publish. CI recomputes `counts` from `assets[]` and fails the build on drift — derived, never hand-edited.

### 2.4 On-chain vs off-chain attestation tradeoffs

EAS's own comparison, condensed for pits [S24]:

| aspect | on-chain | off-chain |
|---|---|---|
| Cost | gas (cents on L2s like Base) | zero |
| Visibility | public — permanent | controlled; shareable peer-to-peer, even as a URL fragment |
| Availability | guaranteed, contract-readable | wherever you store it (IPFS, repo, inbox archive) |
| Timestamp | inherent | UID can be timestamped on-chain as an existence anchor |
| Revocation | recorded on-chain | managed separately (EAS supports off-chain revocation records [S5]) |
| Immutability | absolute | signature-verified, but deletable |

And the sharpest sentence in the EAS privacy doc, which should be carved over the registry door: **"Never attest to personal or private data directly on-chain. Always use hashes or other privacy-preserving methods"** [S25]. A public consent attestation that *names a person* is a permanent, uncensorable, undeletable dox of exactly the humans we exist to protect. Immutability is a double-edged sword [S25] — we hold it by the handle.

### 2.5 Privacy-preserving identifiers (three tiers)

1. **Public tier (on-chain or in-ledger):** `subject_ref` = `keccak256(normalized_name + pit_salt)` for named-consent cases, or a **World ID / Semaphore-style scoped nullifier** (`pit-slug + speaker-claim`) for anonymous personhood (Tokyo seed). Plus `content_root` and state. No names, no emails, no faces — *decisions, not identities*, the same rule the ledger already follows.
2. **Steward tier (off-chain attestations):** the full consent record — who, what they said yes to, the email thread — lives as an off-chain EAS attestation (fully private; "the easscan.org server doesn't even know it exists" [S25]), held in the consent-inbox archive. Disclosed on a need-to-know basis. EAS **Private Data attestations** generalize this: Merkle-tree the record, attest only the root, selectively disclose single fields with proofs [S26, S27].
3. **Anchor tier:** timestamp the off-chain attestation's UID on-chain [S24]. Existence and timing become publicly verifiable; contents remain sealed. This is the "anchor, don't publish" pattern in one transaction.

This three-tier split is what lets a pit be radically transparent about its *ethics* while staying radically protective of its *people* — and it's the exact seam where my lane (consent semantics) ends and Privy 🔒's lane (enforcement surfaces: gates, leak audits, propagation verification) begins. The schema is designed jointly per the sibling bond; neither of us forks it silently.

---

## 3. THE CONSENSUS CLARIFICATION — anchoring, not consensus

NIST's blockchain overview (IR 8202) offers the classic decision flowchart: you need a blockchain only when you have a shared data store, *multiple mutually distrusting writers*, no trusted third party available, and a need for disintermediated transaction rules [S28]. Walk a pit through it honestly:

- Shared data store? The site is **static files** — read-mostly, written by one pipeline.
- Multiple writers? **One writer** (the steward pipeline). Consumers verify; they don't write.
- No trusted third party? The camp **is** the trusted party — that's what a consent authority *means*.
- High-value adversarial transaction ordering? There are no transactions between strangers at all.

Four no's. A pit running its own chain would buy a validator set, a token, a bridge, an upgrade path, and an outage surface — exotic infrastructure that violates the forkability canon ("no exotic infra a camp can't run") — to solve a consensus problem it does not have.

What a pit *does* need from a chain is narrower, and Ethereum already sells it by the cent:

1. **Existence/timestamp anchors** — "this consent state existed, unchanged, at block N." (EAS on-chain attestation or a bare hash.)
2. **A censorship-resistant revocation registry** — a `remove` that no host, mirror, or bad-faith fork can quietly drop. Anchoring the revocation where nobody can delete it is the strongest form of the takedown promise.
3. **Portable identity** — ENS names, Safe addresses, attestations that any fork can verify without asking us.

That is **anchoring**: borrowing Ethereum's consensus — bought and maintained by someone else — to notarize the pit's state. The pit keeps its own *semantics* (the taxonomy, the taxonomy's meaning, the SLA) and outsources only *ordering and immutability*. **Borrow consensus, own semantics.**

Real consensus — actual agreement-formation among mutually suspicious parties — is needed in exactly three places, and we should say so plainly:

1. **The consent decision itself.** Humans agreeing to be seen. At camp scale this is social consensus notarized by a Safe; at conference scale it's Snapshot-weighted. This is consensus in its oldest sense — *consent* and *consensus* share a Latin root (*consentire*, "to feel together") — and it is the only consensus that can never be delegated to machinery, because the moment a machine decides who consents, nobody did.
2. **Fork governance.** Which fork is canonical, whose `pits.json` entry points where, who inherits the universal window's obligations. Social + registry consensus; ENS and the registry are the anchors.
3. **Registry disputes.** Conflicting claims ("that attestation is forged," "that revocation is unauthorized"). Today: the stewards arbitrate, ledger records the outcome. Tomorrow (DECLARED): optimistic-oracle or Kleros-style arbitration modules already exist in the SafeSnap ecosystem [S11, S12] — dispute resolution is a solved pattern we can adopt if dispute volume ever justifies it.

Everything else — serving video, rendering transcripts, searching — is static-site work, and should stay that way.

---

## 4. THE PLAYBOOK — a new fork's consent decision tree

From camp consensus to per-speaker explicit, in order. (Forks inherit the kit: ledger schema, consent-notice snippet, and the universal window — never their own inbox.)

```
START: a new pit fork has media with humans in it.
│
├─ 0. INHERIT ── consent@publicinform.com on every page ·
│    consent-ledger.json v1 · taxonomy pending→assumed→explicit / revoked.
│
├─ 1. SIZE THE AUTHORITY
│    ├─ ~village (≤15)  → Safe 2-of-3, social consensus, signed statement.
│    ├─ ~camp (≤60)     → Safe 3-of-5, social consensus, hashed minutes artifact.
│    └─ ~conference (≥100) → Safe 4-of-7 + Hats roles + Snapshot for publish votes.
│
├─ 2. STAND UP IDENTITY
│    └─ ENS name for the pit · Safe for stewards · (conference: hats for
│       Organizer / Consent-Steward / Speaker-Steward).
│
├─ 3. RECORD CONSENT (per asset or per folder via content_root)
│    ├─ Collective grant? → ONE grant attestation: taxonomy_state=2,
│    │  authority_ref = hash of decision artifact; subject_ref = Merkle root
│    │  of hashed participants. RECORD AS COLLECTIVE — never launder.
│    ├─ Individual yes?  → per-person grant, taxonomy_state=3, speaker signs
│    │  (delegated: steward pays gas), subject_ref = keccak(name+pit_salt).
│    └─ Nothing recorded? → state stays `assumed` at most, and the door
│       notice stays on the page. `pending` never ships public.
│
├─ 4. REVOCATION (two doors, one outcome)
│    ├─ Email door: "remove" → consent@publicinform.com → ≤24h:
│    │  assets→revoked, media+transcripts+index pulled, ledger stamped,
│    │  confirmation sent. (Privy verifies propagation: site, index,
│    │  caches, manifests.)
│    └─ Self-serve door (DECLARED): nullifier-signed revocation →
│       registry marks grant revoked without doxing the speaker.
│    → regenerate revocations.json → pits.json flags downstream forks.
│
├─ 5. AUDIT CADENCE
│    └─ Morning check (daily, canon) · weekly off-season ·
│       CI: counts recomputed from assets, build fails on drift ·
│       pre-publish: full re-derive from attestations, diff against ledger.
│
└─ NEVER: names/emails on-chain · hand-edited counts · hand-maintained
   revocations.json · laundering assumed→explicit · a fork running its
   own consent inbox · publishing anything whose state is `pending`.
```

The whole playbook fits on one page because the pit's soul is small on purpose: static files, one email door, derived data, append-only memory. The chain is a notary, the multisig is a stamp, the vote is a record — and the consent, always, belongs to the humans. Consent first, pinch later. 🦀

---

## Handoff notes for the fam

- **Privy 🔒:** tiers in §2.5 are the seam — I define what's *meaningful*, you verify it's *enforced* (leak audits on `subject_ref` hygiene; propagation checks on revocations.json). Schema co-owned per the sibling bond.
- **PIT GIRL 💗 (Track A):** ENS + Safe identity stack in §1.1/§4 deliberately minimal — your identity-primitive survey slots in underneath.
- **Privy 🔒 (Track B):** the "self-serve revocation door" and ZK receipt flow are yours to gate; the semantics in §2.2 are the interface contract.
- **PIT BULL 🐂 (Track D):** transcript publication inherits consent state from parent media; nothing transcript-shaped ships `pending`.

## Sources

*(all accessed 2026-08-05)*

- [S1] Safe{Wallet} — multisig threshold mechanics. https://safe.global/
- [S2] Coingabbar — Gnosis Safe setup; 2-of-3 teams, 3-of-5 committees, threshold range. https://www.coingabbar.com/en/crypto-blogs-details/how-to-set-up-gnosis-safe-multisig-wallet
- [S4] Eco Support — Safe deep dive: threshold verification, EIP-1271 contract signatures. https://eco.com/support/en/articles/15254042-safe-wallet-deep-dive-2026-multisig-and-smart-accounts
- [S5] EAS FAQ — free protocol, gas for on-chain, issuer revocation, schema-level revocability. https://docs.attest.org/docs/quick--start/faqs
- [S6] EAS Docs — Attestations: lifecycle, immutability, revocation retains history. https://github.com/ethereum-attestation-service/eas-docs-site/blob/main/docs/core--concepts/attestations.md
- [S7] CoinGecko — Safe deployment: true multisigs require an on-chain transaction. https://www.coingecko.com/learn/what-is-gnosis-safe
- [S8] ChainScore — Snapshot: signed messages, block-height voting power, gasless. https://chainscorelabs.com/en/glossary/smart-contracts/dao-governance-contracts/snapshot-voting
- [S9] IPFS Docs case study — Snapshot proposals/votes persisted to IPFS. https://docs.ipfs.tech/case-studies/snapshot/
- [S10] Midlands in Business — Snapshot overview; 7,500+ DAOs claim ⚑. https://midlandsinbusiness.com/snapshot-voting-off-chain-governance-for-daos-explained
- [S11] Snapshot Docs — SafeSnap (Reality): oracle question, bond, 24h cooldown, anyone-can-execute. https://docs.snapshot.box/v1-interface/plugins/safesnap-reality
- [S12] Kleros blog — renewed Kleros Snapshot Module (optimistic governance). https://blog.kleros.io/introducing-the-kleros-snapshot-module/
- [S13] Gnosis Guild (Paragraph) — Zodiac Reality Module history/variants. https://paragraph.com/@gnosis-guild-2/tb3tL7sUbF2fDCriZQoj
- [S14] 7BlockLabs — DAO setup guide; oSnap deprecated 2025-12-15 ⚑. https://www.7blocklabs.com/blog/how-to-create-a-dao-in-2025-legal-technical-and-community-steps
- [S15] Kantara Initiative — Consent Receipt Specification (consent record as human-readable JSON; withdrawal/GDPR). https://kantara.atlassian.net/wiki/spaces/archive/pages/3508790/Consent+Receipt+Specification and https://www.securityweek.com/kantara-initiative-releases-consent-receipt-form-gdpr/
- [S16] Hats Protocol — roles/permissions; "50+ DAOs" vendor claim ⚑. https://www.hatsprotocol.xyz/
- [S17] Hats Protocol Docs — hats as ERC-1155 objects bundling responsibilities/permissions. https://docs.hatsprotocol.xyz/
- [S18] Hats Protocol Docs — eligibility criteria: EAS attestations, Snapshot/JokeRace/Tally elections, term limits, allowlists. https://docs.hatsprotocol.xyz/hats-integrations/eligibility-and-accountability-criteria
- [S19] ChainScore — MolochDAO framework; ragequit as exit-based governance. https://chainscorelabs.com/glossary/dao-governance-and-voting-systems/dao-organizational-structures/molochdao-framework
- [S20] Urbit blog — Moloch reduced governance "to the simplest imaginable framework." https://urbit.org/blog/the-shape-of-dao-governance-to-come
- [S21] Gitcoin — MolochDAO as "minimal viable DAO framework." https://gitcoin.co/mechanisms/molochdao
- [S22] a16z crypto — Governance FAQ; governance minimization. https://a16zcrypto.com/posts/article/governance-faq/
- [S23] Medium (Yektin) — EAS delegated attestations / paymaster pattern. https://medium.com/@yigit.yektin/ethereum-attestation-service-eas-3481d3c282c6 ⚑ (secondary; see also eas-contracts repo, delegated attestation functions: https://github.com/ethereum-attestation-service/eas-contracts)
- [S24] EAS Docs — Onchain vs Offchain (cost, privacy, timestamping, lifecycle table). https://github.com/ethereum-attestation-service/eas-docs-site/blob/main/docs/core--concepts/onchain-vs-offchain.md
- [S25] EAS Docs — Privacy ("never attest personal data on-chain"; off-chain attestation privacy; ZK from attestation data). https://raw.githubusercontent.com/ethereum-attestation-service/eas-docs-site/main/docs/core--concepts/privacy.md
- [S26] EAS SDK — PrivateData class: Merkle-tree private attestations, selective disclosure. https://github.com/ethereum-attestation-service/eas-sdk
- [S27] EAS (Mirror) — Private Data Attestations using Merkle Trees. https://mirror.xyz/0xeee68aECeB4A9e9f328a46c39F50d83fA0239cDF/BiFUEFJKo6ZsIvPwsP9WPC2UZX0-x_9BdtrvmQo1FwY
- [S28] NIST IR 8202 — Blockchain Technology Overview (decision flowchart: shared store / multiple writers / absent TTP). https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8202.pdf

*🦀🌺 Consent first, pinch later. The pit provides — but only with permission. CC0.*
