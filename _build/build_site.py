# -*- coding: utf-8 -*-
"""Generate the Bravaura LLC multi-page website — bold, arty, human-made redesign.

Regenerate everything:  python3 build_site.py
Output goes to the Website folder (the parent of this _build folder) unless the
BRAVAURA_OUT environment variable overrides it.
"""
import os

OUT = os.environ.get("BRAVAURA_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- brand facts
PHONE = "908-894-3611"
PHONE_TEL = "9088943611"
EMAIL = "info@bravaurallc.com"
IG = "bravaurallc"
IG_URL = "https://instagram.com/bravaurallc"

# ---------------------------------------------------------------- photos
# AI-generated, customer-focused, brand-palette shots in Kendal's ImagineArt
# library. Reusing an existing image is free. Swap any ID for a real event
# photo any time — the layout stays the same.
ASSET = "https://asset.imagine.art/processed/"
# ---- REAL event photos (Kendal's own, Sept 2026). Local files in assets/gallery/. ----
# These replaced the AI-generated placeholders everywhere a real photo existed.
P_LAV_FIELD   = "assets/gallery/lavender-field-group.jpg"    # guests in the lavender field holding their canvases
P_LAV_TENT    = "assets/gallery/lavender-tent-table.jpg"     # long purple table under the tent, farm behind
P_LAV_WIDE    = "assets/gallery/lavender-tent-wide.jpg"      # wider shot of the full tent
P_LAV_TABLE   = "assets/gallery/lavender-painting-table.jpg" # painting together at the lavender farm
P_LAV_TEACH   = "assets/gallery/lavender-instructing.jpg"    # instructing at the table
P_LAV_CANVAS  = "assets/gallery/lavender-canvas-held.jpg"    # finished lavender canvas held up
P_LAV_PATIO   = "assets/gallery/lavender-canvas-patio.jpg"   # finished lavender canvas on a patio table
P_BUTTERFLY   = "assets/gallery/butterfly-group.jpg"         # big group holding purple butterfly canvases
P_BUTTERFLY2  = "assets/gallery/butterfly-group-2.jpg"
P_INDOOR      = "assets/gallery/indoor-painting.jpg"         # indoor session, guests mid-paint
P_INDOOR2     = "assets/gallery/indoor-painting-2.jpg"       # indoor session, closer in
P_TABLE_SETUP = "assets/gallery/table-setup.jpg"             # easels + canvases set up before guests arrive
P_STUDIO      = "assets/gallery/studio-setup.jpg"            # supplies, sign, sample canvas
P_CANVAS_BIRD = "assets/gallery/canvas-held-bird.jpg"        # finished canvas held up
P_TENT_SETUP  = "assets/gallery/tent-setup.jpg"              # setting up the tent
P_TENT_ROW    = "assets/gallery/lavender-tent-row.jpg"       # long table under the tent, lavender rows behind
P_TENT_GOLDEN = "assets/gallery/lavender-tent-golden.jpg"    # the tent in the lavender field at golden hour
P_TABLE_GROUP = "assets/gallery/indoor-table-group.jpg"      # full indoor table mid-session
P_CANVAS_PINE = "assets/gallery/canvas-northern-lights.jpg"  # finished northern-lights canvas held up
P_ARTIST      = "assets/gallery/artist-painting-lavender.jpg"# Bravaura artist painting the lavender demo
P_TENT_LAUGH  = "assets/gallery/lavender-tent-laughing.jpg" # Kendal mid-demo, table laughing, lavender rows behind
P_BFLY_CANVAS = "assets/gallery/canvas-butterfly-ribbon.jpg" # finished butterfly-and-ribbon canvas on an easel
P_PATIO       = "assets/gallery/patio-session.jpg"           # backyard gazebo session
P_APRON       = "assets/gallery/apron-palette.jpg"           # Bravaura apron logo + palette close-up
P_BFLY_PAINT  = "assets/gallery/painting-butterfly.jpg"      # guest painting her butterfly canvas
P_HEADSHOT    = "assets/gallery/kendal-headshot.jpg"         # Kendal in the Bravaura apron with a palette
P_DEMO        = "assets/gallery/kendal-demo.jpg"             # Kendal demonstrating at the easel
P_TEAM_NOTE   = "assets/gallery/testimonial-team.jpg"        # 16:10 crop of the indoor table, for the team-building quote

IMG_HERO      = P_LAV_FIELD     # home hero — real guests in the lavender field with their paintings
IMG_SIP       = P_TENT_LAUGH    # paint & sip — Kendal mid-demo, guests laughing, lavender rows behind
IMG_BIRTHDAY  = P_BUTTERFLY     # parties — real mixed-age group with their butterfly canvases
IMG_CORP      = P_TABLE_GROUP   # Oct 2026: real indoor table session (AI photo removed — read as fake)
IMG_FACE      = "assets/gallery/face-painting.jpg"  # Oct 2026: real face painting at a community event
IMG_MASTER    = P_INDOOR2       # lessons — real indoor session, focused work
IMG_LAKE      = "67f4b7da-ed40-424c-ad49-760dd9087a33"  # ladies' lake night
IMG_GALAXY    = "d24aa654-58f8-4c92-b876-176230ec11e6"  # kids' galaxy painting
P_KID_FLOWER  = "assets/gallery/kid-flower-painting.jpg"  # young painter holding her red flower canvas
IMG_HEADSHOT  = P_HEADSHOT  # real photo of Kendal in the Bravaura apron (replaced the AI headshot)

def img_url(pid):
    if pid.startswith("http") or pid.startswith("assets/"):
        return pid
    return ASSET + pid

def frame_photo(pid, alt, tilt="l", shadow="gold", extra=""):
    """Bold framed photo with graceful color-gradient fallback."""
    onerr = "this.closest('.frame-photo').classList.add('fail')"
    cls = "frame-photo tilt-" + tilt + " sh-" + shadow + ((" " + extra) if extra else "")
    return ('<div class="' + cls + '">'
            '<img src="' + img_url(pid) + '" alt="' + alt + '" loading="lazy" onerror="' + onerr + '"></div>')

# ---------------------------------------------------------------- icons
ICONS = {
    "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>',
    "palette": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="13.5" cy="6.5" r="1.5"/><circle cx="17.5" cy="10.5" r="1.5"/><circle cx="8.5" cy="7.5" r="1.5"/><circle cx="6.5" cy="12.5" r="1.5"/><path d="M12 2a10 10 0 0 0 0 20c.55 0 1-.45 1-1 0-.26-.1-.5-.26-.68-.16-.19-.26-.42-.26-.68 0-.55.45-1 1-1H16a6 6 0 0 0 6-6c0-5.52-4.48-10-10-10z"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    "gift": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.9 5.2L19 10l-5.1 1.8L12 17l-1.9-5.2L5 10l5.1-1.8z"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5 12 3l9 6.5"/><path d="M5 10v10h14V10"/></svg>',
}
def icon(name):
    return ICONS.get(name, "")

SITE_URL = "https://bravaurallc.com"   # used for canonical + social preview tags
FORM_EMAIL = "bravaurallc@gmail.com"   # quote/contact forms email straight here via FormSubmit (free, no account)
TICKETS_URL = "https://square.link/u/ehouc1P7"   # Olipop & Paint tickets (Square)
FLYER_IMG   = "assets/olipop-paint-flyer.jpg"    # drop the flyer here; popup hides the image if missing

# ---------------------------------------------------------------- testimonials
TESTIMONIALS = [
    {"quote": "Bravaura turned my daughter's 8th birthday into the easiest party I've ever hosted. They brought everything, ran the whole painting activity, and packed it all up. I didn't lift a finger.", "author": "Jenna R.", "context": "Birthday Party, Cranford NJ", "image": P_BUTTERFLY, "image_alt": "A party group holding up the canvases they painted"},
    {"quote": "Booked a ladies' night on the lake and it was such a fun, relaxed evening. Great instruction for total beginners, and every canvas turned out great. Already planning the next one.", "author": "Kristine G.", "context": "Paint & Sip, Ladies' Night", "image": P_LAV_WIDE, "image_alt": "A tent full of guests at a Bravaura paint & sip"},
    {"quote": "We had a great time. Bravaura took care of everything, and it was a great team bonding experience.", "author": "Keith P.", "context": "Team Building, Effluent Design", "image": P_TEAM_NOTE, "image_alt": "A team painting together around one long table"},
]

# ================================================================ CSS
CSS = r"""/* =========================================================
   Bravaura LLC — "Gallery Night" stylesheet
   Soft light, painted color washes, arched gallery frames.
   Drop-in replacement: same class names as the previous sheet.
   ========================================================= */
:root{
  --teal:#0B9ABF; --teal-deep:#087C9A;
  --gold:#F7B10F; --gold-deep:#B37F0A; --gold-soft:#FFE7A8;
  --purple:#81469C; --purple-deep:#5E2E78;
  --magenta:#D42463; --orange:#D86312;
  --royal:#0354D2;
  --plum:#24123A; --plum-2:#3A1D58;
  --ink:#24123A; --body:#5A4E6B;
  --paper:#FFFFFF; --lilac:#F7F3FB; --lilac-2:#EFE7F7;
  --line:#E6DCF0;
  --grad:linear-gradient(120deg,var(--teal) 0%,var(--purple) 55%,var(--magenta) 100%);
  --grad-warm:linear-gradient(120deg,var(--purple) 0%,var(--magenta) 100%);
  --shadow-sm:0 2px 6px rgba(36,18,58,.06),0 6px 18px rgba(36,18,58,.06);
  --shadow:0 4px 12px rgba(36,18,58,.07),0 18px 40px rgba(94,46,120,.12);
  --shadow-lg:0 10px 24px rgba(36,18,58,.10),0 30px 70px rgba(94,46,120,.18);
  --font-display:"Fraunces",Georgia,serif;
  --font-body:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  --font-hand:"Fraunces",Georgia,serif;
  --maxw:1180px;
  --arch:999px 999px 26px 26px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
#site-splash{position:fixed;inset:0;z-index:999;display:flex;align-items:center;justify-content:center;background:#fffefe;transition:opacity .45s ease}
#site-splash video{width:min(70vw,480px);animation:splash-pop .5s cubic-bezier(.34,1.56,.64,1);-webkit-mask-image:radial-gradient(ellipse 60% 62% at 50% 50%,#000 55%,transparent 86%);mask-image:radial-gradient(ellipse 60% 62% at 50% 50%,#000 55%,transparent 86%)}
#site-splash.splash-out{opacity:0;pointer-events:none}
@keyframes splash-pop{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:scale(1)}}
@media(prefers-reduced-motion:reduce){#site-splash video{animation:none}}
body{margin:0;font-family:var(--font-body);color:var(--body);background:var(--paper);line-height:1.7;font-size:18px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;display:block}
a{color:var(--purple);text-decoration:none}
a:hover{color:var(--magenta)}
h1,h2,h3,h4{font-family:var(--font-display);color:var(--ink);line-height:1.08;margin:0 0 .5em;font-weight:500;letter-spacing:-.025em}
h1{font-size:clamp(2.6rem,6vw,4.6rem)}
h2{font-size:clamp(2rem,4.3vw,3.1rem)}
h3{font-size:clamp(1.2rem,2.1vw,1.5rem);font-weight:600;letter-spacing:-.015em}
p{margin:0 0 1.1rem}
.container{width:100%;max-width:var(--maxw);margin:0 auto;padding:0 26px}
.narrow{max-width:780px}
.center{text-align:center}
.center .lead{margin-left:auto;margin-right:auto}
.mt-0{margin-top:0}.mb-0{margin-bottom:0}
.lead{font-size:1.2rem;color:var(--ink);max-width:56ch;font-weight:400;opacity:.85}
.hand{font-family:var(--font-display);font-style:italic;font-weight:500;line-height:1}

/* eyebrow: small caps label with a paint-dot, no handwriting */
.eyebrow{font-family:var(--font-body);font-size:.8rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--purple);margin:0 0 .9rem;display:inline-flex;align-items:center;gap:.6rem}
.eyebrow::before{content:"";width:22px;height:8px;border-radius:8px;background:var(--grad)}

/* accent words: gradient italic serif over a painted swash */
.script-accent{font-family:var(--font-display);font-style:italic;font-weight:400;color:var(--purple)}

/* buttons: soft rounded rectangles, no outlines, no hard shadows */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.55rem;font-family:var(--font-body);font-weight:600;font-size:1rem;padding:1rem 1.7rem;border-radius:14px;border:0;cursor:pointer;text-decoration:none;line-height:1;transition:transform .2s ease,box-shadow .2s ease,background-position .4s ease,color .2s;box-shadow:var(--shadow-sm);letter-spacing:.005em}
.btn:hover{transform:translateY(-2px);box-shadow:var(--shadow);text-decoration:none}
.btn:active{transform:translateY(0);box-shadow:var(--shadow-sm)}
.btn:focus-visible{outline:3px solid var(--gold);outline-offset:3px}
.btn--gold{background:linear-gradient(120deg,var(--purple-deep),var(--purple) 45%,var(--magenta));background-size:180% 100%;background-position:0 0;color:#fff}
.btn--gold:hover{background-position:100% 0;color:#fff}
.btn--teal{background:var(--teal);color:#fff}
.btn--teal:hover{color:#fff;background:var(--teal-deep)}
.btn--purple{background:var(--purple);color:#fff}
.btn--purple:hover{color:#fff;background:var(--purple-deep)}
.btn--white{background:#fff;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line),var(--shadow-sm)}
.btn--white:hover{color:var(--purple);box-shadow:inset 0 0 0 1.5px var(--purple),var(--shadow)}
.btn--lg{padding:1.15rem 2rem;font-size:1.06rem}
.btn-row{display:flex;flex-wrap:wrap;gap:14px}
.center .btn-row{justify-content:center}

/* top sweep + header */
.sweep-bar{height:4px;border:0;margin:0;background:linear-gradient(90deg,var(--teal),var(--purple) 40%,var(--magenta) 70%,var(--gold))}
.site-header{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.88);backdrop-filter:saturate(160%) blur(14px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;height:80px;gap:20px}
.brand img{height:54px;width:auto}
@media(max-width:480px){.brand img{height:44px}}
.nav-links{display:flex;align-items:center;gap:6px;list-style:none;margin:0;padding:0}
.nav-links a{font-weight:500;font-size:.97rem;color:var(--ink);padding:9px 14px;border-radius:10px;transition:background .2s,color .2s}
.nav-links a:hover{background:var(--lilac);color:var(--purple)}
.nav-links a.active{background:var(--lilac-2);color:var(--purple-deep);font-weight:600}
.nav-cta{display:flex;align-items:center;gap:14px}
.nav-toggle{display:none;background:none;border:0;cursor:pointer;width:46px;height:46px;padding:10px;border-radius:10px}
.nav-toggle:hover{background:var(--lilac)}
.nav-toggle span{display:block;height:2.5px;background:var(--ink);border-radius:2px;margin:5px 0;transition:.25s}
.nav-toggle.open span:nth-child(1){transform:translateY(7.5px) rotate(45deg)}
.nav-toggle.open span:nth-child(2){opacity:0}
.nav-toggle.open span:nth-child(3){transform:translateY(-7.5px) rotate(-45deg)}
@media(max-width:920px){
  .nav-toggle{display:block}
  .nav-links{position:absolute;top:80px;left:0;right:0;flex-direction:column;align-items:stretch;gap:0;background:#fff;border-bottom:1px solid var(--line);box-shadow:var(--shadow);max-height:0;overflow:hidden;transition:max-height .3s}
  .nav-links.open{max-height:560px}
  .nav-links li{border-bottom:1px solid var(--line)}
  .nav-links a{display:block;padding:15px 26px;border-radius:0}
  .nav-cta .btn{display:none}
}

/* hero (home) — white canvas with a painted color wash */
.hero{position:relative;padding:76px 0 96px;overflow:hidden;background:
  radial-gradient(40% 55% at 95% 10%,rgba(247,177,15,.20),transparent 70%),
  radial-gradient(38% 55% at 0% 95%,rgba(11,154,191,.13),transparent 70%),
  var(--paper)}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center;position:relative;z-index:2}
.hero h1{font-size:clamp(2.7rem,6.2vw,4.9rem);font-weight:400}
.hero h1 .pop{color:var(--teal)}
.hero .script-accent{display:block;font-size:1.08em;margin:.04em 0 .02em;padding-bottom:.08em;position:relative;width:max-content;max-width:100%}
.hero .script-accent::after{content:"";position:absolute;left:2%;right:4%;bottom:-.02em;height:.16em;border-radius:99px;background:var(--gold);opacity:.55;z-index:-1;transform:rotate(-1deg)}
.hero-lead{font-size:1.24rem;color:var(--ink);opacity:.82;max-width:46ch;margin:1.5rem 0 2.2rem;font-weight:400}
.hero-cta{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.blob{position:absolute;border-radius:50%;filter:blur(60px);opacity:.22;z-index:0;pointer-events:none}
.arrow-doodle{display:none}
.hero-photo-wrap{position:relative;padding:10px 40px 56px 0}
.hero-photo{position:relative;overflow:hidden;background:var(--lilac-2)}
.hero-photo img{width:100%;height:100%;object-fit:cover}
.hero-photo.fail img{display:none}
.hero-photo.fail{display:grid;place-items:center}
/* arched gallery window */
.hero-photo--main{border-radius:var(--arch);aspect-ratio:4/4.6;box-shadow:var(--shadow-lg);outline:2px solid rgba(247,177,15,.9);outline-offset:10px}
.hero-photo--main.fail{background:var(--grad)}
/* round "porthole" photo */
.hero-photo--mini{position:absolute;right:0;bottom:6px;width:42%;aspect-ratio:1/1;border-radius:50%;border:8px solid #fff;box-shadow:var(--shadow-lg);z-index:4}
.hero-photo--mini.fail{background:var(--grad-warm)}
.hero-badge{position:absolute;z-index:5;font-family:var(--font-body);font-weight:600;font-size:.95rem;padding:11px 18px;border-radius:999px;background:#fff;color:var(--ink);box-shadow:var(--shadow);display:inline-flex;align-items:center;gap:8px}
.hero-badge::before{content:"";width:10px;height:10px;border-radius:50%;background:var(--teal);box-shadow:0 0 0 4px rgba(11,154,191,.18)}
.hero-badge--tl{top:34px;left:-22px}
@media(max-width:920px){
  .hero-grid{grid-template-columns:1fr;gap:40px}
  .hero-photo-wrap{max-width:420px;margin:0 auto;padding:10px 26px 50px 10px}
  .hero-badge--tl{left:-6px}
}

/* marquee — plum ribbon, italic serif, gold dots */
.marquee{background:var(--plum);color:#fff;padding:18px 0;overflow:hidden;white-space:nowrap}
.marquee-track{display:inline-flex;animation:marq 30s linear infinite;will-change:transform}
.marquee-track span{font-family:var(--font-display);font-style:italic;font-weight:400;font-size:1.45rem;padding:0 22px;display:inline-flex;align-items:center;gap:22px;color:rgba(255,255,255,.92)}
.marquee-track .star{color:var(--gold);font-style:normal;font-size:.9rem}
@keyframes marq{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* sections */
.section{padding:96px 0;position:relative}
.section--cream2{background:var(--lilac)}
.section-head{max-width:62ch}
.section-head.center{margin:0 auto;text-align:center}
.section-head.center .eyebrow{justify-content:center}

/* page hero (inner pages) */
.page-hero{position:relative;background:var(--plum);color:#fff;overflow:hidden;padding:84px 0 80px}
.page-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(50% 120% at 90% 0%,rgba(129,70,156,.65),transparent 60%),radial-gradient(45% 110% at 0% 100%,rgba(11,154,191,.35),transparent 60%),radial-gradient(35% 80% at 55% 120%,rgba(247,177,15,.22),transparent 60%)}
.page-hero .container{position:relative;z-index:2}
.page-hero h1,.page-hero p{color:#fff}
.page-hero h1{font-weight:400}
.page-hero .eyebrow{color:var(--gold)}
.page-hero .eyebrow::before{background:var(--gold)}
.page-hero .lead{color:rgba(255,255,255,.86);max-width:60ch;opacity:1}
.page-hero .script-accent{display:block;font-size:clamp(2.2rem,5.4vw,3.5rem);line-height:1.05;margin-bottom:.1em;color:var(--gold)}

/* how it works */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:56px;position:relative}
.step{position:relative;text-align:left;background:#fff;border-radius:22px;padding:28px 24px;box-shadow:var(--shadow-sm);border:1px solid var(--line);transition:transform .25s ease,box-shadow .25s ease}
.step:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.step-num{width:52px;height:52px;border-radius:16px;display:grid;place-items:center;margin:0 0 18px;font-family:var(--font-display);font-style:italic;font-size:1.6rem;font-weight:500;color:#fff;background:var(--teal)}
.step:nth-of-type(1) .step-num{background:var(--teal)}
.step:nth-of-type(2) .step-num{background:var(--gold);color:var(--plum)}
.step:nth-of-type(3) .step-num{background:var(--magenta)}
.step:nth-of-type(4) .step-num{background:var(--purple)}
.step h3{font-size:1.25rem;margin-bottom:.35rem}
.step p{font-size:.99rem;margin:0}
.steps-line{display:none}
@media(max-width:820px){.steps{grid-template-columns:1fr 1fr;gap:18px}}
@media(max-width:460px){.steps{grid-template-columns:1fr}}

/* services — framed artwork cards */
.bento{display:grid;grid-template-columns:repeat(6,1fr);gap:24px;margin-top:52px}
.svc{position:relative;overflow:hidden;border-radius:26px;display:flex;flex-direction:column;justify-content:flex-start;padding:14px 14px 26px;color:var(--ink);text-decoration:none;background:#fff;box-shadow:var(--shadow);transition:transform .3s ease,box-shadow .3s ease}
.svc:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);color:var(--ink)}
.svc-img{position:relative;z-index:0;background:var(--tint);margin-bottom:20px}
.svc .svc-img{aspect-ratio:4/3;overflow:hidden;border-radius:18px}
.svc-img img{width:100%;height:100%;object-fit:cover;transition:transform .6s ease}
.svc:hover .svc-img img{transform:scale(1.06)}
.svc::after{content:"";position:absolute;left:0;right:0;top:0;height:6px;background:var(--tint);opacity:1;z-index:3}
.svc>*{position:relative;z-index:2;padding-left:12px;padding-right:12px}
.svc>.svc-img{padding:0}
.svc .tag{font-family:var(--font-body);font-weight:700;font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;line-height:1;color:var(--tint);margin-bottom:8px}
.svc h3{color:var(--ink);margin:0 0 .35rem;font-size:1.6rem;font-weight:500}
.svc p{color:var(--body);margin:0;font-size:1rem;max-width:44ch}
@media(min-width:760px){.svc p{min-height:4.6em}}
.svc .go{margin-top:16px;font-weight:600;display:inline-flex;gap:.4rem;font-size:.96rem;color:var(--purple);transition:gap .2s}
.svc:hover .go{gap:.75rem;color:var(--magenta)}
.svc--birthday{grid-column:span 3;--tint:var(--magenta)}
.svc--sip{grid-column:span 3;--tint:var(--purple)}
.svc--corp{grid-column:span 2;--tint:var(--royal)}
.svc--face{grid-column:span 2;--tint:var(--orange)}
.svc--master{grid-column:span 2;--tint:var(--teal)}
@media(max-width:980px){.svc--corp,.svc--face,.svc--master{grid-column:span 3}.svc--master{grid-column:1 / -1}}
@media(max-width:820px){.bento{grid-template-columns:1fr 1fr}.svc{grid-column:span 1 !important}.svc--master{grid-column:1 / -1 !important}}
@media(max-width:520px){.bento{grid-template-columns:1fr}.svc--master{grid-column:auto !important}}

/* why band — deep plum with soft light */
.why{background:var(--plum);color:#fff;position:relative;overflow:hidden}
.why::before{content:"";position:absolute;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(129,70,156,.55),transparent 65%);top:-260px;right:-160px}
.why::after{content:"";position:absolute;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(11,154,191,.35),transparent 65%);bottom:-240px;left:-160px}
.why h2{color:#fff;font-weight:400}
.why .eyebrow{color:var(--gold)}
.why .eyebrow::before{background:var(--gold)}
.why-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:52px;position:relative;z-index:1}
.why-item{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:22px;padding:26px 22px;transition:background .25s,transform .25s}
.why-item:hover{background:rgba(255,255,255,.1);transform:translateY(-4px)}
.why-ic{width:52px;height:52px;border-radius:16px;display:grid;place-items:center;margin-bottom:18px;background:linear-gradient(135deg,var(--gold),#FFD27A)}
.why-ic svg{width:26px;height:26px;color:var(--plum)}
.why-item h3{color:#fff;font-size:1.22rem;margin-bottom:.35rem}
.why-item p{color:rgba(255,255,255,.78);font-size:.98rem;margin:0}
@media(max-width:820px){.why-grid{grid-template-columns:1fr 1fr}}
@media(max-width:460px){.why-grid{grid-template-columns:1fr}}

/* testimonials */
.notes{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:54px}
.note{background:#fff;border:1px solid var(--line);border-radius:24px;padding:30px 28px 26px;box-shadow:var(--shadow-sm);position:relative;transition:transform .25s,box-shadow .25s}
.note:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.note::before{content:"\201C";position:absolute;top:6px;right:22px;font-family:var(--font-display);font-size:5rem;line-height:1;color:var(--lilac-2)}
.note-photo{margin:-12px -12px 18px;border-radius:16px;overflow:hidden;aspect-ratio:16/10;background:var(--grad)}
.note-photo img{width:100%;height:100%;object-fit:cover;display:block}
.note-stars{color:var(--gold);font-size:1rem;letter-spacing:3px;margin-bottom:12px}
.note .q{font-family:var(--font-display);font-size:1.1rem;font-weight:400;font-style:italic;color:var(--ink);line-height:1.55;margin-bottom:16px;position:relative}
.note .who{font-weight:600;font-size:.92rem;color:var(--purple)}
.note .who span{color:var(--body);font-weight:400}
@media(max-width:820px){.notes{grid-template-columns:1fr}}

/* CTA */
.cta{background:linear-gradient(135deg,var(--plum) 0%,var(--plum-2) 55%,#4A1F5E 100%);color:#fff;text-align:center;position:relative;overflow:hidden}
.cta::before{content:"";position:absolute;inset:0;background:radial-gradient(45% 100% at 85% 0%,rgba(212,36,99,.35),transparent 60%),radial-gradient(45% 100% at 10% 100%,rgba(11,154,191,.32),transparent 60%)}
.cta .container{position:relative;z-index:1}
.cta h2{color:#fff;font-size:clamp(2.1rem,5vw,3.4rem);font-weight:400}
.cta .script-accent{display:block;font-size:clamp(1.6rem,4vw,2.3rem);line-height:1.1;margin-bottom:.35em;color:var(--gold)}
.cta p{color:rgba(255,255,255,.82);font-size:1.15rem;max-width:54ch;margin:0 auto 2rem}
.cta .btn--gold{background:linear-gradient(120deg,var(--gold),#FFCF4D);color:var(--plum)}
.cta .btn--gold:hover{color:var(--plum);box-shadow:0 0 0 6px rgba(247,177,15,.22),var(--shadow)}
.cta .btn--white,.page-hero .btn--white{background:rgba(255,255,255,.1);color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.35)}
.cta .btn--white:hover,.page-hero .btn--white:hover{background:rgba(255,255,255,.18);color:#fff}

/* split (text + framed photo) */
.split{display:grid;grid-template-columns:1.02fr .98fr;gap:60px;align-items:center}
.split--rev .split-media{order:-1}
@media(max-width:880px){.split{grid-template-columns:1fr;gap:38px}.split--rev .split-media{order:0}}
.frame-photo{position:relative;border-radius:var(--arch);overflow:hidden;background:var(--lilac-2);aspect-ratio:4/4.4;box-shadow:var(--shadow-lg)}
.frame-photo img{width:100%;height:100%;object-fit:cover}
.frame-photo.fail img{display:none}
.frame-photo.tilt-l,.frame-photo.tilt-r{transform:none}
.frame-photo.sh-gold{outline:2px solid var(--gold);outline-offset:10px}
.frame-photo.sh-teal{outline:2px solid var(--teal);outline-offset:10px}
.frame-photo.sh-magenta{outline:2px solid var(--magenta);outline-offset:10px}
.frame-photo.sh-purple{outline:2px solid var(--purple);outline-offset:10px}
.frame-photo.fail{background:var(--grad)}
.frame-photo--headshot{aspect-ratio:4/5}
.frame-photo--headshot img{object-position:center 20%}
@media(max-width:880px){.frame-photo{aspect-ratio:4/4}.frame-photo--headshot{aspect-ratio:4/4.4}}

/* checklist */
.checklist{list-style:none;padding:0;margin:1.2rem 0 0;display:grid;gap:12px}
.checklist li{display:flex;gap:12px;align-items:flex-start;font-size:1.04rem;color:var(--ink)}
.checklist li::before{content:"";flex-shrink:0;margin-top:3px;width:24px;height:24px;border-radius:8px;background:var(--grad) ;-webkit-mask:none}
.checklist li::before{background:var(--teal) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E") center/13px no-repeat}

/* info cards */
.info-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:8px}
@media(max-width:820px){.info-grid{grid-template-columns:1fr}}
.info-card{background:#fff;border:1px solid var(--line);border-radius:22px;padding:28px 26px;box-shadow:var(--shadow-sm);height:100%}
.info-card .ic{width:52px;height:52px;border-radius:16px;display:grid;place-items:center;margin-bottom:16px}
.info-card .ic svg{width:25px;height:25px}
.ic--teal{background:rgba(11,154,191,.12);color:var(--teal-deep)}.ic--gold{background:rgba(247,177,15,.2);color:var(--gold-deep)}
.ic--magenta{background:rgba(212,36,99,.1);color:var(--magenta)}.ic--purple{background:rgba(129,70,156,.12);color:var(--purple)}
.ic--orange{background:rgba(216,99,18,.12);color:var(--orange)}
.info-card h3{margin:0 0 .3rem;font-size:1.22rem}
.info-card p{margin:0;color:var(--body);font-size:1rem}

/* pills */
.pill-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.pill{background:var(--lilac);border:1px solid var(--line);color:var(--ink);font-weight:500;font-size:.93rem;padding:8px 16px;border-radius:999px}

/* forms */
.form-card{background:#fff;border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow);padding:36px}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:620px){.form-grid{grid-template-columns:1fr}.form-card{padding:26px 22px}}
.field{display:flex;flex-direction:column;gap:7px}
.field.full{grid-column:1 / -1}
.field label{font-weight:600;font-size:.92rem;color:var(--ink)}
.field label .req{color:var(--magenta)}
.field input,.field select,.field textarea{font-family:var(--font-body);font-size:1rem;color:var(--ink);padding:13px 15px;border:1.5px solid var(--line);border-radius:12px;background:var(--lilac);transition:border-color .15s,box-shadow .15s,background .15s}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--purple);background:#fff;box-shadow:0 0 0 4px rgba(129,70,156,.15)}
.field textarea{resize:vertical;min-height:120px}
.form-note{font-size:.85rem;color:var(--body);margin-top:14px}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.form-status{margin-top:16px;padding:14px 16px;border-radius:12px;font-weight:600;display:none}
.form-status.ok{display:block;background:#e7f6ef;color:#1a7a4f;border:1px solid #9fd8bd}
.form-status.err{display:block;background:#fdecef;color:#b02a44;border:1px solid #f0aab8}

/* travel calculator */
.calc{background:#fff;border:1px solid var(--line);border-radius:24px;box-shadow:var(--shadow);padding:28px;max-width:780px}

/* contact info */
.contact-info{display:grid;gap:18px;margin-top:18px}
.contact-line{display:flex;gap:14px;align-items:flex-start}
.contact-line .ci{flex-shrink:0;width:50px;height:50px;border-radius:15px;display:grid;place-items:center;background:var(--lilac-2);color:var(--purple)}
.contact-line .ci svg{width:23px;height:23px}
.contact-line a,.contact-line span{font-weight:600;color:var(--ink);font-size:1.05rem}
.contact-line a:hover{color:var(--purple)}
.contact-line small{display:block;color:var(--body);font-size:.85rem;margin-top:2px;font-weight:400}

/* faq */
.faq{max-width:840px;margin:0 auto}
.faq-item{border:1px solid var(--line);border-radius:18px;background:#fff;margin-bottom:12px;box-shadow:var(--shadow-sm);overflow:hidden;transition:box-shadow .2s,border-color .2s}
.faq-item.open{border-color:rgba(129,70,156,.4);box-shadow:var(--shadow)}
.faq-q{width:100%;text-align:left;background:none;border:0;cursor:pointer;font-family:var(--font-display);font-size:1.14rem;font-weight:500;color:var(--ink);padding:20px 56px 20px 24px;position:relative}
.faq-q::after{content:"+";position:absolute;right:20px;top:50%;transform:translateY(-50%);width:30px;height:30px;border-radius:50%;display:grid;place-items:center;background:var(--lilac);font-family:var(--font-body);font-size:1.3rem;line-height:1;color:var(--purple);transition:transform .25s,background .2s}
.faq-item.open .faq-q::after{content:"\2013";background:var(--purple);color:#fff}
.faq-a{max-height:0;overflow:hidden;transition:max-height .3s ease}
.faq-a p{color:var(--body);padding:0 24px 22px;margin:0;font-size:1.02rem}

/* gallery — mixed arch / round / rounded frames */
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
@media(max-width:900px){.gallery-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.gallery-grid{grid-template-columns:1fr}}
.gallery-item{border-radius:22px;overflow:hidden;box-shadow:var(--shadow);aspect-ratio:1/1;background:var(--grad)}
.gallery-item:nth-child(3n+2){border-radius:var(--arch);background:linear-gradient(135deg,var(--purple),var(--gold))}
.gallery-item:nth-child(3n){background:linear-gradient(135deg,var(--teal),var(--magenta))}
.gallery-item img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.gallery-item:hover img{transform:scale(1.05)}
.gallery-grid--solo{grid-template-columns:1fr;max-width:640px;margin:0 auto}
.gallery-grid--solo .gallery-item{aspect-ratio:4/3}

h1,h2,h3,h4,.script-accent,.design-name{font-variation-settings:"SOFT" 0,"WONK" 0}

/* checkbox pills (quote form) */
.field-label{display:block;font-weight:600;color:var(--ink);margin-bottom:9px}
.check-row{display:flex;flex-wrap:wrap;gap:10px}
.check{display:inline-flex;align-items:center;gap:9px;padding:11px 17px;border:1.5px solid var(--line);border-radius:12px;background:var(--lilac);font-weight:500;color:var(--ink);cursor:pointer;user-select:none;transition:background .15s,border-color .15s}
.check:hover{border-color:var(--purple)}
.check input{width:18px;height:18px;margin:0;accent-color:var(--purple);cursor:pointer}
.check:has(input:checked){background:rgba(129,70,156,.1);border-color:var(--purple);color:var(--purple-deep)}
.check:focus-within{outline:3px solid rgba(129,70,156,.35);outline-offset:2px}
.field-hint{display:block;margin-top:9px;font-size:.86rem;color:var(--body)}

/* promo popup */
#promo-pop{position:fixed;inset:0;z-index:900;display:none;align-items:center;justify-content:center;padding:22px;background:rgba(36,18,58,.55);backdrop-filter:blur(4px);opacity:0;transition:opacity .3s ease}
#promo-pop.on{display:flex}
#promo-pop.in{opacity:1}
.promo-card{position:relative;max-width:760px;width:100%;max-height:88vh;overflow-y:auto;background:#fff;color:var(--ink);border-radius:28px;box-shadow:var(--shadow-lg);padding:32px;text-align:center;display:flex;gap:28px;align-items:center;transform:translateY(14px) scale(.97);transition:transform .35s cubic-bezier(.34,1.56,.64,1)}
.promo-flyer{flex:0 0 42%;max-width:42%}
.promo-flyer img{width:100%;max-width:212px;display:block;margin:0 auto;border-radius:14px;box-shadow:var(--shadow)}
.promo-body{flex:1 1 auto;min-width:0}
.promo-note{font-size:.95rem;margin:12px 0 0;line-height:1.5;color:var(--body)}
.promo-early{font-size:.92rem;font-weight:600;margin:12px 0 18px;padding:10px 12px;background:var(--gold-soft);border-radius:12px}
@media(max-width:660px){.promo-card{flex-direction:column;gap:18px;padding:28px 20px}.promo-flyer{flex:0 0 auto;max-width:64%}}
#promo-pop.in .promo-card{transform:none}
.promo-card::before{content:"";position:absolute;left:0;right:0;top:0;height:6px;background:var(--grad)}
.promo-card>*{position:relative;z-index:1}
.promo-kicker{font-family:var(--font-body);font-weight:700;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--magenta);line-height:1;display:block;margin-bottom:10px}
.promo-card h3{font-size:1.9rem;margin:0 0 4px;line-height:1.05;font-weight:500}
.promo-when{font-weight:600;font-size:1.12rem;margin:14px 0 2px}
.promo-where{font-size:1.02rem;margin:0 0 4px}
.promo-cta{margin-top:6px}
.promo-body .btn{width:100%;justify-content:center;margin-top:8px}
.promo-close{position:absolute;top:12px;right:12px;z-index:2;background:var(--lilac);border:0;font-size:1.6rem;line-height:1;cursor:pointer;color:var(--ink);width:40px;height:40px;border-radius:50%}
.promo-close:hover{background:var(--lilac-2)}
@media(max-width:560px){.promo-card{padding:36px 22px 26px}.promo-card h3{font-size:1.7rem}}
@media(prefers-reduced-motion:reduce){#promo-pop,.promo-card{transition:none}}

/* design menu */
.design-carousel{position:relative;margin-top:46px}
.design-track{display:flex;gap:22px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:10px 10px 18px 2px;scroll-padding-left:0;-ms-overflow-style:none;scrollbar-width:none}
.design-track::-webkit-scrollbar{display:none}
.design-track:focus-visible{outline:3px solid var(--purple);outline-offset:4px;border-radius:14px}
.design-card{flex:0 0 calc((100% - 66px)/4);scroll-snap-align:start;display:flex;flex-direction:column;gap:12px}
@media(max-width:1000px){.design-card{flex-basis:calc((100% - 44px)/3)}}
@media(max-width:700px){.design-track{gap:16px}.design-card{flex-basis:calc((100% - 16px)/2)}}
@media(max-width:460px){.design-card{flex-basis:78%}}
.dcar-btn{position:absolute;top:calc(50% - 34px);transform:translateY(-50%);z-index:3;width:50px;height:50px;border-radius:50%;border:0;background:#fff;color:var(--purple);font-size:1.4rem;line-height:1;cursor:pointer;box-shadow:var(--shadow);transition:transform .2s,box-shadow .2s,opacity .18s}
.dcar-btn:hover{transform:translateY(-50%) scale(1.06);box-shadow:var(--shadow-lg)}
.dcar-btn:disabled{opacity:0;pointer-events:none}
.dcar-prev{left:-18px}
.dcar-next{right:-18px}
@media(max-width:900px){.dcar-prev{left:-6px}.dcar-next{right:-6px}.dcar-btn{width:44px;height:44px;font-size:1.2rem}}
@media(prefers-reduced-motion:reduce){.design-track{scroll-behavior:auto}}
.design-thumb{border-radius:var(--arch);overflow:hidden;box-shadow:var(--shadow);aspect-ratio:4/5;background:var(--grad);transition:transform .3s ease,box-shadow .3s ease}
.design-card:hover .design-thumb{transform:translateY(-5px);box-shadow:var(--shadow-lg)}
.design-thumb img{width:100%;height:100%;object-fit:cover;display:block}
.design-name{font-family:var(--font-display);font-weight:500;font-size:1.05rem;color:var(--ink);line-height:1.25;text-align:center}
.design-note{margin-top:34px;font-family:var(--font-display);font-style:italic;font-weight:400;font-size:1.3rem;color:var(--purple);text-align:center}

/* email signup band */
.signup{background:var(--lilac);padding:64px 0}
.signup-card{background:linear-gradient(135deg,#fff 0%,#fff 55%,var(--lilac-2) 100%);border:1px solid var(--line);border-radius:28px;box-shadow:var(--shadow);padding:38px 42px;display:grid;grid-template-columns:1.05fr 1fr;gap:34px;align-items:center;position:relative;overflow:hidden}
.signup-card::before{content:"";position:absolute;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle,rgba(247,177,15,.35),transparent 70%);right:-60px;top:-80px}
.signup-card>*{position:relative}
.signup-card .eyebrow{color:var(--purple)}
.signup-card h2{margin:.2rem 0 .5rem;font-size:1.9rem;color:var(--ink);font-weight:500}
.signup-card p{margin:0;color:var(--body);font-size:1rem;max-width:44ch}
.signup-hand{font-family:var(--font-display);font-style:italic;font-size:1.3rem;color:var(--purple);display:block;margin-bottom:4px}
.signup-row{display:flex;gap:12px;flex-wrap:wrap}
.signup-row input{flex:1;min-width:210px;font-family:var(--font-body);font-size:1rem;color:var(--ink);padding:14px 16px;border:1.5px solid var(--line);border-radius:12px;background:#fff}
.signup-row input:focus{outline:none;border-color:var(--purple);box-shadow:0 0 0 4px rgba(129,70,156,.15)}
.signup-fine{display:block;margin-top:12px;font-size:.85rem;color:var(--body)}
.signup .form-status{margin-top:14px}
@media(max-width:820px){.signup-card{grid-template-columns:1fr;gap:22px;padding:30px 24px}}

/* footer */
.site-footer{background:var(--plum);color:rgba(255,255,255,.85);padding:68px 0 28px;position:relative}
.site-footer::before{content:"";position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,var(--teal),var(--purple) 40%,var(--magenta) 70%,var(--gold))}
.footer-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:44px;padding-bottom:40px;border-bottom:1px solid rgba(255,255,255,.12)}
@media(max-width:720px){.footer-grid{grid-template-columns:1fr;gap:30px}}
.footer-brand img{height:48px;background:#fff;padding:8px 12px;border-radius:14px}
.footer-brand p{color:rgba(255,255,255,.62);max-width:34ch;margin:16px 0 0}
.footer-col h4{color:var(--gold);font-family:var(--font-body);font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em;margin-bottom:14px}
.footer-col ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.footer-col a,.footer-col li{color:rgba(255,255,255,.75);font-size:.98rem}
.footer-col a:hover{color:#fff}
.footer-bottom{display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between;padding-top:22px;font-size:.85rem;color:rgba(255,255,255,.5)}
.footer-bottom .hand{font-family:var(--font-display);font-style:italic;font-size:1.05rem;color:var(--gold)}

/* gentle motion */
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-16px)}}
@keyframes floaty2{0%,100%{transform:translateY(0)}50%{transform:translateY(14px)}}
.ph-blob{position:absolute;border-radius:50%;filter:blur(50px);opacity:.35;z-index:0;pointer-events:none}
.ph-blob--1{width:300px;height:300px;background:var(--purple);top:-100px;right:6%;animation:floaty 9s ease-in-out infinite}
.ph-blob--2{width:240px;height:240px;background:var(--teal);bottom:-110px;left:5%;animation:floaty2 10s ease-in-out infinite}
.info-card{transition:transform .25s ease,box-shadow .25s ease}
.info-card:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.frame-photo{transition:transform .4s ease}
.frame-photo:hover{transform:translateY(-4px)}
.contact-line .ci{transition:transform .2s ease,background .2s}
.contact-line:hover .ci{transform:translateY(-2px);background:var(--purple);color:#fff}
/* floating paint dots */
.float-layer{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:1}
.fd{position:absolute;opacity:.35;line-height:0}
.fd svg{display:block;width:100%;height:100%}
@keyframes drift1{0%,100%{transform:translate(0,0)}50%{transform:translate(12px,-22px)}}
@keyframes drift2{0%,100%{transform:translate(0,0)}50%{transform:translate(-14px,18px)}}
.fd-1{width:46px;height:46px;top:16%;right:11%;color:var(--gold);animation:drift1 11s ease-in-out infinite}
.fd-2{width:58px;height:58px;bottom:18%;left:7%;color:var(--teal);animation:drift2 13s ease-in-out infinite}
.fd-3{width:52px;height:28px;top:30%;left:13%;color:var(--magenta);animation:drift1 10s ease-in-out infinite}
.fd-4{width:34px;height:34px;bottom:26%;right:22%;color:var(--purple);animation:drift2 14s ease-in-out infinite}
@media(max-width:820px){.fd-3,.fd-4{display:none}.fd{opacity:.25}}

/* scroll reveal */
.reveal{opacity:0;transform:translateY(24px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.3,1)}
.reveal.in{opacity:1;transform:none}
.reveal.d1{transition-delay:.08s}.reveal.d2{transition-delay:.16s}.reveal.d3{transition-delay:.24s}.reveal.d4{transition-delay:.32s}
@media(prefers-reduced-motion:reduce){
  .reveal{opacity:1;transform:none;transition:none}
  .btn:hover,.svc:hover,.info-card:hover,.frame-photo:hover,.step:hover,.note:hover,.why-item:hover{transform:none}
  .marquee-track,.fd,.ph-blob,.hero .blob{animation:none}
}

/* =========================================================
   "Real small business" pass — flat, simple, photo-first.
   Overrides the softer layer above: no gradients, glows,
   arches, floating blobs or lift-on-hover.
   ========================================================= */
:root{--r:12px;--r-sm:8px;--paper-2:#F6F4F8}
.blob,.ph-blob,.float-layer,.fd,.arrow-doodle,.steps-line{display:none!important}
.hero{background:var(--paper);padding:56px 0 72px}
.hero h1{font-weight:500}
.script-accent,.hero .script-accent{font-style:normal;color:var(--purple);font-weight:500}
.hero .script-accent::after{display:none}
.eyebrow{letter-spacing:.12em}
.eyebrow::before{display:none}
.hero-photo-wrap{padding:0 0 40px}
.hero-photo--main{border-radius:var(--r);outline:0;box-shadow:none;aspect-ratio:4/3.4}
.hero-photo--mini{border-radius:var(--r);border:6px solid #fff;box-shadow:0 2px 10px rgba(36,18,58,.12);width:40%;right:-12px;bottom:0}
.hero-badge{border-radius:var(--r-sm);box-shadow:0 1px 4px rgba(36,18,58,.12);top:14px;left:14px;font-size:.9rem}
.hero-badge::before{box-shadow:none}
.hero-photo-wrap{padding:0 0 48px 28px}
.hero-photo--mini{right:auto;left:-6px;bottom:0}
.hero-sticker{position:absolute;z-index:5;top:-18px;left:4px;width:118px;height:118px;border-radius:50%;background:#fff;display:grid;place-items:center;padding:14px;box-shadow:0 2px 10px rgba(36,18,58,.14);transform:rotate(-8deg)}
.hero-sticker img{width:100%;height:auto}
@media(max-width:920px){.hero-sticker{width:92px;height:92px;padding:11px;top:-14px;left:0}}
@media(max-width:920px){.hero-photo-wrap{padding:0 0 44px 20px}.hero-photo--mini{left:0}}
.btn,.btn--gold,.btn--gold:hover{background:var(--purple);color:#fff;border-radius:var(--r-sm);box-shadow:none;background-size:auto}
.btn:hover{transform:none;box-shadow:none;background:var(--purple-deep);color:#fff}
.btn--white,.btn--white:hover{background:#fff;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--ink)}
.btn--white:hover{background:var(--paper-2)}
.cta .btn--gold,.cta .btn--gold:hover{background:var(--gold);color:var(--plum);box-shadow:none}
.section--cream2,.signup{background:var(--paper-2)}
.marquee-track span{font-style:normal;font-family:var(--font-body);font-weight:600;font-size:1.05rem;letter-spacing:.02em}
.step,.svc,.note,.info-card,.form-card,.calc,.faq-item,.signup-card,.promo-card{box-shadow:none;border:1px solid var(--line);border-radius:var(--r)}
.step:hover,.svc:hover,.note:hover,.info-card:hover,.why-item:hover,.frame-photo:hover,.design-card:hover .design-thumb{transform:none;box-shadow:none}
.step-num{border-radius:50%;font-style:normal;font-family:var(--font-body);font-weight:700;font-size:1.2rem;width:44px;height:44px}
.svc{padding:0 0 22px}
.svc .svc-img{border-radius:var(--r) var(--r) 0 0}
.svc::after{display:none}
.svc:hover .svc-img img{transform:scale(1.03)}
.svc .tag{color:var(--purple)}
.svc-noimg{aspect-ratio:4/3;display:grid;place-items:center;background:var(--tint);color:#fff;border-radius:var(--r) var(--r) 0 0;margin-bottom:20px;font-family:var(--font-display);font-size:1.3rem;text-align:center;padding:20px}
.why::before,.why::after,.cta::before,.page-hero::before,.signup-card::before,.promo-card::before,.site-footer::before{display:none}
.why-item{background:transparent;border:0;padding:0}
.why-ic{background:var(--gold);border-radius:var(--r-sm)}
.cta{background:var(--plum)}
.page-hero{background:var(--plum);padding:64px 0}
.page-hero .script-accent{font-style:normal}
.frame-photo,.frame-photo.sh-gold,.frame-photo.sh-teal,.frame-photo.sh-magenta,.frame-photo.sh-purple{border-radius:var(--r);outline:0;box-shadow:none;aspect-ratio:4/3.4}
.frame-photo--headshot{aspect-ratio:4/5}
.gallery-item,.gallery-item:nth-child(3n+2),.gallery-item:nth-child(3n){border-radius:var(--r);box-shadow:none}
.design-thumb{border-radius:var(--r);box-shadow:none}
.note::before{display:none}
.note-photo{margin:0 0 16px;border-radius:var(--r-sm)}
.signup-card{background:#fff}
.site-footer{border-top:0}
.reveal{opacity:1;transform:none}
"""

# ================================================================ JS
JS = r"""// Bravaura LLC — site interactions
(function(){
  // landing splash (homepage, first visit of the session only)
  var splash=document.getElementById('site-splash');
  if(splash){
    try{
      if(sessionStorage.getItem('bravaura_splash_seen')){
        splash.remove();
      }else{
        sessionStorage.setItem('bravaura_splash_seen','1');
        var hide=function(){
          splash.classList.add('splash-out');
          setTimeout(function(){splash.remove();},500);
        };
        if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){hide();}
        else{setTimeout(hide,3000);}
      }
    }catch(e){splash.remove();}
  }

  var tog=document.querySelector('.nav-toggle'),links=document.getElementById('nav-links');
  if(tog){tog.addEventListener('click',function(){var o=links.classList.toggle('open');tog.classList.toggle('open',o);tog.setAttribute('aria-expanded',o);});}

  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveals=document.querySelectorAll('.reveal');
  if(!reduce && 'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.14,rootMargin:'0px 0px -8% 0px'});
    reveals.forEach(function(el){io.observe(el);});
  }else{reveals.forEach(function(el){el.classList.add('in');});}

  if(!reduce){
    var blobs=document.querySelectorAll('.hero .blob');
    if(blobs.length){window.addEventListener('scroll',function(){var y=window.scrollY;blobs.forEach(function(b,i){b.style.transform='translateY('+(y*(i?.12:-.08))+'px)';});},{passive:true});}
  }

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function(q){
    q.addEventListener('click',function(){
      var item=q.closest('.faq-item');var a=item.querySelector('.faq-a');
      var open=item.classList.toggle('open');
      q.setAttribute('aria-expanded',open);
      a.style.maxHeight=open?(a.scrollHeight+'px'):'0';
    });
  });

  // current year
  var yr=document.getElementById('year'); if(yr){yr.textContent=new Date().getFullYear();}


  // ---- design menu carousel (arrows + scroll snap)
  document.querySelectorAll('.design-carousel').forEach(function(wrap){
    var track=wrap.querySelector('.design-track');
    var prev=wrap.querySelector('.dcar-prev');
    var next=wrap.querySelector('.dcar-next');
    if(!track||!prev||!next) return;
    function step(){
      var card=track.querySelector('.design-card');
      if(!card) return track.clientWidth*0.8;
      var gap=parseFloat(getComputedStyle(track).columnGap||getComputedStyle(track).gap||22)||22;
      var per=Math.max(1,Math.round(track.clientWidth/(card.offsetWidth+gap)));
      return (card.offsetWidth+gap)*per;
    }
    function sync(){
      var max=track.scrollWidth-track.clientWidth-2;
      prev.disabled = track.scrollLeft<=6;
      next.disabled = track.scrollLeft>=max-6;
    }
    prev.addEventListener('click',function(){track.scrollBy({left:-step(),behavior:'smooth'});});
    next.addEventListener('click',function(){track.scrollBy({left:step(),behavior:'smooth'});});
    track.addEventListener('scroll',function(){window.requestAnimationFrame(sync);});
    window.addEventListener('resize',sync);
    track.addEventListener('keydown',function(e){
      if(e.key==='ArrowRight'){e.preventDefault();track.scrollBy({left:step(),behavior:'smooth'});}
      if(e.key==='ArrowLeft'){e.preventDefault();track.scrollBy({left:-step(),behavior:'smooth'});}
    });
    sync();
  });

  // ---- promo popup (Olipop & Paint). Hides itself from PROMO_END onward.
  (function(){
    var pop=document.getElementById('promo-pop');
    if(!pop) return;
    var PROMO_END=new Date(2026,8,11);           // Sept 11 2026, local time — popup stops showing
    if(new Date()>=PROMO_END){pop.remove();return;}
    try{ if(sessionStorage.getItem('bravaura_promo_olipop')){pop.remove();return;} }catch(e){}
    var card=pop.querySelector('.promo-card');
    var closeBtn=pop.querySelector('.promo-close');
    function close(){
      pop.classList.remove('in');
      try{sessionStorage.setItem('bravaura_promo_olipop','1');}catch(e){}
      setTimeout(function(){pop.classList.remove('on');pop.setAttribute('aria-hidden','true');},300);
      document.removeEventListener('keydown',onKey);
    }
    function onKey(e){ if(e.key==='Escape'){close();} }
    function open(){
      pop.classList.add('on');
      pop.setAttribute('aria-hidden','false');
      requestAnimationFrame(function(){pop.classList.add('in');});
      document.addEventListener('keydown',onKey);
      if(closeBtn) closeBtn.focus();
    }
    closeBtn.addEventListener('click',close);
    var cta=pop.querySelector('.promo-cta');
    if(cta) cta.addEventListener('click',close);
    pop.addEventListener('click',function(e){ if(e.target===pop){close();} });
    // wait out the homepage splash so the two don't collide
    var tries=0;
    (function waitForSplash(){
      var sp=document.getElementById('site-splash');
      if(sp && tries++<80){ setTimeout(waitForSplash,100); return; }
      setTimeout(open,700);
    })();
  })();

  // Forms: graceful AJAX submit with a status message.
  // data-endpoint (the Kit signup band) posts straight to that service;
  // everything else posts to '/' for Netlify Forms.
  document.querySelectorAll('form[data-bravaura-form]').forEach(function(form){
    form.addEventListener('submit',function(ev){
      var status=form.querySelector('.form-status');
      if(!form.checkValidity()){return;} // let native validation handle it
      ev.preventDefault();
      var data=new FormData(form);
      var body=new URLSearchParams();
      data.forEach(function(v,k){body.append(k,v);});
      var endpoint=form.getAttribute('data-endpoint')||'/';
      fetch(endpoint,{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded','Accept':'application/json'},body:body.toString()})
        .then(function(res){
          if(!res.ok){throw new Error('bad status');}
          if(status){status.className='form-status ok';status.textContent=form.getAttribute('data-success')||'Thank you! Your request is in. We\'ll reply by email within 24 hours with your custom quote.';}
          form.reset();
        })
        .catch(function(){
          // If the AJAX call can't get through (local preview, CORS, etc.) but the form
          // posts to a real endpoint, fall back to a plain browser submit so it still works.
          if(form.getAttribute('data-endpoint')){form.submit();return;}
          if(status){status.className='form-status err';status.textContent='Something went wrong sending that. Please email '+ 'bravaurallc@gmail.com' +' or call 908-894-3611 and we\'ll take care of you.';}
        });
    });
  });
})();
"""

# ================================================================ chrome
NAV = [("Home","index.html"),("Services","services.html"),("Pricing","pricing.html"),
       ("Gallery","gallery.html"),("About","about.html"),("Contact","contact.html")]

def header(active):
    items=""
    for label,href in NAV:
        cls=' class="active"' if href==active else ""
        aria=' aria-current="page"' if href==active else ""
        items+=f'<li><a href="{href}"{cls}{aria}>{label}</a></li>'
    return f'''<hr class="sweep-bar">
<header class="site-header">
  <div class="container nav">
    <a href="index.html" class="brand" aria-label="Bravaura LLC home"><img src="assets/bravaura-logo-final.png" alt="Bravaura LLC logo"></a>
    <nav aria-label="Main"><ul class="nav-links" id="nav-links">{items}</ul></nav>
    <div class="nav-cta">
      <a href="contact.html" class="btn btn--gold">Book a date</a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''

# Aug 11 2026: all 12 re-shot against a real canvas-tarp backdrop (was a flat digital white void)
DESIGNS=[  # Oct 2026: real finished canvases only (AI renders removed)
 ("assets/gallery/design-fall-gnome.jpg","Fall Gnome"),
 ("assets/gallery/canvas-butterfly-ribbon.jpg","Butterfly &amp; Ribbon"),
 ("assets/gallery/canvas-northern-lights.jpg","Northern Lights"),
 ("assets/gallery/lavender-canvas-held.jpg","Lavender Field"),
]
# Slight hand-placed tilts so the design menu does not read as 12 identical studio shots.
TILT=[-1.6, 0.9, -0.5, 1.4, -1.1, 0.6, 1.7, -0.8, 1.0, -1.5, 0.7, -0.4]
def designs_section(shade=True):
    cards=""
    for i,(pid,name) in enumerate(DESIGNS):
        rot=TILT[i % len(TILT)]
        cards+=(f'<div class="design-card reveal" style="--rot:{rot}deg"><div class="design-thumb">'
                f'<img src="{img_url(pid)}" alt="{name} — a Bravaura guided painting design" loading="lazy" '
                f'onerror="this.style.display=\'none\'"></div><span class="design-name">{name}</span></div>')
    cls=" section--cream2" if shade else ""
    return f'''<section class="section{cls}">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">crowd favorites</span>
    <h2>A few of the many designs we offer.</h2>
    <p class="lead" style="font-size:1.06rem">These are some of our most-requested paintings, but they're only a starting point. We'll match the design to your group, your occasion, or your theme. Every one is taught step by step.</p></div>
    <div class="design-carousel reveal">
      <button class="dcar-btn dcar-prev" type="button" aria-label="Previous designs" aria-controls="design-track">&#8592;</button>
      <div class="design-track" id="design-track" tabindex="0" role="region" aria-label="Painting designs">{cards}</div>
      <button class="dcar-btn dcar-next" type="button" aria-label="More designs" aria-controls="design-track">&#8594;</button>
    </div>
    <p class="design-note">Picturing something else? Just ask &mdash; we'll paint it.</p>
  </div>
</section>'''

def designs_teaser():
    return '''<section class="section section--cream2">
  <div class="container center narrow">
    <span class="eyebrow">crowd favorites</span>
    <h2>Not sure what to paint?</h2>
    <p class="lead" style="margin:0 auto">We have a whole menu of guided designs, from moonlit lakes to highland cows, and we will happily paint something else entirely if you have an idea.</p>
    <div style="margin-top:24px"><a href="gallery.html" class="btn btn--purple btn--lg">Browse the designs</a></div>
  </div>
</section>'''

def signup_band():
    return '''<section class="signup" id="signup">
  <div class="container">
    <div class="signup-card reveal">
      <div>
        <h2>Want to join our email list?</h2>
        <p>New events, seasonal classes, and open dates, sent about <strong>once a month</strong>. Sometimes less.</p>
      </div>
      <div>
        <form data-bravaura-form name="email-signup" method="post" novalidate
              action="https://app.kit.com/forms/9788191/subscriptions"
              data-endpoint="https://app.kit.com/forms/9788191/subscriptions"
              data-sv-form="9788191" data-uid="bdd7f90ec0"
              data-success="Thanks for joining! Check your email for a confirmation link. One click and you're on the list.">
          <div class="signup-row">
            <label for="signup-email" class="sr-only">Email address</label>
            <input id="signup-email" name="email_address" type="email" required placeholder="you@email.com" autocomplete="email">
            <button type="submit" class="btn btn--purple">Join the list</button>
          </div>
          <span class="signup-fine">Unsubscribe any time. We never share or sell your address.</span>
          <div class="form-status" role="status" aria-live="polite"></div>
        </form>
      </div>
    </div>
  </div>
</section>'''

# Promo popup — Olipop & Paint, Sept 12 2026. Auto-hides on Sept 11 (see PROMO_END in main.js).
def promo_popup():
    tickets=(f'<a href="{TICKETS_URL}" target="_blank" rel="noopener" '
             f'class="btn btn--purple btn--lg promo-cta">Buy tickets</a>') if TICKETS_URL else ''
    secondary_cls='btn btn--white promo-cta' if TICKETS_URL else 'btn btn--purple btn--lg promo-cta'
    flyer=(f'<div class="promo-flyer"><a href="{FLYER_IMG}" target="_blank" rel="noopener" '
           f'title="Open the full flyer"><img src="{FLYER_IMG}" alt="Olipop &amp; Paint flyer: Saturday September 12 2026, '
           f'5 to 7pm at Livi\'s Lavender Farm, Robbinsville NJ. Tickets $65 per person." loading="lazy" '
           f'onerror="this.closest(\'.promo-flyer\').remove()"></a></div>') if FLYER_IMG else ''
    return f'''<div id="promo-pop" role="dialog" aria-modal="true" aria-labelledby="promo-title" aria-hidden="true">
  <div class="promo-card">
    <button class="promo-close" type="button" aria-label="Close">&times;</button>
    {flyer}
    <div class="promo-body">
      <span class="promo-kicker">save the date</span>
      <h3 id="promo-title">Olipop &amp; Paint</h3>
      <p class="promo-when">Saturday, September 12 &middot; 5:00&ndash;7:00 pm</p>
      <p class="promo-where">Livi\'s Lavender Farm &middot; Robbinsville, NJ</p>
      <p class="promo-note">A lavender-themed painting, step by step. All supplies included, plus a lavender sachet fresh from the farm. All ages, no experience needed.</p>
      <p class="promo-early">Early bird: 15% off with code <b>EARLYBIRD15</b> until Aug 23</p>
      {tickets}
      <a href="#signup" class="{secondary_cls}">Get event updates</a>
    </div>
  </div>
</div>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/bravaura-logo-final.png" alt="Bravaura LLC">
        <p>Mobile art parties across New Jersey. We bring everything.</p>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <ul>
          <li><a href="services.html">Services</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="quote.html">Get a Quote</a></li>
          <li><a href="contact.html">Book an Event</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Get in Touch</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{IG_URL}" target="_blank" rel="noopener">@{IG}</a></li>
          <li>Serving New Jersey and surrounding areas</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> Bravaura LLC. All rights reserved.</span>
    </div>
  </div>
</footer>'''

PAGES=[]
def page(filename,title,description,active,body,splash=False):
    PAGES.append(filename)
    splash_html=('<div id="site-splash" aria-hidden="true"><video autoplay muted playsinline '
                 'poster="assets/bravaura-logo-painting-poster.png"><source src="assets/bravaura-logo-painting.mp4" '
                 'type="video/mp4"></video></div>') if splash else ""
    html=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE_URL}/{filename}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}/{filename}">
<meta property="og:site_name" content="Bravaura LLC">
<meta property="og:image" content="{SITE_URL}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Bravaura LLC — mobile art parties in New Jersey">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE_URL}/assets/og-image.jpg">
<link rel="icon" type="image/png" href="assets/bravaura-logo-final.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,WONK@0,9..144,400,0;0,9..144,500,0;0,9..144,600,0;0,9..144,700,0;1,9..144,500,0&family=Inter:wght@400;500;600;700&family=Caveat:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
{splash_html}
{header(active)}
<main>
{body}
</main>
{signup_band()}
{footer()}
{promo_popup()}
<script src="js/main.js"></script>
</body>
</html>'''
    with open(os.path.join(OUT,filename),"w",encoding="utf-8") as f:
        f.write(html)
    print("wrote",filename)

# ---- reusable components ----
def cta(script_line="Got a date in mind?", heading="Let's make something together.",
        text="Tell us the occasion and we'll send a custom quote within 24 hours.",
        primary=("Tell us about your event","contact.html"), secondary=("Browse services","services.html")):
    sec=f'<a href="{secondary[1]}" class="btn btn--white btn--lg">{secondary[0]}</a>' if secondary else ""
    return f'''<section class="section cta">
  <div class="container">
    <span class="script-accent">{script_line}</span>
    <h2>{heading}</h2>
    <p>{text}</p>
    <div class="btn-row" style="justify-content:center">
      <a href="{primary[1]}" class="btn btn--gold btn--lg">{primary[0]}</a>
      {sec}
    </div>
  </div>
</section>'''

def page_hero(eyebrow, h1, lead, script=None, cta_btn=("Book a date","contact.html")):
    scr=f'<span class="script-accent">{script}</span>' if script else ""
    btn=f'<div class="btn-row" style="margin-top:1.6rem"><a href="{cta_btn[1]}" class="btn btn--gold btn--lg">{cta_btn[0]}</a></div>' if cta_btn else ""
    return f'''<section class="page-hero">
  <div class="container">
    <span class="eyebrow">{eyebrow}</span>
    {scr}<h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {btn}
  </div>
</section>'''

def floating_bg():
    star='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.3 6.8L21 10l-5.5 4L17.6 21 12 16.8 6.4 21l2.1-7L3 10l6.7-1.2z"/></svg>'
    splat=('<svg viewBox="0 0 64 64" fill="currentColor"><path d="M33 6c7-3 15 2 15 10 0 5 6 6 8 11 3 6-2 13-9 14-4 .6-5 6-10 7-7 1.6-14-3-14-10 0-4-6-5-8-10-3-7 2-14 9-15 4-.6 5-15 9-17z"/></svg>')
    squig='<svg viewBox="0 0 80 34" fill="none"><path d="M3 18 q 13 -18 26 0 t 26 0 t 22 0" stroke="currentColor" stroke-width="5" stroke-linecap="round"/></svg>'
    return (f'<div class="float-layer" aria-hidden="true">'
            f'<span class="fd fd-1">{star}</span>'
            f'<span class="fd fd-2">{splat}</span>'
            f'<span class="fd fd-3">{squig}</span>'
            f'<span class="fd fd-4">{star}</span></div>')

def marquee():
    line='Paint &amp; Sip <b class="star">&#10038;</b> Birthday Parties <b class="star">&#10038;</b> Team Nights <b class="star">&#10038;</b> Face Painting <b class="star">&#10038;</b> Master Classes <b class="star">&#10038;</b> '
    return f'<div class="marquee" aria-hidden="true"><div class="marquee-track"><span>{line}</span><span>{line}</span></div></div>'

def testimonials_section():
    cards=""
    for i,t in enumerate(TESTIMONIALS):
        d=f" d{i+1}" if i>0 else ""
        photo=""
        if t.get("image"):
            photo=(f'<div class="note-photo"><img src="{img_url(t["image"])}" alt="{t.get("image_alt","")}" '
                   f'loading="lazy" onerror="this.closest(\'.note-photo\').style.display=\'none\'"></div>')
        cards+=f'''<div class="note reveal{d}">
        {photo}<div class="note-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="q">&ldquo;{t["quote"]}&rdquo;</p>
        <div class="who">{t["author"]} <span>&middot; {t["context"]}</span></div>
      </div>'''
    return f'''<section class="section">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">don't just take our word</span><h2>Loved by hosts across New Jersey</h2></div>
    <div class="notes">{cards}</div>
    <div style="text-align:center;margin-top:40px" class="reveal"><a href="{IG_URL}" target="_blank" rel="noopener" class="btn btn--teal">See more on Instagram @{IG}</a></div>
  </div>
</section>'''

def write_seo_files():
    urls="".join(
        f"  <url><loc>{SITE_URL}/{fn}</loc><priority>{'1.0' if fn=='index.html' else '0.7'}</priority></url>\n"
        for fn in PAGES)
    with open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + urls + '</urlset>\n')
    with open(os.path.join(OUT,"robots.txt"),"w",encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    print("wrote sitemap.xml + robots.txt")

def write_assets():
    os.makedirs(os.path.join(OUT,"css"),exist_ok=True)
    os.makedirs(os.path.join(OUT,"js"),exist_ok=True)
    with open(os.path.join(OUT,"css","styles.css"),"w",encoding="utf-8") as f: f.write(CSS)
    with open(os.path.join(OUT,"js","main.js"),"w",encoding="utf-8") as f: f.write(JS)
    print("wrote css/styles.css + js/main.js")

print("helpers loaded")

# ================================================================ HOME
home_body=f'''
<section class="hero">
  <span class="blob" style="width:340px;height:340px;background:var(--teal);top:-60px;left:-90px"></span>
  <span class="blob" style="width:260px;height:260px;background:var(--gold);bottom:-40px;right:38%;opacity:.35"></span>
  <div class="container hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">mobile art parties in NJ &#10038;</span>
      <h1>We bring the<span class="script-accent">whole art party</span>right to your table.</h1>
      <p class="hero-lead">Paint &amp; sip, birthday parties, team nights, face painting, and painting lessons, anywhere in New Jersey. You pick a date. We do the rest.</p>
      <div class="hero-cta">
        <a href="contact.html" class="btn btn--gold btn--lg">Book a date</a>
        <a href="services.html" class="btn btn--white btn--lg">See what we do</a>
      </div>
    </div>
    <div class="hero-photo-wrap">
      <span class="hero-sticker" aria-hidden="true"><img src="assets/bravaura-logo-final.png" alt=""></span>
      <div class="hero-photo hero-photo--main"><img src="{img_url(IMG_HERO)}" alt="Kids proudly holding up their finished paintings at a Bravaura art party" loading="eager" onerror="this.closest('.hero-photo').classList.add('fail')"></div>
      <div class="hero-photo hero-photo--mini"><img src="{img_url(P_KID_FLOWER)}" alt="A young painter holding up her finished flower painting" loading="lazy" onerror="this.closest('.hero-photo').classList.add('fail')"></div>
    </div>
  </div>
</section>

{marquee()}

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">the whole deal</span>
      <h2>All you do is pick a date.</h2>
      <p style="font-size:1.15rem;max-width:52ch">We handle the rest. Supplies, easels, aprons, the teaching, the cleanup. It arrives with us and it leaves with us.</p>
    </div>
    <div class="steps">
      <svg class="steps-line" viewBox="0 0 800 40" preserveAspectRatio="none" fill="none" aria-hidden="true"><path d="M0 20 C 110 7, 210 33, 320 20 S 530 7, 640 20 S 720 31, 800 20" stroke="currentColor" stroke-width="3" stroke-dasharray="2 12" stroke-linecap="round"/></svg>
      <div class="step reveal d1"><div class="step-num">1</div><h3>You pick a date</h3><p>Tell us the occasion and roughly how many people. That's your whole job.</p></div>
      <div class="step reveal d2"><div class="step-num">2</div><h3>We show up loaded</h3><p>Everything comes with us: paints, canvases, easels, aprons, the works.</p></div>
      <div class="step reveal d3"><div class="step-num">3</div><h3>We teach it</h3><p>Step by step, at whatever pace the room needs. No art experience required.</p></div>
      <div class="step reveal d4"><div class="step-num">4</div><h3>We pack it all out</h3><p>Your space ends up cleaner than we found it. You keep the paintings.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream2" id="services">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">pick your kind of fun</span><h2>Five ways to get everyone creating.</h2></div>
    <div class="bento">
      <a class="svc svc--birthday reveal" href="birthday-parties.html">
        <div class="svc-img"><img src="{img_url(IMG_BIRTHDAY)}" alt="Kids painting at a birthday party" loading="lazy" onerror="this.style.display='none'"></div>
        <span class="tag">for the birthday kid</span><h3>Birthday Parties</h3>
        <p>Everyone paints something they'll actually hang up, and you get to be at the party instead of running it.</p>
        <span class="go">See birthday parties &rarr;</span>
      </a>
      <a class="svc svc--sip reveal d1" href="paint-sip.html">
        <div class="svc-img"><img src="{img_url(IMG_SIP)}" alt="Adults at a paint and sip night" loading="lazy" onerror="this.style.display='none'"></div>
        <span class="tag">bring the drinks</span><h3>Paint &amp; Sip</h3>
        <p>You pour the drinks. We handle the rest.</p>
        <span class="go">See paint &amp; sip &rarr;</span>
      </a>
      <a class="svc svc--corp reveal" href="corporate.html">
        <div class="svc-img"><img src="{img_url(IMG_CORP)}" alt="Coworkers painting together at a team event" loading="lazy" onerror="this.style.display='none'"></div>
        <span class="tag">team building &amp; stress relief</span><h3>Corporate &amp; Team Nights</h3>
        <p>Everyone paints the same project and no two come out alike. It gets people off their screens and talking to each other. 10-person minimum.</p>
        <span class="go">See team events &rarr;</span>
      </a>
      <a class="svc svc--face reveal" href="face-painting.html">
        <div class="svc-img"><img src="{img_url(IMG_FACE)}" alt="A child with colorful face paint" loading="lazy" onerror="this.style.display='none'"></div>
        <span class="tag">a party favorite</span><h3>Face Painting</h3>
        <p>Skin-safe designs for whatever the kids ask for. 2-hour minimum.</p>
        <span class="go">See face painting &rarr;</span>
      </a>
      <a class="svc svc--master reveal d1" href="master-classes.html">
        <div class="svc-img"><img src="{img_url(IMG_MASTER)}" alt="A Bravaura painting and drawing lesson in progress" loading="lazy" onerror="this.style.display='none'"></div>
        <span class="tag">go deeper</span><h3>Master Classes</h3>
        <p>Painting and drawing lessons for all ages. One-on-one, two or three together, or a small group. No minimum.</p>
        <span class="go">See master classes &rarr;</span>
      </a>
    </div>
  </div>
</section>

<section class="section why">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">why book us</span><h2>All the art. None of the work.</h2></div>
    <div class="why-grid">
      <div class="why-item reveal d1"><div class="why-ic">{icon("truck")}</div><h3>We come to you</h3><p>Your kitchen, your backyard, your office, a rented hall. Anywhere in New Jersey.</p></div>
      <div class="why-item reveal d2"><div class="why-ic">{icon("check")}</div><h3>It's all included</h3><p>Setup, supplies, teaching, and cleanup in one booking. You don't buy a thing.</p></div>
      <div class="why-item reveal d3"><div class="why-ic">{icon("palette")}</div><h3>No experience needed</h3><p>Most people who book us have never painted before. That's the normal case, not the exception.</p></div>
      <div class="why-item reveal d4"><div class="why-ic">{icon("users")}</div><h3>Any group size</h3><p>A handful of kids or a whole office. We scale the setup to fit.</p></div>
    </div>
  </div>
</section>


{cta()}
'''
page("index.html","Bravaura LLC | Mobile Art Parties in New Jersey",
     "We bring the whole art party to you: paint & sip, birthday parties, team nights, face painting, and painting lessons across New Jersey. We set up, teach, and clean up.",
     "index.html",home_body,splash=True)

# ================================================================ SERVICES HUB
services_body=f'''
{page_hero("what we do","Five ways to get everyone creating",
  "Birthday parties, paint &amp; sip nights, team events, face painting, and painting lessons, all across New Jersey.",
  script="Pick your kind of fun.", cta_btn=("Get a custom quote","contact.html"))}

<section class="section">
  <div class="container">
    <div class="bento">
      <a class="svc svc--birthday reveal" href="birthday-parties.html"><div class="svc-img"><img src="{img_url(IMG_BIRTHDAY)}" alt="Kids painting at a birthday party" loading="lazy" onerror="this.style.display='none'"></div><span class="tag">for the birthday kid</span><h3>Birthday Parties</h3><p>A guided art project that becomes the highlight of the party, for kids, teens, or adults.</p><span class="go">Learn more &rarr;</span></a>
      <a class="svc svc--sip reveal d1" href="paint-sip.html"><div class="svc-img"><img src="{img_url(IMG_SIP)}" alt="Adults at a paint and sip night" loading="lazy" onerror="this.style.display='none'"></div><span class="tag">bring the drinks</span><h3>Paint &amp; Sip</h3><p>Painting, drinks, and good company. You bring the beverages, we bring the art.</p><span class="go">Learn more &rarr;</span></a>
      <a class="svc svc--corp reveal" href="corporate.html"><div class="svc-img"><img src="{img_url(IMG_CORP)}" alt="Coworkers painting together" loading="lazy" onerror="this.style.display='none'"></div><span class="tag">team building &amp; stress relief</span><h3>Corporate &amp; Team Nights</h3><p>Low pressure, no cleanup, and a real break from the desk. 10-person minimum.</p><span class="go">Learn more &rarr;</span></a>
      <a class="svc svc--face reveal" href="face-painting.html"><div class="svc-img"><img src="{img_url(IMG_FACE)}" alt="A child with colorful face paint" loading="lazy" onerror="this.style.display='none'"></div><span class="tag">a party favorite</span><h3>Face Painting</h3><p>Custom designs and character requests for parties, festivals, and events. 2-hour minimum.</p><span class="go">Learn more &rarr;</span></a>
      <a class="svc svc--master reveal d1" href="master-classes.html"><div class="svc-img"><img src="{img_url(IMG_MASTER)}" alt="A Bravaura painting and drawing lesson in progress" loading="lazy" onerror="this.style.display='none'"></div><span class="tag">go deeper</span><h3>Master Classes</h3><p>Private, semi-private, or small-group painting and drawing lessons. All ages, no minimum.</p><span class="go">Learn more &rarr;</span></a>
    </div>
  </div>
</section>

<section class="section section--cream2">
  <div class="container center narrow">
    <span class="eyebrow">every event includes</span>
    <h2>Setup. Instruction. Cleanup.</h2>
    <p class="lead" style="margin:0 auto">We bring the tables, easels, canvases, paints, and aprons. We teach the whole thing. Then we pack it all out.</p>
  </div>
</section>

{cta()}
'''
page("services.html","Art Event Services NJ | Bravaura LLC",
     "Mobile art event services across New Jersey: birthday parties, paint & sip, corporate team building, face painting, and painting lessons. All-inclusive, and we come to you.",
     "services.html",services_body)

# ---- reusable service page ----
def service_page(filename,title,desc,eyebrow,h1,script,tagline,intro,includes,
                 whofor,duration,youprovide,pill_list,book_label,
                 img_id,img_alt,shadow,extra=""):
    inc="".join(f"<li>{i}</li>" for i in includes)
    pills="".join(f'<span class="pill">{p}</span>' for p in pill_list)
    body=f'''
{page_hero(eyebrow,h1,tagline,script=script,cta_btn=(book_label,"contact.html"))}

<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">the experience</span>
      <h2>What to expect</h2>
      <p class="lead" style="font-size:1.12rem">{intro}</p>
      <h3 style="margin-top:1.4rem">What's included</h3>
      <ul class="checklist">{inc}</ul>
    </div>
    <div class="split-media reveal d1">{frame_photo(img_id,img_alt,"r",shadow)}</div>
  </div>
</section>

<section class="section section--cream2">
  <div class="container">
    <div class="info-grid">
      <div class="info-card reveal"><div class="ic ic--magenta">{icon("heart")}</div><h3>Who it's for</h3><p>{whofor}</p></div>
      <div class="info-card reveal d1"><div class="ic ic--teal">{icon("clock")}</div><h3>How long</h3><p>{duration}</p></div>
      <div class="info-card reveal d2"><div class="ic ic--gold">{icon("gift")}</div><h3>You provide</h3><p>{youprovide}</p></div>
    </div>
    <div style="margin-top:34px" class="reveal"><h3>Make it yours</h3><div class="pill-row">{pills}</div></div>
  </div>
</section>
{extra}
{cta(script_line="Let's plan it.", heading="Ready when you are.", primary=(book_label,"contact.html"))}
'''
    page(filename,title,desc,"services.html",body)

service_page("birthday-parties.html",
  "Birthday Party Painting NJ | Bravaura LLC",
  "Stress-free birthday art parties across New Jersey. We set up, teach a guided painting project everyone takes home, and clean up. For kids, teens, and adults.",
  "birthday parties","Birthday parties made easy","The party everyone remembers.",
  "You handle the guest list and the cake. We handle every messy, magical bit in between.",
  "Turn any birthday into a hands-on art party. We arrive with everything, guide your guests through a project they'll be proud of, and clean up every last drop before we go. All you handle is the guest list and the cake.",
  ["Full setup: tables, easels, canvases, paints, brushes, and aprons",
   "A guided project led by a professional art educator",
   "A finished piece for every guest to take home",
   "Complete cleanup. We leave your space spotless"],
  "Kids, teens, and adults. We tailor the project and pacing to the age group so everyone's engaged.",
  "Most parties run 1.5 to 2 hours.",
  "The venue and the guest list. We bring absolutely everything else.",
  ["Choose your project","Kids / teens / adults","1.5 or 2 hours","Decorations","Goodie bags","Slime table","Glow-in-the-dark painting","Games &amp; activities","Add-on face painting"],
  "Book a birthday party", IMG_BIRTHDAY,"Guided painting at a Bravaura birthday party","magenta",
  extra=f'''
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">optional add-ons</span><h2>Make it a whole party, not just a painting.</h2>
    <p class="lead" style="font-size:1.05rem">Decorations, goodie bags, a slime table, glow-in-the-dark painting, games. Mix and match whatever fits the celebration, tell us what you're picturing, and we'll build it into your quote.</p></div>
    <div class="pill-row reveal d1" style="margin-top:22px"><span class="pill">Decorations</span><span class="pill">Goodie bags</span><span class="pill">Slime table</span><span class="pill">Glow-in-the-dark painting</span><span class="pill">Games &amp; activities</span><span class="pill">Add-on face painting</span></div>
  </div>
</section>''')

service_page("paint-sip.html",
  "Paint & Sip Events NJ | Bravaura LLC",
  "Mobile paint & sip parties across New Jersey. Guided painting for adults: ladies' nights, friend groups, and team bonding. You bring the drinks, we bring the art.",
  "paint & sip","Painting + drinks + friends","The easiest good night in.",
  "A relaxed night in. Everyone leaves with a canvas.",
  "Our paint &amp; sip events turn a living room, backyard, or private room into a creative escape. You pour the drinks; we guide the painting. It's the ideal ladies' night, friend gathering, or laid-back team hangout. No art experience required.",
  ["Full setup and breakdown",
   "Guided, step-by-step painting instruction",
   "A beverage-friendly setup. You provide the drinks",
   "A completed canvas for everyone to take home"],
  "Adults: ladies' nights, friend groups, birthdays, and casual team bonding.",
  "Typically 2 to 3 hours.",
  "Your drinks of choice and the space. We bring the art.",
  ["Wine / beer / non-alcoholic","Choose your painting","2 or 3 hours","Private or group","Seasonal themes"],
  "Get a custom quote", IMG_SIP,"Friends painting and laughing at a paint and sip night","purple",
  extra=designs_teaser())

service_page("corporate.html",
  "Corporate Team Building &amp; Wellness Art Events NJ | Bravaura LLC",
  "Art-based corporate team building and mental health breaks across New Jersey. Facilitated, low-pressure creative sessions that relieve stress and build connection. We come to your office, and setup and cleanup are included.",
  "corporate &amp; team nights","Team building &amp; mental health breaks","Connection, minus the trust falls.",
  "The team offsite people don't dread.",
  "Give your team something better than another meeting. An hour with a brush pulls people off their screens and gives them something to talk about that isn't work. Our sessions are facilitated, so nobody has to make small talk from a standing start, and everyone ends up holding something they made. We come to your office or venue and leave it exactly as we found it.",
  ["Professional facilitation and icebreaking",
   "A real break: hands busy, screens off",
   "Guided instruction for collaborative or individual artwork",
   "All materials, setup, and breakdown included",
   "Zero cleanup for your office or venue"],
  "Offices, departments, offsites, wellness days, and client events. 10-person minimum.",
  "Anywhere from a 1-hour lunch break to a 3-hour session.",
  "The space (or let us suggest one) and your headcount. We handle the rest.",
  ["Collaborative or individual","1 to 3 hours","On-site at your office","Wellness / mental health days","Branded project options","Any team size"],
  "Request a team package", IMG_CORP,"A team painting together during a corporate art session","teal",
  extra='''
<section class="section section--cream2">
  <div class="container center narrow">
    <span class="eyebrow">why it works</span>
    <h2>A team that unwinds together works better together.</h2>
    <p class="lead" style="margin:0 auto">Creative time is one of the simplest ways to lower stress at work. There's no scoreboard, no deadline, and nothing to get wrong. Just a couple of hours where everyone gets to make something. Teams leave looser and more talkative. Book it as a wellness day, a lunch-and-learn, or a mid-quarter reset.</p>
  </div>
</section>''')

service_page("face-painting.html",
  "Face Painting Services NJ | Bravaura LLC",
  "Professional face painting for parties, festivals, and events across New Jersey. Custom designs and character art with a 2-hour minimum. Book Bravaura for your celebration.",
  "face painting","Face painting that steals the show","Butterflies, tigers, superheroes.",
  "Bright designs that make any event more fun, for all ages.",
  "Add a splash of magic to your event with professional face painting. From classic butterflies and superheroes to custom character requests, we create bright, skin-safe designs that light up faces at parties, festivals, and celebrations of every kind.",
  ["A professional face painting artist",
   "Custom designs and character requests",
   "Skin-safe, professional-grade paints",
   "Flexible hourly booking"],
  "Birthday parties, festivals, corporate family days, and community celebrations.",
  "Booked hourly, with a 2-hour minimum, then as long as your event needs.",
  "The event and the smiles. We bring the paints, brushes, and designs.",
  ["Traditional designs","Character art","Themed / event branding","Glitter add-ons","2-hour minimum"],
  "Book face painting", IMG_FACE,"A colorful butterfly face paint design","orange")

service_page("master-classes.html",
  "Private Painting &amp; Drawing Lessons NJ | Bravaura LLC",
  "Private and semi-private painting and drawing lessons across New Jersey, for all ages, one-on-one or a group of two or three, no minimum. Focused instruction in acrylics, watercolor, drawing, and technique, all materials included. We come to you.",
  "master classes","Painting &amp; drawing lessons","For all ages, at any group size.",
  "Real instruction for kids, teens, and adults, at whatever size feels right. Even just you.",
  "Master classes are for when you want to build a real skill, not just make one painting. They're for everybody: kids, teens, and adults, beginners and people who've been drawing for years. Take it one-on-one, split it with a friend or two, or gather a small group; there's no minimum here. We go deep on a single technique in painting or drawing: acrylics, watercolor, color mixing, shading, portraits, whatever you want to master. Hands-on, personalized, and paced for you.",
  ["Private one-on-one, semi-private for two or three, or a small group",
   "Painting or drawing: acrylics, watercolor, pencil, charcoal",
   "A technique or theme of your choice",
   "All materials, setup, and cleanup included",
   "Personalized feedback as you work"],
  "Kids, teens, and adults. Total beginners welcome, and so are people who already paint or draw. We match the project and the pace to whoever's in the room. No minimum group size.",
  "One to two hours. Multi-session series available.",
  "The space and the curiosity. We bring everything else.",
  ["All ages","Private one-on-one","Semi-private (2&ndash;3)","Small group","Painting or drawing","Single class or a series","Beginner or advanced","1 or 2 hours","In-home or at a venue"],
  "Ask about master classes", IMG_MASTER,"A painting and drawing lesson in progress","teal")

print("home + services done")

# ================================================================ GALLERY
# NOTE: Kendal's headshot and the celestial/"galaxy" painting were removed (looked too AI).
# Add a fresh "kids holding up their paintings" shot here once generated/chosen.
GALLERY=[(P_LAV_FIELD,"Guests holding their finished paintings at a lavender farm paint & sip"),
         (P_TENT_GOLDEN,"Our tent set up in the lavender field at golden hour"),
         (P_BUTTERFLY,"A group holding up their finished butterfly canvases"),
         (P_TENT_ROW,"A long table of painters under the tent at the lavender farm"),
         (P_TENT_LAUGH,"Guests laughing their way through a lavender farm paint & sip"),
         (P_BFLY_CANVAS,"A finished butterfly and ribbon canvas from a fundraiser paint & sip"),
         (P_LAV_CANVAS,"A finished lavender canvas held up at the end of the night"),
         (P_CANVAS_PINE,"A finished northern lights canvas"),
         (P_APRON,"Mixing colors on the palette"),
         (P_ARTIST,"Painting the demo canvas guests follow along with"),
         (P_LAV_TEACH,"Step-by-step instruction at every table"),
         (P_TABLE_GROUP,"An indoor paint & sip in full swing"),
         ("assets/gallery/face-painting.jpg","Face painting at a community event"),
         (P_KID_FLOWER,"A young painter with her finished flower canvas"),
         ("assets/gallery/design-fall-gnome.jpg","A finished fall gnome canvas"),
         ("assets/gallery/community-tent.jpg","Kids lining up at the Bravaura tent at a local event"),
         ("assets/gallery/vendor-table.jpg","Our table at a community event"),
         ("assets/gallery/vendor-stickers.jpg","Bravaura stickers at our event table")]
def gallery_grid():
    items=""
    for pid,alt in GALLERY:
        onerr="this.style.display='none'"
        items+=f'<div class="gallery-item reveal"><img src="{img_url(pid)}" alt="{alt}" loading="lazy" onerror="{onerr}"></div>'
    solo=" gallery-grid--solo" if len(GALLERY)==1 else ""
    return f'<div class="gallery-grid{solo}">{items}</div>'
gallery_body=f'''
{page_hero("gallery","A peek at the paint",
  "Real photos from real Bravaura events across New Jersey &mdash; lavender farm paint &amp; sip nights, private parties, and in-home sessions. Every canvas on this page was painted by a guest.",
  script="See the mess we make.", cta_btn=("Book your event","contact.html"))}
<section class="section"><div class="container">{gallery_grid()}</div></section>
{cta(script_line="Want in?", heading="Your event could be up here next.", primary=("Book your event","contact.html"))}
'''
page("gallery.html","Gallery | Bravaura LLC Mobile Art Events NJ",
     "See Bravaura mobile art events in action across New Jersey and browse some of our most popular painting designs from birthday parties, paint & sip nights, team building, and face painting.",
     "gallery.html",gallery_body)

# ================================================================ ABOUT
about_body=f'''
{page_hero("about bravaura","All you have to do is paint",
  "Bravaura started with a simple idea: everyone deserves the fun of making something without the work around it. We haul it in, we teach it, we clean it up. All you have to do is paint. We're based in New Jersey, serving New Jersey and surrounding areas.",
  script="Hi, we're Bravaura.", cta_btn=("Book an event","contact.html"))}

<section class="section">
  <div class="container split">
    <div class="split-media reveal">{frame_photo(IMG_HEADSHOT,"Kendal Plumstead, founder of Bravaura LLC","l","magenta","frame-photo--headshot")}</div>
    <div class="reveal d1">
      <span class="eyebrow">our story</span>
      <h2>Founded by Kendal Plumstead</h2>
      <p>It started with a girl from New Jersey who loves art and loves teaching it even more. Kendal has a BA in Art Education and is certified K–12, and she teaches every age group, from little kids to adults. She also studied business at Indiana University&rsquo;s Kelley School of Business.</p>
      <p>She wanted art parties that didn't ask for a studio, any experience, or much planning. The name comes from two things she loves: theater, where "brava" is the cheer for a performance that lands, and "aura," the feeling a room carries. That's what she set out to build into every event.</p>
      <p>Most people who book us are sure they can't paint. Watching that change over the course of an evening is the reason this business exists.</p>
      <p class="mb-0">Celebrations shouldn't get buried in setup and cleanup, so we handle all of it. You pick the occasion. We bring the rest to your door.</p>
    </div>
  </div>
</section>

<section class="section why">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">what makes us different</span><h2>We come to you, and we bring all of it.</h2></div>
    <div class="why-grid">
      <div class="why-item reveal d1"><div class="why-ic">{icon("truck")}</div><h3>Mobile</h3><p>We come to you, anywhere in NJ.</p></div>
      <div class="why-item reveal d2"><div class="why-ic">{icon("check")}</div><h3>All-inclusive</h3><p>Setup, instruction, and cleanup, all handled.</p></div>
      <div class="why-item reveal d3"><div class="why-ic">{icon("palette")}</div><h3>Professional</h3><p>Taught by a certified art educator, not a host reading a script.</p></div>
      <div class="why-item reveal d4"><div class="why-ic">{icon("heart")}</div><h3>Personal</h3><p>We build the project around your group.</p></div>
    </div>
  </div>
</section>

{cta(script_line="Let's make something.", heading="Bring the art to your door.", primary=("Book an event","contact.html"))}
'''
page("about.html","About | Bravaura LLC Mobile Art Events NJ",
     "Meet Kendal Plumstead, the TCNJ-trained art educator behind Bravaura LLC, running mobile all-inclusive art events across New Jersey. We set up, teach, and clean up; all you have to do is paint.",
     "about.html",about_body)

# ================================================================ PRICING (no dollar amounts)
def price_card(shadow_ic, icon_name, title, blurb, items):
    lis="".join(f"<li>{i}</li>" for i in items)
    return f'''<div class="info-card reveal"><div class="ic ic--{shadow_ic}">{icon(icon_name)}</div>
      <h3>{title}</h3><p style="margin-bottom:.6rem">{blurb}</p>
      <ul class="checklist" style="margin-top:.4rem">{lis}</ul></div>'''
pricing_cards=(
  price_card("magenta","heart","Birthday Parties","Priced per guest, with the whole experience included.",["Setup, instruction &amp; cleanup included","Guided project for any age","Add-ons available: decorations, goodie bags, slime table, glow-in-the-dark, games"])+
  price_card("purple","spark","Paint &amp; Sip","Priced per guest — you bring the drinks, we bring the art.",["Setup, instruction &amp; cleanup included","Great for ladies' nights &amp; friend groups","Seasonal themes on request"])+
  price_card("teal","users","Corporate &amp; Team Nights","Priced per person, 10-person minimum.",["Facilitation, materials &amp; cleanup included","Collaborative or individual projects","On-site at your office or a venue"])+
  price_card("orange","palette","Face Painting","Booked hourly, 2-hour minimum.",["A professional artist for your event","Custom designs &amp; character art","Perfect alongside a birthday party"]))
pricing_body=f'''
{page_hero("pricing","Every event is a custom quote",
  "No two events are the same, so every quote is built around yours: your service, your group size, and how far we're traveling. We confirm the exact number by email before you book.",
  script="Simple and up front.", cta_btn=("Get your quote","contact.html"))}

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">how it's priced</span><h2>What goes into your quote.</h2></div>
    <div class="info-grid" style="grid-template-columns:repeat(2,1fr);margin-top:44px">{pricing_cards}</div>
  </div>
</section>

<section class="section section--cream2">
  <div class="container center narrow">
    <span class="eyebrow">good to know</span>
    <h2>Travel, deposits, and the fine print</h2>
    <p class="lead" style="margin:0 auto">Events include a travel fee based on distance from our Flemington base, included in your custom quote. A deposit reserves your date and applies toward your total, with the balance due at or before the event. Pay by card, check, or Venmo, and we can take card in person on the day of the event. Want us to bring a tent, tables, or chairs for an outdoor setup? That's available for an extra fee, so just mention it when you request your quote. And if you're a non-profit, school, or PTA, let us know on the quote form. We offer a reduced rate and we'll work within your budget.</p>
    <p class="form-note" style="margin-top:1.4rem">Your final, all-inclusive quote is confirmed by email within 24 hours of reaching out.</p>
  </div>
</section>

{cta(script_line="Ready for a number?", heading="Tell us about your event.", text="Send your details and we'll reply with an exact, all-inclusive quote within 24 hours.", primary=("Get your quote","contact.html"), secondary=("Browse services","services.html"))}
'''
page("pricing.html","Pricing | Bravaura LLC Mobile Art Events NJ",
     "How Bravaura pricing works — every mobile art event is a custom, all-inclusive quote covering setup, instruction, and cleanup, confirmed by email. Birthday parties, paint & sip, corporate, face painting, and master classes across NJ.",
     "pricing.html",pricing_body)

# ================================================================ QUOTE / BOOKING FORM
def booking_form(name="quote-request", heading="Request a quote", note_extra=""):
    return f'''<div class="form-card">
        <h2 class="mt-0" style="font-size:1.7rem">{heading}</h2>
        <p style="color:var(--body)">Tell us a little about your event and we'll take it from there.</p>
        <form data-bravaura-form name="{name}" method="POST" novalidate
              action="https://formsubmit.co/{FORM_EMAIL}"
              data-endpoint="https://formsubmit.co/ajax/{FORM_EMAIL}">
          <input type="hidden" name="_subject" value="Bravaura website: {heading}">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_next" value="{SITE_URL}/thank-you.html">
          <p style="display:none"><label>Leave this empty: <input name="_honey"></label></p>
          <div class="form-grid">
            <div class="field"><label for="name">Name <span class="req">*</span></label><input id="name" name="name" type="text" required autocomplete="name"></div>
            <div class="field"><label for="email">Email <span class="req">*</span></label><input id="email" name="email" type="email" required autocomplete="email"></div>
            <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
            <div class="field"><label for="event_type">Event type <span class="req">*</span></label>
              <select id="event_type" name="event_type" required>
                <option value="" disabled selected>Choose one&hellip;</option>
                <option>Birthday Party</option><option>Paint &amp; Sip</option>
                <option>Corporate &amp; Team Night</option><option>Face Painting</option>
                <option>Master Class</option><option>Other</option>
              </select>
            </div>
            <div class="field"><label for="event_date">Preferred date</label><input id="event_date" name="event_date" type="date"></div>
            <div class="field"><label for="group_size">Group size</label><input id="group_size" name="group_size" type="number" min="1" placeholder="e.g. 12"></div>
            <div class="field"><label for="nonprofit">Are you a non-profit?</label>
              <select id="nonprofit" name="nonprofit">
                <option value="" disabled selected>Choose one&hellip;</option>
                <option>No</option>
                <option>Yes &mdash; we're a non-profit</option>
                <option>Yes &mdash; a school or PTA</option>
              </select>
            </div>
            <div class="field full"><label for="location">Event location — town / venue / ZIP <span class="req">*</span></label><input id="location" name="location" type="text" placeholder="e.g. Flemington, NJ 08822" required></div>
            <div class="field full"><label for="setting">Is your event indoors or outdoors? <span class="req">*</span></label>
              <select id="setting" name="setting" required>
                <option value="" disabled selected>Choose one&hellip;</option>
                <option>Indoors</option>
                <option>Outdoors</option>
                <option>A bit of both</option>
                <option>Not sure yet</option>
              </select>
            </div>
            <div class="field full">
              <span class="field-label">Will you need a tent, tables, or chairs?</span>
              <div class="check-row">
                <label class="check"><input type="checkbox" name="setup_needs" value="Tent"> Tent</label>
                <label class="check"><input type="checkbox" name="setup_needs" value="Tables"> Tables</label>
                <label class="check"><input type="checkbox" name="setup_needs" value="Chairs"> Chairs</label>
              </div>
              <small class="field-hint">Check any you'd like us to bring, or leave them all blank if you're covered. These carry an extra fee, included in your quote.</small>
            </div>
            <div class="field full"><label for="message">Anything you're picturing?</label><textarea id="message" name="message" placeholder="The occasion, the vibe, add-ons, or any questions."></textarea></div>
          </div>
          <div style="margin-top:20px"><button type="submit" class="btn btn--gold btn--lg">Send my request</button></div>
          <div class="form-status" role="status" aria-live="polite"></div>
          <p class="form-note">Non-profits, schools, and PTAs get a reduced rate, so tell us your budget and we'll work with you. Your info is only used to plan your event, never shared.{note_extra}</p>
        </form>
      </div>'''

quote_body=f'''
{page_hero("get a quote","Tell us about your event",
  "Give us the basics and we'll send an exact, all-inclusive quote within 24 hours. Not sure on the details yet? Send what you've got and we'll help you figure it out.",
  script="No guessing games.", cta_btn=None)}


<section class="section">
  <div class="container split" style="align-items:start;gap:44px">
    <div class="reveal">{booking_form(name="quote-request", heading="Request your quote")}</div>
    <div class="reveal d1">
      <span class="eyebrow">what to expect</span>
      <h2>Here's what happens next.</h2>
      <ul class="checklist">
        <li>We read your details and put together an exact, all-inclusive price.</li>
        <li>You get a reply by email. No pressure, no obligation.</li>
        <li>Love it? A deposit reserves your date and we start planning the fun part.</li>
      </ul>
      <div class="info-card reveal d2" style="margin-top:26px">
        <h3 class="mt-0">Prefer to talk it through?</h3>
        <p class="mb-0">Call or text <a href="tel:{PHONE_TEL}" style="font-weight:700">{PHONE}</a>, or email <a href="mailto:{EMAIL}" style="font-weight:700">{EMAIL}</a>. We'd love to hear about your event.</p>
      </div>
    </div>
  </div>
</section>

{cta(script_line="Prefer we just handle it?", heading="Reach out and we'll take it from here.", primary=("Contact us","contact.html"), secondary=("Browse services","services.html"))}
'''
page("quote.html","Get a Quote | Bravaura LLC Art Events NJ",
     "Request a custom, all-inclusive quote for your Bravaura art event in New Jersey: birthday parties, paint & sip, corporate, face painting, and painting lessons. Reply within 24 hours.",
     "quote.html",quote_body)

# ================================================================ CONTACT
contact_body=f'''
{page_hero("book your event","Let's bring the art to you",
  "Fill out the form and we'll respond within 24 hours with a custom quote and next steps. Prefer to talk? Call, text, or email. We'd love to hear about your event.",
  script="Say hi.", cta_btn=None)}

<section class="section">
  <div class="container split" style="align-items:start;gap:44px">
    <div class="reveal">{booking_form(name="booking-request", heading="Book / request a quote", note_extra=" A deposit reserves your date once you're ready.")}</div>
    <div class="reveal d1">
      <span class="eyebrow">reach us directly</span>
      <h2>Three ways to get us.</h2>
      <div class="contact-info">
        <div class="contact-line"><div class="ci">{icon("phone")}</div><div><a href="tel:{PHONE_TEL}">{PHONE}</a><small>Call or text</small></div></div>
        <div class="contact-line"><div class="ci">{icon("mail")}</div><div><a href="mailto:{EMAIL}">{EMAIL}</a><small>We reply within 24 hours</small></div></div>
        <div class="contact-line"><div class="ci">{icon("instagram")}</div><div><a href="{IG_URL}" target="_blank" rel="noopener">@{IG}</a><small>See our latest work</small></div></div>
        <div class="contact-line"><div class="ci">{icon("pin")}</div><div><span>Serving New Jersey and surrounding areas</span><small>Distance affects pricing</small></div></div>
      </div>
    </div>
  </div>
</section>
'''
page("contact.html","Contact & Booking | Bravaura LLC Art Events NJ",
     "Book a Bravaura mobile art event in New Jersey. Request a custom quote for birthday parties, paint & sip, corporate team building, face painting, or a master class. Call or text 908-894-3611.",
     "contact.html",contact_body)

# ================================================================ FAQ
faqs=[
 ("Do you come to our location?",
  "Yes. Bravaura is fully mobile, serving New Jersey and surrounding areas, and we set everything up at your home, office, park, or venue. Distance affects pricing, and we'll always include any travel fee in your quote up front."),
 ("What if someone has no art experience?",
  "Perfect — that's most of our guests. Every session is led by a professional art educator with step-by-step instruction for all skill levels. No experience needed; everyone leaves with something they're proud of."),
 ("Can we customize the art project?",
  "Absolutely. We'll work with you to choose a project that fits your group, occasion, and theme. Just tell us what you're picturing and we'll make it happen."),
 ("What do we need to provide?",
  "Just the space and the people. We bring the tables, easels, canvases, paints, brushes, and aprons. For paint &amp; sip, you supply the drinks. That's it. If you'd like us to bring a tent, extra tables, or chairs for an outdoor event, that's available for an additional fee, so just mention it when you request your quote."),
 ("Do you provide decorations?",
  "We provide all the art supplies, setup, and cleanup. Decor is up to you, though decorations, goodie bags, and more can be added on to birthday parties — just ask and we'll build it into your quote."),
 ("How much does it cost?",
  "Every event is a custom, all-inclusive quote — it depends on the service, your group size, and how far we're traveling, and it always covers setup, instruction, and cleanup. Send us your details and we'll confirm an exact price by email within 24 hours."),
 ("Do you offer non-profit rates?",
  "We do. Non-profits, schools, and PTAs get a reduced rate — just select it on the quote form and tell us what your budget looks like. We'll work with you to make it happen."),
 ("What's your cancellation policy?",
  "A deposit reserves your date and is applied toward your total. It secures our time and supplies, so it isn't refundable if you cancel — but we're always happy to help you reschedule. Reach out any time."),
 ("How far in advance should we book?",
  "The sooner the better, especially for weekends and holidays. That said, reach out any time — if your date is open, we'll do our best to make it work."),
]
faq_items=""
for q,a in faqs:
    faq_items+=f'''<div class="faq-item"><button class="faq-q" aria-expanded="false">{q}</button><div class="faq-a"><p>{a}</p></div></div>'''
faq_body=f'''
{page_hero("faq","Good questions, honest answers",
  "Everything you might be wondering before you book. Still curious? Just reach out.",
  script="Ask away.", cta_btn=("Ask us anything","contact.html"))}
<section class="section"><div class="container"><div class="faq">{faq_items}</div></div></section>
{cta(script_line="Didn't see it?", heading="Send your question our way.", text="We'll get back to you within 24 hours.", primary=("Contact us","contact.html"), secondary=("Get a quote","quote.html"))}
'''
page("faq.html","FAQ | Bravaura LLC Mobile Art Events NJ",
     "Answers to common questions about Bravaura's mobile art events in New Jersey — travel, skill levels, customization, pricing, and cancellations.",
     "faq.html",faq_body)

thanks_body=f'''
{page_hero("thank you","Your request is in",
  "Thanks for reaching out. We read every message and reply by email within 24 hours with a custom, all-inclusive quote and next steps.",
  script="Talk soon.", cta_btn=("Back to the site","index.html"))}
'''
page("thank-you.html","Thank You | Bravaura LLC",
     "Thanks for your request. Bravaura replies by email within 24 hours with a custom quote for your New Jersey art event.",
     "", thanks_body)

write_assets()
write_seo_files()
print("ALL PAGES DONE")
