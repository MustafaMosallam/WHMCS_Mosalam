# Mosalam section-local electric circuits (version 2)

## Why the old effect looked fixed
The earlier implementation put the same `ms-ambient-geometry` SVG directly in every page, positioned `fixed`, and injected another identical SVG in selected sections. Although a gold dash animated, the pattern itself never varied or belonged to a particular section.

## What's changed
- Removed the fixed SVG overlay in all 40 HTML pages.
- Replaced repeated geometry with programmatically generated, section-local inline SVG circuits.
- Every section has its own geometric arrangement from a consistent family of 45° and 90° paths.
- Subtle sky-blue or white tracks form the static infrastructure pattern; **brief gold electric pulses move along the actual paths**.
- Each route is staggered and has slightly varying travel speed (approximately 750–1160 ms) and rest interval (approximately 1150–2400 ms). There is no synchronized one-second global flash.
- Layers are anchored near a section edge, never `position: fixed`. The moving light is behind the content and cannot intercept clicks.
- Pulse timers run only for near-viewport sections, pause when hidden, and stop entirely if `prefers-reduced-motion: reduce` is active. The geometric framework remains faintly visible.
- Kept the small existing branded page transition for regular same-origin page navigation, without forced long waits.

## Engineering reference
- `motion.css`: surface-aware colors, pulse appearance, layout containment, reduced-motion rules, page-transition appearance.
- `motion.js`: per-section SVG construction, pulse scheduling, scroll/visibility awareness, navigation transitions.
- To tune intensity, start with `.ms-circuit-field` opacity and `.ms-route` opacity in `motion.css`; to tune frequency, edit the duration and rest intervals in `motion.js`.
- No third-party animation libraries, videos, or large background GIFs.

## QA
Prototype tested via Chromium in-memory rendering because local file navigation is restricted in the sandbox. Verify the extracted multi-page site in your own browser before deployment. Prices, checkout, and server provisioning are not connected to production services.
