# Bravaura LLC Website — Project Handoff / Context

**New chat? Attach this file (or open the Website folder) and say "read _PROJECT-CONTEXT.md to catch up." That's all it takes to get a fresh Claude up to speed.**

## ⚡ Latest update — Aug 8, 2026: bold redesign
The site was fully redesigned from the old "elegant/minimal" look to a **bold, arty, human-made** style (Kendal's request — the minimal version read as "AI simple"). What changed:
- Vibrant **teal + gold + purple** (magenta/orange accents), thick ink borders with hard offset shadows, asymmetric layouts, scroll + hover animations, hand-drawn SVG doodles.
- Added a **hand-lettered font (Caveat)** for accents alongside Fraunces + Inter.
- Home page: asymmetric hero photo cluster, scrolling marquee, color-coded how-it-works, a 5-card services **bento** (now includes **Master Classes**), purple "why us" band, sticky-note testimonials.
- Voice rewritten to a warm-but-professional company **"we"** (not solo-Kendal). Removed the "Trusted by / teams that booked us" strip.
- **Still no prices** — pricing + quote pages use custom-quote framing; the old dollar estimator was replaced with a quote-request form.
- `_build/build_site.py` was **rewritten** as the source of truth; its OUT now auto-resolves to the Website folder. Photos use the ImagineArt customer IDs listed below.

*(The "Design (current)" section below describes the OLD look and is kept only for history.)*

---

## Animated logo (home hero) — added Aug 9, 2026
The home page hero opens with an **animated "painted-on" logo**: a paintbrush paints the swoosh, letters and star onto a blank canvas, then rests as the brush in the finished logo. Generated in **Higgsfield** (Seedance 2.0, image-to-video with a blank cream start frame and the finished logo as the end frame).
- Files: `assets/bravaura-logo-painting.mp4` (6s, 1080p, silent, ~1MB) + `assets/bravaura-logo-painting-poster.png` (final frame, used as the video poster).
- Markup lives in `index.html` (`<div class="hero-logo" id="hero-logo">`), styles in `css/styles.css` (`.hero-logo*`), behavior in `js/main.js`.
- It **plays once and stops** — do NOT add `loop`, or the logo will erase and repaint forever. For the same reason the small header/nav logo stays the static PNG.
- The video background was color-corrected to exactly match the page cream `#FBF7EF`, and the video edges are feathered with a CSS mask so no rectangle is visible.
- Falls back to the static logo when reduced-motion is on or the video fails to load.
- `assets/bravaura-logo-animated.mp4` is an earlier "shimmer" version that is **not used** anywhere — safe to delete.

## What this is
Marketing website for **Bravaura LLC** — mobile art events across New Jersey (birthday parties, paint & sip, corporate team building, face painting, master classes). Founder: **Kendal Plumstead**, TCNJ Art Education grad. Hand-coded static HTML/CSS/JS (not a website builder).

## Where it lives
Folder: `Dropbox\Kendal's Stuff\Bravaura\CoworkOS\Website`
- To preview: double-click `index.html` (opens the full site in a browser).
- Pages: index (home), services, pricing, gallery, about, contact, quote, faq, birthday-parties, paint-sip, corporate, face-painting, master-classes.
- Shared: `css/styles.css`, `js/main.js`. Logo: `assets/bravaura-logo-final.png`.
- Built by a Python script: `_build/build_site.py`. To regenerate everything: edit that script, then run `python3 build_site.py` (its OUT path may need setting to the Website folder). Small text tweaks can be made directly in the .html files with any text editor.

## Design (current)
Elegant / minimal. Disciplined palette: teal + gold accents, deep navy for dark sections. NO rainbow, NO confetti dots (an earlier "AI-looking" version had those — removed). Fonts: Fraunces (headings) + Inter (body). Real Bravaura logo in the header and footer.

## Pricing (IMPORTANT)
All specific dollar prices were **removed** — they were guesses. Everything now says **"Custom quote"** and the quote estimator says "we'll confirm by email." When Kendal sets real prices, update them in `_build/build_site.py` (search "Custom quote") or directly in the HTML.

## Photos — all AI-generated in ImagineArt, hosted at `https://asset.imagine.art/processed/<id>`
Main pics are CUSTOMER-focused (Kendal is NOT in them, by her request). Her real headshot is on the About page only.
- Hero (home): `09d8bba0-9b5f-432d-b3a9-39d74f039488` — kids holding up hot-air-balloon paintings
- Paint & Sip: `c9952430-d5b7-4c4b-b8ed-065acc8c2407` — adults at a home paint & sip
- Birthday: `f9a8cc9b-67ef-4b6e-8fd1-3b262ec15a77` — kids painting
- Corporate: `2b45db44-9905-422b-b9c8-bde0577d8afd` — coworkers painting
- Face painting: `bcb154fd-48ef-4029-8091-971b9a36416f` — kids showing painted faces
- Master classes: `f5757167-cbf3-4bb5-a2c1-c66b9297fa05` — high-school teens drawing in a home
- Gallery also includes: ladies' lake night `67f4b7da-ed40-424c-ad49-760dd9087a33` and kids' galaxy `d24aa654-58f8-4c92-b876-176230ec11e6`
- About page headshot (Kendal's REAL photo, not AI): `31f727e7-4cf5-4831-9552-23b287758064`

**Every image we ever generated is still saved in Kendal's ImagineArt library** (org: "kendalplumstead's personal"), including earlier versions with Kendal in them and a corporate/master-class set. Reusing an existing image is FREE. ImagineArt credits are spent ONLY when generating a brand-new image.

## Email (already working)
`kendal@bravaurallc.com` and `info@bravaurallc.com` forward to `bravaurallc@gmail.com` via Cloudflare Email Routing. (Receive/forward only; replies come from Gmail.)

## Publishing / going live (NOT done yet)
- Hosted on **Netlify**. Private preview: `main--bravaura-llc.netlify.app`. Public domain `bravaurallc.com` currently shows a **"Coming Soon"** page.
- Live publishing pipeline: **edit files → push to GitHub → Netlify auto-publishes** (~1 min).
- **TO DO:** confirm whether the local Website folder is linked to the GitHub repo. If not, set up **GitHub Desktop** pointed at the repo so Kendal can Commit + Push to publish. (Kendal's dad wants to teach her this — good idea.)
- Note: a cloud Cowork session generally CANNOT push to GitHub itself; publishing is done from Kendal's computer (GitHub Desktop) or by someone with repo access.

## Open items
- Publish to live when ready (set up / verify GitHub Desktop + repo link).
- Set real prices when decided (replace "Custom quote").
- Optional: swap AI photos for real event photos over time.
- Optional: exact logo on the aprons (AI couldn't render it exactly; aprons are plain black in the photos).

## How to edit (no credits)
- Text: open the .html file in Notepad, Ctrl+F to find words, change them (don't delete the `<tags>`), save, refresh index.html.
- Swapping to an already-generated photo, wording, colors, layout: free — just ask Claude.
- New AI photo = the only thing that uses ImagineArt credits.
