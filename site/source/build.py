#!/usr/bin/env python3
"""Generate a file:// compatible multi-page Mosalam prototype. No backend integrations."""
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parent.parent
H=html.escape
# Route registries. Capability lists are educational examples, not contractual product promises.
NAV=[
 ('Hosting','hosting',[('Hosting overview','hosting','Find the right home for your site'),('cPanel hosting','hosting/cpanel','An approachable way to manage a site'),('WordPress hosting','hosting/wordpress','WordPress workload options'),('Reseller hosting','hosting/reseller','Multiple customer websites')]),
 ('Servers','servers',[('Compare servers','servers','VPS, VDS and dedicated'),('VPS servers','servers/vps','Flexible virtual compute'),('VDS servers','servers/vds','Define reserved resource needs'),('Dedicated servers','servers/dedicated','Single-tenant compute options')]),
 ('Cloud & infrastructure','cloud',[('Cloud overview','cloud','From an app to an environment'),('Managed cloud','cloud/managed','Scope operational responsibilities'),('Backup & recovery','cloud/backup','Plan resilience and restores'),('Custom architecture','solutions/custom-infrastructure','Get help planning a stack')]),
 ('Solutions','solutions',[('All solutions','solutions','Find a fit for your team'),('Software houses','solutions/software-houses','Infrastructure for development teams'),('Agencies','solutions/agencies','Multiple websites and clients'),('Businesses','solutions/businesses','Operational reliability needs'),('Migration','solutions/migration','Move with a clear plan')]),
 ('Resources','support',[('Support hub','support','Find answers and next steps'),('Documentation','docs','Technical guidance and checklists'),('Service status','status','Where to verify availability'),('About Mosalam','company/about','Brand and approach')]),
]
R={
 '':('Home','Build without limits'),
 'hosting':('Hosting','Hosting that fits your website'),
 'hosting/cpanel':('cPanel hosting','A simpler place to manage your website'),
 'hosting/wordpress':('WordPress hosting','A home for your WordPress site'),
 'hosting/reseller':('Reseller hosting','One workflow for multiple client sites'),
 'servers':('Servers','Compute for the way you build'),
 'servers/vps':('VPS servers','Your project. Your server environment.'),
 'servers/vds':('VDS servers','Plan for dedicated resource needs'),
 'servers/dedicated':('Dedicated servers','Compute tailored to demanding workloads'),
 'cloud':('Cloud & infrastructure','Infrastructure that grows with your ideas'),
 'cloud/managed':('Managed cloud','Focus on your application, with a clear support model'),
 'cloud/backup':('Backup & recovery','Prepare for recovery before you need it'),
 'solutions':('Solutions','Start with the outcome, not the server'),
 'solutions/software-houses':('For software houses','Infrastructure that fits your software'),
 'solutions/agencies':('For agencies','A clearer way to manage client infrastructure'),
 'solutions/businesses':('For businesses','Keep critical websites and services on track'),
 'solutions/custom-infrastructure':('Custom infrastructure','Design the right architecture together'),
 'solutions/migration':('Migration','Move your workload with a plan'),
 'domains':('Domains','A name for what you are building'),
 'pricing':('Plans & pricing','Compare what matters before you commit'),
 'contact/sales':('Contact sales','Tell us what you are building'),
 'support':('Support','Find the right kind of help'),
 'docs':('Documentation','Useful guides for clearer decisions'),
 'status':('Service status','Know where to find service updates'),
 'company/about':('About Mosalam','Technology built around clarity'),
 'company/contact':('Contact','Get in touch with the right team'),
 'portal/login':('Client portal','A place for your infrastructure'),
 'portal/overview':('Overview','Your account at a glance'),
 'portal/services':('Services','Your services'),
 'portal/billing':('Billing','Billing and renewals'),
 'portal/tickets':('Support tickets','Keep conversations in one place'),
 'portal/domains':('Domains','Your domain portfolio'),
 'portal/servers':('Servers','Compute management'),
 'portal/team':('Team','People and permissions'),
 'design-system':('Design system','One visual language, many interfaces'),
 'legal/terms':('Terms','Terms of service'),
 'legal/privacy':('Privacy','Privacy policy'),
 'legal/sla':('SLA','Service-level agreement'),
}
INTRO={
 'hosting':'From a first website to a growing portfolio, start with the level of control and support your project actually needs.',
 'hosting/cpanel':'A familiar control panel can make files, domains, databases and email easier to manage. Explore the package details and responsibilities before ordering.',
 'hosting/wordpress':'Explore website hosting for WordPress, understand setup choices and clarify what is managed versus self-managed.',
 'hosting/reseller':'For agencies and independent providers who need to organize client websites and account responsibilities.',
 'servers':'Move beyond shared hosting when your application needs operating-system control, customized services or dedicated resource planning.',
 'servers/vps':'A virtual private server gives developers more control over operating systems, software and deployment environments.',
 'servers/vds':'Use VDS comparisons to discuss resource allocation and isolation. Exact guaranteed specifications depend on the published plan.',
 'servers/dedicated':'For larger or specialized workloads where a whole physical machine may be the appropriate architecture.',
 'cloud':'Think in systems: computing, data, connectivity, recoverability and people who know who is responsible.',
 'cloud/managed':'Managed infrastructure is only useful when responsibilities are explicit. Define monitoring, patching, backup and incident support before you buy.',
 'cloud/backup':'Set practical recovery objectives and confirm backup coverage, retention and restore tests for each workload.',
 'solutions':'Whether you are a solo founder, an agency or an engineering team, find your starting point without translating your needs into infrastructure jargon first.',
 'solutions/software-houses':'Plan environments for web apps, APIs, databases, workers and internal services. Keep production, staging and development needs visible.',
 'solutions/agencies':'Organize hosting decisions around websites, clients, maintenance and support responsibilities.',
 'solutions/businesses':'A reliable deployment starts with understanding which services are important, how they are supported and what happens when things fail.',
 'solutions/custom-infrastructure':'Describe the application and constraints. We will use a structured brief to discuss the infrastructure that could support it.',
 'solutions/migration':'Every migration has dependencies. Map your current environment, cutover requirements and rollback options before moving.',
 'domains':'Discover a name, learn about DNS and renewal considerations, and verify availability through a live registration system.',
 'pricing':'Clear specifications, transparent renewal terms and informed choices matter more than a flashy starting price.',
 'contact/sales':'Share the essentials of your project and prepare a short, readable infrastructure brief.',
 'support':'Find guidance, clarify service responsibilities and locate the appropriate contact channel.',
 'docs':'Practical checklists for website owners, developers, agencies and teams planning infrastructure.',
 'status':'This prototype does not provide live availability or incident information; connect an official verified source before launch.',
 'company/about':'Mosalam connects website hosting and software infrastructure through a calm, precise experience.',
 'company/contact':'Different questions deserve different routes. Choose product guidance, technical help or account assistance.',
}
ICON={'hosting':'web-hosting','hosting/cpanel':'cpanel','hosting/wordpress':'web-hosting','hosting/reseller':'reseller','servers':'vps-hosting','servers/vps':'vps-hosting','servers/vds':'vds','servers/dedicated':'dedicated','cloud':'managed-cloud','cloud/managed':'managed-cloud','cloud/backup':'backups','domains':'domains','solutions':'in-house','solutions/software-houses':'api','solutions/agencies':'reseller','solutions/businesses':'security','solutions/custom-infrastructure':'networking','solutions/migration':'migration','support':'support','docs':'api','status':'monitoring','pricing':'affordable','contact/sales':'support','company/about':'in-house','company/contact':'support'}
ART={'hosting':'hero-servers','hosting/cpanel':'hero-servers','hosting/wordpress':'hero-servers','hosting/reseller':'infrastructure-network-large','servers':'hero-servers','servers/vps':'hero-servers','servers/vds':'server-stack-large','servers/dedicated':'server-stack-large','cloud':'managed-cloud-large','cloud/managed':'managed-cloud-large','cloud/backup':'infrastructure-network-large','solutions':'infrastructure-network-large','solutions/software-houses':'infrastructure-network-large','solutions/agencies':'managed-cloud-large','solutions/businesses':'infrastructure-network-large','solutions/custom-infrastructure':'infrastructure-network-large','solutions/migration':'server-stack-large','domains':'managed-cloud-large','support':'managed-cloud-large'}
FEATURES={
 'hosting':[('cPanel','An approachable dashboard to work with site files, databases and domains.','hosting/cpanel'),('WordPress','A focused path for WordPress websites and content teams.','hosting/wordpress'),('Reseller','Organize multiple client accounts with clear responsibility boundaries.','hosting/reseller')],
 'servers':[('VPS','Server-level flexibility for apps and development environments.','servers/vps'),('VDS','Explore resource reservations and isolation requirements.','servers/vds'),('Dedicated','Discuss whole-server needs and physical resources.','servers/dedicated')],
 'cloud':[('Managed cloud','Define the operational support your team actually needs.','cloud/managed'),('Backup and recovery','Plan recovery before an outage or accidental change.','cloud/backup'),('Architecture consultation','Clarify how components communicate and are protected.','solutions/custom-infrastructure')],
 'solutions':[('Software houses','Production and staging environments for applications and APIs.','solutions/software-houses'),('Agencies','Maintain a growing set of client websites.','solutions/agencies'),('Migration','Move infrastructure with a documented path.','solutions/migration')],
}
# 3 issue-specific feature rows for all detail pages
BENEFITS={
 'hosting/cpanel':[('Manage the essentials','Work with your domains, website files and databases through a familiar interface.'),('Understand the scope','Check the hosting account limits, licensing and email arrangements.'),('Plan your next step','Know when shared hosting is enough and when VPS control will be useful.')],
 'hosting/wordpress':[('Launch a WordPress site','Start with compatible hosting requirements and a clear setup path.'),('Prepare for updates','Know who owns plugin updates, site backups and troubleshooting.'),('Move an existing site','Document the source server, database and DNS cutover before migration.')],
 'hosting/reseller':[('Organize websites','Plan resource allocation and management for multiple clients.'),('Clarify WHM vs cPanel','Keep reseller administration distinct from end-user site management.'),('Support clients clearly','Agree on who handles accounts, incidents and upgrades.')],
 'servers/vps':[('Operating system control','Consider the OS, access level and software stack needed for your application.'),('Choose by workload','Size compute, RAM, storage and networking against actual requirements.'),('Define management','Know where self-managed responsibility ends and optional support starts.')],
 'servers/vds':[('Discuss guaranteed allocation','Ask how CPU, RAM and disk I/O are isolated and what is contractually reserved.'),('Build around load','Plan CPU-intensive or predictable workloads with verified specs.'),('Compare alternatives','Understand whether VPS or dedicated is a better fit.')],
 'servers/dedicated':[('Physical resource planning','Match CPU, RAM, disks and bandwidth to a real workload.'),('Operational ownership','Clarify OS administration, hardware incident process and backups.'),('Architecture assistance','Assess whether a single machine, multiple nodes or cloud topology is best.')],
 'cloud/managed':[('Write down responsibilities','Define patching, incident response, monitoring and backup obligations.'),('Build an environment','Model connectivity between application, data and other components.'),('Protect continuity','Review recovery needs and escalation paths with the team.')],
 'cloud/backup':[('Define recovery objectives','Discuss acceptable data loss (RPO) and time to restore (RTO).'),('Check coverage','Identify data, databases, volumes and configurations that need protection.'),('Practice restores','Determine how backups are verified and who starts recovery.')],
 'solutions/software-houses':[('Separate environments','Account for development, staging and production boundaries.'),('See the whole stack','Map frontend, application servers, background workers and data.'),('Make ownership explicit','Choose who operates the OS, backups, deployments and security controls.')],
 'solutions/agencies':[('Keep projects organized','Consider client separation and consistent operational patterns.'),('Make handoffs easier','Document domain, site and infrastructure ownership.'),('Plan growth','Choose between reseller hosting and server-level control as needs evolve.')],
 'solutions/businesses':[('Start with criticality','List what must keep working and the impact if it stops.'),('Understand recovery','Discuss backups, incident notification and restore procedures.'),('Know who to call','Provide a clear operational contact and escalation process.')],
 'solutions/custom-infrastructure':[('Map your workload','Describe services, data stores, capacity and deployment patterns.'),('Decide ownership','Evaluate managed and self-managed responsibilities.'),('Prepare a brief','Bring environment and compliance needs into a useful conversation.')],
 'solutions/migration':[('Inventory dependencies','List sites, databases, mail, DNS and external integrations.'),('Plan cutover','Choose a sequence, test method and rollback approach.'),('Confirm responsibilities','Agree who changes DNS, moves data and validates the result.')],
}
FAQS={
 'hosting/cpanel':[('Is cPanel the same as WHM?','No. cPanel manages an individual hosting account or website. WHM provides server or reseller account administration, if that service is offered.'),('Can I move an existing website?','Migration feasibility, scope and fees need confirmation for the specific website and plan.'),('Are backups included?','Backup scope, frequency, retention and restoration terms must be checked on the chosen service.')],
 'servers/vps':[('Do I need VPS or cPanel hosting?','Choose cPanel-style hosting for an easier website setup. Consider VPS when you need OS access, custom runtime services or additional control.'),('Can I choose an operating system?','Supported operating systems depend on the actual available server inventory and management model.'),('Who maintains my server?','That depends on whether the service is self-managed or contracted as managed. Confirm patching, security and backup responsibilities.')],
 'servers/vds':[('What is the difference between VPS and VDS?','Naming varies by provider. Compare the contractually allocated CPU, memory, storage, virtualization, isolation and service guarantees rather than the label alone.'),('Are resources guaranteed?','Exact reservations and contention policy must be stated in an approved plan specification.'),('Which is better for a database?','Compare workload profile, storage latency, recovery objectives and management responsibilities before deciding.')],
 'cloud/managed':[('Does managed mean everything is included?','No. Managed services vary. The written scope must clarify monitoring, patching, application support, incident response and backup responsibility.'),('Can I request a custom architecture?','You can create a requirements brief here; a real consultation requires connecting a verified sales channel.'),('What about backups and security?','These are shared responsibilities. Define their scope for your service before production use.')],
}
DEFAULT_FAQ=[('How do I choose the right product?','Start from the workload, then compare the control you need, expected resource usage, team skills and the support model.'),('Can I grow to a different solution later?','A migration path depends on the applications, data and service specifications. Discuss it before ordering.'),('Where are prices and terms?','This prototype does not show unverified prices. Confirm the final configuration, setup cost, renewal and service terms through the official sales process.')]

def depth(route):return len([x for x in route.split('/') if x])
def prefix(route):return '../'*depth(route)
def url(route,from_route):return prefix(from_route)+(route+'/index.html' if route else 'index.html')
def icon(name,route):return prefix(route)+'assets/icons/'+name+'.svg'
def art(name,route):return prefix(route)+'assets/illustrations/'+name+'.svg'
def btn(label,to,route,style='primary',arrow=True):
 return f'<a class="button {style}" href="{url(to,route)}">{H(label)}'+(' <span aria-hidden="true">↗</span>' if arrow else '')+'</a>'
def nav(route):
 groups=''.join(f'''<div class="nav-item"><button class="nav-trigger" type="button" aria-expanded="false" aria-controls="fly-{i}">{H(title)} <span class="chev" aria-hidden="true">⌄</span></button><div class="flyout" id="fly-{i}"><a href="{url(base,route)}">View all {H(title)} <small>Browse this section</small></a>{''.join(f'<a href="{url(slug,route)}">{H(label)}<small>{H(desc)}</small></a>' for label,slug,desc in items)}</div></div>''' for i,(title,base,items) in enumerate(NAV))
 return f'''<header class="site-header"><div class="container"><nav class="nav-shell" aria-label="Primary navigation"><a class="brand" href="{url('',route)}" aria-label="Mosalam home"><img src="{prefix(route)}assets/logo.svg" alt="Mosalam"></a><div class="nav-center" id="nav-links">{groups}<a class="nav-direct" href="{url('domains',route)}">Domains</a></div><div class="nav-end"><a class="muted-link" href="{url('portal/login',route)}">Client portal</a>{btn('Get started','hosting',route,'primary small',False)}<button id="menu-toggle" class="menu-toggle" aria-label="Open navigation" aria-controls="nav-links" aria-expanded="false"><span></span><span></span><span></span></button></div></nav></div></header>'''
def footer(route):
 gs=[('Products',[('cPanel Hosting','hosting/cpanel'),('VPS Servers','servers/vps'),('VDS Servers','servers/vds'),('Domains','domains')]),('Infrastructure',[('Cloud solutions','cloud'),('Managed cloud','cloud/managed'),('Custom infrastructure','solutions/custom-infrastructure'),('For software houses','solutions/software-houses')]),('Resources',[('Support','support'),('Documentation','docs'),('Service status','status'),('Contact sales','contact/sales')]),('Company',[('About Mosalam','company/about'),('Contact','company/contact'),('Terms','legal/terms'),('Privacy','legal/privacy'),('Service terms / SLA','legal/sla')])]
 col=''.join(f'<div><h3>{H(k)}</h3>'+''.join(f'<a class="footlink" href="{url(r,route)}">{H(t)}</a>' for t,r in links)+'</div>' for k,links in gs)
 return f'''<footer class="footer"><div class="container"><div class="footer-top"><div class="footer-brand"><a href="{url('',route)}"><img src="{prefix(route)}assets/logo.svg" alt="Mosalam"></a><p>From your first website to infrastructure for your next application. Built around clarity and control.</p><a class="footlink" href="{url('contact/sales',route)}">Talk to our team ↗</a></div>{col}</div><div class="footer-end"><span>© 2026 Mosalam · Website implementation prototype</span><span>English · Arabic interface requires full localization review</span><a href="#top">Back to top ↑</a></div></div></footer>'''
def render(route,content,description=''):
 name,title=R[route]
 isportal=route.startswith('portal/')
 warning='<div class="mock-band" role="status">DESIGN PROTOTYPE: Prices, availability, service features, operational data and account information are not connected to live Mosalam systems.</div>' if isportal else ''
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><meta name="theme-color" content="#033AA7"><meta name="description" content="{H(description or INTRO.get(route,'Mosalam hosting, cloud and infrastructure solutions.'))}"><title>{H(name)} | Mosalam</title><link rel="icon" href="{prefix(route)}assets/logo.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix(route)}style.css"></head><body id="top" data-route="{H(route)}" data-root="{prefix(route)}"><a class="skip" href="#main">Skip to main content</a>{nav(route)}{warning}<main id="main">{content}</main>{footer(route)}<script src="{prefix(route)}app.js" defer></script></body></html>'''
def hero(route,eyebrow=None,title=None,desc=None,artname=None,compact=True,buttons=None):
 desc=desc or INTRO.get(route,'')
 title=title or R[route][1]
 crumbs=f'<div class="crumbs"><a href="{url("",route)}">Home</a><span>/</span><span>{H(R[route][0])}</span></div>' if route else ''
 ctas=buttons if buttons is not None else (btn('Explore solutions','solutions',route,'white')+' <a class="text-link light" href="'+url('contact/sales',route)+'">Talk infrastructure ↗</a>')
 pict=artname or ART.get(route,'hero-servers')
 return f'''<section class="hero {'compact' if compact else ''}"><div class="container hero-inner"><div class="hero-copy">{crumbs}<div class="eyebrow">{H(eyebrow or 'MOSALAM · HOSTING & CLOUD')}</div><h1>{H(title)}</h1><p class="lead">{H(desc)}</p><div class="hero-buttons">{ctas}</div>{'' if compact else '<div class="hero-notes"><span>Clearer hosting choices</span><span>From sites to infrastructure</span><span>Support-led decisions</span></div>'}</div><div class="hero-aside"><img class="hero-art" src="{art(pict,route)}" alt="Geometric illustration of '+H(pict.replace('-',' '))+'" width="720" height="560"></div></div></section>'''
def section_title(kicker,head,sub=''):return f'<div class="section-title"><p class="kicker">{H(kicker)}</p><h2>{H(head)}</h2>{f"<p>{H(sub)}</p>" if sub else ""}</div>'
def cards(items,route,kind='normal',columns=3):
 items=list(items)
 out=[]
 for x in items:
  if len(x)==3:
   t,p,r=x; i=ICON.get(r,'networking')
  else: t,p,r,i=x
  out.append(f'''<article class="card"><img class="icon-geom" src="{icon(i,route)}" alt="" width="72" height="72" loading="lazy"><h3>{H(t)}</h3><p>{H(p)}</p>{'<a class="card-link" href="'+url(r,route)+'">Explore '+H(t)+' <span aria-hidden="true">→</span></a>' if r else ''}</article>''')
 return '<div class="grid cols-'+str(columns)+'">'+''.join(out)+'</div>'
def faq(route,questions=None):
 qs=questions or FAQS.get(route,DEFAULT_FAQ)
 out=''.join(f'<details><summary>{H(q)}</summary><p>{H(a)}</p></details>' for q,a in qs)
 return f'<section class="section soft"><div class="container">{section_title("Questions answered","The details, without the guesswork","Understand responsibilities and constraints before you decide.")}<div class="faq-list">{out}</div></div></section>'
def cta(route):
 return f'<section class="dark-banner"><div class="container content"><div><p class="kicker">NEXT STEP</p><h2>Tell us what you are building.</h2><p>Start with a small hosting plan or prepare an infrastructure brief for a more complex workload.</p></div>{btn("Discuss my project","contact/sales",route,"white")}</div></section>'
def feature_specs(route):
 vals=BENEFITS.get(route,[('Choose the right starting point','Understand what you need to run today.'),('Make ownership visible','Clarify who maintains each layer of the service.'),('Plan for what comes next','Think about support and recovery before you grow.')])
 return '<div class="info-list">'+''.join(f'<div class="info-row"><span class="number">{n:02}</span><div><strong>{H(t)}</strong><p>{H(p)}</p></div></div>' for n,(t,p) in enumerate(vals,1))+'</div>'
def compare_table(route):
 return f'''<div class="table-scroll"><table class="compare"><thead><tr><th>Consideration</th><th>What to clarify</th><th>Where to go</th></tr></thead><tbody><tr><td>Resource specifications</td><td>CPU model/share, RAM, storage type, bandwidth and location, where applicable.</td><td><a class="text-link" href="{url('contact/sales',route)}">Request details ↗</a></td></tr><tr><td>Management model</td><td>Who handles OS updates, security, monitoring, application incidents and restoration?</td><td><a class="text-link" href="{url('cloud/managed',route)}">Read management scope ↗</a></td></tr><tr><td>Commercial terms</td><td>Recurring price, renewal price, billing cycle, licensing, setup and cancellation policies.</td><td><a class="text-link" href="{url('pricing',route)}">Pricing guidance ↗</a></td></tr><tr><td>Recovery & support</td><td>Backup coverage, restore process, support channels and response targets, if contractually offered.</td><td><a class="text-link" href="{url('support',route)}">Support options ↗</a></td></tr></tbody></table></div>'''
def category(route):
 if route=='hosting': title='A home for every kind of website'; sub='Start simple. Understand the tradeoffs before you outgrow the first plan.'
 elif route=='servers': title='Find the right kind of server'; sub='Compare control, resource isolation and operational responsibility without marketing jargon.'
 elif route=='cloud': title='Build the whole environment'; sub='Think about infrastructure as connected layers, not a collection of unrelated products.'
 else: title='What are you building?'; sub='Discover a route that matches your team and goals.'
 body=hero(route,compact=False,buttons=btn('See options',route,route,'white')+f'<a class="text-link light" href="{url("contact/sales",route)}">Ask a question ↗</a>')
 body+=f'<section class="section soft"><div class="container">{section_title("Explore",title,sub)}{cards(FEATURES[route],route)}</div></section>'
 body+=f'''<section class="section"><div class="container feature-row"><div class="feature-copy"><p class="kicker">YOUR DECISION</p><h2>Choose for the work, not the label.</h2><p>Different workloads require different levels of access, performance, backup and operational help. Describe your real needs and compare their implications before committing.</p>{feature_specs(route)}<p>{btn('Describe my requirements','contact/sales',route,'outline')}</p></div><div class="feature-media"><img src="{art('infrastructure-network-large',route)}" alt="Connected infrastructure components" loading="lazy"></div></div></section>'''
 body+=f'<section class="section pale"><div class="container">{section_title("Before you order","What to compare")}'+compare_table(route)+'</div></section>'
 body+=faq(route)+cta(route)
 return body

def detail(route):
 if route.startswith('hosting/'):
  sibling=[('cPanel hosting','hosting/cpanel'),('WordPress hosting','hosting/wordpress'),('Reseller hosting','hosting/reseller')]
 elif route.startswith('servers/'):
  sibling=[('VPS servers','servers/vps'),('VDS servers','servers/vds'),('Dedicated servers','servers/dedicated')]
 elif route.startswith('cloud/'):
  sibling=[('Managed cloud','cloud/managed'),('Backup & recovery','cloud/backup'),('Custom infrastructure','solutions/custom-infrastructure')]
 else:
  sibling=[('Software houses','solutions/software-houses'),('Agencies','solutions/agencies'),('Custom infrastructure','solutions/custom-infrastructure')]
 b=hero(route,buttons=btn('Discuss this service','contact/sales',route,'white')+f'<a class="text-link light" href="{url("pricing",route)}">Pricing guidance ↗</a>')
 b+=f'<section class="section"><div class="container">{section_title("A clear starting point","What this approach helps you do","Each service decision should come with a clear scope, not simply a feature list.")}'+cards([(t,p,None,ICON.get(route,'networking')) for t,p in BENEFITS.get(route,[])],route,columns=3)+'</div></section>'
 b+=f'''<section class="section pale"><div class="container feature-row"><div class="feature-media"><img src="{art(ART.get(route,'infrastructure-network-large'),route)}" loading="lazy" alt="Illustration of infrastructure"></div><div class="feature-copy"><p class="kicker">IMPLEMENTATION</p><h2>Know what you're responsible for.</h2><p>The infrastructure itself is only one part of a reliable service. Understand what is included, what is operated by the customer and what must be separately agreed.</p>{feature_specs(route)}</div></div></section>'''
 b+=f'<section class="section"><div class="container">{section_title("Specifications & terms","Compare the details before buying","The fields below are a checklist. They are not claims of currently available Mosalam product inventory.")}'+compare_table(route)+'</div></section>'
 b+=f'<section class="section soft"><div class="container">{section_title("Related paths","Other ways to build")}'+cards([(n,"Explore how this option compares for your workload.",r) for n,r in sibling if r!=route],route,columns=2)+'</div></section>'
 b+=faq(route)+cta(route)
 return b

def home(route=''):
 b=hero(route,eyebrow='PREMIUM HOSTING · CLOUD INFRASTRUCTURE',title='Build Without Limits',desc='Hosting for your first website. Infrastructure for your next big project. One clear place to find the right starting point.',artname='hero-servers',compact=False,buttons=btn('Explore hosting','hosting',route,'white')+f'<a class="text-link light" href="{url("solutions/software-houses",route)}">For software teams ↗</a>')
 b+=f'''<section class="section soft"><div class="container">{section_title('FIND YOUR FIT','What are you building?','Start with your goal. We will point you toward the right kind of service without making you decode infrastructure terminology.')}<div class="pill-tabs" role="tablist" aria-label="Select your project type"><button type="button" role="tab" id="choice-site" aria-controls="fit-result" aria-selected="true" data-fit="site">A website</button><button type="button" role="tab" id="choice-app" aria-controls="fit-result" aria-selected="false" data-fit="app">An app or API</button><button type="button" role="tab" id="choice-agency" aria-controls="fit-result" aria-selected="false" data-fit="agency">Client websites</button><button type="button" role="tab" id="choice-team" aria-controls="fit-result" aria-selected="false" data-fit="team">Team infrastructure</button></div><div class="chooser-result" id="fit-result" role="tabpanel" aria-labelledby="choice-site"><div><h3 id="fit-title">Start with website hosting</h3><p id="fit-desc">Explore familiar cPanel-style website management, then compare plans and account responsibilities.</p></div><a class="button primary" id="fit-link" href="{url('hosting/cpanel',route)}">Explore the fit ↗</a></div></div></section>'''
 b+=f'<section class="section"><div class="container">{section_title("OUR SERVICES","Everything you need to grow online","From simple hosting to custom infrastructure, follow a clear path as your needs change.")}'+cards([('cPanel Hosting','A straightforward place to manage your site.','hosting/cpanel'),('VPS & VDS','More control for applications and services.','servers'),('Cloud infrastructure','A connected stack for growing teams.','cloud'),('Domains','Your name, DNS and registration journey.','domains')],route,columns=4)+'</div></section>'
 b+=f'''<section class="section pale"><div class="container feature-row"><div class="feature-copy"><p class="kicker">FOR SOFTWARE TEAMS</p><h2>Infrastructure for everything behind the screen.</h2><p>Plan where your apps run, where your data lives and how services connect. Consider deployment environments, recovery needs and who maintains each layer.</p><div><span class="solution-chip">APIs & web apps</span><span class="solution-chip">Development & staging</span><span class="solution-chip">Backup planning</span><span class="solution-chip">Operational scope</span></div><p style="margin-top:26px">{btn('Explore team solutions','solutions/software-houses',route)}</p></div><div class="feature-media"><img src="{art('infrastructure-network-large',route)}" alt="Connected application infrastructure" loading="lazy"></div></div></section>'''
 b+=f'''<section class="dark-panel"><div class="container"><div class="grid cols-2" style="align-items:center"><div><p class="kicker">WHY MOSALAM</p><h2 class="section-heading">Built on principles that last.</h2><p style="font-size:15px;line-height:1.8;color:#cbdffd">Clear choices, considered infrastructure and support that starts with understanding the workload. A visual system inspired by order and geometric repetition.</p></div><div class="grid cols-2"><div><h3 style="margin:0 0 8px;font:800 19px var(--heading)">Simple starts</h3><p style="font-size:13px;color:#c5d9f5;line-height:1.6">Get online without unnecessary complexity.</p></div><div><h3 style="margin:0 0 8px;font:800 19px var(--heading)">Room to grow</h3><p style="font-size:13px;color:#c5d9f5;line-height:1.6">Explore more control when your requirements evolve.</p></div><div><h3 style="margin:0 0 8px;font:800 19px var(--heading)">Clear ownership</h3><p style="font-size:13px;color:#c5d9f5;line-height:1.6">Understand support and operational boundaries.</p></div><div><h3 style="margin:0 0 8px;font:800 19px var(--heading)">Precise design</h3><p style="font-size:13px;color:#c5d9f5;line-height:1.6">Modern hosting with a coherent visual identity.</p></div></div></div></div></section>'''
 b+=f'''<section class="section"><div class="container">{section_title('THE PROCESS','A clearer path from question to deployment','No fake instant provisioning: follow the real decisions that need to happen first.')}<div class="steps"><div class="step"><h3>Choose your workload</h3><p>Site, app, or a connected set of services. Start where you are.</p></div><div class="step"><h3>Compare the right options</h3><p>Review management, limits, location and recovery requirements.</p></div><div class="step"><h3>Confirm and deploy</h3><p>Use approved product inventory and a real order flow when connected.</p></div></div></div></section>'''
 b+=faq(route,[('Which hosting product should I choose?','If you manage a website and want a familiar panel, start with cPanel. If you need OS-level control or custom applications, explore VPS or VDS.'),('Can Mosalam help our software house?','The proposed solutions section is designed to capture architecture requirements; confirm the exact scope of infrastructure and managed services with the team.'),('Are the plans available to purchase here?','This is a UX implementation prototype. Live pricing, availability and checkout require an approved catalog and commerce integration.')])+cta(route)
 return b

def pricing(route):
 products=[('Website hosting','For sites and small businesses.','hosting/cpanel',['Site & account limits','Backups and restore terms','Control panel and email','Renewal price & taxes']),('Virtual servers','For apps and development teams.','servers/vps',['CPU/RAM/storage configuration','Operating system & location','Management and access','Bandwidth and renewal terms']),('Cloud solution','For connected infrastructure needs.','cloud/managed',['Environment architecture','Operations responsibility','Data protection needs','Deployment and billing scope'])]
 b=hero(route,artname='server-stack-large',buttons=btn('Request a quote','contact/sales',route,'white'))
 b+=f'<section class="section soft"><div class="container">{section_title("SELECT A PATH","Start with the right plan category","Pricing must come from a verified live catalog. These cards show what you should compare before making a purchase.")}<div class="grid cols-3">'
 for title,desc,r,fields in products:
  b+=f'<article class="card pricing-card"><p class="caps">PRODUCT CATEGORY</p><h3>{H(title)}</h3><p>{H(desc)}</p><div class="price-callout">Request current price</div><ul>'+''.join('<li>'+H(x)+'</li>' for x in fields)+'</ul>'+btn('Explore options',r,route,'outline')+'</article>'
 b+='</div><p class="notice warning" style="margin-top:20px">No prices are displayed because the approved plan catalog, currency, taxes, renewal pricing and service availability have not been provided. Do not use placeholder numbers in a customer purchase decision.</p></div></section>'
 b+='<section class="section"><div class="container">'+section_title('FAIR COMPARISON','What a complete price needs to show')+compare_table(route)+'</div></section>'+faq(route)+cta(route)
 return b

def domains(route):
 b=hero(route,artname='managed-cloud-large',buttons=btn('Contact domains team','contact/sales',route,'white'))
 b+=f'''<section class="section"><div class="container">{section_title("DOMAIN NAME","Find a name that fits","Try a domain name below. This prototype does not check the registry or reserve a name.")}<form class="searchbox" id="domain-form"><label class="sr" for="domain-input">Domain name</label><input id="domain-input" name="domain" placeholder="example.com" autocomplete="off" required maxlength="253"><button type="submit" class="button primary">Review domain ↗</button></form><div id="domain-result" class="domain-result" role="status" aria-live="polite"></div><p class="utility-note">Availability, registration fees, transfer rules and renewal prices require a verified live domain service.</p></div></section>'''
 b+=f'<section class="section pale"><div class="container">{section_title("THE BASICS","Domain essentials")}'+cards([('Register a domain','Choose a name and verify availability through a live registrar.','domains'),('Understand DNS','Connect the domain to the right website, email or services.','docs'),('Plan renewal','Confirm your renewal cycle, ownership and contact details.','contact/sales')],route)+'</div></section>'+faq(route)+cta(route)
 return b

def contact_form(route):
 return f'''<form id="brief-form" class="quote-panel" novalidate><div class="form-grid"><div class="field"><label for="project-name">Your name <span aria-hidden="true">*</span></label><input id="project-name" name="name" autocomplete="name" required maxlength="120"></div><div class="field"><label for="project-email">Work email <span aria-hidden="true">*</span></label><input type="email" id="project-email" name="email" autocomplete="email" required maxlength="160"></div><div class="field"><label for="project-type">What are you building?</label><select id="project-type" name="project"><option>Website / cPanel hosting</option><option>Application / API</option><option>Software-house infrastructure</option><option>Multiple client websites</option><option>Migration</option><option>Not sure yet</option></select></div><div class="field"><label for="manage-pref">Preferred management</label><select id="manage-pref" name="management"><option>Need advice</option><option>Self-managed</option><option>Managed support (if available)</option></select></div></div><div class="field"><label for="project-brief">Tell us about the workload</label><textarea id="project-brief" name="brief" placeholder="What is running, how many environments, and what is your biggest question?" maxlength="2000"></textarea><span class="help">Avoid passwords, credentials and confidential production details.</span></div><button class="button primary" type="submit">Prepare my brief ↗</button><p class="utility-note">This prototype does not send messages. It prepares a brief you can copy into a verified Mosalam contact channel.</p><div class="form-result" id="brief-result" aria-live="polite"><strong>Your brief is ready</strong><pre id="brief-text" style="white-space:pre-wrap;font:13px/1.7 var(--font)"></pre><button type="button" class="button outline small" id="copy-brief">Copy brief</button><p id="copy-status" aria-live="polite"></p></div></form>'''
def contact(route):
 b=hero(route,artname='infrastructure-network-large',buttons=btn('Explore services','solutions',route,'white'))
 b+=f'''<section class="section"><div class="container section-split"><div><p class="kicker">DISCOVERY</p><h2 class="section-heading">Start with what you need to run.</h2><p style="color:#64738f;line-height:1.75">You do not need to know the perfect server specification. Tell us the application, the scale and the kind of help you want.</p>{feature_specs('solutions/custom-infrastructure')}<p class="notice">When real contact details and secure form processing are supplied, this brief can be connected to the sales workflow.</p></div><div>{contact_form(route)}</div></div></section>'''
 b+=faq(route,[('Will this form send my request?','No. In this prototype it creates a copyable brief without transferring any data.'),('Should I include server passwords or IP credentials?','No. Do not share secrets, access tokens or production credentials through a public enquiry form.'),('Can you advise on a complex workload?','Use the software house and custom infrastructure pages to structure the requirements; actual service scope must be confirmed.')])+cta(route)
 return b

def support(route):
 b=hero(route,artname='managed-cloud-large',buttons=btn('Read documentation','docs',route,'white')+f'<a class="text-link light" href="{url("portal/tickets",route)}">Ticket demo ↗</a>')
 b+=f'<section class="section"><div class="container">{section_title("SUPPORT PATHS","What do you need help with?","Find the appropriate next step without sending sensitive account information to the wrong place.")}'+cards([('Learn something','Setup guidance, DNS basics and technical checklists.','docs'),('Account question','Manage services and invoices in the client area.','portal/login'),('Existing issue','Follow the ticket process for your active service.','portal/tickets'),('New infrastructure','Discuss an implementation or commercial requirement.','contact/sales')],route,columns=4)+'</div></section>'+faq(route)+cta(route)
 return b

def docs(route):
 topics=[('Choose hosting or VPS','A website-focused panel is often easier; a VPS supports more specialized application control.'),('DNS cutover checklist','Record nameservers, TTL, email records, redirects and rollback steps before changing DNS.'),('Backups and restores','Identify what is backed up, frequency, recovery objectives and restoration access.'),('VPS access and hardening','Consider SSH key management, least privilege, patching and service monitoring.'),('Website migration plan','Inventory files, databases, email, dependencies, DNS and a rollback route.'),('Support responsibility','Check who handles the OS, control panel, application code and urgent incidents.')]
 b=hero(route,artname='infrastructure-network-large',buttons=btn('Contact support','support',route,'white'))
 b+='<section class="section"><div class="container docs-layout"><aside class="docs-aside" aria-label="Documentation topics"><strong style="display:block;margin:0 8px 12px">Guides</strong>'+''.join(f'<a href="#topic-{i}">{H(t)}</a>' for i,(t,d) in enumerate(topics))+'</aside><div class="doc-body"><p class="notice">These are decision and onboarding guides, not operational API documentation or a substitute for service-specific instructions.</p>'
 for i,(t,d) in enumerate(topics):
  b+=f'<section id="topic-{i}"><h2>{H(t)}</h2><p>{H(d)}</p><ul><li>Confirm your current service details and account permissions.</li><li>Make a change plan and identify a safe rollback step.</li><li>Record the final configuration and who owns future changes.</li></ul></section>'
 b+='</div></div></section>'+cta(route)
 return b

def status(route):
 b=hero(route,artname='infrastructure-network-large',buttons=btn('Get support','support',route,'white'))
 b+='<section class="section"><div class="container"><div class="empty-state"><img src="'+art('infrastructure-network-large',route)+'" alt=""><h2>Live service health is not connected</h2><p>Do not interpret this page as reporting that every service is operational. A verified incident/status feed is required before it can display current availability.</p><p>'+btn('Support resources','support',route)+'</p></div></div></section>'
 return b

def about(route):
 b=hero(route,artname='server-stack-large',buttons=btn('See our services','hosting',route,'white'))
 b+='<section class="section"><div class="container">'+section_title('OUR APPROACH','Clarity, precision and a system that scales','The same ordered design principles that shape our identity should shape product choices and support experiences.')+cards([('Clarity first','Describe what each service does before adding jargon.','hosting'),('Built for progress','Let site owners, developers and teams find a natural next step.','solutions'),('Dependable foundations','Make ownership, recovery and support explicit from the outset.','cloud')],route)+'</div></section>'+cta(route)
 return b

def legal(route):
 title=R[route][0]
 b=hero(route,artname='infrastructure-network-large',buttons=btn('Contact Mosalam','company/contact',route,'white'))
 b+=f'<section class="section"><div class="container"><div class="notice warning"><strong>{H(title)} — publication required.</strong><p>Legally approved {H(title.lower())} text has not been supplied. This page is an editorial placeholder only and must not be treated as a binding customer agreement, privacy notice or availability commitment.</p></div><div style="height:35px"></div>{section_title("PRODUCTION CHECK","What must be supplied before launch")}{cards([("Reviewed document","Provide the final text and document owner.",None,"security"),("Version and effective date","Include a verifiable last-updated date and regional applicability.",None,"backups"),("Accessible publication","Provide readable HTML, contact pathways and change history.",None,"api")],route)}</div></section>'
 return b

PORTAL=[('Overview','portal/overview','⌂'),('My services','portal/services','▣'),('Billing','portal/billing','▤'),('Tickets','portal/tickets','◷'),('Domains','portal/domains','◎'),('Servers','portal/servers','▥'),('Team','portal/team','♙')]
def portal(route):
 if route=='portal/login':
  b=hero(route,artname='server-stack-large',title='A clearer place to manage your services',desc='The portal interface below is a demonstration, not a functioning login or customer account.',buttons=btn('Open portal demo','portal/overview',route,'white'))
  b+=f'<section class="section"><div class="container grid cols-2"><div class="card"><h2>What belongs in a real client portal?</h2><p>Verified sign-in, multi-factor authentication, account recovery, service ownership, invoices and support history, connected to Mosalam business systems.</p><p class="notice warning">No passwords should be entered here. This package contains no authentication backend.</p></div><div class="card"><h2>Explore the interface safely</h2><p>Inspect clearly marked sample service and billing screens without pretending to manage any real resources.</p>{btn('Explore the demo','portal/overview',route)}</div></div></section>'
  return b
 side=''.join(f'<a class="{"active" if route==path else ""}" href="{url(path,route)}"><span aria-hidden="true">{sym}</span>{H(title)}</a>' for title,path,sym in PORTAL)
 header=f'''<div class="portal-layout"><aside class="portal-sidebar" aria-label="Portal demo navigation">{side}</aside><div class="portal-main"><div class="demo-tag" style="display:inline-block;margin-bottom:20px">DEMO DATA ONLY</div><h1>{H(R[route][1])}</h1><p class="sub">This is a local interaction prototype. Nothing here is connected to your real account.</p>'''
 if route=='portal/overview':
  main='''<div class="grid cols-3"><div class="portal-kpi"><span>Sample services</span><strong>2</strong><span>Example only</span></div><div class="portal-kpi"><span>Open tickets</span><strong>1</strong><span>Example only</span></div><div class="portal-kpi"><span>Next action</span><strong>Review</strong><span>Demo tasks</span></div></div><div class="card" style="margin-top:24px"><h3>Example service activity</h3><ul class="proto-list"><li><span>Website Hosting <small>Example service • no live data</small></span><span class="status-pill">Sample</span></li><li><span>VPS Environment <small>Example service • no live data</small></span><span class="status-pill">Sample</span></li></ul></div>'''
 elif route=='portal/services':
  main='''<div class="card"><div class="compare-heading"><h2>Services</h2><span class="demo-tag">EXAMPLE</span></div><ul class="proto-list"><li><span>Website Hosting <small>Example account • demonstration only</small></span><span class="status-pill">Example</span></li><li><span>VPS Environment <small>Example server • no provisioning connection</small></span><span class="status-pill">Example</span></li></ul></div><p class="notice warning" style="margin-top:18px">Actions such as upgrade, reboot and cancellation are intentionally unavailable until authenticated APIs and confirmation flows are implemented.</p>'''
 elif route=='portal/billing':
  main='''<div class="card"><h2>Invoices & renewals</h2><div class="empty-state"><h2>No live billing data</h2><p>Actual invoices, payment methods, tax totals and renewal dates require an authenticated billing integration.</p></div></div>'''
 elif route=='portal/tickets':
  main='''<div class="grid cols-2"><div class="card"><h2>Support ticket drafts</h2><ul class="proto-list" id="draft-list"><li><span>No drafts created yet.</span></li></ul><p class="utility-note">Stored locally in this browser. They are NOT sent to support.</p></div><form id="ticket-form" class="quote-panel"><h2>Create a local draft</h2><div class="field"><label for="ticket-subject">Issue summary</label><input name="subject" id="ticket-subject" required maxlength="100"></div><div class="field"><label for="ticket-body">What happened?</label><textarea id="ticket-body" name="body" required maxlength="1000"></textarea></div><button class="button primary" type="submit">Save local draft</button><p class="utility-note" id="ticket-status" aria-live="polite">Never include passwords or access tokens.</p></form></div>'''
 elif route=='portal/domains':main=f'''<div class="empty-state"><img src="{art('managed-cloud-large',route)}" alt=""><h2>No verified domains loaded</h2><p>Renewal, DNS and domain lock controls require an authenticated registrar integration.</p></div>'''
 elif route=='portal/servers':main=f'''<div class="empty-state"><img src="{art('server-stack-large',route)}" alt=""><h2>Server controls are locked in this demo</h2><p>Power, console and rebuild actions must use authenticated APIs, verified resource ownership and explicit confirmation.</p></div>'''
 else:main='''<div class="empty-state"><h2>Permissions require a real account</h2><p>Team invitations, role changes and audit history must use server-side access controls. This demo will not create or modify users.</p></div>'''
 return header+main+'</div></div>'

def design_gallery(route):
 b=hero(route,eyebrow='INTERNAL · COMPONENT LIBRARY',title='The Mosalam visual system',desc='The approved geometric direction, translated into reusable assets and predictable interface behaviors.',artname='server-stack-large',buttons=btn('Explore hosting','hosting',route,'white'))
 icons=[('cPanel','cpanel'),('VDS','vds'),('Dedicated','dedicated'),('Cloud','managed-cloud'),('Networking','networking'),('Database','database'),('Backup','backups'),('Security','security'),('Monitoring','monitoring'),('Support','support'),('Migration','migration'),('Domains','domains')]
 b+=f'<section class="section"><div class="container">{section_title("FOUNDATIONS","Functional icons stay flat","A geometric keyline, coherent stroke and an optical size appropriate for the context.")}<div class="grid cols-4">'+''.join(f'<div class="card"><img class="icon-geom" src="{icon(i,route)}" alt="" loading="lazy"><h3>{H(t)}</h3></div>' for t,i in icons)+'</div></div></section>'
 b+=f'<section class="section pale"><div class="container">{section_title("ILLUSTRATIONS","Depth has one clear role","Large hero and product illustrations may use restrained 45-degree extrusion. Small controls never do.")}<div class="grid cols-3">'+''.join(f'<article class="card"><div class="feature-media"><img src="{art(x,route)}" alt="" loading="lazy"></div><h3>{H(t)}</h3></article>' for x,t in [('hero-servers','Hosting stack'),('managed-cloud-large','Cloud infrastructure'),('infrastructure-network-large','Infrastructure architecture')])+'</div></div></section>'
 b+=f'<section class="section"><div class="container">{section_title("INTERACTION","Buttons, patterns and states","Buttons stay flat and predictable. Loading should explain what is happening.")}<div class="grid cols-3"><article class="card"><h3>Primary & secondary</h3><p>{btn("Primary action","hosting",route)} {btn("Secondary","pricing",route,"outline")}</p><p>Every action has a clear target and a visible keyboard focus state.</p></article><article class="card"><h3>Loading state</h3><img style="height:110px;margin:auto" src="{prefix(route)}assets/loaders/geometric-loader.svg" alt="Example loading animation" loading="lazy"><p>Used only while waiting for real data, with reduced-motion fallback.</p></article><article class="card"><h3>Provisioning example</h3><img style="height:110px;margin:auto" src="{prefix(route)}assets/loaders/provisioning-status.svg" alt="Illustrative provisioning status" loading="lazy"><p>Never show a fake provisioning success without a backend response.</p></article></div></div></section>'
 b+=f'<section class="section soft"><div class="container">{section_title("DESIGN TOKENS","Built for consistent components","Spacing, color, type and motion come from one documented source.")}<div class="grid cols-4">'+''.join(f'<div class="card"><div style="height:55px;background:{color};border:1px solid #d5e1f3;border-radius:9px"></div><h3>{name}</h3><p>{color}</p></div>' for name,color in [('Mosalam blue','#0774FF'),('Deep blue','#033AA7'),('Sky blue','#2D86FF'),('Yellow accent','#FFC107')])+'</div></div></section>'+cta(route)
 return b

pages={}
for route in R:
 if not route: body=home(route)
 elif route in FEATURES:body=category(route)
 elif route.startswith(('hosting/','servers/','cloud/','solutions/')):body=detail(route)
 elif route=='pricing':body=pricing(route)
 elif route=='design-system':body=design_gallery(route)
 elif route=='domains':body=domains(route)
 elif route in ('contact/sales','company/contact'):body=contact(route)
 elif route=='support':body=support(route)
 elif route=='docs':body=docs(route)
 elif route=='status':body=status(route)
 elif route=='company/about':body=about(route)
 elif route.startswith('portal/'):body=portal(route)
 elif route.startswith('legal/'):body=legal(route)
 else:body=hero(route)+cta(route)
 out=ROOT/(route if route else '')/'index.html'
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(render(route,body),encoding='utf-8')
 pages[route or '/']=str(out.relative_to(ROOT))
(ROOT/'source/routes.json').write_text(json.dumps(pages,indent=2),encoding='utf-8')
print('generated',len(pages),'routes')
