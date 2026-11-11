// Gera os slides dos carrosséis em PNG 1080x1350 (4:5).
// uso: node render_carrosseis.js [id ...]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { FONT_LINK, BASE_CSS, BRAND_HTML, esc } = require('./estilo');

const W = 1080, H = 1350;
const dados = JSON.parse(fs.readFileSync(path.join(__dirname, 'posts.json'), 'utf8'));
const SAIDA = path.join(__dirname, '..', 'midia', 'carrosseis');

const CSS = BASE_CSS + `
.slide{position:relative;width:${W}px;height:${H}px;overflow:hidden}
.wrap{position:absolute;inset:0;padding:90px 90px 80px;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center}
.count{font-size:24px;color:var(--muted)}
.mid{flex:1;display:flex;flex-direction:column;justify-content:center}
.foot{display:flex;justify-content:space-between;align-items:center;color:var(--muted);font-size:26px}
.swipe{display:flex;align-items:center;gap:12px;color:var(--text);font-weight:500}
.swipe b{display:inline-flex;width:56px;height:56px;border-radius:50%;background:var(--blue);align-items:center;justify-content:center;font-size:30px;color:#fff}
.kicker{display:inline-block;align-self:flex-start;font-size:26px;letter-spacing:3px;color:var(--green);border:2px solid rgba(61,214,140,.4);background:rgba(61,214,140,.08);padding:12px 22px;border-radius:999px;margin-bottom:44px}
.capa h1{font-size:100px;line-height:1.02;font-weight:800;letter-spacing:-3px}
.capa .sub{margin-top:44px;font-size:38px;color:var(--orange);font-weight:500}
.num{font-size:150px;font-weight:800;line-height:1;letter-spacing:-4px;background:linear-gradient(135deg,var(--blue),var(--green));-webkit-background-clip:text;color:transparent;margin-bottom:36px}
.item h2{font-size:76px;line-height:1.06;font-weight:800;letter-spacing:-2px}
.item p,.ad p{margin-top:36px;font-size:42px;line-height:1.35;color:#c4c9d9}
.card{background:rgba(26,30,40,.85);border:2px solid rgba(255,255,255,.08);border-radius:32px;padding:48px 52px}
.ad .tag{font-size:26px;letter-spacing:3px;font-weight:700;margin-bottom:18px}
.ad .mito{font-size:64px;font-weight:800;line-height:1.08;letter-spacing:-1.5px}
.ad .mito.x{text-decoration:line-through;text-decoration-thickness:6px;text-decoration-color:var(--red);color:#aeb3c4}
.ad .seta{font-size:30px;letter-spacing:3px;color:var(--green);font-weight:700;margin:44px 0 0}
.lista h2{font-size:80px;font-weight:800;letter-spacing:-2px;margin-bottom:48px}
.lista li{list-style:none;font-size:46px;line-height:1.25;padding:30px 0 30px 80px;position:relative;border-bottom:2px solid rgba(255,255,255,.07)}
.lista li:before{content:"✓";position:absolute;left:0;top:28px;width:54px;height:54px;border-radius:14px;background:rgba(61,214,140,.15);color:var(--green);font-weight:800;display:flex;align-items:center;justify-content:center;font-size:32px}
.cta h2{font-size:88px;line-height:1.04;font-weight:800;letter-spacing:-2.5px}
.cta p{margin-top:40px;font-size:44px;line-height:1.35;color:#c4c9d9}
.cta .btn{margin-top:64px;align-self:flex-start;background:linear-gradient(135deg,var(--blue),#3a74e0);color:#fff;font-size:40px;font-weight:700;padding:30px 46px;border-radius:22px;box-shadow:0 20px 60px rgba(79,142,247,.35)}
`;

function corpoSlide(s) {
  switch (s.tipo) {
    case 'capa':
      return `<div class="mid capa"><span class="kicker mono">${esc(s.kicker)}</span>
        <h1>${destacar(esc(s.titulo))}</h1>${s.sub ? `<div class="sub">${esc(s.sub)} →</div>` : ''}</div>`;
    case 'item':
      return `<div class="mid item"><div class="num">${esc(s.n)}</div><h2>${esc(s.titulo)}</h2><p>${esc(s.corpo)}</p></div>`;
    case 'antesdepois': {
      const ruim = s.cor === 'vermelho', bom = s.cor === 'verde';
      const tag = bom ? `<div class="tag mono" style="color:var(--green)">${esc(s.n)} AUTOMAÇÃO</div>`
        : ruim ? `<div class="tag mono" style="color:var(--red)">${esc(s.n)} AUTOMAÇÃO</div>`
        : `<div class="tag mono" style="color:var(--red)">MITO #${esc(s.n)}</div>`;
      const mitoCls = (ruim || bom) ? 'mito' : 'mito x';
      const seta = (ruim || bom) ? '' : `<div class="seta mono">NA REAL ↓</div>`;
      return `<div class="mid ad"><div class="card" style="${bom ? 'border-color:rgba(61,214,140,.45)' : ruim ? 'border-color:rgba(247,97,79,.4)' : ''}">
        ${tag}<div class="${mitoCls}">${esc(s.mito)}</div>${seta}<p>${esc(s.verdade)}</p></div></div>`;
    }
    case 'lista':
      return `<div class="mid lista"><h2>${esc(s.titulo)}</h2><ul>${s.itens.map(i => `<li>${esc(i)}</li>`).join('')}</ul></div>`;
    case 'cta':
      return `<div class="mid cta"><h2>${destacar(esc(s.titulo))}</h2><p>${esc(s.corpo)}</p><div class="btn">${esc(s.acao)}</div></div>`;
  }
  throw new Error('tipo desconhecido ' + s.tipo);
}

// pinta de verde a palavra-chave mais forte do título
function destacar(t) {
  return t.replace(/(WhatsApp|automação de WhatsApp|automação|perdendo cliente|4 mentiras|Dois finais diferentes\.|4 colunas|não perder venda|preço\.)/i, '<span class="hl">$1</span>');
}

function html(c, s, i) {
  const total = c.slides.length;
  const ultimo = i === total - 1;
  return `<!doctype html><html><head><meta charset="utf-8">${FONT_LINK}<style>${CSS}</style></head><body>
  <div class="slide"><div class="bg"><div class="g1"></div><div class="g2"></div><div class="grid"></div></div>
  <div class="wrap">
    <div class="top">${BRAND_HTML(dados.marca)}<span class="count mono">${i + 1}/${total}</span></div>
    ${corpoSlide(s)}
    <div class="foot"><span class="mono">automação de whatsapp + crm</span>${ultimo ? '' : '<span class="swipe">arrasta <b>→</b></span>'}</div>
  </div></div></body></html>`;
}

(async () => {
  const filtro = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  for (const c of dados.carrosseis) {
    if (filtro.length && !filtro.includes(c.id)) continue;
    const dir = path.join(SAIDA, c.id);
    fs.mkdirSync(dir, { recursive: true });
    for (const [i, s] of c.slides.entries()) {
      await page.setContent(html(c, s, i), { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      const f = path.join(dir, `slide-${String(i + 1).padStart(2, '0')}.png`);
      await page.screenshot({ path: f });
    }
    console.log(c.id, c.slides.length, 'slides');
  }
  await browser.close();
})();
