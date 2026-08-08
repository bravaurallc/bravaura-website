# -*- coding: utf-8 -*-
"""Generate the Bravaura LLC multi-page website."""
import os

OUT = "/sessions/serene-stoic-ride/mnt/CoworkOS/Work-Business/Website"

PHONE = "908-894-3611"
PHONE_TEL = "9088943611"
EMAIL = "bravaurallc@gmail.com"
IG = "bravaurallc"
IG_URL = "https://instagram.com/bravaurallc"

# ---------------------------------------------------------------- photos
# Verified free-license Unsplash photos (images.unsplash.com CDN, hotlink-friendly)
# plus a couple of AI-generated, brand-colored shots from ImagineArt (full URLs).
IMG_GROUP   = "photo-1757085242652-f8cd4d3de889"  # people painting together at a table (Anya Richter)
IMG_WINE    = "https://asset.imagine.art/processed/1a2e5d56-0212-4ea6-b794-728e4bda1d95"  # AI: paint & sip friends, brand palette
IMG_TEACH   = "photo-1758522275031-70ea3febfa2e"  # instructor teaching a student to paint (Vitaly Gariev)
IMG_PALETTE = "photo-1752649935255-c10e9a3e2ad3"  # hand mixing colours on a palette (Vitaly Gariev)
IMG_FACE    = "photo-1635598350959-ebc5af57d3c9"  # butterfly face paint (Himanshu Choudhary)
IMG_HERO_AI = "https://asset.imagine.art/processed/8aaf5b09-5fc9-4747-8fa7-6c7c9f58ba32"  # AI: group painting together, brand palette
IMG_DECOR   = "photo-1604668915840-580c30026e5f"  # yellow & white balloons on table — decorations add-on (Lucas Law)
IMG_ART     = "photo-1541961017774-22349e4a1262"  # colorful abstract painting — finished artwork (Steve A Johnson)
IMG_GLOW    = "photo-1758636089767-49c5e6b37c42"  # glowing paint under blacklight — glow-in-the-dark add-on (Markus Kammermann)

def _resolve_src(base_id, w):
    if base_id.startswith("http"):
        return base_id
    return "https://images.unsplash.com/" + base_id + "?q=75&w=" + str(w) + "&auto=format&fit=crop"

def photo(base_id, alt, variant="wide", w=1100):
    url = _resolve_src(base_id, w)
    onerr = "this.closest('.photo').classList.add('photo--failed');this.remove();"
    return ('<div class="photo photo--' + variant + ' photo--frame">'
            '<img src="' + url + '" alt="' + alt + '" loading="lazy" onerror="' + onerr + '"></div>')

def placeholder_photo(label="Real event photos coming soon", variant="wide"):
    return ('<div class="photo photo--' + variant + ' photo--frame photo--placeholder">'
            '<div class="photo-placeholder-label">' + icon("palette") + '<span>' + label + '</span></div></div>')

def service_card(href, accent, base_id, alt, title, desc, color):
    thumb_url = _resolve_src(base_id, 560)
    onerr = "this.closest('.card-photo').classList.add('photo--failed');this.remove();"
    return ('<a class="card card--accent ' + accent + '" href="' + href + '">'
            '<div class="card-photo"><img src="' + thumb_url + '" alt="' + alt + '" loading="lazy" '
            'onerror="' + onerr + '"></div>'
            '<h3>' + title + '</h3><p>' + desc + '</p>'
            '<span class="card-link" style="color:' + color + ';">Learn more &rarr;</span></a>')

# ---------------------------------------------------------------- icons
ICONS = {
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
    "brush": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.06 11.9l8.07-8.06a2.85 2.85 0 1 1 4.03 4.03l-8.06 8.08"/><path d="M7.07 14.94c-1.66 0-3 1.35-3 3.02 0 1.33-2.5 1.52-2 2.02 1.08 1.1 2.49 2.02 4 2.02 2.2 0 4-1.8 4-4.04a3.01 3.01 0 0 0-3-3.02z"/></svg>',
    "sparkle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.9 5.2L19 10l-5.1 1.8L12 17l-1.9-5.2L5 10l5.1-1.8z"/></svg>',
    "cake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21h16"/><path d="M4 21v-8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8"/><path d="M4 15c1.5 1.2 3 1.2 4 0s2.5-1.2 4 0 2.5 1.2 4 0 2.5-1.2 4 0"/><path d="M12 8V5"/><circle cx="12" cy="3.5" r="1"/></svg>',
    "wine": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 22h8"/><path d="M12 15v7"/><path d="M6 3h12l-1 7a5 5 0 0 1-10 0z"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "smile": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "gift": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    "palette": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="13.5" cy="6.5" r="1.5"/><circle cx="17.5" cy="10.5" r="1.5"/><circle cx="8.5" cy="7.5" r="1.5"/><circle cx="6.5" cy="12.5" r="1.5"/><path d="M12 2a10 10 0 0 0 0 20c.55 0 1-.45 1-1 0-.26-.1-.5-.26-.68-.16-.19-.26-.42-.26-.68 0-.55.45-1 1-1H16a6 6 0 0 0 6-6c0-5.52-4.48-10-10-10z"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
}

def icon(name):
    return ICONS.get(name, "")

# ---------------------------------------------------------------- testimonials
# Simple editable array — swap these for real reviews any time.
TESTIMONIALS = [
    {"quote": "Bravaura turned my daughter's 8th birthday into the easiest party I've ever hosted. They brought everything, ran the whole painting activity, and packed it all up — I didn't lift a finger.", "author": "Jenna R.", "context": "Birthday Party, Cranford NJ"},
    {"quote": "Booked Bravaura for a ladies' night out on the lake and it was such a fun, relaxed evening. Great instruction for total beginners, gorgeous setting, and every canvas turned out great — already planning the next one.", "author": "Kristine G.", "context": "Paint & Sip, Ladies' Night on the Lake"},
    {"quote": "Wasn't sure the team would go for a painting afternoon, but it turned out to be the best team outing we've had in years. Relaxed, genuinely fun, and half the office still has their canvas hanging up at their desk.", "author": "Keith P.", "context": "Corporate Team Building, Effluent Design LLC"},
]

def testimonials_section():
    cards = ""
    for t in TESTIMONIALS:
        cards += f'''<div class="testimonial">
      <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p class="quote">&ldquo;{t["quote"]}&rdquo;</p>
      <div class="testimonial-author">{t["author"]} &mdash; <span style="color:var(--cool-gray);font-weight:500;">{t["context"]}</span></div>
    </div>'''
    return f'''<section class="section section--mist">
  <div class="container center">
    <p class="eyebrow">What Clients Say</p>
    <h2>Loved by hosts across New Jersey</h2>
  </div>
  <div class="container" style="margin-top:40px;">
    <div class="testimonial-grid">{cards}</div>
  </div>
  <div class="container center" style="margin-top:34px;">
    <a href="{IG_URL}" target="_blank" rel="noopener" class="btn btn--ghost">See More on Instagram @{IG}</a>
  </div>
</section>'''

# ---------------------------------------------------------------- trusted-by
# Simple editable list — add a name here as soon as a client says yes to being listed.
TRUSTED_BY = ["Effluent Design LLC"]

def trusted_by_strip():
    chips = "".join(f'<span class="pill" style="font-size:1rem;padding:10px 20px;">{name}</span>' for name in TRUSTED_BY)
    return f'''<section class="section section--tight">
  <div class="container center">
    <p class="eyebrow" style="margin-bottom:1rem;">Trusted By</p>
    <div class="pill-row" style="justify-content:center;">{chips}</div>
  </div>
</section>'''

# ---------------------------------------------------------------- nav / chrome
NAV = [
    ("Home", "index.html"),
    ("Services", "services.html"),
    ("Pricing", "pricing.html"),
    ("Gallery", "gallery.html"),
    ("About", "about.html"),
]

def header(active):
    items = ""
    for label, href in NAV:
        cls = ' class="active"' if href == active else ""
        aria = ' aria-current="page"' if href == active else ""
        items += f'<li><a href="{href}"{cls}{aria}>{label}</a></li>'
    ccls = ' class="active"' if active == "contact.html" else ""
    caria = ' aria-current="page"' if active == "contact.html" else ""
    items += f'<li><a href="contact.html"{ccls}{caria}>Contact</a></li>'
    return f'''<hr class="sweep-bar">
<header class="site-header">
  <div class="container nav">
    <a href="index.html" class="brand" aria-label="Bravaura LLC home">
      <img src="assets/bravaura-logo-final.png" alt="Bravaura LLC logo">
    </a>
    <nav aria-label="Main">
      <ul class="nav-links" id="nav-links">{items}</ul>
    </nav>
    <div class="nav-cta">
      <a href="contact.html" class="btn btn--gold">Book Now</a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-links">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <span class="footer-logo-chip"><img src="assets/bravaura-logo-final.png" alt="Bravaura LLC"></span>
        <p>Mobile art events across New Jersey. We bring everything. You just create.</p>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <ul>
          <li><a href="services.html">Services</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="quote.html">Quote Estimator</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="contact.html">Book an Event</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Get in Touch</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{IG_URL}" target="_blank" rel="noopener">@{IG}</a></li>
          <li>Serving all of NJ, incl. Hunterdon &amp; Mercer County</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> Bravaura LLC. All rights reserved.</span>
      <span>Art Without the Stress.</span>
    </div>
  </div>
</footer>'''

def page(filename, title, description, active, body, og_extra=""):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="assets/bravaura-logo-final.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
{header(active)}
<main>
{body}
</main>
{footer()}
<script src="js/main.js"></script>
</body>
</html>'''
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

# Reusable CTA band
def cta_band(heading="Ready to book your art event?",
             text="Tell us the occasion and we'll send a custom quote within 24 hours — setup, instruction, and cleanup all included.",
             primary=("Get an Estimate", "quote.html"),
             secondary=("Browse Services", "services.html")):
    sec = f'<a href="{secondary[1]}" class="btn btn--white btn--lg">{secondary[0]}</a>' if secondary else ""
    return f'''<section class="section cta-band">
  <div class="container center">
    <h2>{heading}</h2>
    <p class="lead" style="margin:0 auto 1.8rem;">{text}</p>
    <div class="btn-row" style="justify-content:center;">
      <a href="{primary[1]}" class="btn btn--gold btn--lg">{primary[0]}</a>
      {sec}
    </div>
  </div>
</section>'''

print("helpers loaded")

# ================================================================ HOME
home_body = f'''
<section class="hero">
  <div class="container hero-inner hero-split">
    <div>
      <p class="eyebrow">Mobile Art Events · New Jersey</p>
      <h1>Art Without the <span class="accent">Stress.</span></h1>
      <p class="lead">We come to you. You just create. We bring the supplies, teach the art, and clean up after.</p>
      <div class="btn-row">
        <a href="contact.html" class="btn btn--gold btn--lg">Book Your Event</a>
        <a href="services.html" class="btn btn--teal btn--lg">See Services</a>
      </div>
    </div>
    {placeholder_photo("Real event photos coming soon", "hero")}
  </div>
</section>

<section class="section">
  <div class="container center">
    <p class="eyebrow">How It Works</p>
    <h2>Four steps. Zero logistics.</h2>
  </div>
  <div class="container" style="margin-top:44px;">
    <div class="grid grid-4 steps">
      <div class="step"><div class="step-num">1</div><h3>Book it</h3><p>Pick a service and date.</p></div>
      <div class="step"><div class="step-num">2</div><h3>We set up</h3><p>We bring and arrange everything.</p></div>
      <div class="step"><div class="step-num">3</div><h3>We teach</h3><p>Step-by-step, any skill level.</p></div>
      <div class="step"><div class="step-num">4</div><h3>We clean up</h3><p>Your space, spotless again.</p></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container center">
    <p class="eyebrow">What We Do</p>
    <h2>Pick your kind of fun</h2>
  </div>
  <div class="container" style="margin-top:40px;">
    <div class="grid grid-auto">
      {service_card("birthday-parties.html", "a-magenta", IMG_TEACH, "Guided painting at a birthday party", "Birthday Parties", "A guided art project everyone remembers. Starting at $40/person, with decorations, goodie bags, and more available.", "var(--magenta)")}
      {service_card("paint-sip.html", "a-purple", IMG_WINE, "Friends at a paint and sip event", "Paint &amp; Sip", "Painting, drinks, and good company. Starting at $40/person.", "var(--purple)")}
      {service_card("corporate.html", "", IMG_GROUP, "A team painting together", "Corporate Team Building", "Team building through art. Starting at $45/person, 10-person min.", "var(--teal-text)")}
      {service_card("face-painting.html", "a-gold", IMG_FACE, "Colorful face paint design", "Face Painting", "Bright, custom designs. $135/hour, 2-hour minimum.", "var(--orange-text)")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container center">
    <p class="eyebrow">Why Bravaura</p>
    <h2>All the art. None of the work.</h2>
  </div>
  <div class="container" style="margin-top:40px;">
    <div class="grid grid-4" style="gap:30px 36px;">
      <div class="feature"><div class="fi">{icon("truck")}</div><div><h3>We come to you</h3><p>Anywhere in New Jersey.</p></div></div>
      <div class="feature"><div class="fi">{icon("shield")}</div><div><h3>All-inclusive</h3><p>Setup, teaching, cleanup — done.</p></div></div>
      <div class="feature"><div class="fi">{icon("palette")}</div><div><h3>Pro instruction</h3><p>No experience needed.</p></div></div>
      <div class="feature"><div class="fi">{icon("users")}</div><div><h3>Any group size</h3><p>Small gathering to big bash.</p></div></div>
    </div>
  </div>
</section>

{trusted_by_strip()}

{testimonials_section()}

{cta_band()}
'''
page("index.html",
     "Bravaura LLC | Mobile Art Event Services in New Jersey",
     "Bravaura brings all-inclusive mobile art events to New Jersey — birthday parties, paint & sip, corporate team building, and face painting. We set up, teach, and clean up. You just create.",
     "index.html", home_body)

# ================================================================ SERVICES HUB
services_body = f'''
<section class="page-hero">
  <div class="container page-hero-inner">
    <p class="eyebrow">Our Services</p>
    <h1>Professional art experiences, brought to you</h1>
    <p class="lead">Whether you're celebrating a birthday, planning a team event, or looking for entertainment, Bravaura brings the supplies, the instruction, and the cleanup — anywhere in New Jersey.</p>
    <div class="btn-row" style="margin-top:1.6rem;"><a href="contact.html" class="btn btn--gold btn--lg">Get a Custom Quote</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-auto">
      {service_card("birthday-parties.html", "a-magenta", IMG_TEACH, "Guided painting at a birthday party", "Birthday Parties", "A guided art project that becomes the highlight of the party. Starting at $40/person, plus optional add-ons.", "var(--magenta)")}
      {service_card("paint-sip.html", "a-purple", IMG_WINE, "Friends at a paint and sip event", "Paint &amp; Sip", "Painting, drinks, and friends. You bring the beverages, we bring the art.", "var(--purple)")}
      {service_card("corporate.html", "", IMG_GROUP, "A team painting together", "Corporate Team Building", "Bond your team through art. Low pressure, high energy, zero cleanup.", "var(--teal-text)")}
      {service_card("face-painting.html", "a-gold", IMG_FACE, "Colorful face paint design", "Face Painting", "Custom designs and character requests for parties, festivals, and events.", "var(--orange-text)")}
      {service_card("master-classes.html", "a-blue", IMG_PALETTE, "Focused art technique class", "Master Classes", "Focused, small-group instruction to level up a real skill or technique.", "var(--deep-blue)")}
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container center narrow">
    <p class="eyebrow">Every Event Includes</p>
    <h2>Setup. Instruction. Cleanup.</h2>
    <p class="lead" style="margin:0 auto;">We bring the tables, easels, canvases, paints, and aprons — teach the whole thing — then pack it all out. You just show up.</p>
  </div>
</section>

{cta_band()}
'''
page("services.html",
     "Art Event Services NJ | Bravaura LLC",
     "Explore Bravaura's mobile art event services in New Jersey: birthday parties, paint & sip events, corporate team building, and professional face painting. All-inclusive, we come to you.",
     "services.html", services_body)


# ---- reusable service page builder ----
def service_page(filename, active_icon, accent_class, icon_class, eyebrow, h1, tagline,
                 intro, includes, whofor, whatprovide, pricing_line, duration, customization,
                 book_label, title, desc, img_id=IMG_PALETTE, img_alt="People painting at a Bravaura event",
                 extra_section=""):
    inc = "".join(f"<li>{i}</li>" for i in includes)
    cust = "".join(f'<span class="pill">{c}</span>' for c in customization)
    body = f'''
<section class="page-hero">
  <div class="container page-hero-inner">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lead">{tagline}</p>
    <div class="btn-row" style="margin-top:1.6rem;"><a href="contact.html" class="btn btn--gold btn--lg">{book_label}</a></div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <p class="eyebrow">The Experience</p>
      <h2>{h1}</h2>
      <p class="lead" style="font-size:1.1rem;">{intro}</p>
      <h3 style="margin-top:1.6rem;">What's included</h3>
      <ul class="checklist">{inc}</ul>
    </div>
    {photo(img_id, img_alt, "wide")}
  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <div class="grid grid-3">
      <div class="card"><div class="card-icon {icon_class}">{icon(active_icon)}</div><h3>Who it's for</h3><p>{whofor}</p></div>
      <div class="card"><div class="card-icon i-blue">{icon("clock")}</div><h3>Duration</h3><p>{duration}</p></div>
      <div class="card"><div class="card-icon i-gold">{icon("gift")}</div><h3>You provide</h3><p>{whatprovide}</p></div>
    </div>
    <div class="card" style="margin-top:26px;">
      <div class="split" style="gap:24px;align-items:center;">
        <div>
          <h3 class="mt-0">Pricing</h3>
          <p class="mb-0" style="font-size:1.1rem;color:#4a5763;">{pricing_line}</p>
        </div>
        <div style="text-align:right;"><a href="quote.html" class="btn btn--ghost">Get an estimate</a></div>
      </div>
    </div>
    <div style="margin-top:30px;">
      <h3>Make it yours</h3>
      <div class="pill-row">{cust}</div>
    </div>
  </div>
</section>

{extra_section}
{cta_band(heading="Let's plan your event", primary=(book_label, "contact.html"))}
'''
    page(filename, title, desc, "services.html", body)


service_page(
    "birthday-parties.html", "cake", "a-magenta", "i-magenta",
    "Birthday Parties", "Birthday Parties Made Easy",
    "The party everyone remembers — and you don't have to lift a finger to pull it off.",
    "Turn any birthday into a hands-on art party. We arrive with everything, guide your guests through a project they'll be proud of, and clean up every last drop before we go. All you handle is the guest list and the cake.",
    ["Full setup — tables, easels, canvases, paints, brushes, and aprons",
     "Guided painting or canvas art led by a professional art educator",
     "A finished piece for every guest to take home",
     "Complete cleanup — we leave your space spotless"],
    "Kids, teens, and adults. We tailor the project and pacing to the age group so everyone's engaged.",
    "The venue and the guest list. We bring absolutely everything else.",
    "$40 per person, plus a travel fee ($25 local, or $60+ farther than 30 minutes out). Bigger groups save more: $4 off each person past 12, and $6 off each person past 15. Want decorations, goodie bags, a slime table, glow-in-the-dark painting, or games added on? Just ask — add-ons are priced per event. Final quotes are confirmed by email.",
    "Flexible — most parties run 1.5 to 2 hours.",
    ["Choose your art project", "Kids / teens / adults", "1.5 or 2 hours", "Decorations", "Goodie bags", "Slime table", "Glow-in-the-dark painting", "Games &amp; activities", "Add-on face painting"],
    "Book a Birthday Party",
    "Birthday Party Painting NJ | Bravaura LLC",
    "Stress-free birthday art parties across New Jersey. We set up, teach a guided painting project, and clean up. Starting at $40/person, with optional decorations, goodie bags, slime tables, and more. For kids, teens, and adults.",
    img_id=IMG_TEACH, img_alt="Guided painting instruction at a birthday party",
    extra_section=f'''
<section class="section">
  <div class="container">
    <p class="eyebrow">Optional Add-Ons</p>
    <h2>Make it a whole party, not just a painting</h2>
    <p class="lead" style="font-size:1.05rem;">Decorations, goodie bags, a slime table, glow-in-the-dark painting, games &mdash; mix and match whatever fits the celebration. Every add-on is priced per event, so tell us what you're picturing and we'll build it into your quote.</p>
    <div class="grid grid-2" style="margin-top:30px;gap:26px;">
      {photo(IMG_DECOR, "Colorful balloon decorations for a birthday party", "wide")}
      {photo(IMG_GLOW, "Glow-in-the-dark painting add-on", "wide")}
    </div>
  </div>
</section>''')

service_page(
    "paint-sip.html", "wine", "a-purple", "i-purple",
    "Paint & Sip", "Painting + Drinks + Friends = Perfect Evening",
    "A relaxed, social night of creativity — everyone leaves with a canvas and a good time.",
    "Our paint & sip events turn a living room, backyard, or private room into a creative escape. You pour the drinks; we guide the painting. It's the ideal ladies' night, friend gathering, or laid-back team hangout — no art experience required.",
    ["Full setup and breakdown",
     "Guided, step-by-step painting instruction",
     "Beverage-friendly setup (you provide the drinks; we handle the art)",
     "A completed canvas for everyone to take home"],
    "Adults — ladies' nights, friend groups, birthdays, and casual team bonding.",
    "Your drinks of choice (wine, beer, or non-alcoholic) and the space. We bring the art.",
    "$40 per person, plus a travel fee ($25 local, or $60+ farther than 30 minutes out). Bigger groups save more: $4 off each person past 12, and $6 off each person past 15. Final quotes are confirmed by email.",
    "Typically 2 to 3 hours.",
    ["Wine / beer / non-alcoholic", "Choose your painting", "2 or 3 hours", "Private or group", "Seasonal themes"],
    "Get a Custom Quote",
    "Paint & Sip Events NJ | Bravaura LLC",
    "Mobile paint & sip parties across New Jersey. Guided painting for adults — ladies' nights, friend groups, and team bonding. You bring the drinks, we bring the art.",
    img_id=IMG_WINE, img_alt="Friends painting and enjoying drinks at a paint and sip event")

service_page(
    "corporate.html", "users", "a-teal", "i-teal",
    "Corporate Team Building", "Team Building Through Art",
    "Connection without the trust falls. A creative experience your team will actually enjoy.",
    "Give your team something better than another meeting. Our facilitated art sessions break the ice, spark collaboration, and give everyone a shared win — all in a low-pressure, genuinely fun setting. We come to your office or venue and leave it exactly as we found it.",
    ["Professional facilitation and icebreaking",
     "Guided instruction for collaborative or individual artwork",
     "All materials, setup, and breakdown included",
     "Zero cleanup for your office or venue"],
    "Teams of any size — offices, departments, offsites, and client events.",
    "The space (or let us suggest one) and your headcount. We handle the rest.",
    "$45 per person (10-person minimum), plus a travel fee ($25 local, or $60+ farther than 30 minutes out). Bigger groups save more: $4 off each person past 12, and $6 off each person past 15. Final quotes are confirmed by email.",
    "Customizable — from a 1-hour session to a 3-hour experience.",
    ["Collaborative or individual", "1 to 3 hours", "On-site at your office", "Branded project options", "Any team size"],
    "Request a Corporate Package",
    "Corporate Team Building Art Events NJ | Bravaura LLC",
    "Art-based corporate team building across New Jersey. Facilitated, low-pressure creative sessions that build connection. We come to your office — setup and cleanup included.",
    img_id=IMG_GROUP, img_alt="A team painting together during a corporate art session")

service_page(
    "face-painting.html", "smile", "a-gold", "i-gold",
    "Face Painting", "Professional Face Painting Entertainment",
    "Bright, beautiful designs that make any event more fun — for all ages.",
    "Add a splash of magic to your event with professional face painting. From classic butterflies and superheroes to custom character requests, we create designs that light up faces at parties, festivals, and celebrations of every kind.",
    ["A professional face painting artist",
     "Custom designs and character requests",
     "Skin-safe, professional-grade paints",
     "Flexible hourly booking"],
    "Birthday parties, festivals, corporate family days, and community celebrations.",
    "The event and the smiles. We bring the paints, brushes, and designs.",
    "$135 per hour, 2-hour minimum booking, plus a travel fee ($25 local, or $60+ farther than 30 minutes out).",
    "Booked hourly — 2-hour minimum, then as long as your event needs.",
    ["Traditional designs", "Character art", "Themed / event branding", "Glitter add-ons", "2-hour minimum booking"],
    "Book Face Painting",
    "Face Painting Services NJ | Bravaura LLC",
    "Professional face painting for parties, festivals, and events across New Jersey. Custom designs and character art, $135/hour with a 2-hour minimum, plus travel. Book Bravaura for your celebration.",
    img_id=IMG_FACE, img_alt="A colorful butterfly face paint design")

service_page(
    "master-classes.html", "palette", "a-blue", "i-blue",
    "Master Classes", "Master Classes",
    "Go beyond the one-off. Focused sessions for people who want to really learn.",
    "Master classes are for when you want to build a real skill — not just make one painting. In a small-group setting, we go deep on a single technique: acrylics, watercolor, color mixing, portraits, whatever you want to master. Hands-on, personalized, and paced for you.",
    ["Small-group, focused instruction",
     "A technique or theme of your choice",
     "All materials, setup, and cleanup included",
     "Personalized feedback as you work"],
    "Teens and adults who want to level up. Total beginners welcome — so are people who already paint.",
    "The space and the curiosity. We bring everything else.",
    "Custom quote based on group size, session length, and location. Ask us for a rate.",
    "Usually 2–3 hours. Multi-session series available.",
    ["Choose your technique", "Single class or a series", "Beginner or advanced", "2 or 3 hours", "In-home or at a venue"],
    "Ask About Master Classes",
    "Art Master Classes NJ | Bravaura LLC",
    "Small-group art master classes across New Jersey — focused instruction in acrylics, watercolor, color, and technique, all materials included. We come to you.",
    img_id=IMG_PALETTE, img_alt="Mixing colors while learning a painting technique")

print("home + services done")

# ================================================================ QUOTE ESTIMATOR
QUOTE_TOP = '''
<section class="page-hero">
  <div class="container page-hero-inner">
    <p class="eyebrow">Get a Quote</p>
    <h1>Build your estimate</h1>
    <p class="lead">Pick your event, add the size and location, and get a ballpark on the spot. Ready to book? Send it over and we'll confirm an exact, all-inclusive price within 24 hours.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split" style="align-items:start;gap:44px;">
      <div class="form-card">
        <h2 class="mt-0" style="font-size:1.6rem;">Your event</h2>
        <div class="form-grid">
          <div class="field full">
            <label for="q-service">Service <span class="req">*</span></label>
            <select id="q-service">
              <option value="" disabled selected>Choose one…</option>
              <option value="birthday">Birthday Party</option>
              <option value="paintsip">Paint &amp; Sip</option>
              <option value="corporate">Corporate Team Building</option>
              <option value="face">Face Painting</option>
              <option value="master">Master Class</option>
            </select>
          </div>
          <div class="field" id="q-people-wrap">
            <label for="q-people">How many people?</label>
            <input id="q-people" type="number" min="1" inputmode="numeric" placeholder="e.g. 12">
          </div>
          <div class="field" id="q-hours-wrap" style="display:none;">
            <label for="q-hours">How many hours? <span style="font-weight:500;color:var(--cool-gray);">(2-hour minimum)</span></label>
            <input id="q-hours" type="number" min="2" step="0.5" inputmode="decimal" placeholder="e.g. 2">
          </div>
          <div class="field full">
            <label for="q-location">Your location</label>
            <select id="q-location">
              <option value="local" selected>Local — within ~30 minutes of us ($25 travel)</option>
              <option value="far">Farther than 30 minutes away</option>
            </select>
          </div>
          <div class="field full" id="q-miles-wrap" style="display:none;">
            <label for="q-miles">About how many miles from us?</label>
            <input id="q-miles" type="number" min="1" inputmode="numeric" placeholder="e.g. 25">
          </div>
          <div class="field full">
            <label for="q-town">Town / venue (optional)</label>
            <input id="q-town" type="text" placeholder="City or venue in NJ">
          </div>
          <div class="field full" id="q-addons-wrap" style="display:none;">
            <label>Want any add-ons?</label>
            <p class="mb-0" style="color:#4a5763;font-size:0.92rem;">Decorations, goodie bags, a slime table, glow-in-the-dark painting, and games can all be added on — priced per event. Mention what you'd like when you request your quote.</p>
          </div>
        </div>
      </div>

      <div>
        <div class="card" style="border-top:5px solid var(--gold);">
          <p class="eyebrow" style="margin-bottom:6px;">Your estimate</p>
          <div id="q-amount" style="font-family:var(--font-display);font-size:2.1rem;font-weight:600;color:var(--deep-blue);line-height:1.12;">Pick a service to start</div>
          <div id="q-breakdown" style="color:#4a5763;margin-top:10px;font-size:0.98rem;line-height:1.5;"></div>
          <a href="contact.html" class="btn btn--gold btn--lg" style="margin-top:18px;">Request This Quote</a>
          <p class="form-note" id="q-note" style="margin-top:14px;">Ballpark only — your final, all-inclusive quote is confirmed by us within 24 hours.</p>
        </div>
        <div class="card" style="margin-top:20px;background:var(--mist);border:none;">
          <h3 class="mt-0" style="font-size:1.1rem;">Good to know</h3>
          <p class="mb-0" style="color:#4a5763;font-size:0.96rem;">Every estimate covers setup, instruction, and cleanup. A $100 non-refundable deposit secures your date; the balance is due at or before the event. Pay by card, check, Venmo, or PayPal.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''

QUOTE_SCRIPT = r'''
<script>
(function(){
  // ----- Editable rates (change these anytime) -----
  var RATES = { birthday: 40, paintsip: 40, corporate: 45 };  // per person, base rate
  var CORPORATE_MIN = 10;               // corporate 10-person minimum
  // Volume discount: people 1-12 at the base rate, people 13-15 at $4 off,
  // people 16+ at $6 off. Applies per added person, not the whole group.
  var TIER1_CUTOFF = 12, TIER2_CUTOFF = 15, TIER2_OFF = 4, TIER3_OFF = 6;
  var FACE_RATE = 135, FACE_MIN_HOURS = 2;  // face painting per hour + minimum booking
  // Travel: $25 flat if local (<=30 min). Farther than 30 min: $60 base,
  // +$10 for every additional 5 miles beyond LOCAL_MILES.
  var TRAVEL_LOCAL = 25, TRAVEL_FAR_BASE = 60, TRAVEL_PER_5MI = 10, LOCAL_MILES = 15;
  // -------------------------------------------------
  var svc = document.getElementById('q-service');
  if(!svc) return;
  var people = document.getElementById('q-people');
  var hours = document.getElementById('q-hours');
  var loc = document.getElementById('q-location');
  var miles = document.getElementById('q-miles');
  var peopleWrap = document.getElementById('q-people-wrap');
  var hoursWrap = document.getElementById('q-hours-wrap');
  var milesWrap = document.getElementById('q-miles-wrap');
  var addonsWrap = document.getElementById('q-addons-wrap');
  var amount = document.getElementById('q-amount');
  var breakdown = document.getElementById('q-breakdown');
  var note = document.getElementById('q-note');

  function money(n){ return '$' + Math.round(n).toLocaleString(); }

  function tieredCost(p, rate){
    var t1 = Math.min(p, TIER1_CUTOFF);
    var t2 = Math.max(0, Math.min(p, TIER2_CUTOFF) - TIER1_CUTOFF);
    var t3 = Math.max(0, p - TIER2_CUTOFF);
    var total = t1 * rate + t2 * (rate - TIER2_OFF) + t3 * (rate - TIER3_OFF);
    var parts = [t1 + ' &times; $' + rate];
    if(t2 > 0) parts.push(t2 + ' &times; $' + (rate - TIER2_OFF));
    if(t3 > 0) parts.push(t3 + ' &times; $' + (rate - TIER3_OFF));
    return { total: total, line: parts.join(' + ') };
  }

  function travelFee(){
    if(loc.value !== 'far') return TRAVEL_LOCAL;
    var mi = parseFloat(miles.value) || LOCAL_MILES;
    var extra = Math.max(0, mi - LOCAL_MILES);
    return TRAVEL_FAR_BASE + Math.ceil(extra / 5) * TRAVEL_PER_5MI;
  }

  function render(){
    var s = svc.value;
    milesWrap.style.display = (loc.value === 'far') ? '' : 'none';
    var travel = travelFee();
    var travelLine = '<br>+ travel fee ' + money(travel) + (loc.value === 'far' ? ' (over 30 min out)' : ' (local)');
    hoursWrap.style.display = (s === 'face') ? '' : 'none';
    peopleWrap.style.display = (s === 'face') ? 'none' : '';
    addonsWrap.style.display = (s === 'birthday') ? '' : 'none';
    note.textContent = 'Ballpark only — your final, all-inclusive quote is confirmed by us by email.';

    if(s === 'birthday' || s === 'paintsip' || s === 'corporate'){
      var rate = RATES[s];
      var p = parseInt(people.value, 10);
      if(!p || p < 1){ amount.textContent = 'Add your headcount'; breakdown.textContent = 'Starts at $' + rate + ' per person, with a discount once your group passes ' + TIER1_CUTOFF + '.' + (s === 'corporate' ? ' (' + CORPORATE_MIN + '-person minimum.)' : ''); return; }
      var billedP = (s === 'corporate' && p < CORPORATE_MIN) ? CORPORATE_MIN : p;
      var pc = tieredCost(billedP, rate);
      var total = pc.total + travel;
      amount.textContent = '~ ' + money(total);
      var minNote = (s === 'corporate' && p < CORPORATE_MIN) ? ' (10-person minimum applied)' : '';
      breakdown.innerHTML = billedP + ' people' + minNote + ': ' + pc.line + ' = ' + money(pc.total) + travelLine + (s === 'birthday' ? '<br>Add-ons (decorations, goodie bags, etc.) priced separately.' : '');
    } else if(s === 'face'){
      var h = parseFloat(hours.value);
      if(!h || h < 1){ amount.textContent = 'Add your hours'; breakdown.textContent = '$' + FACE_RATE + '/hour, ' + FACE_MIN_HOURS + '-hour minimum.'; return; }
      var billedH = Math.max(h, FACE_MIN_HOURS);
      var base2 = billedH * FACE_RATE, total2 = base2 + travel;
      amount.textContent = '~ ' + money(total2);
      var hrNote = (h < FACE_MIN_HOURS) ? ' (' + FACE_MIN_HOURS + '-hour minimum applied)' : '';
      breakdown.innerHTML = billedH + ' hr' + hrNote + ' &times; $' + FACE_RATE + ' = ' + money(base2) + travelLine;
    } else if(s === 'master'){
      amount.textContent = "Let's customize it";
      breakdown.innerHTML = 'Master classes are quoted per event. Send your details and we&rsquo;ll reply with an exact price.';
    } else {
      amount.textContent = 'Pick a service to start';
      breakdown.textContent = '';
    }
  }
  [svc, people, hours, loc, miles].forEach(function(el){
    el.addEventListener('input', render);
    el.addEventListener('change', render);
  });
  render();
})();
</script>
'''

quote_body = (QUOTE_TOP +
    cta_band(heading="Prefer we just handle it?",
             text="Skip the estimator — tell us about your event and we'll send a custom, all-inclusive quote within 24 hours.",
             primary=("Contact Us", "contact.html"),
             secondary=("Browse Services", "services.html")) +
    QUOTE_SCRIPT)
page("quote.html",
     "Get a Quote | Bravaura LLC Art Events NJ",
     "Estimate your Bravaura art event in seconds — birthday parties, paint & sip, corporate, face painting, and master classes across New Jersey. Then request an exact quote.",
     "quote.html", quote_body)

# ================================================================ PRICING
def formula_card(accent, icon_name, title, rate_html, items, note_text):
    tiers = "".join(f'<span class="travel-tier">{t}</span>' for t in ["$25 local (≤30 min)", "$60+ farther (>30 min)", "+$10 per 5 mi beyond that"])
    lis = "".join(f"<li>{i}</li>" for i in items)
    note_html = f'<p class="formula-note mb-0" style="margin-top:10px;">{note_text}</p>' if note_text else ""
    return f'''<div class="formula-card" style="border-top:5px solid var({accent});">
      <div class="card-icon i-{accent.replace("--","")}" style="margin-bottom:14px;">{icon(icon_name)}</div>
      <h3 class="mt-0">{title}</h3>
      <div class="formula-big">{rate_html}</div>
      <ul class="checklist" style="margin-bottom:14px;">{lis}</ul>
      {note_html}
      <p class="formula-note mb-0">Plus a travel fee based on distance:</p>
      <div class="travel-tiers">{tiers}</div>
    </div>'''

UNIT_SPAN = '<span style="font-size:1rem;font-weight:600;color:var(--cool-gray);">{}</span>'
RATE_BIRTHDAY = "$40 " + UNIT_SPAN.format("/ person")
RATE_PAINTSIP = "$40 " + UNIT_SPAN.format("/ person")
RATE_CORPORATE = "$45 " + UNIT_SPAN.format("/ person")
RATE_FACE = "$135 " + UNIT_SPAN.format("/ hour")

VOLUME_DISCOUNT_ITEM = "Price drops per person once your group grows: $4 off each person past 12, $6 off each person past 15"

pricing_cards = (
    formula_card("--magenta", "cake", "Birthday Parties", RATE_BIRTHDAY, ["Full setup, instruction &amp; cleanup included", "Guided project for any age group", VOLUME_DISCOUNT_ITEM], "Optional add-ons: decorations, goodie bags, slime table, glow-in-the-dark painting, games &mdash; priced on request.") +
    formula_card("--purple", "wine", "Paint &amp; Sip", RATE_PAINTSIP, ["Full setup, instruction &amp; cleanup included", "You provide the drinks, we provide the art", VOLUME_DISCOUNT_ITEM], "") +
    formula_card("--teal", "users", "Corporate Team Building", RATE_CORPORATE, ["10-person minimum", "Full setup, facilitation &amp; cleanup included", VOLUME_DISCOUNT_ITEM], "") +
    formula_card("--gold", "smile", "Face Painting", RATE_FACE, ["2-hour minimum booking", "Booked hourly, any event size after that"], "")
)

pricing_body = f'''
<section class="page-hero">
  <div class="container page-hero-inner">
    <p class="eyebrow">Pricing</p>
    <h1>Simple, transparent pricing</h1>
    <p class="lead">No hidden fees, no guessing games — here's exactly how every quote is built. Travel fees scale with distance, and every price below already includes setup, instruction, and cleanup.</p>
    <div class="btn-row" style="margin-top:1.6rem;"><a href="quote.html" class="btn btn--gold btn--lg">Try the Quote Estimator</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="gap:26px;">
      {pricing_cards}
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container center narrow">
    <p class="eyebrow">Good to Know</p>
    <h2>How travel fees work</h2>
    <p class="lead" style="margin:0 auto;">Events within about 30 minutes of our home base are a flat <strong>$25</strong> travel fee. Farther than that, it's a <strong>$60</strong> base fee, plus <strong>$10 for every additional 5 miles</strong> beyond that. We'll always confirm the exact travel fee before you book. <strong>Final quotes are confirmed by email</strong> after we review your event details.</p>
    <p class="form-note" style="margin-top:1.4rem;">A $100 non-refundable deposit is required to reserve your date. The deposit is applied toward your total; the remaining balance is due at or before the event.</p>
  </div>
</section>

{cta_band(heading="Want an exact number?", text="Use our quote estimator for an instant ballpark, or send us your details and we'll confirm your exact, all-inclusive price by email.", primary=("Get an Estimate", "quote.html"), secondary=("Request a Quote", "contact.html"))}
'''
page("pricing.html",
     "Pricing | Bravaura LLC Mobile Art Events NJ",
     "Transparent pricing for Bravaura's mobile art events: Birthday Parties $40/person, Paint & Sip $40/person, Corporate $45/person, Face Painting $135/hour (2-hr min). Plus a distance-based travel fee, confirmed by email.",
     "pricing.html", pricing_body)

# ================================================================ GALLERY
# Mix of AI-generated brand-palette shots (full URLs) and curated stock placeholders.
# Swap any of these for your real event photos any time — same grid, same size.
GALLERY_IMAGES = [
    (IMG_WINE, "Friends enjoying a paint & sip evening"),
    (IMG_TEACH, "A birthday party guided painting session"),
    (IMG_FACE, "A colorful butterfly face painting design"),
    (IMG_GROUP, "A corporate team building art session"),
    (IMG_PALETTE, "Close-up of paint and brushes set up for an event"),
    (IMG_DECOR, "Colorful balloon decorations, a birthday add-on"),
    (IMG_GLOW, "Glow-in-the-dark painting, a birthday add-on"),
    (IMG_ART, "A finished, vibrant painting ready to take home"),
]

def gallery_grid():
    items = ""
    for base_id, alt in GALLERY_IMAGES:
        src = _resolve_src(base_id, 700)
        onerr = "this.closest('.gallery-item').style.background='var(--sweep)';this.remove();"
        items += f'<div class="gallery-item"><img src="{src}" alt="{alt}" loading="lazy" onerror="{onerr}"></div>'
    return f'<div class="gallery-grid">{items}</div>'

gallery_body = f'''
<section class="page-hero">
  <div class="container page-hero-inner">
    <p class="eyebrow">Gallery</p>
    <h1>A peek at the paint</h1>
    <p class="lead">Moments from Bravaura events across New Jersey — birthday parties, paint &amp; sip nights, corporate sessions, and face painting. More real event photos coming soon.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    {gallery_grid()}
  </div>
</section>

{cta_band(heading="Want your event featured here next?", primary=("Book Your Event", "contact.html"))}
'''
page("gallery.html",
     "Gallery | Bravaura LLC Mobile Art Events NJ",
     "See Bravaura LLC mobile art events in action — birthday parties, paint & sip nights, corporate team building, and face painting across New Jersey.",
     "gallery.html", gallery_body)

# ================================================================ ABOUT
about_body = f'''
<section class="page-hero">
  <div class="container page-hero-inner">
    <p class="eyebrow">About Bravaura</p>
    <h1>Art should be a joy, not a project to manage</h1>
    <p class="lead">Bravaura was built on a simple idea: everyone deserves the fun of making something, without the stress of planning it. We're based in New Jersey and travel to events across the state, including Hunterdon and Mercer County.</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    {photo(IMG_PALETTE, "Mixing paint colors on an artist's palette", "tall")}
    <div class="split--rev">
      <p class="eyebrow">Our Story</p>
      <h2>Hi, I'm Kendal Plumstead</h2>
      <p>It all started with a girl from New Jersey who loves art — and loves teaching it even more. I have a degree in Art Education from The College of New Jersey (TCNJ) and lots of hands-on experience teaching people of every age how to create something they're proud of.</p>
      <p>I'm an art educator who loves watching people light up when they realize they <em>can</em> make something beautiful. Bravaura brings that feeling to you — right where you already are.</p>
      <p class="mb-0">Great celebrations shouldn't get buried in setup and cleanup. So I handle all of it. You pick the occasion; I bring the whole experience to your door.</p>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container center">
    <p class="eyebrow">What Makes Us Different</p>
    <h2>Mobile. All-inclusive. Actually fun.</h2>
  </div>
  <div class="container" style="margin-top:40px;">
    <div class="grid grid-4">
      <div class="card center"><div class="card-icon i-teal" style="margin:0 auto 16px;">{icon("truck")}</div><h3>Mobile</h3><p>We come to you, anywhere in NJ.</p></div>
      <div class="card center"><div class="card-icon i-magenta" style="margin:0 auto 16px;">{icon("shield")}</div><h3>All-inclusive</h3><p>Setup, instruction, and cleanup — handled.</p></div>
      <div class="card center"><div class="card-icon i-purple" style="margin:0 auto 16px;">{icon("palette")}</div><h3>Professional</h3><p>Led by a trained art educator.</p></div>
      <div class="card center"><div class="card-icon i-gold" style="margin:0 auto 16px;">{icon("heart")}</div><h3>Personal</h3><p>Every event built around your people.</p></div>
    </div>
  </div>
</section>

{cta_band(heading="Let's make something together", primary=("Book an Event", "contact.html"))}
'''
page("about.html",
     "About | Bravaura LLC Mobile Art Events NJ",
     "Meet Kendal Plumstead, the TCNJ-trained art educator behind Bravaura LLC — mobile, all-inclusive art events across New Jersey, including Hunterdon and Mercer County. Our mission: the joy of creating, without the stress of planning.",
     "about.html", about_body)

# ================================================================ CONTACT
contact_body = f'''
<section class="page-hero">
  <div class="container page-hero-inner">
    <p class="eyebrow">Book Your Event</p>
    <h1>Let's bring the art to you</h1>
    <p class="lead">Fill out the form and we'll respond within 24 hours with a custom quote and next steps. Prefer to talk? Call or email — we'd love to hear about your event.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split" style="align-items:start;gap:44px;">
      <div class="form-card">
        <h2 class="mt-0" style="font-size:1.7rem;">Request a quote</h2>
        <p style="color:#4a5763;">Tell us a little about your event and we'll take it from there. Your final, all-inclusive quote is confirmed by email.</p>
        <form data-bravaura-form name="quote-request" method="POST" data-netlify="true" netlify-honeypot="bot-field" novalidate>
          <input type="hidden" name="form-name" value="quote-request">
          <p style="display:none;"><label>Leave this empty: <input name="bot-field"></label></p>
          <div class="form-grid">
            <div class="field"><label for="name">Name <span class="req">*</span></label><input id="name" name="name" type="text" required autocomplete="name"></div>
            <div class="field"><label for="email">Email <span class="req">*</span></label><input id="email" name="email" type="email" required autocomplete="email"></div>
            <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
            <div class="field"><label for="event_type">Event type <span class="req">*</span></label>
              <select id="event_type" name="event_type" required>
                <option value="" disabled selected>Choose one…</option>
                <option>Birthday Party</option>
                <option>Paint &amp; Sip</option>
                <option>Corporate Team Building</option>
                <option>Face Painting</option>
                <option>Other</option>
              </select>
            </div>
            <div class="field"><label for="event_date">Preferred date</label><input id="event_date" name="event_date" type="date"></div>
            <div class="field"><label for="group_size">Group size</label><input id="group_size" name="group_size" type="number" min="1" placeholder="e.g. 12"></div>
            <div class="field full"><label for="location">Event location — town / venue / ZIP</label><input id="location" name="location" type="text" placeholder="e.g. Montclair, NJ 07042" required></div>
            <div class="field full"><label for="message">Special requests or questions</label><textarea id="message" name="message" placeholder="Tell us about the occasion, the vibe, or anything you're picturing."></textarea></div>
          </div>
          <div style="margin-top:20px;"><button type="submit" class="btn btn--gold btn--lg">Send My Request</button></div>
          <div class="form-status" role="status" aria-live="polite"></div>
          <p class="form-note">We reply by email within 24 hours with a custom, all-inclusive quote and next steps. Your info is only used to plan your event — never shared. A $100 non-refundable deposit is required to reserve your date.</p>
        </form>
      </div>

      <div>
        <h2 class="mt-0" style="font-size:1.7rem;">Reach us directly</h2>
        <div class="contact-info" style="margin-top:18px;">
          <div class="contact-line"><div class="ci">{icon("phone")}</div><div><a href="tel:{PHONE_TEL}">{PHONE}</a><small>Call or text</small></div></div>
          <div class="contact-line"><div class="ci">{icon("mail")}</div><div><a href="mailto:{EMAIL}">{EMAIL}</a><small>We reply within 24 hours</small></div></div>
          <div class="contact-line"><div class="ci">{icon("instagram")}</div><div><a href="{IG_URL}" target="_blank" rel="noopener">@{IG}</a><small>See our latest work</small></div></div>
          <div class="contact-line"><div class="ci">{icon("pin")}</div><div><span>Serving all of New Jersey</span><small>Including Hunterdon &amp; Mercer County — we travel to you, distance affects pricing</small></div></div>
        </div>
        <div class="card" style="margin-top:26px;background:var(--mist);border:none;">
          <h3 class="mt-0">Prefer to book by phone?</h3>
          <p class="mb-0" style="color:#4a5763;">Give us a call at <a href="tel:{PHONE_TEL}" style="font-weight:700;">{PHONE}</a> and we'll walk through your event together.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''
page("contact.html",
     "Contact & Booking | Bravaura LLC Art Events NJ",
     "Book a Bravaura mobile art event in New Jersey. Request a custom quote for birthday parties, paint & sip, corporate team building, or face painting. Call 908-894-3611.",
     "contact.html", contact_body)

# ================================================================ FAQ
faqs = [
    ("Do you come to our location?",
     "Yes! Bravaura is fully mobile — we travel throughout New Jersey and set everything up at your home, office, park, or venue. Distance from our base affects pricing, and we'll always include any travel fee in your quote up front."),
    ("What if someone has no art experience?",
     "Perfect — that's most of our guests. Every session is led by a professional art educator with step-by-step instruction designed for all skill levels. No experience needed; everyone leaves with something they're proud of."),
    ("What happens if a guest can't attend?",
     "No problem — just reach out and we'll discuss options. We're flexible and happy to work with you on adjustments before your event."),
    ("Can we customize the art project?",
     "Absolutely. We'll work with you to choose a project that fits your group, occasion, and theme. Just tell us what you're picturing and we'll make it happen."),
    ("Do you provide decorations?",
     "We provide all art supplies, setup, and cleanup. Decor is up to you — feel free to add your own to match your theme, and we'll build the art experience around it."),
    ("What's your cancellation policy?",
     "A $100 non-refundable deposit reserves your date and is applied toward your total. It secures our time and supplies for your event, so it isn't refundable if you cancel — but we're always happy to help you reschedule. Reach out any time and we'll help you sort out new dates."),
    ("How far will you travel?",
     "Anywhere in New Jersey. Closer events keep costs lowest; farther locations include a travel fee, which we'll always show you in your quote before you book."),
    ("How much does it cost?",
     "Birthday parties are $40/person (plus optional add-ons like decorations, goodie bags, a slime table, glow-in-the-dark painting, or games — priced on request), Paint &amp; Sip is $40/person, Corporate Team Building is $45/person (10-person minimum), and Face Painting is $135/hour with a 2-hour minimum. Bigger groups save more on the per-person services — $4 off each person past 12, and $6 off each person past 15. Every service adds a travel fee — $25 for local events within about 30 minutes, or $60+ farther out (plus $10 per additional 5 miles). See the Pricing page for the full breakdown, use our quote estimator for a ballpark, or request your exact quote — confirmed by email."),
]
faq_items = ""
for i, (q, a) in enumerate(faqs):
    faq_items += f'''<div class="faq-item">
      <button class="faq-q" aria-expanded="false">{q}</button>
      <div class="faq-a"><p>{a}</p></div>
    </div>'''
faq_body = f'''
<section class="page-hero">
  <div class="container page-hero-inner">
    <p class="eyebrow">FAQ</p>
    <h1>Good questions, honest answers</h1>
    <p class="lead">Everything you might be wondering before you book. Still curious? Just reach out.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="faq">{faq_items}</div>
  </div>
</section>

{cta_band(heading="Didn't see your question?", text="Send it our way — we'll get back to you within 24 hours.", primary=("Contact Us", "contact.html"), secondary=("Get a Quote", "quote.html"))}
'''
page("faq.html",
     "FAQ | Bravaura LLC Mobile Art Events NJ",
     "Answers to common questions about Bravaura's mobile art events in New Jersey — travel, skill levels, customization, pricing, and cancellation policy.",
     "faq.html", faq_body)

print("ALL PAGES DONE")
