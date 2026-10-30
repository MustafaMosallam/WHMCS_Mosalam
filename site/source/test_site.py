from pathlib import Path
from bs4 import BeautifulSoup
import asyncio,base64,mimetypes,re
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parent.parent
pages=list(ROOT.glob('**/index.html'))
errors=[]
for p in pages:
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for e in s.select('[href],[src]'):
  key='href' if e.has_attr('href') else 'src'
  target=e[key]
  if target.startswith(('http:','https:','mailto:','#','data:')):continue
  dest=(p.parent/target.split('#')[0]).resolve()
  if not dest.exists():errors.append((str(p.relative_to(ROOT)),target))
print('STATIC_PAGES',len(pages),'MISSING_REFERENCES',len(errors),errors[:8]);assert not errors

def inline_page(route):
 p=ROOT/route/'index.html' if route else ROOT/'index.html'
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for e in list(s.select('img[src],link[href],script[src]')):
  k='href' if e.name=='link' else 'src';v=e.get(k,'')
  if not v or v.startswith('http'):continue
  target=(p.parent/v).resolve()
  if e.name=='link' and e.get('rel')==['stylesheet']:
   css=target.read_text()
   css='\n'.join(line for line in css.splitlines() if not line.lstrip().startswith('@import '))
   def to_uri(m):
    src=m.group(1).strip("'\" ")
    if src.startswith('data:'):return m.group(0)
    f=(ROOT/src).resolve()
    if not f.exists():return m.group(0)
    return 'url("data:image/svg+xml;base64,'+base64.b64encode(f.read_bytes()).decode()+'")'
   css=re.sub(r'url\(([^)]+)\)',to_uri,css)
   tag=s.new_tag('style');tag.string=css;e.replace_with(tag)
  elif e.name=='script':
   tag=s.new_tag('script');tag.string=target.read_text();e.replace_with(tag)
  elif e.name=='img':
   mt=mimetypes.guess_type(target.name)[0] or 'image/svg+xml';e['src']='data:'+mt+';base64,'+base64.b64encode(target.read_bytes()).decode()
  elif e.name=='link' and e.get('rel')==['icon']:
   e.decompose()
 return str(s)
async def run():
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage','--no-proxy-server'])
  for width,name in [(1440,'desktop'),(390,'mobile'),(320,'small-mobile')]:
   page=await browser.new_page(viewport={'width':width,'height':900},device_scale_factor=1)
   reports=[];page.on('pageerror',lambda err:reports.append(str(err)))
   await page.set_content(inline_page(''),wait_until='domcontentloaded');await page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(x=>x.loading='eager')");await page.wait_for_timeout(250)
   result=await page.evaluate('''() => ({scroll:document.documentElement.scrollWidth,viewport:innerWidth,images:[...document.images].filter(x=>!x.complete||x.naturalWidth===0).length,heading:document.querySelector('h1')?.innerText})''')
   await page.screenshot(path=str(ROOT/'previews'/f'home-{name}.png'),full_page=True)
   if width<=390:
    await page.click('#menu-toggle');assert await page.locator('#nav-links').evaluate('(el)=>getComputedStyle(el).display')!='none';await page.click('#menu-toggle')
   await page.locator('[data-fit="team"]').click();assert 'application stack' in (await page.locator('#fit-title').inner_text()).lower()
   print('HOME',name,result,'ERRORS',reports)
   assert result['scroll']<=width+1 and not result['images'] and not reports
   await page.close()
  for slug in ['hosting/cpanel','servers/vps','servers/vds','cloud/managed','solutions/software-houses','contact/sales','pricing','domains','portal/overview','portal/tickets']:
   page=await browser.new_page(viewport={'width':390,'height':850});reports=[];page.on('pageerror',lambda err:reports.append(str(err)))
   await page.set_content(inline_page(slug),wait_until='domcontentloaded');await page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(x=>x.loading='eager')");await page.wait_for_timeout(200)
   data=await page.evaluate('''() => ({scroll:document.documentElement.scrollWidth,viewport:innerWidth,images:[...document.images].filter(x=>!x.complete||x.naturalWidth===0).length,heading:document.querySelector('h1')?.innerText})''')
   await page.screenshot(path=str(ROOT/'previews'/f'{slug.replace("/","-")}.png'),full_page=True)
   print('PAGE',slug,data,'ERRORS',reports)
   assert data['scroll']<=391 and not data['images'] and not reports
   if slug=='domains':
    await page.fill('#domain-input','mosalamtest.example');await page.click('#domain-form button');assert await page.locator('#domain-result').is_visible()
   if slug=='contact/sales':
    await page.fill('#project-name','Sample Person');await page.fill('#project-email','example@example.com');await page.click('#brief-form button[type=submit]');assert await page.locator('#brief-result').is_visible()
   if slug=='portal/tickets':
    await page.fill('#ticket-subject','Demo issue');await page.fill('#ticket-body','Description');await page.click('#ticket-form button');assert (await page.locator('#ticket-status').inner_text()).startswith(('Draft saved','Browser storage unavailable'))
   await page.close()
  await browser.close()
asyncio.run(run())
