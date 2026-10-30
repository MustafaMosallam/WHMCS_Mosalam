/* Mosalam Electric Lines v2: per-section geometric circuits and organic gold pulses. */
(()=>{
'use strict';
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
const SVG_NS = 'http://www.w3.org/2000/svg';
const random = (lo,hi) => Math.round(lo + Math.random()*(hi-lo));
const circuits = new Set();

// All section geometry is drawn as native SVG lines, not a fixed image or wallpaper.
// Variants share 45° / 90° construction but do not repeat the exact same artwork.
const paths = [
  ['M -20 128 H 76 L 150 54 H 276 L 333 111 H 442 L 526 195 H 660',
   'M 650 36 L 542 144 H 435 L 366 213 H 278 L 217 274 H 105 L 38 341'],
  ['M 650 130 H 558 L 468 220 H 365 L 306 161 H 230 L 151 240 H -20',
   'M 12 43 H 110 L 173 106 H 290 L 375 191 H 470 L 547 268 H 650'],
  ['M -16 374 H 105 L 188 291 H 303 L 369 225 H 454 L 554 125 H 654',
   'M 625 420 L 526 321 H 411 L 355 265 H 263 L 191 193 H 101 L 4 96'],
  ['M 652 52 L 548 156 H 440 L 382 214 H 272 L 202 144 H 109 L 12 241',
   'M -16 438 L 79 343 H 189 L 258 274 H 372 L 449 351 H 555 L 642 264']
];

function createField(section,i){
  const dark=section.matches('.hero,.dark-panel,.dark-banner') || section.classList.contains('ms-dark-section');
  const side=(i%3===2) ? 'left':'right';
  const variant=i%paths.length;
  const flip=side==='left' ? 'transform="translate(640 0) scale(-1 1)"' : '';
  const starCenters=[
    [[180,82],[390,238],[555,390]],
    [[116,206],[368,91],[530,302]],
    [[178,327],[348,190],[560,84]],
    [[115,110],[345,326],[525,202]]
  ][variant];
  const stars=starCenters.map(([x,y],j)=>{
    const radius=j===1?37:28;
    const x0=x-radius,y0=y-radius,size=radius*2;
    return `<rect x="${x0}" y="${y0}" width="${size}" height="${size}" />`+
           `<rect x="${x0}" y="${y0}" width="${size}" height="${size}" transform="rotate(45 ${x} ${y})" />`;
  }).join('');
  const routeMarkup=paths[variant].map((d,j)=>{
    const nodeX=(variant*67+j*113+324)%420+110;
    const nodeY=(variant*37+j*71+80)%250+82;
    return `<path class="ms-route" d="${d}"/>`+
      `<g class="ms-electric-pulse" data-pulse="${j}">`+
       `<path class="ms-flare ms-flare-halo" pathLength="1000" d="${d}"/>`+
       `<path class="ms-flare ms-flare-core" pathLength="1000" d="${d}"/>`+
      `</g>`+
      `<circle class="ms-node-halo" cx="${nodeX}" cy="${nodeY}" r="7"/>`+
      `<circle class="ms-node" cx="${nodeX}" cy="${nodeY}" r="2.5"/>`;
  }).join('');
  const layer=document.createElement('div');
  layer.className='ms-circuit-field';
  layer.dataset.side=side;
  layer.dataset.surface=dark?'dark':'light';
  layer.setAttribute('aria-hidden','true');
  layer.innerHTML=`<svg viewBox="0 0 640 460" preserveAspectRatio="xMidYMid slice" xmlns="${SVG_NS}" aria-hidden="true" focusable="false">`+
    `<g ${flip}><g class="ms-symmetry">${stars}</g>${routeMarkup}</g></svg>`;
  section.classList.add('ms-circuit-zone');
  section.insertBefore(layer,section.firstChild);
  return {layer,groups:[...layer.querySelectorAll('.ms-electric-pulse')],timers:new Set(),visible:false};
}

const sections=[...document.querySelectorAll('main > section, main > .dark-panel, main > .dark-banner, footer.footer, .portal-main')];
sections.forEach((section,i)=>circuits.add(createField(section,i)));

function stop(circuit){
  circuit.visible=false;
  circuit.timers.forEach(id=>window.clearTimeout(id));
  circuit.timers.clear();
  circuit.groups.forEach(group=>group.classList.remove('is-firing'));
}
function schedule(circuit,group,delay){
  if(!circuit.visible || document.hidden || reduced.matches) return;
  const timer=window.setTimeout(()=>{
    circuit.timers.delete(timer);
    if(!circuit.visible || document.hidden || reduced.matches) return;
    const duration=random(750,1160);
    group.style.setProperty('--pulse-duration',duration+'ms');
    group.classList.remove('is-firing');
    // Reflow the tiny SVG group only to restart its short animated stroke.
    void group.getBoundingClientRect();
    group.classList.add('is-firing');
    const cleanup=window.setTimeout(()=>{
      circuit.timers.delete(cleanup);
      group.classList.remove('is-firing');
      schedule(circuit,group,random(1150,2400));
    },duration+25);
    circuit.timers.add(cleanup);
  },delay);
  circuit.timers.add(timer);
}
function start(circuit){
  if(circuit.visible || document.hidden || reduced.matches) return;
  circuit.visible=true;
  circuit.groups.forEach((group,i)=>schedule(circuit,group,random(140,900)+i*520));
}
if(!reduced.matches){
  if('IntersectionObserver' in window){
    const observer=new IntersectionObserver(entries=>{
      entries.forEach(({target,isIntersecting})=>{
        const c=[...circuits].find(item=>item.layer===target);
        if(!c) return;
        if(isIntersecting) start(c); else stop(c);
      });
    },{rootMargin:'80px',threshold:.01});
    circuits.forEach(c=>observer.observe(c.layer));
  } else circuits.forEach(start);
}
document.addEventListener('visibilitychange',()=>{
  if(document.hidden) circuits.forEach(stop);
  else circuits.forEach(c=>{
    const r=c.layer.getBoundingClientRect();
    if(r.bottom>0&&r.top<window.innerHeight) start(c);
  });
});
reduced.addEventListener?.('change',()=>{
  if(reduced.matches) circuits.forEach(stop);
  else circuits.forEach(c=>{
    const r=c.layer.getBoundingClientRect();
    if(r.bottom>0&&r.top<window.innerHeight) start(c);
  });
});

// Retain the short existing page transition without simulating a loading wait.
const showPage=()=>document.documentElement.classList.remove('ms-page-entering','ms-page-leaving');
if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',()=>requestAnimationFrame(()=>setTimeout(showPage,100)),{once:true});
else requestAnimationFrame(()=>setTimeout(showPage,100));
window.addEventListener('pageshow',showPage);
window.addEventListener('pagehide',()=>document.documentElement.classList.remove('ms-page-leaving'));
document.addEventListener('click',e=>{
  const a=e.target.closest('a[href]');
  if(!a || e.defaultPrevented || e.button!==0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.hasAttribute('download') || (a.target&&a.target!=='_self') || reduced.matches) return;
  let url;
  try{url=new URL(a.href,document.baseURI);}catch(_){return;}
  if(url.protocol!==location.protocol || url.host!==location.host ||
     (url.pathname===location.pathname && url.search===location.search) ||
     !url.pathname.endsWith('.html')) return;
  e.preventDefault();
  document.documentElement.classList.add('ms-page-leaving');
  window.setTimeout(()=>location.assign(url.href),165);
},true);
})();
