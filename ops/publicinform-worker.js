// ═══════════════════════════════════════════════════════════════
// Cloudflare Worker: serve The P.I.T. Protocol AT publicinform.com
// (not just a redirect — the site lives under the pretty domain)
//
// Deploy: Cloudflare dashboard → Workers & Pages → create Worker →
// paste this → then add route:  publicinform.com/*  (and
// www.publicinform.com/* if desired). Free tier is plenty.
//
// Remove/keep the existing 302 redirect: once this route is active,
// the Worker takes precedence for matched routes.
// — PIT BOY 🕳️😤 · 2026-07-25
// ═══════════════════════════════════════════════════════════════

const ORIGIN = "https://pit-protocol-6igjnwuy3u-lydgveie.taur.link";

export default {
  async fetch(request) {
    const url = new URL(request.url);
    // single-page site: every path serves the pit (future-proof for subpages)
    const target = ORIGIN + (url.pathname === "/" ? "/" : url.pathname) + url.search;

    const resp = await fetch(target, {
      headers: { "User-Agent": request.headers.get("User-Agent") || "pit-proxy" },
      redirect: "follow",
    });

    // pass through, but let the pretty domain own the address bar
    const out = new Response(resp.body, resp);
    out.headers.set("x-served-by", "publicinform.com → the pit 🕳️");
    // strip framing restrictions only relevant to the taur.link host context
    out.headers.delete("content-security-policy");
    return out;
  },
};
