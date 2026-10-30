(()=>{
'use strict';
const root=document.body.dataset.root||'./';
const route=(p)=>root+(p?p.replace(/^\/+|\/+$/g,'')+'/':'')+'index.html';
const prefersReduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* mobile nav */
const menu=document.getElementById('menu-toggle');
const links=document.getElementById('nav-links');
function closeNav(){
  if(!menu||!links) return;
  links.classList.remove('open');
  menu.setAttribute('aria-expanded','false');
  menu.setAttribute('aria-label','Open navigation');
}
if(menu&&links){
  menu.addEventListener('click',()=>{
    const open=!links.classList.contains('open');
    links.classList.toggle('open',open);
    menu.setAttribute('aria-expanded',String(open));
    menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');
  });
  document.addEventListener('keydown',e=>{ if(e.key==='Escape') closeNav(); });
  document.addEventListener('click',e=>{ if(!e.target.closest('.nav-shell')) closeNav(); });
}

/* nav flyouts */
const groups=[...document.querySelectorAll('.nav-item')];
groups.forEach(group=>{
  const b=group.querySelector('button');
  if(!b) return;
  b.addEventListener('click',e=>{
    e.stopPropagation();
    const now=!group.classList.contains('open');
    groups.forEach(g=>{
      g.classList.remove('open');
      g.querySelector('button')?.setAttribute('aria-expanded','false');
    });
    group.classList.toggle('open',now);
    b.setAttribute('aria-expanded',String(now));
  });
  group.addEventListener('keydown',e=>{
    if(e.key==='Escape'){
      group.classList.remove('open');
      b.setAttribute('aria-expanded','false');
      b.focus();
    }
  });
});
document.addEventListener('click',e=>{
  if(!e.target.closest('.nav-item')) groups.forEach(g=>{
    g.classList.remove('open');
    g.querySelector('button')?.setAttribute('aria-expanded','false');
  });
});

/* fit selector */
const fit={
  site:['Start with website hosting','Explore familiar cPanel-style site management, and compare account limits and responsibilities.','hosting/cpanel'],
  app:['Explore virtual servers','VPS is a good comparison point when you need custom runtimes, software or OS-level control.','servers/vps'],
  agency:['Plan for multiple client sites','Consider reseller hosting or server-level management based on client isolation and operational needs.','hosting/reseller'],
  team:['Map your full application stack','Start with environments, data, security and ownership before picking an infrastructure shape.','solutions/software-houses']
};
const tabs=[...document.querySelectorAll('[data-fit]')];
tabs.forEach(tab=>tab.addEventListener('keydown',e=>{
  if(!['ArrowRight','ArrowLeft','Home','End'].includes(e.key)) return;
  e.preventDefault();
  const i=tabs.indexOf(tab);
  const next=e.key==='Home'?0:e.key==='End'?tabs.length-1:e.key==='ArrowRight'?(i+1)%tabs.length:(i+tabs.length-1)%tabs.length;
  tabs[next].focus();
  tabs[next].click();
}));
tabs.forEach(tab=>tab.addEventListener('click',()=>{
  tabs.forEach(x=>{ x.setAttribute('aria-selected',String(x===tab)); x.tabIndex=x===tab?0:-1; });
  const data=fit[tab.dataset.fit];
  const title=document.getElementById('fit-title');
  const desc=document.getElementById('fit-desc');
  const link=document.getElementById('fit-link');
  const panel=document.getElementById('fit-result');
  if(title) title.textContent=data[0];
  if(desc) desc.textContent=data[1];
  if(link) link.href=route(data[2]);
  if(panel) panel.setAttribute('aria-labelledby',tab.id);
}));

/* domain review */
const domain=document.getElementById('domain-form');
if(domain) domain.addEventListener('submit',e=>{
  e.preventDefault();
  const val=document.getElementById('domain-input').value.trim().toLowerCase().replace(/^https?:\/\//,'').replace(/\/$/,'');
  const out=document.getElementById('domain-result');
  out.classList.add('visible');
  out.innerHTML='';
  const valid=/^(?=.{4,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$/.test(val);
  const strong=document.createElement('strong');
  const p=document.createElement('p');
  strong.textContent=valid?'Review: '+val:'Check the domain name';
  p.textContent=valid?'This is a format review only. Availability, registration and current price have NOT been checked. Use a connected registrar before making a purchase.':'Enter a full domain such as example.com (without spaces or a protocol).';
  out.append(strong,p);
});

/* infrastructure brief */
const brief=document.getElementById('brief-form');
if(brief) brief.addEventListener('submit',e=>{
  e.preventDefault();
  const name=document.getElementById('project-name');
  const email=document.getElementById('project-email');
  if(!name.value.trim()){
    name.setCustomValidity('Please enter your name.');
    name.reportValidity();
    name.setCustomValidity('');
    return;
  }
  if(!email.value.trim()||!email.checkValidity()){
    email.reportValidity();
    return;
  }
  const data=new FormData(brief);
  const msg=[
    'MOSALAM INFRASTRUCTURE ENQUIRY',
    'Name: '+(data.get('name')||''),
    'Email: '+(data.get('email')||''),
    'Project: '+(data.get('project')||''),
    'Management: '+(data.get('management')||''),
    'Workload: '+(data.get('brief')||'(not provided)'),
    '',
    'Prepared locally; not submitted.'
  ].join('\n');
  const target=document.getElementById('brief-text');
  target.textContent=msg;
  document.getElementById('brief-result').classList.add('visible');
  target.parentElement.scrollIntoView({block:'nearest',behavior:prefersReduced?'auto':'smooth'});
});
const cp=document.getElementById('copy-brief');
if(cp) cp.addEventListener('click',async()=>{
  const out=document.getElementById('copy-status');
  const data=document.getElementById('brief-text').textContent;
  try{
    await navigator.clipboard.writeText(data);
    out.textContent='Brief copied. Paste it into an official Mosalam contact channel.';
  }catch(_){
    const el=document.getElementById('brief-text');
    const sel=window.getSelection();
    const range=document.createRange();
    range.selectNodeContents(el);
    sel.removeAllRanges();
    sel.addRange(range);
    out.textContent='Select and copy the text above manually.';
  }
});

/* local support ticket drafts */
const ticket=document.getElementById('ticket-form');
function drafts(){
  try{return JSON.parse(localStorage.getItem('mosalam_ticket_drafts')||'[]')}catch(_){return []}
}
function paintDrafts(){
  const list=document.getElementById('draft-list');
  if(!list) return;
  list.innerHTML='';
  const all=drafts();
  if(!all.length){
    const li=document.createElement('li');
    li.textContent='No drafts created yet.';
    list.append(li);
  }else{
    all.forEach(d=>{
      const li=document.createElement('li');
      const s=document.createElement('span');
      const small=document.createElement('small');
      s.textContent=d.subject;
      small.textContent='Local draft · not submitted';
      s.append(small);
      li.append(s);
      list.append(li);
    });
  }
}
if(ticket){
  paintDrafts();
  ticket.addEventListener('submit',e=>{
    e.preventDefault();
    if(!ticket.reportValidity()) return;
    const f=new FormData(ticket);
    const all=drafts();
    all.unshift({subject:String(f.get('subject')).slice(0,100),body:String(f.get('body')).slice(0,1000)});
    try{
      localStorage.setItem('mosalam_ticket_drafts',JSON.stringify(all.slice(0,20)));
      document.getElementById('ticket-status').textContent='Draft saved in this browser only. No ticket was sent.';
      ticket.reset();
      paintDrafts();
    }catch(_){
      document.getElementById('ticket-status').textContent='Browser storage unavailable. Your draft was not saved.';
    }
  });
}

})();
