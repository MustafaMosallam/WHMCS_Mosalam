# Mosalam — Hosting & Cloud Platform

This repository is the home for the Mosalam public website and its future WHMCS integration.

## Project separation

- `apps/web/` — Mosalam's public website (Next.js and TypeScript)
- `integrations/whmcs/` — future WHMCS adapter and documentation (not yet implemented)
- `docs/` — product catalog, brand/UX decisions, launch and integration checklists

**Safety:** Do not commit WHMCS credentials, API keys, private server details, production customer data or paid WHMCS source files.

Implementation is developed in reviewable pull requests. No commerce, provisioning, customer login or payment behavior should be described as live before backend integration and testing.
