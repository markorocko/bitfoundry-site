#!/usr/bin/env python3
"""Static site generator for bitfoundrylabs.com.

Multi-page site with shared head/nav/footer. Run: python3 build.py
Outputs: index.html, about/, products/, company/, contact/, privacy/, terms/
Each non-root page is <dir>/index.html so it serves as /<dir>/.
Assets stay at repo root (assets/, favicon). Pages reference them with a
leading slash so paths work from any depth.
"""
import os

SITE = "https://bitfoundrylabs.com"
EMAIL = "hello@bitfoundrylabs.com"
ADMIN = "admin@bitfoundrylabs.com"
YEAR = 2026

LINK_SVG = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none">'
            '<path d="M7 17L17 7M17 7H9M17 7v8" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---- shared <head> + styles ------------------------------------------------
STYLES = open(os.path.join(os.path.dirname(__file__), "_styles.css")).read()

def head(title, desc, path):
    canonical = SITE + "/" + (path + "/" if path else "")
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="keywords" content="Bit Foundry, Gangsta AI, Ask Consensus, AI company, California software company, multi-model AI, AI consensus" />
<meta name="author" content="Bit Foundry" />
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
<link rel="canonical" href="{canonical}" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Bit Foundry" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:locale" content="en_US" />
<meta property="og:image" content="{SITE}/assets/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="Bit Foundry — the company behind Gangsta AI and Ask Consensus" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{SITE}/assets/og-image.png" />
<meta name="theme-color" content="#05070d" />
<link rel="icon" href="/favicon.ico" sizes="any" />
<link rel="icon" type="image/png" href="/favicon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "@id": "{SITE}/#organization",
      "name": "Bit Foundry",
      "legalName": "Bit Foundry",
      "alternateName": "Bit Foundry Labs",
      "url": "{SITE}",
      "logo": "{SITE}/assets/og-image.png",
      "image": "{SITE}/assets/og-image.png",
      "description": "California software company building AI you can trust. Parent company of Gangsta AI and Ask Consensus.",
      "duns": "06-845-0007",
      "foundingDate": "2026",
      "slogan": "Building AI you can actually trust.",
      "knowsAbout": ["Artificial Intelligence", "Large Language Models", "AI model comparison", "AI consensus", "Multi-model AI"],
      "address": {{ "@type": "PostalAddress", "streetAddress": "34189 CA-1 #201", "addressLocality": "Dana Point", "addressRegion": "CA", "postalCode": "92629", "addressCountry": "US" }},
      "areaServed": "US",
      "email": "{EMAIL}",
      "founder": {{ "@type": "Person", "name": "Mark Jenkins" }},
      "identifier": {{ "@type": "PropertyValue", "propertyID": "D-U-N-S", "value": "06-845-0007" }},
      "sameAs": [ "https://gangstaai.org", "https://askconsensus.ai", "https://www.linkedin.com/company/gangsta-ai", "https://www.linkedin.com/company/askconsensus" ]
    }},
    {{
      "@type": "WebSite",
      "@id": "{SITE}/#website",
      "url": "{SITE}",
      "name": "Bit Foundry",
      "publisher": {{ "@id": "{SITE}/#organization" }},
      "inLanguage": "en-US"
    }}
  ]
}}
</script>
<style>
{STYLES}
</style>
</head>
<body>
'''

def nav(active):
    def a(href, label, key):
        cls = ' class="active"' if key == active else ''
        return f'<a href="{href}"{cls}>{label}</a>'
    return f'''
<nav>
  <div class="wrap">
    <a class="brand" href="/"><span class="mark"></span>Bit Foundry</a>
    <div class="navlinks">
      {a("/about/", "About", "about")}
      {a("/products/", "Products", "products")}
      {a("/company/", "Company", "company")}
      {a("/contact/", "Contact", "contact")}
    </div>
  </div>
</nav>
'''

# ---- propedix-style footer -------------------------------------------------
def footer():
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-col foot-brand">
        <div class="brand"><span class="mark"></span>Bit Foundry</div>
        <p class="foot-tag">Building AI you can actually trust. The company behind Gangsta AI and Ask Consensus.</p>
        <div class="foot-social">
          <a href="https://www.linkedin.com/company/gangsta-ai" target="_blank" rel="noopener" aria-label="Gangsta AI on LinkedIn">Gangsta AI {LINK_SVG}</a>
          <a href="https://www.linkedin.com/company/askconsensus" target="_blank" rel="noopener" aria-label="Ask Consensus on LinkedIn">Ask Consensus {LINK_SVG}</a>
        </div>
      </div>
      <div class="foot-col">
        <h4>Quick Links</h4>
        <a href="/">Home</a>
        <a href="/about/">About Us</a>
        <a href="/products/">Products</a>
        <a href="/company/">Company</a>
        <a href="/contact/">Contact</a>
      </div>
      <div class="foot-col">
        <h4>Products</h4>
        <a href="https://askconsensus.ai" target="_blank" rel="noopener">Ask Consensus</a>
        <a href="https://gangstaai.org" target="_blank" rel="noopener">Gangsta AI</a>
      </div>
      <div class="foot-col">
        <h4>Get in Touch</h4>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <p class="foot-addr">34189 CA-1 #201<br>Dana Point, CA 92629</p>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; {YEAR} Bit Foundry</span>
      <span class="sep">|</span>
      <a href="mailto:{ADMIN}">{ADMIN}</a>
      <span class="sep">|</span>
      <a href="/privacy/">Privacy Policy</a>
      <span class="sep">|</span>
      <a href="/terms/">Terms of Use</a>
      <span class="sep">|</span>
      <span class="duns">D-U-N-S 06-845-0007</span>
    </div>
  </div>
</footer>
'''

SCRIPT = '''
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
  (function(){
    if(!window.gsap || !window.ScrollTrigger){ return; }
    document.documentElement.classList.add('gsap-ready');
    gsap.registerPlugin(ScrollTrigger);
    gsap.to('.hero .reveal', { opacity:1, y:0, duration:.8, ease:'power3.out', stagger:.1, delay:.1 });
    gsap.utils.toArray('section').forEach(function(sec){
      var heads = sec.querySelectorAll('.reveal');
      if(heads.length){ gsap.to(heads,{opacity:1,y:0,duration:.7,ease:'power3.out',stagger:.08,scrollTrigger:{trigger:sec,start:'top 85%'}}); }
    });
    ScrollTrigger.refresh();
    setTimeout(function(){
      document.querySelectorAll('.reveal').forEach(function(el){
        if(getComputedStyle(el).opacity === '0'){ gsap.to(el,{opacity:1,y:0,duration:.4}); }
      });
    }, 1200);
  })();
</script>
</body>
</html>
'''

def page(title, desc, path, active, body):
    return head(title, desc, path) + nav(active) + body + footer() + SCRIPT

def write(path, html):
    if path == "":
        out = os.path.join(os.path.dirname(__file__), "index.html")
    else:
        d = os.path.join(os.path.dirname(__file__), path)
        os.makedirs(d, exist_ok=True)
        out = os.path.join(d, "index.html")
    open(out, "w").write(html)
    print("wrote", out.replace(os.path.dirname(__file__) + "/", ""))

# ---- board data ------------------------------------------------------------
BOARD = [
    ("gregg-cunningham", "Gregg Cunningham", "Board Member", "",
     "Attorney. Former two-term Member, Pennsylvania House of Representatives. Founder &amp; Executive Director, Center for Bio-Ethical Reform. Vietnam veteran and retired Air Force Reserve colonel, with roughly a decade in military intelligence.",
     [("Visit", "https://www.abortionno.org"), ("LinkedIn", "https://www.linkedin.com/in/gregg-cunningham-2a916b23")]),
    ("niv-caviar", "Niv Caviar", "Board Member", "shift-right",
     "Life sciences CEO, CFO &amp; CBO across biopharma, biotech, medtech and health services. CEO, ProPedix. Former CEO, Suneva Medical. Former VP of Marketing, Allergan. Harvard MBA.",
     [("LinkedIn", "https://www.linkedin.com/in/niv-edward-caviar")]),
    ("isak-bosman", "Isak Bosman", "Board Member", "shift-right",
     "Co-founder &amp; CTO, Indago Solutions. Chief AI Scientist, SensorOps. Former lecturer in AI and neural networks, UC Irvine.",
     [("LinkedIn", "https://www.linkedin.com/in/isak-bosman")]),
    ("rob-stickler", "Rob Stickler", "Board Member", "",
     "Agentic AI expert specializing in AI-driven marketing and data analysis. Builds autonomous systems for campaign optimization, audience insight, and decision support.",
     [("LinkedIn", "https://www.linkedin.com/in/rob-stickler-1466b931")]),
    ("jeannine-kofford", "Jeannine Kofford, MD", "Investor", "",
     "Physician. Founder &amp; Medical Director, Riviera Laser Studios, Dana Point. National trainer in nonsurgical aesthetics.",
     [("Visit", "https://rivieralaserstudio.net")]),
    ("jeremiah-jenkins", "Jeremiah Jenkins", "Director of QA", "shift-left",
     "AI Trainer, DataAnnotation.tech.", []),
]

def board_card(slug, name, role, shift, bio, links):
    cls = ("avatar " + shift).strip()
    name_q = name.replace(",", "").replace(" ", "+")
    fallback = f"https://ui-avatars.com/api/?name={name_q}&size=256&background=161b28&color=cbd5f5&bold=true"
    if len(links) >= 2:
        linkhtml = '<div class="cardlinks">' + "".join(
            f'<a class="cardlink" href="{u}" target="_blank" rel="nofollow noopener">{l} {LINK_SVG}</a>' for l, u in links) + '</div>'
    elif links:
        l, u = links[0]
        linkhtml = f'<a class="cardlink" href="{u}" target="_blank" rel="nofollow noopener">{l} {LINK_SVG}</a>'
    else:
        linkhtml = ""
    return f'''      <article class="card reveal">
        <img class="{cls}" src="/assets/board/{slug}.jpg" alt="{name}" onerror="this.src='{fallback}'">
        <h3>{name}</h3>
        <div class="role">{role}</div>
        <p class="bio">{bio}</p>
        {linkhtml}
      </article>'''

def board_grid():
    return '<div class="grid">\n' + "\n\n".join(board_card(*b) for b in BOARD) + "\n    </div>"

# ===========================================================================
# PAGE BODIES
# ===========================================================================

HOME = f'''
<header class="hero">
  <div class="wrap">
    <div class="eyebrow reveal">About Bit Foundry</div>
    <h1 class="reveal">Building AI you can actually trust.</h1>
    <div class="lede">
      <p class="reveal">AI is reshaping how people find answers — but a single model, however powerful, is still one opinion that can be confidently wrong. <strong>We think the answer is consensus.</strong></p>
      <p class="reveal">Bit Foundry is a California software company building the tools for this new era: products where the world's most powerful AI models work together — cross-checked, adjudicated, and accountable — so the answer you act on is one you can trust.</p>
      <p class="reveal">We're the company behind <strong>Gangsta AI</strong> and <strong>Ask Consensus</strong>.</p>
    </div>
    <div class="stats reveal">
      <div class="stat"><div class="n">2026</div><div class="l">Founded</div></div>
      <div class="stat"><div class="n">2</div><div class="l">Products shipped</div></div>
      <div class="stat"><div class="n">30+</div><div class="l">AI models integrated</div></div>
      <div class="stat"><div class="n">CA</div><div class="l">Registered S-corp</div></div>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="reveal">
      <div class="kicker">Our thesis</div>
      <h2>An ensemble of elite models beats any single model — every time.</h2>
      <p class="lead">It's true in machine learning, and it's true for the answers you rely on. Rather than betting a decision on one model's blind spot, we run the best models in parallel, surface where they agree and disagree, and let a top model adjudicate a single, sourced verdict. That principle runs through everything we build.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="reveal">
      <div class="kicker">What we build</div>
      <h2>Two front doors, one engine</h2>
      <p class="lead">Explore our products, meet the team, and see the company behind them.</p>
    </div>
    <div class="products reveal">
      <a class="product" href="/products/">
        <div class="ptag">askconsensus.ai</div>
        <h3>Ask Consensus</h3>
        <p>Ask once. The world's most powerful AIs weigh in, then one adjudicates — one cross-checked verdict you can trust.</p>
      </a>
      <a class="product" href="/products/">
        <div class="ptag">gangstaai.org</div>
        <h3>Gangsta AI</h3>
        <p>Compare 30+ leading AI models side by side from a single prompt — pick the best answer for the job.</p>
      </a>
    </div>
    <p class="lead reveal" style="margin-top:28px"><a class="textlink" href="/products/">See how they're different →</a></p>
  </div>
</section>
'''

ABOUT = f'''
<header class="hero hero-sm">
  <div class="wrap">
    <div class="eyebrow reveal">About</div>
    <h1 class="reveal">The company behind the answer.</h1>
    <div class="lede">
      <p class="reveal">Bit Foundry is a California software company (a registered S-corporation, D-U-N-S 06-845-0007) building AI you can actually trust. We believe the most reliable answer doesn't come from one model — it comes from <strong>consensus</strong> among the best.</p>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="reveal">
      <div class="kicker">Our thesis</div>
      <h2>An ensemble of elite models beats any single model — every time.</h2>
      <p class="lead">It's true in machine learning, and it's true for the answers you rely on. Rather than betting a decision on one model's blind spot, we run the best models in parallel, surface where they agree and disagree, and let a top model adjudicate a single, sourced verdict. That principle runs through everything we build.</p>
    </div>
  </div>
</section>

<section id="leadership">
  <div class="wrap">
    <div class="reveal">
      <div class="kicker">Leadership &amp; governance</div>
      <h2>The people behind Bit Foundry</h2>
      <p class="lead">Operators, scientists, physicians, and builders guiding the company.</p>
    </div>
    <div class="founder reveal" id="founder">
      <img src="/assets/mark-jenkins.jpg" alt="Mark Jenkins" onerror="this.src='https://ui-avatars.com/api/?name=Mark+Jenkins&size=256&background=161b28&color=cbd5f5&bold=true'">
      <div class="f-body">
        <h3>Mark Jenkins</h3>
        <div class="role">Founder &amp; CEO</div>
        <p>Senior Software Engineer at Sony PlayStation. Lead Software Engineer at Verizon Networkfleet. Software Engineer at Quest Diagnostics.</p>
        <div class="chips">
          <span class="chip">Sony PlayStation</span>
          <span class="chip">Verizon Networkfleet</span>
          <span class="chip">Quest Diagnostics</span>
        </div>
        <a class="cardlink" href="https://www.linkedin.com/in/markejenkins" target="_blank" rel="nofollow noopener">LinkedIn {LINK_SVG}</a>
      </div>
    </div>
    {board_grid()}
  </div>
</section>
'''

PRODUCTS = f'''
<header class="hero hero-sm">
  <div class="wrap">
    <div class="eyebrow reveal">Products</div>
    <h1 class="reveal">One engine. Two very different front doors.</h1>
    <div class="lede">
      <p class="reveal">Both products run on the same idea — the world's most powerful AI models, together — but they're built for different people and different moments. Here's what makes each one powerful, and how they differ.</p>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="reveal prod-head">
      <div class="kicker">askconsensus.ai</div>
      <h2>Ask Consensus</h2>
      <p class="lead">The research and decision tool. Ask once; get one answer you can trust.</p>
      <a class="btn" href="https://askconsensus.ai" target="_blank" rel="noopener">Visit Ask Consensus →</a>
    </div>
    <div class="prose reveal">
      <p>Why pay for one AI when you can have every top model weigh in — and get a single answer you can trust? Ask Consensus sends your question to the world's leading AI models at once, cross-checks their answers, and delivers one clear verdict. Instead of wondering whether a single chatbot got it right, you see where the best models agree, where they disagree, and the conclusion you can actually act on.</p>
    </div>
    <div class="feat-grid reveal">
      <div class="feat"><h4>Ask once</h4><p>Your question goes to multiple top AI models simultaneously.</p></div>
      <div class="feat"><h4>They weigh in</h4><p>Each leading model answers independently — no single point of failure.</p></div>
      <div class="feat"><h4>You get a verdict</h4><p>Ask Consensus reconciles them into one sourced, confidence-rated answer.</p></div>
      <div class="feat"><h4>See the agreement</h4><p>Know when the models are unanimous — and when they split.</p></div>
    </div>
    <p class="prose reveal"><strong>Who it's for:</strong> researchers, builders, students, and professionals who need a dependable answer, not a coin flip from a single model.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="reveal prod-head">
      <div class="kicker">gangstaai.org</div>
      <h2>Gangsta AI</h2>
      <p class="lead">The side-by-side arena. See 30+ models answer the same prompt — and pick your winner.</p>
      <a class="btn" href="https://gangstaai.org" target="_blank" rel="noopener">Visit Gangsta AI →</a>
    </div>
    <div class="prose reveal">
      <p>Gangsta AI puts 30+ leading AI models head-to-head on a single prompt. Type once and watch the top models — from every major provider — answer side by side, so you can compare their reasoning, tone, and accuracy in real time and choose the best response for the job. It's the fast, visual, playful way to explore what today's AI can do.</p>
    </div>
    <div class="feat-grid reveal">
      <div class="feat"><h4>30+ models, one prompt</h4><p>Every major model answering the same question, side by side.</p></div>
      <div class="feat"><h4>Compare in real time</h4><p>See reasoning, tone, and speed across providers at a glance.</p></div>
      <div class="feat"><h4>Pick the winner</h4><p>Choose the best answer for your task — no vendor lock-in.</p></div>
      <div class="feat"><h4>Beyond text</h4><p>Image and music generation models in the same arena.</p></div>
    </div>
    <p class="prose reveal"><strong>Who it's for:</strong> builders, creators, and the AI-curious who want to explore, compare, and find the right model fast.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="reveal">
      <div class="kicker">The difference</div>
      <h2>Same power, different purpose</h2>
    </div>
    <div class="compare reveal">
      <div class="compare-col">
        <div class="ptag">Ask Consensus</div>
        <ul>
          <li>Ask once → <strong>one cross-checked verdict</strong></li>
          <li>Built for <strong>decisions and research</strong></li>
          <li>Sourced, confidence-rated answer</li>
          <li>Clean, professional, focused</li>
        </ul>
      </div>
      <div class="compare-col">
        <div class="ptag">Gangsta AI</div>
        <ul>
          <li>Ask once → <strong>30+ answers side by side</strong></li>
          <li>Built for <strong>comparison and exploration</strong></li>
          <li>You pick the best response</li>
          <li>Fast, visual, playful</li>
        </ul>
      </div>
    </div>
    <p class="lead reveal" style="margin-top:28px">Two products, one company. Both are built by <strong style="color:var(--text)">Bit Foundry</strong> on the same principle: the best answer comes from the best models, together.</p>
  </div>
</section>
'''

COMPANY = f'''
<header class="hero hero-sm">
  <div class="wrap">
    <div class="eyebrow reveal">Company</div>
    <h1 class="reveal">A real, registered company.</h1>
    <div class="lede">
      <p class="reveal">Bit Foundry is a California S-corporation and the legal entity behind Gangsta AI and Ask Consensus. Here are the details that make us a verifiable business.</p>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="reveal">
      <div class="kicker">Company</div>
      <h2>Registered business</h2>
      <div class="reginfo">
        <div class="regitem">
          <div class="reglabel">Legal entity</div>
          <div class="regvalue">Bit Foundry</div>
          <div class="regsub">California S-corporation</div>
        </div>
        <div class="regitem">
          <div class="reglabel">Registered address</div>
          <div class="regvalue">34189 CA-1 #201</div>
          <div class="regsub">Dana Point, CA 92629, USA</div>
        </div>
        <div class="regitem">
          <div class="reglabel">D-U-N-S number</div>
          <div class="regvalue duns">06-845-0007</div>
          <div class="regsub">Dun &amp; Bradstreet verified</div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

CONTACT = f'''
<header class="hero hero-sm">
  <div class="wrap">
    <div class="eyebrow reveal">Contact</div>
    <h1 class="reveal">Get in touch.</h1>
    <div class="lede">
      <p class="reveal">Questions, press, or partnerships — we'd love to hear from you.</p>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="reveal">
      <div class="kicker">Email</div>
      <h2>Say hello</h2>
      <div class="contactrow">
        <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
      <p class="lead" style="margin-top:20px">Bit Foundry<br>34189 CA-1 #201, Dana Point, CA 92629, USA</p>
      <p class="lead" style="margin-top:14px">Find our products on LinkedIn:
        <a class="textlink" href="https://www.linkedin.com/company/gangsta-ai" target="_blank" rel="noopener">Gangsta AI</a> ·
        <a class="textlink" href="https://www.linkedin.com/company/askconsensus" target="_blank" rel="noopener">Ask Consensus</a>
      </p>
    </div>
  </div>
</section>
'''

def legal_page(kind):
    if kind == "privacy":
        heading = "Privacy Policy"
        intro = "Bit Foundry operates Gangsta AI (gangstaai.org) and Ask Consensus (askconsensus.ai). This policy explains what we collect, how we use it, and your rights."
        sections = [
            ("Who we are", "Bit Foundry, a California S-corporation (D-U-N-S 06-845-0007), 34189 CA-1 #201, Dana Point, CA 92629, USA, is the operator of the Gangsta AI and Ask Consensus services and the data controller for personal data described here. Contact: " + EMAIL + "."),
            ("Information we collect", "Account details you provide (such as email and sign-in method); your queries and the content you submit; usage data (features used, subscription tier, free-tier usage counts); device and session information; and payment status (card details are handled by our payment processor, not stored by us)."),
            ("How we use it", "To provide and operate the services; maintain your query history and account preferences; enforce usage limits based on your subscription tier; process subscription payments; monitor for abuse, fraud, and security threats; and comply with legal obligations."),
            ("Service providers", "We rely on reputable third-party processors to run the services, which may include cloud database and hosting providers, a payment processor (Stripe), email delivery, and AI model routing providers. Each processes data only to deliver its function."),
            ("Cookies and local storage", "We use cookies and local storage to maintain your login session, remember your preferred settings, track free-tier usage on anonymous visits, and recall your most recent sign-in method for convenience."),
            ("Your rights", "Depending on where you live, you may have the right to access the personal data we hold about you, correct inaccurate data, request deletion of your account and data, restrict or object to certain processing, and lodge a complaint with your local data protection authority. To exercise any of these, email " + EMAIL + "."),
            ("Data retention", "We retain personal data for as long as your account is active or as needed to provide the services, and thereafter only as required to comply with legal obligations, resolve disputes, and enforce agreements."),
            ("Children", "The services are not directed to children under 13, and we do not knowingly collect personal data from them."),
            ("Changes", "We may update this policy from time to time. Material changes will be reflected by updating the date below."),
        ]
    else:
        heading = "Terms of Use"
        intro = "These Terms govern your use of the Gangsta AI and Ask Consensus services, operated by Bit Foundry. By using the services you agree to these Terms."
        sections = [
            ("Acceptance", "By accessing or using the services you agree to be bound by these Terms. If you do not agree, do not use the services."),
            ("The service", "The services provide AI-powered responses by querying and comparing third-party AI models. Output is generated by AI and may be inaccurate, incomplete, or out of date. It is provided for informational purposes only."),
            ("No professional advice", "The services do not provide legal, medical or health, financial or investment, tax, or psychological or mental-health advice. Do not rely on output as a substitute for a qualified professional."),
            ("Acceptable use", "You agree not to interfere with or disrupt the service or its infrastructure, misrepresent yourself or impersonate any person or entity, use the service unlawfully, or attempt to circumvent usage limits or security controls."),
            ("Accounts and subscriptions", "You are responsible for activity under your account and for keeping your credentials secure. Paid subscriptions are billed through our payment processor and are subject to the plan you select."),
            ("Intellectual property", "The services, including their software and branding, are owned by Bit Foundry. These Terms grant you a limited, non-exclusive, non-transferable license to use the services for their intended purpose."),
            ("Disclaimers", "The services are provided “as is” and “as available,” without warranties of any kind, to the fullest extent permitted by law."),
            ("Limitation of liability", "To the fullest extent permitted by law, Bit Foundry will not be liable for indirect, incidental, special, consequential, or punitive damages arising from your use of the services."),
            ("Indemnification", "You agree to indemnify Bit Foundry against claims arising from your use of or access to the service, your violation of these Terms, any content you submit, or your violation of any applicable law."),
            ("Governing law &amp; disputes", "These Terms are governed by the laws of the State of California. The parties will first seek informal resolution; unresolved disputes are subject to binding arbitration on an individual basis, and class actions are waived, except where prohibited by law."),
            ("General", "If any provision is held unenforceable, the remainder stays in effect. Our failure to enforce a provision is not a waiver. These Terms are the entire agreement between you and Bit Foundry regarding the services."),
            ("Changes", "We may update these Terms from time to time; continued use after changes means you accept them."),
        ]
    body = f'''
<header class="hero hero-sm">
  <div class="wrap">
    <div class="eyebrow reveal">Legal</div>
    <h1 class="reveal">{heading}</h1>
    <div class="lede"><p class="reveal">{intro}</p></div>
  </div>
</header>

<section>
  <div class="wrap legal">
'''
    for i, (h, t) in enumerate(sections):
        body += f'''    <div class="reveal legal-sec"><h3>{i+1}. {h}</h3><p>{t}</p></div>\n'''
    body += f'''    <p class="legal-updated reveal">Last updated: October 10, {YEAR}. Questions? <a class="textlink" href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</section>
'''
    return body

# ===========================================================================
PAGES = [
    ("", "Bit Foundry — The company behind Gangsta AI and Ask Consensus",
     "Bit Foundry is a California software company building AI you can trust — the parent company of Gangsta AI and Ask Consensus. D-U-N-S 06-845-0007.", "home", HOME),
    ("about", "About — Bit Foundry",
     "Bit Foundry is a California software company building AI you can trust. Meet the team and the thesis behind Gangsta AI and Ask Consensus.", "about", ABOUT),
    ("products", "Products — Gangsta AI and Ask Consensus | Bit Foundry",
     "How Gangsta AI and Ask Consensus are powerful, unique, and different — two AI products from Bit Foundry built on the world's most powerful models.", "products", PRODUCTS),
    ("company", "Company — Bit Foundry",
     "Bit Foundry is a registered California S-corporation (D-U-N-S 06-845-0007), the company behind Gangsta AI and Ask Consensus.", "company", COMPANY),
    ("contact", "Contact — Bit Foundry",
     "Get in touch with Bit Foundry, the company behind Gangsta AI and Ask Consensus.", "contact", CONTACT),
    ("privacy", "Privacy Policy — Bit Foundry",
     "Privacy Policy for Bit Foundry, operator of Gangsta AI and Ask Consensus.", None, legal_page("privacy")),
    ("terms", "Terms of Use — Bit Foundry",
     "Terms of Use for Bit Foundry, operator of Gangsta AI and Ask Consensus.", None, legal_page("terms")),
]

for path, title, desc, active, body in PAGES:
    write(path, page(title, desc, path, active, body))

print("done — generated", len(PAGES), "pages")
