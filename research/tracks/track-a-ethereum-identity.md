# TRACK A — ETHEREUM IDENTITY & THE BHUTAN PRECEDENT
*owner: PIT GIRL 💗 · research cycle №1 "The Consensual Pit" · CC0 · draft-in-progress (filed early, filed often)*
*last saved: 2026-08-05 04:05 UTC · STATUS: COMPLETE*

> Radical honesty contract: every factual claim carries a source URL + access date (2026-08-05). Unverifiable = ⚑ UNVERIFIED. Declared visions stay DECLARED.

---

## 1. THE BHUTAN CASE (the anchor) 🇧🇹

### 1.1 Timeline — what the Kingdom actually did, in order

| date | event | source |
|---|---|---|
| 2020 | Digital Drukyul Flagship Program initiated by the PM's Office; NDI project initiated by Royal Command to the GovTech Agency; SSI chosen as foundation "guided by His Majesty the King's personal vision to provide every citizen with the right to privacy" | ToIP Case Study, §1 (accessed 2026-08-05) https://trustoverip.org/wp-content/uploads/Case-Study-Bhutan-NDI-National-Digital-Identity-ToIP-Digital-Trust-Ecosystems-V1.0-2024-05-21.ext_.pdf |
| July 2023 | **National Digital Identity Act of Bhutan 2023** passed by Parliament — governance anchor establishing "secure, privacy-enhancing digital credentials" | ToIP Case Study, §4 (2026-08-05) |
| October 2023 | NDI launches **nationwide** on **Hyperledger Indy** (Indicio Network, `did:sov` method); HRH The Gyalsey (Crown Prince Jigme Namgyel Wangchuck) becomes the nation's first digital citizen. "First country in the world with a self-sovereign digital identity" at national scale | ToIP Case Study (2026-08-05); Biometric Update (2026-08-05) https://www.biometricupdate.com/202510/bhutan-begins-migrating-self-sovereign-digital-id-to-ethereum |
| August 2024 | Migration from Hyperledger Indy to **Polygon** (for "better security and performance"; blockhead cites Polygon's "zero-knowledge protocols and scalability") | Biometric Update (2026-08-05); Blockhead (2026-08-05) https://www.blockhead.co/2025/10/14/self-sovereign-identity-goes-national-inside-bhutans-ethereum-transition/ |
| June–July 2025 | GovTech Agency + Ethereum Foundation run a dApp **hackathon** powered by NDI | Biometric Update (2026-08-05) |
| September 2025 | NDI launches **digital signature platform** — every signature tied to a verifiable credential in the citizen's NDI wallet, secured with DIDs | Biometric Update (2026-08-05) |
| **October 13, 2025** | **Ethereum integration announced at ceremony in Thimphu**: "first nation to anchor its national digital identity system on Ethereum." Attendees: PM Lyonchen Tshering Tobgay, GovTech Secretary Jigme Tenzing, Druk Holding & Investments chair, HRH the Crown Prince, **Vitalik Buterin**, **EF President Aya Miyaguchi** | Aya Miyaguchi on X (2026-08-05) https://twitter.com/AyaMiyagotchi/status/1977798764485361966 · Daily Bhutan https://www.dailybhutan.com/article/bhutan-makes-history-as-the-world-s-first-nation-to-launch-a-national-digital-id-on-ethereum · The Block https://www.theblock.co/post/374480/bhutan-migrates-national-digital-id-system-ethereum (all 2026-08-05) |
| Q1 2026 (target) | Full migration of all citizen credentials to Ethereum mainnet — announced target. As of research date (2026-08-05): completion confirmed by ⚑ UNVERIFIED — the GovTech Agency said integration was complete in Oct 2025 with credential migration to follow; no primary 2026 completion announcement found in this research pass | crypto.news (2026-08-05) https://crypto.news/bhutan-migrates-digital-identity-system-ethereum-2025/ |

### 1.2 The tech stack (as documented in the official ToIP case study, May 2024 — CC-BY 4.0)

This is the part most coverage gets vague on. The stack, per the case study written WITH the NDI team:

- **DIDs:** `did:sov` method — Decentralized Identifiers for all ecosystem parties (individuals, orgs, government), resolved via the Verifiable Data Registry. [ToIP §6]
- **Verifiable Credentials:** W3C VC standard; **AnonCreds** format with **CL signatures** — and this is the ZK answer: *"parties in the NDI ecosystem can exchange verifiable data supported by zero-knowledge proof (ZKP) protocols. For example, individuals can confirm that they are above the age of 18 without disclosing their actual age."* Selective disclosure is native: a holder answers a proof request by disclosing only chosen attributes from one or more credentials. [ToIP §6]
- **Verifiable Data Registry:** Hyperledger Indy blockchain + Indicio-run network at launch → Polygon (Aug 2024) → **Ethereum mainnet** (Oct 2025 announced). Stores issuer public keys, DID documents, schemas, cryptographic metadata — **not personal data**. [ToIP §5]
- **NDI Trust Registry:** list of trusted Organizational Public DIDs (banks, telcos, university, GovTech). [ToIP §5]
- **Platform layer:** "Acentrid" — a custom protocol layer forked from Evernym's open-sourced **Verity** platform. ⚑ Contradicts a Decrypt claim that the system was "initially built with Cardano developer IOG" (https://decrypt.co/344166/bhutan-national-digital-id-ethereum-early-2026, accessed 2026-08-05) — the ToIP case study (authored with the NDI team itself) names Evernym Verity + Hyperledger Indy, no IOG/Cardano involvement. The Decrypt claim is judged UNRELIABLE against the primary-ish source.
- **Revocation:** Revocation Service with active / suspended / revoked statuses. [ToIP §6]
- **Wallet backup:** sharding — encrypted wallet data distributed across shards on undisclosed servers. [ToIP §6]

### 1.3 What "anchor national ID on Ethereum" precisely means

Per multiple corroborating reports and ethereum.org's own decentralized-identity page (which now cites Bhutan):

- **Personal data is NOT on-chain.** Citizen records stay in the citizen's wallet / government off-chain systems. What goes on Ethereum: **cryptographic hashes, issuer schemas, DIDs, public keys, credential status** — the trust metadata. "By anchoring issuer schemas of these credentials on Ethereum, the system ensures they are authentic, tamper-proof, and can be verified by any party without querying a central authority." [ethereum.org/decentralized-identity, accessed 2026-08-05; crypto.news (2026-08-05); bitcoinist (2026-08-05) https://bitcoinist.com/bhutan-picks-ethereum-to-anchor-citizen-identity-on-the-blockchain/]
- Ethereum's role = **the public, neutral, maximally-decentralized notary** for the identity layer. GovTech Secretary Jigme Tenzing: Ethereum's decentralization makes it "virtually impervious to disruption." [Biometric Update (2026-08-05)]
- The ZK piece (AnonCreds/CL selective disclosure) lives in the **credential presentation layer**, not on Ethereum itself — a crucial architectural distinction for the pit mapping below.

### 1.4 How citizens actually use it (verified use cases)

- **Onboarding:** biometric facial scan matched against the DCRC (civil registry) database → Foundational ID VC in the NDI Wallet (iOS/Android). [ToIP §7; App Store listing (2026-08-05)]
- **Passwordless login** ("Login with Bhutan NDI") to the G2C portal (QR/deeplink → wallet consent) and to Bank of Bhutan's mBOB app (persistent relationship DID). [ToIP §7]
- **eKYC:** banks, telcos; customized per sector. [ToIP §7]
- **Passport applications:** NDI wallet + eKYC integrated with the national passport system (photos/signatures uploaded via wallet) — first core government transactional service integration. [Ministry of Foreign Affairs press release via idtechwire (2026-08-05) https://idtechwire.com/bhutan-integrates-ndi-wallet-with-passport-system-for-ekyc-enabled-applications/]
- **Credentials in circulation:** Foundational ID, permanent address, mobile number (TashiCell), academic (Royal University), employment (DHI, RCSC), driver's/learner's licenses, vehicle ownership, audit clearance + self-attested (email, telephone, allergy). [ToIP §3]
- **Scale:** 234,568 foundational IDs issued by end of March 2025 (~3 in 10 residents of the ~750–800k population), "ninefold jump in twelve months." [The Token Dispatch (2026-08-05) https://www.thetokendispatch.com/p/the-fortress-and-the-phone]
- **Reality checks (honesty):** smartphone access + digital literacy remain obstacles in remote areas; government trained village coordinators, partnered with Bhutan Post, optimized the app for offline use. [Biometric Update (2026-08-05) https://www.biometricupdate.com/202507/bhutan-upgrades-digital-identity-wallet-including-liveness-and-p2p-chat]
- Bhutan NDI's own GitHub org now describes the platform as "all anchored on Ethereum for long-term security and resilience." [github.com/Bhutan-NDI (2026-08-05)]

### 1.5 The five lessons Bhutan teaches a pit

1. **Anchor, don't store.** Hashes/schemas/keys on-chain; humans' data off-chain. This is EXACTLY the pit pattern: manifest hashes anchored, transcripts served static.
2. **The ZK lives at the edges.** Selective disclosure happens holder↔verifier; the chain just notarizes the schema. Pits don't need ZK-on-chain — they need ZK-at-the-doorbell.
3. **Consent is a first-class trust task.** Every NDI sharing flow is a wallet consent pop-up. Consent UX = the protocol.
4. **Legal anchor before tech anchor.** Bhutan passed the NDI Act (July 2023) BEFORE nationwide launch (Oct 2023). Pits' equivalent: the consent covenant + manifest spec before the harvest.
5. **Small is an advantage.** ~750k people, small team, small budget, world-first. A village CAN run sovereign identity infra. (Biometric Update's phrase: "a small team and smaller budget." https://www.biometricupdate.com/202312/bhutan-stands-up-self-sovereign-identity-with-a-small-team-and-smaller-budget (2026-08-05))

---

## 2. THE PRIMITIVES LANDSCAPE (Aug 2026)

| primitive | what it is | maturity | cost to a pit | what a pit could use it for |
|---|---|---|---|---|
| **ENS** | Human-readable names (`name.eth`) → addresses + arbitrary text records; hierarchical subnames | Very high (live since 2017; ENSv2 in progress) | `$5/yr` for a 5+ char `.eth` + mainnet gas; **subnames free** (parent's choice), gasless off-chain subnames via CCIP-Read | `speaker.pit.eth` identity anchors on transcripts; consent metadata in text records; pit registry naming |
| **EAS** (Ethereum Attestation Service) | Public-good registry for signed claims ("attestations") about anything, on-chain **or off-chain**; schemas; native revocation | Production; deployed on mainnet + major L2s | **Off-chain attestations: \$0** (EIP-712 signatures, stored anywhere); on-chain: gas only (cents on L2) | **Consent grants as attestations** — speaker-signed, revocable, storable in-repo as derived data |
| **SIWE** (Sign-In with Ethereum, EIP-4361) | Standard message format for wallet-based authentication; no tx, no gas | **Finalized** ERC (Aug 2025); universal wallet support | \$0 | Sign consent/revocation messages client-side; gate interactive lanes where a verifier exists |
| **World ID** (World) | ZK proof-of-personhood from Orb iris verification; Semaphore-style nullifiers scoped per app+action → anonymous-but-human | Production; **~18M Orb-verified humans**, 39M+ World App accounts | Free for users; dev integration via World Developer Portal / IDKit; on-chain verify on World Chain or Ethereum | Anonymous-but-human **takedown/consent lane**; doorbell for talk-to-the-pit |
| **Human Passport** (ex-Gitcoin Passport) | Aggregates web2/web3 "stamps" → Unique Humanity Score; on-chain predicates ("score > 20") | Production; acquired by Holonym Foundation (Feb 2025), now under human.tech; ~2M users at acquisition | Mostly \$0 for users (some stamps cost gas); API key for devs | Lighter, biometric-free humanity check; score-gated doorbell |
| **Verax** | Shared on-chain attestation registry (Consensys/Linea-led community), multi-chain | Live; ~20 issuers; lower visible activity than EAS (docs note "last updated 10 months ago") | Gas per attestation | Alternative attestation rail; redundant with EAS for pit purposes |
| **Hats Protocol** | DAO-native **roles as non-transferable ERC-1155 "hats"** — revocable delegation of authority/responsibility, composable with token gates | Production v1; niche but real | L2 gas for setup | Organizer/archivist/consent-steward roles for a pit; pairs with Safe multisig |

### 2.1 ENS — names as identity
- **2026 state:** ENS Labs **scrapped the planned Namechain L2 on Feb 6, 2026** and is shipping **ENSv2 fully on Ethereum mainnet** — hierarchical registries giving each `.eth` name its own registry, so name owners control subname ownership/transfer rules directly (a camp could governance-gate its subname tree). [The Block https://www.theblock.co/post/388932/ens-labs-scraps-namechain-l2-shifts-ensv2-fully-ethereum-mainnet (2026-08-05); ENS docs https://docs.ens.domains/contracts/ensv2/overview/ (2026-08-05)]
- **Pricing (official):** 5+ chars `$5/yr`, 4 chars `$160/yr`, 3 chars `$640/yr`, paid in ETH on mainnet + gas. **ENS sets no fees for subnames — the parent owner decides.** [support.ens.domains https://support.ens.domains/en/articles/12238910-ens-pricing-how-much-do-names-cost (2026-08-05)]
- **Off-chain subnames are gasless** (CCIP-Read / EIP-3668 resolution); issuance providers (e.g., Namespace) explicitly offer free offchain subnames at any volume. [namespace.ninja (2026-08-05)]
- **Family precedent:** OSO P.I.T. won **Most Creative Use of ENS at ETHGlobal New Delhi** with ENS subnames for the orchestra. ⚑ Family canon (Shaka's account; /shared/kb/tokyo-worldid-consent-hack.md) — external confirmation NOT found in this research pass; treated as DECLARED, not independently verified. The ENS-subnames-as-community-identity pattern is real and documented regardless.

### 2.2 EAS — attestations, and yes, consent can be one
- Two rails: **on-chain** (attestation UID in the EAS contract; costs gas — cents on an L2) and **off-chain** (EIP-712 signed message; free; stored/shared anywhere; can be anchored later by hash if wanted). [EAS docs https://docs.attest.org/docs/core--concepts/how-eas-works (2026-08-05)]
- **Revocation is native:** the issuer can revoke on-chain or off-chain attestations (state → "revoked"; not deleted — the audit trail persists); schemas declare whether they're revocable. Delegated revocation also exists in the SDK. [EAS FAQ https://docs.attest.org/docs/quick--start/faqs (2026-08-05); eas-sdk npm (2026-08-05)]
- Schemas are simple typed field lists — a `PITConsent` schema (`sessionId, consentState, scope, timestamp`) is an afternoon's work.
- This is the closest living analog to Bhutan's VCs in the Ethereum-native world: signed claims, issuer-keyed, revocable, verifiable without phoning the issuer.

### 2.3 SIWE — the wallet is the login
- EIP-4361 standard message ("domain wants you to sign in with your Ethereum account…"), signed with the wallet, verified by checking the recovered address. **ERC-4361 reached Final status in Aug 2025.** [eips.ethereum.org/EIPS/eip-4361 (2026-08-05); etherworld.co https://etherworld.co/2025/08/06/erc-4361-finalized-what-sign-in-with-ethereum-means-for-ethereum/ (2026-08-05)]
- Zero gas, zero cost, works in every major wallet. On a **pure static site** it can still do one beautiful thing: let a speaker **sign** a consent/revocation message client-side, producing a portable signed artifact (no backend needed to *create* proof — only to *gate* content, which is where Track B's encryption comes in).

### 2.4 World ID — anonymous-but-human
- Orb iris verification → World ID → ZK proofs of uniqueness with **nullifiers scoped to (app, action)** — a speaker can prove "a unique human" without revealing which one. [world.org/world-id (2026-08-05); World docs https://docs.world.org/world-id/overview (2026-08-05)]
- Scale: **nearly 18M Orb-verified humans across 160 countries**; 39M+ World App accounts. [world.org blog "World ID Full-Stack Proof of Human" (2026-08-05); StockTitan (2026-08-05)]
- **Honest caveats:** legal blocks/suspensions in several jurisdictions over biometric-data concerns (documented through 2025); geographic Orb access is uneven — a village in the Andes may have no Orb nearby; and even friendly observers (incl. Vitalik) flag the single-vendor Orb hardware as a centralization risk. [Biometric Update https://www.biometricupdate.com/202501/world-network-reaches-10-million-verified-humans-amid-continued-legal-blocks (2026-08-05); Plisio guide (2026-08-05)]
- Cost: free for end users; developers integrate via IDKit + Developer Portal; verification needs either World's cloud verifier or an on-chain verify call (World Chain / Ethereum) — i.e., **not fully static-site-native** without one small verification hop.

### 2.5 Human Passport — the biometric-free alternative
- Gitcoin Passport → acquired by **Holonym Foundation (Feb 10, 2025)** → **Human Passport** under human.tech. Aggregates "stamps" (web2 accounts, on-chain history, BrightID-ish signals) into a **Unique Humanity Score**; Q1 2025 added **native on-chain predicates** ("must have score above 20") enforceable without a trusted server. [CoinDesk https://www.coindesk.com/business/2025/02/10/digital-identity-startup-holonym-acquires-gitcoin-passport (2026-08-05); passport.human.tech blog (2026-08-05)]
- Weaker uniqueness guarantee than an Orb, but **no hardware, no biometrics, globally reachable** — the pragmatic doorbell for villages.

### 2.6 Verax & Hats — the supporting cast
- **Verax:** shared on-chain attestation registry on Linea + other EVM chains, ~20 issuers. Conceptually overlaps EAS; smaller adoption; fine as an alternative rail, not a reason to split the pit's consent format. [docs.ver.ax (2026-08-05); Linea docs (2026-08-05)]
- **Hats Protocol:** roles as revocable, non-transferable ERC-1155 tokens — "archivist hat," "consent-steward hat" — composable with token gates and Safe. Perfect for the *organizer* side of a pit's identity (who may bless, who may publish), leaving speaker-side to ENS+EAS. [docs.hatsprotocol.xyz (2026-08-05); GitHub Hats-Protocol/hats-protocol (2026-08-05)]

---

## 3. THE PIT MAPPING — ranked for a static-site, ~$0, forkable-by-any-village protocol

Feasibility scoring: ⭐ = cost, infra, and fork-simplicity combined (5 = a village can do it this weekend).

### 🥇 1. Speaker identity via ENS on transcripts — ⭐⭐⭐⭐⭐ (ship first)
One parent name per pit (`zuitzpit.eth`, `$5/yr`) or subnames under a family root (`speaker.pit.eth`). Speakers get (or bring) names; transcript speaker labels link to ENS profiles; consent metadata lives in text records. Resolution is read-only via public RPC + CCIP-Read — **works from a static site, zero backend**. This is the Delhi ancestor's pattern, leveled to canon. Gasless off-chain subnames mean even a 300-speaker pit costs nothing beyond the parent renewal.
*Bhutan parallel:* their Organizational DIDs in the Trust Registry = our pit's ENS names in the manifest.

### 🥈 2. Consent grants as EAS attestations — ⭐⭐⭐⭐½
The consent taxonomy (`pending → assumed → explicit`, `revoked`) becomes a `PITConsent` EAS schema. Speakers sign **off-chain** attestations (free, EIP-712, via SIWE-flavored wallet UX) — the signed JSON **lives in the repo** as the consent ledger, regenerated into the manifest exactly like the search index ("regenerate, don't hand-merge" — existing canon). Revocation = a second signed attestation; the UI derives state. Optional on-chain anchoring of the ledger hash on an L2 for pennies gives Bhutan-style notarization. Half-star docked only because wallet UX for non-crypto speakers needs a gentle fallback (signed email receipt → organizer co-signs).
*Bhutan parallel:* every NDI sharing flow is a consent pop-up; ours is a sign-this-consent flow. Same trust task, village scale.

### 🥉 3. Organizer multisig identity (Safe + ENS, optionally Hats) — ⭐⭐⭐⭐
The pit's publishing authority = a Safe multisig named `ops.<pit>.eth`, with Hats for role legibility (archivist, consent steward). Deploy cost is L2 gas (cents); no static-site conflict — the multisig signs *off-chain* statements (manifest releases, consent blessings) that the static site merely displays/verifies. Details belong to Track C (CRUSTY 🦀); flagged here as identity-layer-ready.

### 4. World ID anonymous-but-human takedown/consent lane — ⭐⭐⭐ (value ⭐⭐⭐⭐⭐)
The Tokyo seed (ENS × World ID, doorbell-not-library): a speaker proves personhood → exercises revocation without doxing themselves. **Feasibility caveat:** verification needs World's cloud verifier or an on-chain call — one small non-static hop per action. Architect it as an **optional module**: pits with a helper server (or an L2 wallet relay) enable it; pure-static pits fall back to signed-message revocation (#2). Orb access and jurisdiction blocks mean it can never be the *only* lane — radical honesty to villagers.

### 5. SIWE-gated access to private transmissions — ⭐⭐⭐ (natively), ⭐⭐⭐⭐ (with Track B)
SIWE alone can't gate a static site (nothing checks the signature). Its $0 superpower today: **client-side signing** of consent/revocation artifacts (#2's UX). True gating pairs with Track B (Privy 🔒): SIWE signature → key release / client-side decryption. Rated as an enabler, not a standalone.

### 6. Human Passport score-gating — ⭐⭐⭐
Drop-in alternative where Orbs are far away: "Humanity Score ≥ 20" as the doorbell for talk-to-the-pit or takedown lanes. On-chain predicates remove the trusted-server need. Weaker uniqueness than World ID; good enough for spam-resistance, not for high-stakes identity.

### 7. Verax — ⭐⭐
Redundant with EAS for the pit's consent format; keep watching, don't build on it first.

### The architectural takeaway (Bhutan's real gift to the pits)
**Anchoring, not storage. Verification at the edges, not the center. Legal/social covenant before code.** A pit's manifest + consent ledger = the credential; Ethereum = the neutral notary; ENS/EAS/SIWE = the village-affordable instruments; World ID/Human Passport = the doorbell. The library stays public; the doorbell checks humanity; the speaker can always take back.

---

## SOURCES CONSULTED (all accessed 2026-08-05)
1. ToIP Foundation Case Study: Bhutan NDI (May 2024, CC-BY 4.0) — https://trustoverip.org/wp-content/uploads/Case-Study-Bhutan-NDI-National-Digital-Identity-ToIP-Digital-Trust-Ecosystems-V1.0-2024-05-21.ext_.pdf
2. Biometric Update — Bhutan begins migrating self-sovereign digital ID to Ethereum — https://www.biometricupdate.com/202510/bhutan-begins-migrating-self-sovereign-digital-id-to-ethereum
3. Blockhead — Self-Sovereign Identity Goes National — https://www.blockhead.co/2025/10/14/self-sovereign-identity-goes-national-inside-bhutans-ethereum-transition/
4. Daily Bhutan — world's first national digital ID on Ethereum — https://www.dailybhutan.com/article/bhutan-makes-history-as-the-world-s-first-nation-to-launch-a-national-digital-id-on-ethereum
5. The Block — Bhutan to anchor its national digital identity system on Ethereum — https://www.theblock.co/post/374480/bhutan-migrates-national-digital-id-system-ethereum
6. Aya Miyaguchi on X (Oct 13, 2025) — https://twitter.com/AyaMiyagotchi/status/1977798764485361966
7. crypto.news — Bhutan moves national digital identity system to Ethereum — https://crypto.news/bhutan-migrates-digital-identity-system-ethereum-2025/
8. ethereum.org — Decentralized identity — https://ethereum.org/decentralized-identity/
9. idtechwire — NDI wallet × passport eKYC — https://idtechwire.com/bhutan-integrates-ndi-wallet-with-passport-system-for-ekyc-enabled-applications/
10. The Token Dispatch — The Fortress and the Phone — https://www.thetokendispatch.com/p/the-fortress-and-the-phone
11. Biometric Update — Bhutan wallet upgrade (Jul 2025) — https://www.biometricupdate.com/202507/bhutan-upgrades-digital-identity-wallet-including-liveness-and-p2p-chat
12. Biometric Update — Bhutan SSI small team/budget (Dec 2023) — https://www.biometricupdate.com/202312/bhutan-stands-up-self-sovereign-identity-with-a-small-team-and-smaller-budget
13. GitHub — Bhutan-NDI org — https://github.com/Bhutan-NDI
14. Decrypt — Bhutan to Anchor National Digital ID (contains the ⚑ IOG claim) — https://decrypt.co/344166/bhutan-national-digital-id-ethereum-early-2026
15. The Block — ENS Labs scraps Namechain — https://www.theblock.co/post/388932/ens-labs-scraps-namechain-l2-shifts-ensv2-fully-ethereum-mainnet
16. ENS support — pricing — https://support.ens.domains/en/articles/12238910-ens-pricing-how-much-do-names-cost
17. ENS docs — ENSv2 overview — https://docs.ens.domains/contracts/ensv2/overview/
18. Namespace — https://www.namespace.ninja/
19. EAS — https://attest.org/ · docs https://docs.attest.org/docs/core--concepts/how-eas-works · FAQ https://docs.attest.org/docs/quick--start/faqs · SDK https://www.npmjs.com/package/@ethereum-attestation-service/eas-sdk
20. EIP-4361 — https://eips.ethereum.org/EIPS/eip-4361 · finalized Aug 2025 https://etherworld.co/2025/08/06/erc-4361-finalized-what-sign-in-with-ethereum-means-for-ethereum/
21. World — https://world.org/world-id · https://world.org/blog/announcements/world-id-full-stack-proof-of-human · https://docs.world.org/world-id/overview
22. Biometric Update — World 10M verified / legal blocks — https://www.biometricupdate.com/202501/world-network-reaches-10-million-verified-humans-amid-continued-legal-blocks
23. CoinDesk — Holonym acquires Gitcoin Passport — https://www.coindesk.com/business/2025/02/10/digital-identity-startup-holonym-acquires-gitcoin-passport
24. Human Passport — https://passport.human.tech/ · Q1 2025 update https://passport.human.tech/blog/holonym-quarterly-update-q1-2025
25. Verax — https://docs.ver.ax/ · https://www.ver.ax/
26. Hats Protocol — https://docs.hatsprotocol.xyz/ · https://github.com/Hats-Protocol/hats-protocol
27. Family canon — /shared/kb/tokyo-worldid-consent-hack.md (DECLARED items marked as such)

*— PIT GIRL 💪🕳️✨ · accuracy IS beauty · CC0 · fork me like crazy 🍴*
