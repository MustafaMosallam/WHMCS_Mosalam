# Mosalam — Full Website Frontend Implementation

**Version:** 0.9 prototype | **Date:** 30 October 2026

A navigable, responsive, multi-page static website prototype for Mosalam hosting, virtual servers, cloud infrastructure and software-house solutions. Extends the owner's **approved blue landing-page reference**, rather than the glossy 3D exploratory concepts. Functional icons are flat SVGs; the large server and cloud illustrations use restrained dimensionality.

## Start here

Open `index.html` after extracting **the entire ZIP**. The links and local SVG files are relative, so all pages work as a static folder. For a local web server:

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080/` in your own browser. Deploy the folder unchanged to ordinary static hosting. The project does not require Node.js, a database or a build system for preview.

**Important:** The individual `index.html` file is **not** standalone. The full ZIP is required. This intentionally avoids repeating the previous single-file delivery bug.

## Delivered

- **38 real HTML routes**, each with a proper title and its own page-specific content.
- Responsive desktop/tablet/mobile navigation; keyboard-operated menus, focus indicators and mobile toggle.
- A project-type recommendation selector on the homepage (website, app, agency, engineering team).
- Product and service pages: shared/cPanel, WordPress, reseller, VPS, VDS, dedicated, cloud, managed cloud, backup/recovery, domains.
- Solutions pages: software houses, agencies, business hosting, infrastructure design and migration.
- Pricing *requirements* page without fake rates; quote enquiry brief with optional workload details; client-side domain format check clearly distinguished from availability search.
- Support, documentation, service-status explanation, company and legal placeholders.
- **Portal demo:** overview, services, billing, tickets, domains, servers and team access. Ticket drafts use browser local storage only when available. No real account/login/provisioning.
- Reusable blue/white geometric patterns, **23 flat icons**, three large vector illustrations, and two loader/status illustrations.
- Internal `design-system/index.html` visual assets and component sample page.
- Shared `style.css` and `app.js`; Jinja-free Python source generator in `source/build.py` (Python stdlib + Jinja import unused; no runtime dependencies for site).

## Site map

`source/routes.json` contains all generated routes. The high-level groups:

1. **Home** `/`
2. **Hosting** `/hosting/`, `/hosting/cpanel/`, `/hosting/wordpress/`, `/hosting/reseller/`
3. **Servers** `/servers/`, `/servers/vps/`, `/servers/vds/`, `/servers/dedicated/`
4. **Cloud** `/cloud/`, `/cloud/managed/`, `/cloud/backup/`
5. **Solutions** `/solutions/`, `/solutions/software-houses/`, `/solutions/agencies/`, `/solutions/businesses/`, `/solutions/custom-infrastructure/`, `/solutions/migration/`
6. **Domains & pricing** `/domains/`, `/pricing/`
7. **Contact, support, docs** `/contact/sales/`, `/support/`, `/docs/`, `/status/`, `/company/about/`, `/company/contact/`
8. **Account demo** `/portal/login/`, `/portal/overview/`, `/portal/services/`, `/portal/billing/`, `/portal/tickets/`, `/portal/domains/`, `/portal/servers/`, `/portal/team/`
9. **Legal placeholders** `/legal/terms/`, `/legal/privacy/`, `/legal/sla/`
10. **Internal style showcase** `/design-system/`

## Interactive experiences

- **Homepage selector** changes the recommendation and destination link; supports arrow/Home/End keyboard keys.
- **Mobile navigation and desktop menus** are click/keyboard operable; Escape closes menus.
- **FAQ** uses accessible native `<details>` elements.
- **Domain field** validates basic ASCII domain-name format; it intentionally does **not** check live availability, WHOIS, price or registration.
- **Architecture brief** validates name/email; it does **not** submit or send personal information; it produces a copyable text brief.
- **Ticket draft** stores local browser draft information where supported and never sends it to a server. Do not use real secrets in a demo.
- **No fake financial or infrastructure actions:** server reboot, billing, DNS editing and account controls are disabled or descriptive until real APIs exist.

## Visual rules and design provenance

- Hero gradient `#2D86FF → #033AA7`, deep navy sections, sparse yellow `#FFC107` emphasis.
- Large illustration only: modest oblique extrusion and white connectors. Never dimensional small icons/buttons.
- Navigation uses a white band and simple pill actions. Cards use 10–12px radii; large sections use limited diagonal cuts.
- Service icons use the approved reference's flat geometric keyline design; additional flat line icons come from the preceding foundation package.
- Decorative patterns remain away from content/form text. No flashy animation, only optional loader assets and tactile hover feedback; `prefers-reduced-motion` is supported.
- Current site uses Latin typography Plus Jakarta Sans and Inter, with local fallbacks when the remote Google Font stylesheet cannot load.
- **The star-style logo is still the prior concept logo** from the selected reference. Replace only after receiving the brand owner's authorized vector master.

## Testing completed

Ran `source/test_site.py` in Chromium with document assets embedded for the sandbox browser (the environment blocked direct navigation to local file and localhost URLs). This validated:

- all 38 route documents have valid local image/CSS/JS/page link references;
- 1440px, 390px and 320px home layouts have no horizontal overflow;
- no missing visible SVG images, no JavaScript exceptions in representative pages;
- representative cPanel, VPS, VDS, managed cloud, software-house, sales, pricing, domains and portal pages at 390px;
- mobile menu, project selector, domain check and architecture brief;
- ticket draft responds gracefully if localStorage is restricted.

Captured screenshots in `previews/`. These are **prototype tests, not a penetration test, accessibility certification, or production browser QA**.

## Not production-complete (do not ship without these)

See `docs/INTEGRATIONS.md` and `docs/RELEASE-CHECKLIST.md`. Especially:

1. Approved active service catalog (plans, regions, currency, resources, exact support responsibility, inclusions, taxes, setup and renewal prices).
2. Commerce and payments, order validation, invoices, refunds and cancellation rules.
3. Genuine authentication, session management, MFA, authorization/RBAC, audit events and credentials handling.
4. Actual server/orchestration APIs and protected operational actions (provisioning, console, DNS, power, backup/restore).
5. Verified contact/ticket system endpoints and privacy/retention policy.
6. Actual registrar integration for search, purchase, renewal, transfer and DNS.
7. Legally approved Terms, Privacy and SLA pages and an official status provider.
8. Complete Arabic localization, RTL regression tests and locale-specific product information. **Arabic text is NOT implemented in this phase.**
9. Original verified logo, illustration rights, infrastructure claims and commercial proof points.
10. Full production QA (automated end-to-end tests under HTTPS, accessibility audit with real users, screen readers, cross-browser test and security review).

## Source and rebuilding

`python3 source/build.py` regenerates all HTML pages from the page content data and shared templates. Edit `style.css`, `app.js`, `source/build.py` and `assets/` directly. The files work without running the generator; the generator is there to keep shared components in sync.

### Implementation principle

The public marketing site and client portal share colors/type/icons but have different information densities. The portal interface deliberately avoids the giant geometric pattern on tables and forms.


## Phase 2 update: animations and irregular section shapes

This package adds a site-wide motion system and a more expressive shape system across all pages.

### Added motion
- Scroll reveal for major sections and cards
- Subtle hero floating motion
- Hover elevation for cards and surfaces
- Animated nav flyouts
- Button sheen / interaction polish
- Reduced-motion safe fallbacks

### Added shape language
- Alternating faceted section transitions
- Irregular section wrappers for soft/pale sections
- More cut-corner treatment on cards and supporting surfaces
- Broader use of geometric pattern overlays

These updates are implemented globally via `style.css` and `app.js`, so they affect the whole static site consistently.


## vNext (new asset system + plan journeys)

Added: 24 unique flat vector service icons; 18 large scalable service illustrations; 47 concept crops from the previously generated creative boards; distinct product hero visuals; product-level 3-tier plan selection sections; categorized global plan browsing; and an order-request configurator at `/order/index.html`. All prices/specifications remain unverified and the request flow does not place orders. See `assets/ASSET_MANIFEST.md` and `docs/VNEXT-IMPLEMENTATION.md`.


## Natural electric circuits update
See `GOLD-MOTION-NOTES.md`. The old fixed SVG was removed from all pages. Subtle section-local gold pulses now follow different geometric paths, with asynchronous timings, viewport pausing, and reduced-motion support.
