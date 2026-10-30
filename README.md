# Mosalam Website

Public-facing Mosalam hosting website built using Next.js App Router, React, TypeScript and the Mosalam design system.

## Run locally

```bash
cd apps/web
npm install
npm run dev
```

Open http://localhost:3000.

## Available pages

- Home
- Web Hosting (`/hosting/cpanel`)
- VPS Hosting (`/servers/vps`)
- VDS Servers (`/servers/vds`)
- Domains (`/domains`)
- Website Design (`/website-design`)
- Cloud Support (`/cloud/managed`)
- About (`/about`)
- Contact (`/contact`)

## Current limitations

This branch provides the public-facing frontend, service information and responsive styles. Live WHMCS products, actual prices, checkout, customer account login, payment processing, message submission and server provisioning are **not yet implemented**. Do not advertise live order capability until those systems are connected and tested.

See `docs/ARCHITECTURE.md` and `integrations/whmcs/README.md` for backend requirements. Confirm current commercial offers and undertake accessibility and browser testing before production launch.
