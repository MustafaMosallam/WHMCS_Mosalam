# Backend integration contract (planning document, not implemented)

## Product catalog

- Approved product IDs and route mapping for hosting, VPS, VDS, cloud, domain offerings.
- A structured catalog response with `name`, `category`, `features`, `cpu`, `memory_mb`, `storage_gb`, `storage_type`, `location`, `traffic`, `management_model`, `backup_policy`, `availability`, `currency`, `billing_cycle`, `price_due_now`, `renewal_price`, `tax_display`, `setup_fee`, `contract_terms_url`.
- All optional capability fields must be marked explicitly, never replaced with a guessed value. User should see the billing total and renewal price before a checkout event.
- Use server-side prices, not price calculations trusted from browser code. Make checkout idempotent and protect against replay/double charge.

## Authentication and portal

- SSO or verified account service. Secure session cookies (`HttpOnly`, `Secure`, `SameSite` appropriate), server-side access controls and MFA.
- Resource authorization for every request; never rely on a route, hidden button or account ID to grant ownership.
- Audit high-risk actions including console access, reboots, backup restores, DNS changes, team invitations and payment method updates.
- Show last-known verified status and actual request errors; never display success until API acknowledgement and subsequent state verification.

## Provisioning lifecycle

`requested → validated → payment_confirmed → queued → provisioning → configuring → verifying → ready` (or `failed`, `manual_review`, `cancelled`). States must be returned by the provisioner; no animated illustration can replace this state machine. Support retriable actions and status polling/webhook updates with idempotency keys.

## Ticket system and enquiry

- Explicit consent, anti-abuse protection, file upload policy, retention, email verification if needed, privacy notice.
- API validates inputs and returns an actual ticket/reference number; make sure users can return to an existing ticket.
- Secrets must never appear in a contact form or be logged inadvertently.

## Domain operations

- Real registrar API for live check, purchase, transfer, ownership verification, DNS and renewal. Mark results as current at query time and clarify that availability can change before checkout.

## Status

- Verified official service-status provider or real monitoring backend. Unknown service state must not be translated as "operational."

## Customer roles

- Owner, billing manager, technical admin, limited support contact. Role permissions should be server-side and service-specific. Team membership and invitations require owner approvals and audit history.

## Localization

- Translate entire route content in professional Arabic, not just menu labels. Proper RTL layout; keep IPs, hostnames, domains, shell commands and resource specs LTR; localized numerals and currencies based on policy. Test with native readers and screen reader navigation.
