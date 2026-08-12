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
IMG_HERO      = "1adb03a5-532e-4d76-8b06-ed7f8b91a887"  # kids holding up paintings (Aug 11 2026 — same subject, each canvas a different hand)
IMG_SIP       = "e4b94598-efc8-4878-b23d-e8183f1097bd"  # ladies' outdoor paint & sip, string lights, same moonlit-lake painting on every canvas
IMG_BIRTHDAY  = "1d486419-3a55-4b5f-b395-14404fd86123"  # birthday party, mixed ages, sun painting, candid/real style
IMG_CORP      = "2b45db44-9905-422b-b9c8-bde0577d8afd"  # coworkers painting
IMG_FACE      = "bcb154fd-48ef-4029-8091-971b9a36416f"  # kids with painted faces
IMG_MASTER    = "2123a9a1-9e43-479c-bc08-3af6727b57d5"  # master class, seated eye-level angle, no foreground, approved Aug 11 2026
IMG_LAKE      = "67f4b7da-ed40-424c-ad49-760dd9087a33"  # ladies' lake night
IMG_GALAXY    = "d24aa654-58f8-4c92-b876-176230ec11e6"  # kids' galaxy painting
IMG_HEADSHOT  = "48da3559-305e-4e37-9839-494b5ac1ec61"  # Kendal hosting/instructing a painting class (AI-generated, matched to her likeness)

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
EVENTBRITE_URL = ""   # Olipop & Paint tickets — paste the Eventbrite link here and rebuild

# ---------------------------------------------------------------- testimonials
TESTIMONIALS = [
    {"quote": "Bravaura turned my daughter's 8th birthday into the easiest party I've ever hosted. They brought everything, ran the whole painting activity, and packed it all up. I didn't lift a finger.", "author": "Jenna R.", "context": "Birthday Party, Cranford NJ"},
    {"quote": "Booked a ladies' night on the lake and it was such a fun, relaxed evening. Great instruction for total beginners, and every canvas turned out great. Already planning the next one.", "author": "Kristine G.", "context": "Paint & Sip, Ladies' Night", "image": IMG_LAKE, "image_alt": "A Bravaura ladies' night paint & sip out on the lake"},
    {"quote": "We had a great time. Bravaura took care of everything, and it was a great team bonding experience.", "author": "Keith P.", "context": "Team Building, Effluent Design"},
]

# ================================================================ CSS
CSS = r"""/* =========================================================
   Bravaura LLC — bold, arty, human-made stylesheet
   ========================================================= */
:root{
  --teal:#0B9ABF; --teal-deep:#09809F;
  --gold:#F7B10F; --gold-deep:#B37F0A;
  --purple:#81469C; --purple-deep:#6C3A85;
  --magenta:#D42463; --orange:#D86312;
  --royal:#0354D2;
  --ink:#1E2A38; --body:#45535f;
  --cream:#FBF7EF; --cream-2:#F4ECDD;
  --line:#ece3d4;
  --font-display:"Fraunces",Georgia,serif;
  --font-body:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  --font-hand:"Caveat",cursive;
  --maxw:1180px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
#site-splash{position:fixed;inset:0;z-index:999;display:flex;align-items:center;justify-content:center;background:#fffefe;transition:opacity .45s ease}
#site-splash video{width:min(70vw,480px);animation:splash-pop .5s cubic-bezier(.34,1.56,.64,1);-webkit-mask-image:radial-gradient(ellipse 60% 62% at 50% 50%,#000 55%,transparent 86%);mask-image:radial-gradient(ellipse 60% 62% at 50% 50%,#000 55%,transparent 86%)}
#site-splash.splash-out{opacity:0;pointer-events:none}
@keyframes splash-pop{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:scale(1)}}
@media(prefers-reduced-motion:reduce){#site-splash video{animation:none}}
body{margin:0;font-family:var(--font-body);color:var(--body);background:var(--cream);line-height:1.7;font-size:18px;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;display:block}
a{color:var(--teal-deep);text-decoration:none}
h1,h2,h3,h4{font-family:var(--font-display);color:var(--ink);line-height:1.1;margin:0 0 .5em;font-weight:600;letter-spacing:-.02em}
h1{font-size:clamp(2.6rem,6vw,4.6rem)}
h2{font-size:clamp(2rem,4.3vw,3.1rem)}
h3{font-size:clamp(1.2rem,2.1vw,1.55rem)}
p{margin:0 0 1.1rem}
.container{width:100%;max-width:var(--maxw);margin:0 auto;padding:0 26px}
.narrow{max-width:780px}
.center{text-align:center}
.center .lead{margin-left:auto;margin-right:auto}
.mt-0{margin-top:0}.mb-0{margin-bottom:0}
.lead{font-size:1.22rem;color:var(--ink);max-width:56ch;font-weight:500}
.hand{font-family:var(--font-hand);font-weight:700;line-height:.9}
.eyebrow{font-family:var(--font-hand);font-size:1.5rem;font-weight:700;color:var(--magenta);margin:0 0 .3rem;display:inline-block;transform:rotate(-2deg)}

/* buttons */
.btn{display:inline-flex;align-items:center;gap:.55rem;font-family:var(--font-body);font-weight:700;font-size:1rem;padding:1rem 1.8rem;border-radius:999px;border:2.5px solid var(--ink);cursor:pointer;text-decoration:none;line-height:1;transition:transform .16s cubic-bezier(.34,1.56,.64,1),box-shadow .16s,background .16s,color .16s;box-shadow:4px 4px 0 var(--ink)}
.btn:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink);text-decoration:none}
.btn:active{transform:translate(2px,2px);box-shadow:1px 1px 0 var(--ink)}
.btn--gold{background:var(--gold);color:#3a2c00}
.btn--teal{background:var(--teal);color:#fff}
.btn--purple{background:var(--purple);color:#fff}
.btn--white{background:#fff;color:var(--ink)}
.btn--lg{padding:1.15rem 2.2rem;font-size:1.1rem}
.btn-row{display:flex;flex-wrap:wrap;gap:16px}
.center .btn-row{justify-content:center}

/* top sweep + header */
.sweep-bar{height:6px;border:0;margin:0;background:linear-gradient(90deg,var(--teal),var(--gold) 30%,var(--orange) 52%,var(--magenta) 74%,var(--purple))}
.site-header{position:sticky;top:0;z-index:60;background:rgba(251,247,239,.82);backdrop-filter:saturate(150%) blur(12px);border-bottom:2px solid var(--ink)}
.nav{display:flex;align-items:center;justify-content:space-between;height:82px;gap:20px}
.brand img{height:56px;width:auto}
@media(max-width:480px){.brand img{height:44px}}
.nav-links{display:flex;align-items:center;gap:26px;list-style:none;margin:0;padding:0}
.nav-links a{font-weight:600;font-size:.98rem;color:var(--ink);position:relative;padding:4px 0}
.nav-links a::after{content:"";position:absolute;left:0;right:100%;bottom:-3px;height:3px;border-radius:3px;background:var(--magenta);transition:right .25s}
.nav-links a:hover::after,.nav-links a.active::after{right:0}
.nav-links a.active::after{background:var(--gold)}
.nav-cta{display:flex;align-items:center;gap:14px}
.nav-toggle{display:none;background:none;border:0;cursor:pointer;width:46px;height:46px;padding:10px}
.nav-toggle span{display:block;height:3px;background:var(--ink);border-radius:2px;margin:5px 0;transition:.25s}
.nav-toggle.open span:nth-child(1){transform:translateY(8px) rotate(45deg)}
.nav-toggle.open span:nth-child(2){opacity:0}
.nav-toggle.open span:nth-child(3){transform:translateY(-8px) rotate(-45deg)}
@media(max-width:920px){
  .nav-toggle{display:block}
  .nav-links{position:absolute;top:82px;left:0;right:0;flex-direction:column;align-items:stretch;gap:0;background:var(--cream);border-bottom:2px solid var(--ink);max-height:0;overflow:hidden;transition:max-height .3s}
  .nav-links.open{max-height:560px}
  .nav-links li{border-bottom:1px solid var(--line)}
  .nav-links a{padding:15px 26px}
  .nav-links a::after{display:none}
  .nav-cta .btn{display:none}
}

/* hero (home) */
.hero{position:relative;padding:70px 0 90px;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:1.08fr .92fr;gap:40px;align-items:center;position:relative;z-index:2}
.hero h1{font-size:clamp(2.7rem,6.4vw,5rem)}
.hero h1 .pop{color:var(--teal)}
.hero .script-accent{font-family:var(--font-hand);font-weight:700;font-size:clamp(3.2rem,8vw,6.2rem);color:var(--magenta);display:block;transform:rotate(-3deg);margin:.05em 0 -.05em -.03em;line-height:.85}
.hero-lead{font-size:1.28rem;color:var(--ink);max-width:46ch;margin:1.6rem 0 2.2rem;font-weight:500}
.hero-cta{display:flex;flex-wrap:wrap;gap:16px;align-items:center}
.blob{position:absolute;border-radius:50%;filter:blur(3px);opacity:.34;z-index:0;pointer-events:none}
.arrow-doodle{position:absolute;left:34%;bottom:5%;width:104px;z-index:3;color:var(--teal-deep);opacity:.85}
.hero-photo-wrap{position:relative;padding:16px 12px 46px}
.hero-photo{position:relative;overflow:hidden;border:5px solid var(--ink);background:var(--cream-2)}
.hero-photo img{width:100%;height:100%;object-fit:cover}
.hero-photo.fail img{display:none}
.hero-photo.fail{display:grid;place-items:center}
.hero-photo--main{border-radius:28px;box-shadow:11px 13px 0 var(--gold);transform:rotate(-2deg);aspect-ratio:4/3.5}
.hero-photo--main.fail{background:linear-gradient(135deg,var(--teal),var(--purple))}
.hero-photo--mini{position:absolute;right:-10px;bottom:2px;width:46%;aspect-ratio:1/1;border-radius:22px;box-shadow:8px 8px 0 var(--teal);transform:rotate(5deg);z-index:4}
.hero-photo--mini.fail{background:linear-gradient(135deg,var(--magenta),var(--gold))}
.hero-badge{position:absolute;z-index:5;font-family:var(--font-hand);font-weight:700;font-size:1.5rem;padding:12px 20px 10px;border-radius:16px;border:3px solid var(--ink);box-shadow:4px 4px 0 var(--ink);transform:rotate(-6deg)}
.hero-badge--tl{top:-6px;left:-16px;background:var(--gold);color:#3a2c00}
@media(max-width:920px){
  .hero-grid{grid-template-columns:1fr;gap:34px}
  .hero-photo-wrap{max-width:420px;margin:0 auto}
  .arrow-doodle{display:none}
  .hero .blob{opacity:.16;filter:blur(6px)}
}

/* marquee */
.marquee{background:var(--ink);color:#fff;border-top:3px solid var(--ink);border-bottom:3px solid var(--ink);padding:16px 0;overflow:hidden;white-space:nowrap}
.marquee-track{display:inline-flex;animation:marq 26s linear infinite;will-change:transform}
.marquee-track span{font-family:var(--font-display);font-weight:600;font-size:1.5rem;padding:0 26px;display:inline-flex;align-items:center;gap:26px}
.marquee-track .star{color:var(--gold)}
@keyframes marq{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* sections */
.section{padding:92px 0;position:relative}
.section--cream2{background:var(--cream-2)}
.section-head{max-width:62ch}
.section-head.center{margin:0 auto;text-align:center}

/* page hero (inner pages) */
.page-hero{position:relative;background:var(--ink);color:#fff;overflow:hidden;padding:76px 0}
.page-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(55% 130% at 88% 6%,rgba(247,177,15,.22),transparent 55%),radial-gradient(50% 120% at 8% 96%,rgba(212,36,99,.26),transparent 55%),radial-gradient(48% 130% at 60% 120%,rgba(11,154,191,.28),transparent 55%)}
.page-hero .container{position:relative;z-index:1}
.page-hero h1,.page-hero p{color:#fff}
.page-hero .eyebrow{color:var(--gold)}
.page-hero .lead{color:rgba(255,255,255,.9);max-width:60ch}
.page-hero .script-accent{font-family:var(--font-hand);font-weight:700;color:var(--gold);font-size:clamp(2.4rem,6vw,3.8rem);display:block;transform:rotate(-2deg);line-height:.9;margin-bottom:.05em}

/* how it works */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:26px;margin-top:56px;position:relative}
.step{position:relative;text-align:center}
.step-num{width:74px;height:74px;border-radius:50%;display:grid;place-items:center;margin:0 auto 18px;font-family:var(--font-display);font-size:1.9rem;font-weight:700;color:#fff;border:3px solid var(--ink);box-shadow:3px 3px 0 var(--ink);background:var(--teal)}
.step:nth-of-type(1) .step-num{background:var(--teal)}
.step:nth-of-type(2) .step-num{background:var(--gold);color:#3a2c00}
.step:nth-of-type(3) .step-num{background:var(--magenta)}
.step:nth-of-type(4) .step-num{background:var(--purple)}
.step h3{font-size:1.3rem;margin-bottom:.35rem}
.step p{font-size:1rem;margin:0}
.steps-line{position:absolute;top:17px;left:12%;right:12%;height:40px;z-index:-1;color:var(--gold-deep);opacity:.75}
@media(max-width:820px){.steps{grid-template-columns:1fr 1fr;gap:34px 20px}.steps-line{display:none}}
@media(max-width:460px){.steps{grid-template-columns:1fr}}

/* services bento */
.bento{display:grid;grid-template-columns:repeat(6,1fr);grid-auto-rows:minmax(210px,auto);gap:20px;margin-top:52px}
.svc{position:relative;overflow:hidden;border-radius:22px;border:3px solid var(--ink);box-shadow:6px 6px 0 var(--ink);display:flex;flex-direction:column;justify-content:flex-end;padding:26px;color:#fff;text-decoration:none;min-height:220px;background:var(--ink);transition:transform .2s cubic-bezier(.34,1.56,.64,1),box-shadow .2s}
.svc:hover{transform:translate(-3px,-3px);box-shadow:9px 9px 0 var(--ink)}
.svc-img{position:absolute;inset:0;z-index:0;background:linear-gradient(150deg,var(--tint),rgba(30,42,56,.9))}
.svc-img img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.svc:hover .svc-img img{transform:scale(1.07)}
.svc::after{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,transparent 30%,rgba(0,0,0,.15),var(--tint) 118%);mix-blend-mode:multiply}
.svc>*{position:relative;z-index:2}
.svc .tag{font-family:var(--font-hand);font-weight:700;font-size:1.35rem;line-height:1;opacity:.95;margin-bottom:2px}
.svc h3{color:#fff;margin:0 0 .3rem;font-size:1.7rem}
.svc p{color:rgba(255,255,255,.94);margin:0;font-size:1.02rem;max-width:36ch;font-weight:500}
@media(min-width:760px){.svc p{min-height:4.6em}}  /* reserve ~3 lines so short and long blurbs still line up */
.svc .go{margin-top:14px;font-weight:700;display:inline-flex;gap:.4rem;font-size:.98rem}
.svc:hover .go{gap:.7rem}
.svc--birthday{grid-column:span 3;--tint:rgba(212,36,99,.72)}
.svc--sip{grid-column:span 3;--tint:rgba(129,70,156,.74)}
.svc--corp{grid-column:span 3;--tint:rgba(3,84,210,.68)}
.svc--face{grid-column:span 3;--tint:rgba(216,99,18,.72)}
.svc--master{grid-column:1 / -1;justify-self:center;width:100%;max-width:calc((100% - 20px)/2);--tint:rgba(11,154,191,.7)}
@media(max-width:820px){.bento{grid-template-columns:1fr 1fr}.svc{grid-column:span 1 !important}.svc--master{justify-self:stretch;max-width:none}}
@media(max-width:520px){.bento{grid-template-columns:1fr}}

/* why band */
.why{background:var(--purple);color:#fff;position:relative;overflow:hidden}
.why::before{content:"";position:absolute;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(247,177,15,.32),transparent 68%);top:-180px;right:-120px}
.why::after{content:"";position:absolute;width:460px;height:460px;border-radius:50%;background:radial-gradient(circle,rgba(11,154,191,.4),transparent 68%);bottom:-200px;left:-140px}
.why h2,.why .eyebrow{color:#fff}
.why .eyebrow{color:var(--gold)}
.why-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:30px;margin-top:52px;position:relative;z-index:1}
.why-ic{width:60px;height:60px;border-radius:18px;display:grid;place-items:center;margin-bottom:18px;border:3px solid rgba(255,255,255,.28);background:rgba(255,255,255,.1)}
.why-ic svg{width:30px;height:30px;color:#fff}
.why-item h3{color:#fff;font-size:1.28rem;margin-bottom:.3rem}
.why-item p{color:rgba(255,255,255,.86);font-size:1rem;margin:0}
@media(max-width:820px){.why-grid{grid-template-columns:1fr 1fr;gap:36px 26px}}
@media(max-width:460px){.why-grid{grid-template-columns:1fr}}

/* testimonials (sticky notes) */
.notes{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:54px}
.note{background:#fff;border:3px solid var(--ink);border-radius:6px;padding:28px 26px 24px;box-shadow:5px 6px 0 rgba(30,42,56,.14);position:relative}
.note:nth-child(1){transform:rotate(-1.6deg)}
.note:nth-child(2){transform:rotate(1.2deg)}
.note:nth-child(3){transform:rotate(-.8deg)}
.note:hover{transform:rotate(0) translateY(-4px);transition:transform .2s}
.note::before{content:"";position:absolute;top:-14px;left:50%;transform:translateX(-50%) rotate(-4deg);width:78px;height:26px;background:rgba(247,177,15,.55);border:1px solid rgba(179,127,10,.3)}
.note-photo{margin:-6px -4px 16px;border:3px solid var(--ink);border-radius:10px;overflow:hidden;aspect-ratio:16/10;background:linear-gradient(135deg,var(--teal),var(--purple))}
.note-photo img{width:100%;height:100%;object-fit:cover;display:block}
.note-stars{color:var(--gold-deep);font-size:1.05rem;letter-spacing:3px;margin-bottom:12px}
.note .q{font-family:var(--font-display);font-size:1.08rem;font-weight:500;color:var(--ink);line-height:1.5;margin-bottom:16px}
.note .who{font-weight:700;font-size:.92rem;color:var(--purple)}
.note .who span{color:var(--body);font-weight:500}
@media(max-width:820px){.notes{grid-template-columns:1fr}.note,.note:nth-child(n){transform:none}}

/* CTA */
.cta{background:var(--ink);color:#fff;text-align:center;position:relative;overflow:hidden}
.cta::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 120% at 82% 8%,rgba(247,177,15,.24),transparent 55%),radial-gradient(55% 120% at 12% 92%,rgba(212,36,99,.28),transparent 55%),radial-gradient(50% 120% at 50% 120%,rgba(11,154,191,.3),transparent 55%)}
.cta .container{position:relative;z-index:1}
.cta h2{color:#fff;font-size:clamp(2.1rem,5vw,3.4rem)}
.cta .script-accent{font-family:var(--font-hand);color:var(--gold);font-size:clamp(2.4rem,7vw,4.2rem);display:block;transform:rotate(-2deg);line-height:.9;margin-bottom:.1em}
.cta p{color:rgba(255,255,255,.85);font-size:1.18rem;max-width:54ch;margin:0 auto 2rem}

/* split (text + framed photo) */
.split{display:grid;grid-template-columns:1.02fr .98fr;gap:52px;align-items:center}
.split--rev .split-media{order:-1}
@media(max-width:880px){.split{grid-template-columns:1fr;gap:36px}.split--rev .split-media{order:0}}
.frame-photo{position:relative;border:5px solid var(--ink);border-radius:24px;overflow:hidden;background:var(--cream-2);aspect-ratio:4/3.2}
.frame-photo img{width:100%;height:100%;object-fit:cover}
.frame-photo.fail img{display:none}
.frame-photo.tilt-l{transform:rotate(-2deg)}
.frame-photo.tilt-r{transform:rotate(2deg)}
.frame-photo.sh-gold{box-shadow:11px 12px 0 var(--gold)}
.frame-photo.sh-teal{box-shadow:11px 12px 0 var(--teal)}
.frame-photo.sh-magenta{box-shadow:11px 12px 0 var(--magenta)}
.frame-photo.sh-purple{box-shadow:11px 12px 0 var(--purple)}
.frame-photo.fail{background:linear-gradient(135deg,var(--teal),var(--purple))}
.frame-photo--headshot{aspect-ratio:4/5}
.frame-photo--headshot img{object-position:center 20%}
@media(max-width:880px){.frame-photo--headshot{aspect-ratio:4/4}}

/* checklist */
.checklist{list-style:none;padding:0;margin:1.2rem 0 0;display:grid;gap:13px}
.checklist li{display:flex;gap:12px;align-items:flex-start;font-size:1.05rem;color:var(--ink)}
.checklist li::before{content:"";flex-shrink:0;margin-top:3px;width:24px;height:24px;border-radius:50%;background:var(--teal) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E") center/13px no-repeat;border:2px solid var(--ink)}

/* info cards */
.info-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:8px}
@media(max-width:820px){.info-grid{grid-template-columns:1fr}}
.info-card{background:#fff;border:3px solid var(--ink);border-radius:20px;padding:28px 26px;box-shadow:6px 6px 0 var(--ink);height:100%}
.info-card .ic{width:54px;height:54px;border-radius:15px;display:grid;place-items:center;margin-bottom:16px;border:2.5px solid var(--ink)}
.info-card .ic svg{width:26px;height:26px}
.ic--teal{background:var(--teal);color:#fff}.ic--gold{background:var(--gold);color:#3a2c00}
.ic--magenta{background:var(--magenta);color:#fff}.ic--purple{background:var(--purple);color:#fff}
.ic--orange{background:var(--orange);color:#fff}
.info-card h3{margin:0 0 .3rem;font-size:1.25rem}
.info-card p{margin:0;color:var(--body);font-size:1rem}

/* pills */
.pill-row{display:flex;flex-wrap:wrap;gap:12px;margin-top:14px}
.pill{background:#fff;border:2.5px solid var(--ink);color:var(--ink);font-weight:600;font-size:.94rem;padding:9px 17px;border-radius:999px;box-shadow:3px 3px 0 var(--ink)}

/* forms */
.form-card{background:#fff;border:3px solid var(--ink);border-radius:22px;box-shadow:8px 8px 0 var(--ink);padding:34px}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media(max-width:620px){.form-grid{grid-template-columns:1fr}}
.field{display:flex;flex-direction:column;gap:7px}
.field.full{grid-column:1 / -1}
.field label{font-weight:700;font-size:.92rem;color:var(--ink)}
.field label .req{color:var(--magenta)}
.field input,.field select,.field textarea{font-family:var(--font-body);font-size:1rem;color:var(--ink);padding:12px 14px;border:2.5px solid var(--ink);border-radius:12px;background:var(--cream);transition:box-shadow .15s}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;box-shadow:3px 3px 0 var(--teal)}
.field textarea{resize:vertical;min-height:120px}
.form-note{font-size:.85rem;color:var(--body);margin-top:14px}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.form-status{margin-top:16px;padding:14px 16px;border-radius:12px;font-weight:700;display:none}
.form-status.ok{display:block;background:#e7f6ef;color:#1a7a4f;border:2px solid #1a7a4f}
.form-status.err{display:block;background:#fdecef;color:#b02a44;border:2px solid #b02a44}

/* travel calculator */
.calc{background:#fff;border:3px solid var(--ink);border-radius:22px;box-shadow:8px 8px 0 var(--ink);padding:26px;max-width:780px}

/* contact info */
.contact-info{display:grid;gap:18px;margin-top:18px}
.contact-line{display:flex;gap:14px;align-items:flex-start}
.contact-line .ci{flex-shrink:0;width:52px;height:52px;border-radius:15px;display:grid;place-items:center;background:var(--cream-2);border:2.5px solid var(--ink);color:var(--ink)}
.contact-line .ci svg{width:24px;height:24px}
.contact-line a,.contact-line span{font-weight:700;color:var(--ink);font-size:1.05rem}
.contact-line a:hover{color:var(--teal-deep)}
.contact-line small{display:block;color:var(--body);font-size:.85rem;margin-top:2px;font-weight:500}

/* faq */
.faq{max-width:840px;margin:0 auto}
.faq-item{border:3px solid var(--ink);border-radius:16px;background:#fff;margin-bottom:16px;box-shadow:5px 5px 0 var(--ink);overflow:hidden}
.faq-q{width:100%;text-align:left;background:none;border:0;cursor:pointer;font-family:var(--font-display);font-size:1.14rem;font-weight:600;color:var(--ink);padding:20px 52px 20px 22px;position:relative}
.faq-q::after{content:"+";position:absolute;right:20px;top:50%;transform:translateY(-50%);font-family:var(--font-body);font-size:1.7rem;color:var(--magenta);transition:transform .2s}
.faq-item.open .faq-q::after{content:"\2013";color:var(--teal-deep)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .3s ease}
.faq-a p{color:var(--body);padding:0 22px 20px;margin:0;font-size:1.02rem}

/* gallery */
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media(max-width:900px){.gallery-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.gallery-grid{grid-template-columns:1fr}}
.gallery-item{border-radius:18px;overflow:hidden;border:3px solid var(--ink);box-shadow:6px 6px 0 var(--ink);aspect-ratio:1/1;background:linear-gradient(135deg,var(--teal),var(--magenta))}
.gallery-item:nth-child(3n+2){background:linear-gradient(135deg,var(--purple),var(--gold))}
.gallery-item:nth-child(3n){background:linear-gradient(135deg,var(--orange),var(--magenta))}
.gallery-item img{width:100%;height:100%;object-fit:cover;transition:transform .35s}
.gallery-item:hover img{transform:scale(1.06)}
.gallery-grid--solo{grid-template-columns:1fr;max-width:640px;margin:0 auto}
.gallery-grid--solo .gallery-item{aspect-ratio:4/3}

/* footer */
/* Fraunces has a WONK axis that gives "f" a swashy hook; keep it off */
h1,h2,h3,h4,.script-accent,.design-name{font-variation-settings:"SOFT" 0,"WONK" 0}

/* checkbox pills (quote form) */
.field-label{display:block;font-weight:700;color:var(--ink);margin-bottom:9px}
.check-row{display:flex;flex-wrap:wrap;gap:10px}
.check{display:inline-flex;align-items:center;gap:9px;padding:11px 17px;border:2.5px solid var(--ink);border-radius:999px;background:var(--cream);font-weight:600;color:var(--ink);cursor:pointer;user-select:none;transition:background .15s,box-shadow .15s,transform .15s}
.check:hover{box-shadow:3px 3px 0 var(--ink);transform:translate(-1px,-1px)}
.check input{width:18px;height:18px;margin:0;accent-color:var(--purple);cursor:pointer}
.check:has(input:checked){background:var(--gold);box-shadow:3px 3px 0 var(--ink)}
.check:focus-within{outline:3px solid var(--purple);outline-offset:3px}
.field-hint{display:block;margin-top:9px;font-size:.86rem;color:var(--body)}

/* promo popup */
#promo-pop{position:fixed;inset:0;z-index:900;display:none;align-items:center;justify-content:center;padding:22px;background:rgba(30,42,56,.55);backdrop-filter:blur(3px);opacity:0;transition:opacity .3s ease}
#promo-pop.on{display:flex}
#promo-pop.in{opacity:1}
.promo-card{position:relative;max-width:520px;width:100%;background:var(--gold);color:var(--ink);border:3px solid var(--ink);border-radius:24px;box-shadow:10px 10px 0 var(--ink);padding:38px 34px 32px;text-align:center;transform:translateY(14px) scale(.97);transition:transform .35s cubic-bezier(.34,1.56,.64,1)}
#promo-pop.in .promo-card{transform:none}
.promo-card::before{content:"";position:absolute;width:120px;height:120px;border-radius:50%;background:var(--teal);opacity:.35;top:-46px;left:-40px;z-index:0}
.promo-card>*{position:relative;z-index:1}
.promo-kicker{font-family:var(--font-hand);font-weight:700;font-size:1.7rem;color:var(--purple);line-height:1;display:block;margin-bottom:6px}
.promo-card h3{font-size:2.1rem;margin:0 0 4px;line-height:1.05}
.promo-when{font-weight:700;font-size:1.18rem;margin:14px 0 2px}
.promo-where{font-size:1.02rem;margin:0 0 4px}
.promo-more{font-family:var(--font-hand);font-weight:700;font-size:1.3rem;color:var(--ink);margin:16px 0 20px}
.promo-close{position:absolute;top:10px;right:12px;z-index:2;background:transparent;border:0;font-size:1.9rem;line-height:1;cursor:pointer;color:var(--ink);padding:6px 10px;border-radius:10px}
.promo-close:hover{background:rgba(30,42,56,.12)}
@media(max-width:560px){.promo-card{padding:34px 22px 26px}.promo-card h3{font-size:1.7rem}}
@media(prefers-reduced-motion:reduce){#promo-pop,.promo-card{transition:none}}

/* design menu */
.design-carousel{position:relative;margin-top:46px}
.design-track{display:flex;gap:22px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:6px 10px 14px 0;scroll-padding-left:0;-ms-overflow-style:none;scrollbar-width:none}
.design-track::-webkit-scrollbar{display:none}
.design-track:focus-visible{outline:3px solid var(--purple);outline-offset:4px;border-radius:14px}
.design-card{flex:0 0 calc((100% - 66px)/4);scroll-snap-align:start;display:flex;flex-direction:column;gap:10px}
@media(max-width:1000px){.design-card{flex-basis:calc((100% - 44px)/3)}}
@media(max-width:700px){.design-track{gap:16px}.design-card{flex-basis:calc((100% - 16px)/2)}}
@media(max-width:460px){.design-card{flex-basis:78%}}
.dcar-btn{position:absolute;top:calc(50% - 34px);transform:translateY(-50%);z-index:3;width:52px;height:52px;border-radius:50%;border:3px solid var(--ink);background:var(--gold);color:var(--ink);font-size:1.5rem;line-height:1;cursor:pointer;box-shadow:4px 4px 0 var(--ink);transition:transform .18s cubic-bezier(.34,1.56,.64,1),box-shadow .18s,opacity .18s}
.dcar-btn:hover{transform:translateY(-50%) translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink)}
.dcar-btn:disabled{opacity:0;pointer-events:none}
.dcar-prev{left:-18px}
.dcar-next{right:-18px}
@media(max-width:900px){.dcar-prev{left:-6px}.dcar-next{right:-6px}.dcar-btn{width:44px;height:44px;font-size:1.25rem}}
@media(prefers-reduced-motion:reduce){.design-track{scroll-behavior:auto}}
.design-thumb{border:3px solid var(--ink);border-radius:16px;overflow:hidden;box-shadow:5px 5px 0 var(--ink);aspect-ratio:4/5;background:linear-gradient(150deg,var(--teal),var(--purple));transition:transform .2s cubic-bezier(.34,1.56,.64,1),box-shadow .2s}
.design-thumb{transform:rotate(var(--rot,0deg))}
.design-card:hover .design-thumb{transform:translate(-3px,-3px) rotate(var(--rot,0deg));box-shadow:8px 8px 0 var(--ink)}
.design-name{transform:rotate(calc(var(--rot,0deg) * .35))}
.design-thumb img{width:100%;height:100%;object-fit:cover;display:block}
.design-name{font-family:var(--font-body);font-weight:700;font-size:.98rem;color:var(--ink);line-height:1.25}
.design-note{margin-top:34px;font-family:var(--font-hand);font-weight:700;font-size:1.5rem;color:var(--purple);text-align:center}

/* email signup band */
.signup{background:var(--cream-2);border-top:3px solid var(--ink);padding:56px 0}
.signup-card{background:var(--gold);border:3px solid var(--ink);border-radius:24px;box-shadow:9px 9px 0 var(--ink);padding:34px 38px;display:grid;grid-template-columns:1.05fr 1fr;gap:34px;align-items:center}
.signup-card .eyebrow{color:var(--ink);opacity:.7}
.signup-card h2{margin:.2rem 0 .5rem;font-size:1.9rem;color:var(--ink)}
.signup-card p{margin:0;color:var(--ink);opacity:.82;font-size:1rem;max-width:44ch}
.signup-hand{font-family:var(--font-hand);font-weight:700;font-size:1.5rem;color:var(--ink);opacity:.75;display:block;margin-bottom:2px}
.signup-row{display:flex;gap:12px;flex-wrap:wrap}
.signup-row input{flex:1;min-width:210px;font-family:var(--font-body);font-size:1rem;color:var(--ink);padding:14px 15px;border:2.5px solid var(--ink);border-radius:12px;background:#fff}
.signup-row input:focus{outline:none;box-shadow:3px 3px 0 var(--purple)}
.signup-fine{display:block;margin-top:12px;font-size:.86rem;color:var(--ink);opacity:.72}
.signup .form-status{margin-top:14px}
@media(max-width:820px){.signup-card{grid-template-columns:1fr;gap:22px;padding:28px 24px}}
.site-footer{background:var(--ink);color:rgba(255,255,255,.85);padding:64px 0 26px;border-top:6px solid var(--gold)}
.footer-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:44px;padding-bottom:40px;border-bottom:1px solid rgba(255,255,255,.14)}
@media(max-width:720px){.footer-grid{grid-template-columns:1fr;gap:30px}}
.footer-brand img{height:46px;background:#fff;padding:8px 12px;border-radius:12px}
.footer-brand p{color:rgba(255,255,255,.62);max-width:34ch;margin:16px 0 0}
.footer-col h4{color:#fff;font-family:var(--font-body);font-size:.82rem;text-transform:uppercase;letter-spacing:.12em;margin-bottom:14px}
.footer-col ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.footer-col a,.footer-col li{color:rgba(255,255,255,.72);font-size:.98rem}
.footer-col a:hover{color:var(--gold)}
.footer-bottom{display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between;padding-top:22px;font-size:.85rem;color:rgba(255,255,255,.5)}
.footer-bottom .hand{font-family:var(--font-hand);font-size:1.2rem;color:var(--gold)}

/* interactivity — moving accents + hover pop (all inner pages) */
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-18px)}}
@keyframes floaty2{0%,100%{transform:translateY(0)}50%{transform:translateY(15px)}}
@keyframes wiggle{0%,100%{transform:rotate(-2deg)}50%{transform:rotate(1.5deg)}}
.ph-blob{position:absolute;border-radius:50%;filter:blur(9px);opacity:.5;z-index:0;pointer-events:none}
.ph-blob--1{width:270px;height:270px;background:var(--teal);top:-80px;right:7%;animation:floaty 7s ease-in-out infinite}
.ph-blob--2{width:210px;height:210px;background:var(--magenta);bottom:-90px;left:6%;animation:floaty2 8.5s ease-in-out infinite}
.page-hero .container{z-index:2}
.page-hero .script-accent{animation:wiggle 5s ease-in-out infinite;transform-origin:left center}
.info-card{transition:transform .2s cubic-bezier(.34,1.56,.64,1),box-shadow .2s}
.info-card:hover{transform:translate(-3px,-3px);box-shadow:9px 9px 0 var(--ink)}
.pill{transition:transform .15s cubic-bezier(.34,1.56,.64,1),box-shadow .15s}
.pill:hover{transform:translate(-2px,-2px);box-shadow:5px 5px 0 var(--ink)}
.frame-photo{transition:transform .3s cubic-bezier(.34,1.56,.64,1)}
.frame-photo:hover{transform:rotate(0) scale(1.015)}
.contact-line .ci{transition:transform .2s cubic-bezier(.34,1.56,.64,1)}
.contact-line:hover .ci{transform:translateY(-3px) rotate(-7deg)}
.checklist li{transition:transform .15s}
.checklist li:hover{transform:translateX(5px)}
.faq-item{transition:transform .18s,box-shadow .18s}
.faq-item:hover{transform:translate(-2px,-2px);box-shadow:7px 7px 0 var(--ink)}
/* floating background doodles (pizazz layer) */
.float-layer{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:1}
.fd{position:absolute;opacity:.55;line-height:0}
.fd svg{display:block;width:100%;height:100%}
@keyframes drift1{0%,100%{transform:translate(0,0) rotate(0)}50%{transform:translate(16px,-30px) rotate(20deg)}}
@keyframes drift2{0%,100%{transform:translate(0,0) rotate(0)}50%{transform:translate(-20px,24px) rotate(-16deg)}}
@keyframes drift3{0%,100%{transform:translate(0,0) rotate(-8deg)}50%{transform:translate(22px,16px) rotate(10deg)}}
.fd-1{width:58px;height:58px;top:16%;right:11%;color:var(--gold);animation:drift1 9s ease-in-out infinite}
.fd-2{width:74px;height:74px;bottom:18%;left:7%;color:var(--teal);animation:drift2 12s ease-in-out infinite}
.fd-3{width:66px;height:34px;top:30%;left:13%;color:var(--magenta);animation:drift3 8s ease-in-out infinite}
.fd-4{width:40px;height:40px;bottom:26%;right:22%;color:var(--purple);animation:drift1 13s ease-in-out infinite}
@media(max-width:820px){.fd-3,.fd-4{display:none}.fd{opacity:.4}}

/* scroll reveal */
.reveal{opacity:0;transform:translateY(28px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.3,1)}
.reveal.in{opacity:1;transform:none}
.reveal.d1{transition-delay:.08s}.reveal.d2{transition-delay:.16s}.reveal.d3{transition-delay:.24s}.reveal.d4{transition-delay:.32s}
@media(prefers-reduced-motion:reduce){
  .reveal{opacity:1;transform:none;transition:none}
  .btn:hover,.svc:hover,.info-card:hover,.pill:hover,.frame-photo:hover,.faq-item:hover{transform:none}
  .marquee-track,.fd,.ph-blob,.page-hero .script-accent,.hero .blob{animation:none}
}
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
DESIGNS=[
 ("636ec2cb-894f-4e73-b875-7303a983d49d","Moonlit Lake"),
 ("6bfaa3d5-8b2e-48de-8c39-23730e63ecba","Sunset Palms"),
 ("239e9ed9-daef-439b-8179-56bd9941f7bc","Sunflowers"),
 ("02c0d1d5-3396-41da-959a-7690e918cd9a","Wildflower Jar"),
 ("c3edcf2f-636d-4a66-acba-ca772a65a807","Lavender Field"),
 ("c945c49c-8dd0-45f9-8bbb-cdb0f7b4dfe8","Jellyfish"),
 ("6a214910-1512-419b-9dc4-b9ab8dd28bb6","Highland Cow"),
 ("7d943730-29fa-439e-b53c-d5925e3f45a4","Heart Tree"),
 ("273134df-a5f1-497f-953a-29dc873210ce","Cats on a Fence"),
 ("06955123-2c89-46d7-ac4e-10f48dedfc14","Pumpkin Porch"),
 ("4e6b4f39-4279-4b4b-ae93-18bd3a30be8c","Fireworks on the Lake"),
 ("0b58ef96-2206-4db5-90b8-efe190ababb3","Red Truck &amp; Tree"),
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
    tickets=(f'<a href="{EVENTBRITE_URL}" target="_blank" rel="noopener" '
             f'class="btn btn--purple btn--lg promo-cta">Purchase tickets</a>') if EVENTBRITE_URL else ''
    secondary_cls='btn btn--white btn--lg' if EVENTBRITE_URL else 'btn btn--purple btn--lg'
    return f'''<div id="promo-pop" role="dialog" aria-modal="true" aria-labelledby="promo-title" aria-hidden="true">
  <div class="promo-card">
    <button class="promo-close" type="button" aria-label="Close">&times;</button>
    <span class="promo-kicker">save the date</span>
    <h3 id="promo-title">Olipop &amp; Paint</h3>
    <p class="promo-when">Saturday, September 12 &middot; 5:00&ndash;7:00 pm</p>
    <p class="promo-where">Livi\'s Lavender Farm &middot; Robbinsville, NJ</p>
    <p class="promo-more">more details coming soon!</p>
    {tickets}
    <a href="#signup" class="{secondary_cls} promo-cta">Get the details first</a>
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
      <span class="hero-badge hero-badge--tl">we come to you &#10038;</span>
      <div class="hero-photo hero-photo--main"><img src="{img_url(IMG_HERO)}" alt="Kids proudly holding up their finished paintings at a Bravaura art party" loading="eager" onerror="this.closest('.hero-photo').classList.add('fail')"></div>
      <div class="hero-photo hero-photo--mini"><img src="{img_url(IMG_SIP)}" alt="Adults laughing at a Bravaura paint and sip night" loading="lazy" onerror="this.closest('.hero-photo').classList.add('fail')"></div>
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
GALLERY=[(IMG_LAKE,"A ladies' night paint & sip on the lake"),
         ("36a659d6-0a8f-4dea-8e96-3164406b2a43","Kids holding up their finished paintings at a Bravaura art party")]
def gallery_grid():
    items=""
    for pid,alt in GALLERY:
        onerr="this.style.display='none'"
        items+=f'<div class="gallery-item reveal"><img src="{img_url(pid)}" alt="{alt}" loading="lazy" onerror="{onerr}"></div>'
    solo=" gallery-grid--solo" if len(GALLERY)==1 else ""
    return f'<div class="gallery-grid{solo}">{items}</div>'
gallery_body=f'''
{page_hero("gallery","A peek at the paint",
  "Moments from Bravaura events across New Jersey. We're adding fresh photos from recent parties, paint &amp; sip nights, and team sessions. Check back soon.",
  script="See the mess we make.", cta_btn=("Book your event","contact.html"))}
<section class="section"><div class="container">{gallery_grid()}</div></section>
{designs_section()}
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
      <p>It started with a girl from New Jersey who loves art and loves teaching it even more. Kendal has a BA in Art Education and is certified K–12, and she teaches every age group, from little kids to adults.</p>
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
        <form data-bravaura-form name="{name}" method="POST" data-netlify="true" netlify-honeypot="bot-field" novalidate>
          <input type="hidden" name="form-name" value="{name}">
          <p style="display:none"><label>Leave this empty: <input name="bot-field"></label></p>
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

write_assets()
write_seo_files()
print("ALL PAGES DONE")
