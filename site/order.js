
// Mosalam order-request prototype. No checkout, payments, availability or provisioning.
(()=>{
'use strict';
const f=document.getElementById('order-configurator');if(!f)return;
const assetRoot=document.body.dataset.root||'../';
const catalog=[{"slug":"hosting/cpanel","title":"cPanel Hosting","icon":"cpanel","illustration":"cpanel-hosting","tiers":["Launch","Grow","Business"],"bullets":["Website control panel","Domain and email requirements","Backup policy to confirm"]},{"slug":"hosting/wordpress","title":"WordPress Hosting","icon":"wordpress","illustration":"wordpress-hosting","tiers":["Starter","Grow","Scale"],"bullets":["WordPress environment","Caching and updates scope","Restore and migration options"]},{"slug":"hosting/reseller","title":"Reseller Hosting","icon":"reseller","illustration":"reseller-hosting","tiers":["Solo","Agency","Studio"],"bullets":["Client account separation","Panel and licensing scope","Team workflow options"]},{"slug":"servers/vps","title":"VPS Servers","icon":"vps","illustration":"vps-hosting","tiers":["Build","Deploy","Scale"],"bullets":["vCPU, RAM and storage selection","OS and root access scope","Management and backup choices"]},{"slug":"servers/vds","title":"VDS Servers","icon":"vds","illustration":"vds-hosting","tiers":["Reserved","Performance","Enterprise"],"bullets":["Dedicated allocation needs","Operating system choice","Support and backup scope"]},{"slug":"servers/dedicated","title":"Dedicated Servers","icon":"dedicated","illustration":"dedicated-servers","tiers":["Single node","Advanced","Custom"],"bullets":["Processor and storage requirements","Networking and location","Managed or self-managed"]},{"slug":"cloud/managed","title":"Managed Cloud","icon":"managed-cloud","illustration":"managed-cloud","tiers":["Application","Team","Platform"],"bullets":["Infrastructure architecture","Operations ownership","Security and recovery responsibilities"]},{"slug":"cloud/backup","title":"Backup & Recovery","icon":"backups","illustration":"backup-recovery","tiers":["Protect","Recover","Continuity"],"bullets":["Backup frequency requirements","Retention and restore objectives","Coverage and exclusions"]},{"slug":"solutions/software-houses","title":"Software House Infrastructure","icon":"software-house","illustration":"software-house","tiers":["Dev & staging","Production","Platform"],"bullets":["Workload and environments","CI/CD and observability needs","Security and team ownership"]},{"slug":"solutions/custom-infrastructure","title":"Custom Infrastructure","icon":"infrastructure","illustration":"custom-infrastructure","tiers":["Discovery","Architecture","Managed scope"],"bullets":["Topology and workload planning","Networking and data needs","Deployment and ongoing operations"]},{"slug":"domains","title":"Domains & DNS","icon":"domains","illustration":"domains","tiers":["Register","Transfer","Portfolio"],"bullets":["Domain and TLD checks","DNS and ownership responsibilities","Renewal and transfer terms"]}];
const service=document.getElementById('order-service');
const tier=document.getElementById('order-tier');
const art=document.getElementById('order-art');
const title=document.getElementById('order-title');
const desc=document.getElementById('order-description');
const recap=document.getElementById('order-recap');
const out=document.getElementById('order-output');
const query=new URLSearchParams(location.search);
function element(name,attrs={},text){const e=document.createElement(name);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,v);if(text!==undefined)e.textContent=text;return e}
function fillTiers(value){const x=catalog.find(x=>x.slug===value)||catalog[0];tier.innerHTML='';x.tiers.forEach(t=>tier.append(element('option',{value:t},t)));if(x.tiers.includes(query.get('tier')))tier.value=query.get('tier');art.src=assetRoot+'assets/illustrations/solutions/'+x.illustration+'.svg';title.textContent=x.title;desc.textContent='Choose a '+x.title+' plan direction. Commercial and technical specifications require confirmation.';updateSummary()}
function updateSummary(){const data=new FormData(f);recap.innerHTML='';for(const [k,v] of [['Service',catalog.find(x=>x.slug===service.value)?.title||''],['Plan',tier.value],['Billing preference',data.get('cycle')],['Management',data.get('management')]]){const r=element('div');r.append(element('dt',{},k),element('dd',{},String(v)));recap.append(r)}out.hidden=true}
catalog.forEach(x=>service.append(element('option',{value:x.slug},x.title)));
if(catalog.some(x=>x.slug===query.get('service')))service.value=query.get('service');
service.addEventListener('change',()=>{query.delete('tier');fillTiers(service.value)});
f.addEventListener('input',updateSummary);
f.addEventListener('change',updateSummary);
fillTiers(service.value);
f.addEventListener('submit',e=>{e.preventDefault();if(!f.reportValidity())return;const data=new FormData(f);const x=catalog.find(x=>x.slug===service.value);const body=[
'MOSALAM — ORDER REQUEST (NOT PLACED)',
'Product: '+x.title,'Plan direction: '+tier.value,
'Billing preference: '+data.get('cycle'),
'Management: '+data.get('management'),
'Location preference: '+(data.get('location')||'not stated'),
'Requirements: '+(data.get('notes')||'not stated'),
'','Price, stock, tax, SLA and technical configuration require confirmation.',
'This form did not submit or collect payment.'
].join('\n');document.getElementById('order-copy-text').value=body;out.hidden=false;out.scrollIntoView({block:'nearest',behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});
});
document.getElementById('order-copy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(document.getElementById('order-copy-text').value);document.getElementById('order-copy-status').textContent='Request copied. Share it via an official Mosalam contact channel.'}catch(_){const input=document.getElementById('order-copy-text');input.focus();input.select();document.getElementById('order-copy-status').textContent='Select and copy the request above manually.'}});
})();
