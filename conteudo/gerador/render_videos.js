// Gera os vídeos verticais (Reels/TikTok) 1080x1920 a 30fps, quadro a quadro.
// A animação é determinística: window.render(t) desenha o instante t, o
// Playwright tira um print e o ffmpeg monta o MP4 (H.264 + faixa de áudio muda).
// uso: node render_videos.js [id ...]
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { chromium } = require('playwright');
const { FONT_LINK, BASE_CSS, BRAND_HTML, esc } = require('./estilo');

const W = 1080, H = 1920, FPS = 30;
const dados = JSON.parse(fs.readFileSync(path.join(__dirname, 'posts.json'), 'utf8'));
const SAIDA = path.join(__dirname, '..', 'midia', 'videos');

// Área segura: a interface do Reels/TikTok cobre ~380px embaixo e ~140px à direita.
const CSS = BASE_CSS + `
body{width:${W}px;height:${H}px;overflow:hidden}
#stage{position:absolute;inset:0}
.bg .g1{width:1100px;height:1100px}
.prog{position:absolute;top:70px;left:90px;right:90px;height:6px;border-radius:3px;background:rgba(255,255,255,.12);overflow:hidden;z-index:5}
.prog i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--blue),var(--green))}
.top{position:absolute;top:110px;left:90px;z-index:5}
.scene{position:absolute;left:90px;right:150px;top:260px;bottom:420px;display:flex;flex-direction:column;justify-content:center;opacity:0}
[data-at]{opacity:0}
.kicker{align-self:flex-start;font-size:36px;letter-spacing:4px;color:var(--green);border:3px solid rgba(61,214,140,.45);background:rgba(61,214,140,.08);padding:16px 30px;border-radius:999px;margin-bottom:56px}
.big{font-size:118px;line-height:1.02;font-weight:800;letter-spacing:-3.5px}
.big .w{display:inline-block;margin-right:.22em}
.mid{font-size:92px;line-height:1.06;font-weight:800;letter-spacing:-2.5px}
.sub{margin-top:48px;font-size:54px;color:var(--orange);font-weight:500;line-height:1.25}
.grad{background:linear-gradient(135deg,var(--blue),var(--green));-webkit-background-clip:text;color:transparent}
/* chat */
.phone{background:#0b141a;border-radius:48px;border:3px solid rgba(255,255,255,.1);overflow:hidden;box-shadow:0 40px 120px rgba(0,0,0,.5)}
.phone .hd{background:#1f2c34;padding:30px 36px;display:flex;align-items:center;gap:22px;font-size:38px;font-weight:600}
.phone .av{width:70px;height:70px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--green));display:flex;align-items:center;justify-content:center;color:#0d0f14;font-weight:800;font-size:28px}
.phone .hd small{display:block;font-size:26px;color:#8696a0;font-weight:400;margin-top:4px}
.phone .body{padding:40px 30px 50px;display:flex;flex-direction:column;gap:22px;min-height:700px}
.msg{max-width:82%;font-size:44px;line-height:1.3;padding:22px 30px 26px;border-radius:26px}
.msg.in{align-self:flex-start;background:#202c33;border-top-left-radius:6px}
.msg.out{align-self:flex-end;background:#005c4b;border-top-right-radius:6px}
.msg .h{display:block;text-align:right;font-size:24px;color:rgba(255,255,255,.55);margin-top:6px}
/* lista */
.lt{font-size:76px;font-weight:800;letter-spacing:-2px;margin-bottom:50px;line-height:1.08}
.li{display:flex;gap:34px;align-items:center;font-size:58px;line-height:1.2;font-weight:500;padding:34px 0;border-bottom:3px solid rgba(255,255,255,.07)}
.li b{flex:none;width:84px;height:84px;border-radius:22px;display:flex;align-items:center;justify-content:center;font-size:46px;background:rgba(61,214,140,.15);color:var(--green)}
.li.neg b{background:rgba(247,97,79,.15);color:var(--red)}
/* painel */
.dash{background:rgba(19,22,30,.92);border:3px solid rgba(255,255,255,.09);border-radius:40px;padding:50px}
.dash .t{font-size:44px;font-weight:700;margin-bottom:10px}
.dash .s{font-size:28px;color:var(--muted);margin-bottom:46px}
.bars{display:flex;align-items:flex-end;gap:14px;height:620px}
.bars i{flex:1;border-radius:10px 10px 4px 4px;background:rgba(79,142,247,.55);transform-origin:bottom}
.bars i.pk{background:var(--green)}
.axis{display:flex;justify-content:space-between;color:var(--muted);font-size:28px;margin-top:18px}
.cols{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
.col{background:var(--bg3);border-radius:26px;padding:26px;min-height:300px}
.col h4{font-size:30px;margin-bottom:20px;display:flex;justify-content:space-between}
.col .c{background:#232836;border-radius:16px;padding:20px 22px;margin-bottom:14px;font-size:28px;color:#c4c9d9;border-left:6px solid var(--blue)}
.pill{display:inline-block;margin-top:40px;font-size:30px;color:var(--muted)}
.cap{margin-top:46px;font-size:64px;font-weight:800;letter-spacing:-1.5px}
/* cta */
.ctab{align-self:flex-start;margin-top:60px;background:linear-gradient(135deg,var(--blue),#3a74e0);color:#fff;font-size:56px;font-weight:700;padding:38px 58px;border-radius:28px;box-shadow:0 26px 80px rgba(79,142,247,.4)}
.logo{width:150px;height:150px;border-radius:40px;background:linear-gradient(135deg,var(--blue),var(--green));display:flex;align-items:center;justify-content:center;font-size:64px;font-weight:800;color:#0d0f14;margin-bottom:60px}
`;

// --------------------------------------------------------------- cenas
const palavras = (txt, t0, passo) => esc(txt).split(' ')
  .map((w, i) => `<span class="w" data-at="${(t0 + i * passo).toFixed(2)}" data-a="up">${w}</span>`).join('');

function cena(c) {
  switch (c.tipo) {
    case 'gancho':
      return `<span class="kicker mono" data-at="0" data-a="pop">${esc(c.kicker)}</span>
        <div class="big">${palavras(c.texto, 0.25, 0.12)}</div>`;
    case 'texto':
      return `<div class="mid ${c.destaque ? 'grad' : ''}" data-at="0.05" data-a="up">${esc(c.texto)}</div>
        ${c.sub ? `<div class="sub" data-at="0.75" data-a="up">${esc(c.sub)}</div>` : ''}`;
    case 'chat': {
      const passo = (c.dur - 1.0) / c.msgs.length;
      const hora = ['23:47', '23:47', '23:48', '23:48'];
      return `<div class="phone" data-at="0" data-a="pop">
        <div class="hd"><div class="av">CR</div><div>${esc(dados.marca)}<small>online</small></div></div>
        <div class="body">${c.msgs.map(([d, txt], i) =>
          `<div class="msg ${d}" data-at="${(0.35 + i * passo).toFixed(2)}" data-a="${d === 'in' ? 'left' : 'right'}">${esc(txt)}<span class="h">${hora[i % 4]}${d === 'out' ? ' ✓✓' : ''}</span></div>`).join('')}
        </div></div>`;
    }
    case 'lista': {
      const passo = Math.min(0.9, (c.dur - 1.4) / c.itens.length);
      return `<div class="lt" data-at="0" data-a="up">${esc(c.titulo)}</div>
        ${c.itens.map((it, i) => `<div class="li ${c.negativo ? 'neg' : ''}" data-at="${(0.6 + i * passo).toFixed(2)}" data-a="left"><b>${c.negativo ? '✕' : '✓'}</b>${esc(it)}</div>`).join('')}`;
    }
    case 'painel':
      return `<div class="dash" data-at="0" data-a="pop">${painel(c.foco)}</div>
        <div class="cap" data-at="0.6" data-a="up">${esc(c.legenda)}</div>`;
    case 'cta':
      return `<div class="logo" data-at="0" data-a="pop">CR</div>
        <div class="mid" data-at="0.2" data-a="up">${esc(c.texto)}</div>
        <div class="ctab" data-at="0.6" data-a="pulse">${esc(c.sub)}</div>`;
  }
  throw new Error('cena desconhecida ' + c.tipo);
}

// Dados ilustrativos (não são de cliente real); o vídeo avisa na tela.
function painel(foco) {
  if (foco === 'dias') {
    const v = [42, 55, 48, 70, 63, 88, 36];
    return `<div class="t">Mensagens por dia</div><div class="s mono">painel CR · exemplo ilustrativo</div>
      <div class="bars">${v.map((x, i) => `<i style="height:${x}%" data-at="${(0.3 + i * 0.12).toFixed(2)}" data-a="grow" class="${x === 88 ? 'pk' : ''}"></i>`).join('')}</div>
      <div class="axis mono"><span>seg</span><span>ter</span><span>qua</span><span>qui</span><span>sex</span><span>sáb</span><span>dom</span></div>`;
  }
  if (foco === 'horas') {
    const v = [4, 2, 1, 1, 1, 2, 5, 12, 22, 30, 34, 31, 26, 28, 30, 29, 27, 30, 38, 55, 72, 90, 64, 25];
    return `<div class="t">Distribuição por hora</div><div class="s mono">painel CR · exemplo ilustrativo</div>
      <div class="bars" style="gap:6px">${v.map((x, i) => `<i style="height:${x}%" data-at="${(0.25 + i * 0.05).toFixed(2)}" data-a="grow" class="${x === 90 ? 'pk' : ''}"></i>`).join('')}</div>
      <div class="axis mono"><span>0h</span><span>6h</span><span>12h</span><span>18h</span><span>23h</span></div>`;
  }
  const col = (nome, cor, cards, t0) => `<div class="col"><h4>${nome}<span style="color:${cor}">${cards.length}</span></h4>
    ${cards.map((c, i) => `<div class="c" style="border-left-color:${cor}" data-at="${(t0 + i * 0.25).toFixed(2)}" data-a="left">${c}</div>`).join('')}</div>`;
  return `<div class="t">CRM · Gestão de contatos</div><div class="s mono">arraste os cartões · exemplo ilustrativo</div>
    <div class="cols">${col('Novo contato', 'var(--blue)', ['Mariana · preço', 'João · horário'], 0.3)}
    ${col('Interessado', 'var(--orange)', ['Clínica Sol · orçamento'], 0.8)}
    ${col('Agendado', 'var(--purple)', ['Pedro · sex 9h', 'Ana · sáb 10h'], 1.1)}
    ${col('Concluído', 'var(--green)', ['Rafael · pago'], 1.6)}</div>`;
}

function html(v) {
  let t = 0;
  const cenas = v.cenas.map((c, i) => {
    const s = `<div class="scene" data-start="${t.toFixed(2)}" data-dur="${c.dur}" data-i="${i}">${cena(c)}</div>`;
    t += c.dur;
    return s;
  }).join('');
  return { total: t, doc: `<!doctype html><html><head><meta charset="utf-8">${FONT_LINK}<style>${CSS}</style></head><body>
  <div id="stage"><div class="bg"><div class="g1"></div><div class="g2"></div><div class="grid"></div></div>
  <div class="prog"><i></i></div><div class="top">${BRAND_HTML(esc(dados.marca))}</div>${cenas}</div>
  <script>
  const TOTAL=${t};
  const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
  const back=x=>{x=Math.min(Math.max(x,0),1);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
  window.render=function(t){
    document.querySelector('.prog i').style.width=(100*t/TOTAL)+'%';
    const g1=document.querySelector('.g1');
    g1.style.transform='translate('+(Math.sin(t*.5)*60)+'px,'+(Math.cos(t*.4)*50)+'px)';
    document.querySelectorAll('.scene').forEach(s=>{
      const st=+s.dataset.start,d=+s.dataset.dur,lt=t-st;
      const fin=Math.min(1,lt/0.22), fout=Math.min(1,(d-lt)/0.22);
      const vis=lt>=0&&lt<d;
      s.style.opacity=vis?Math.min(fin,fout):0;
      s.style.transform=vis?'translateY('+((1-ease(fin))*30-(1-ease(fout))*30)+'px)':'';
      if(!vis)return;
      s.querySelectorAll('[data-at]').forEach(e=>{
        const p=(lt-(+e.dataset.at))/0.45, a=e.dataset.a, k=ease(p);
        e.style.opacity=p<=0?0:Math.min(1,p*2.2);
        if(a==='up')e.style.transform='translateY('+((1-k)*60)+'px)';
        else if(a==='left')e.style.transform='translateX('+((1-k)*-80)+'px)';
        else if(a==='right')e.style.transform='translateX('+((1-k)*80)+'px)';
        else if(a==='pop')e.style.transform='scale('+(0.85+0.15*back(p))+')';
        else if(a==='grow'){e.style.opacity=p<=0?0:1;e.style.transform='scaleY('+k+')'}
        else if(a==='pulse'){const q=Math.max(0,lt-(+e.dataset.at)-0.5);e.style.transform='scale('+((0.85+0.15*back(p))*(1+0.035*Math.sin(q*6)))+')'}
      });
    });
  };
  </script></body></html>` };
}

function ffmpeg(saida) {
  return spawn('ffmpeg', ['-y', '-loglevel', 'error',
    '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100',
    '-shortest', '-map', '0:v', '-map', '1:a',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', String(FPS),
    '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', saida], { stdio: ['pipe', 'inherit', 'inherit'] });
}

(async () => {
  const filtro = process.argv.slice(2);
  fs.mkdirSync(SAIDA, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  for (const v of dados.videos) {
    if (filtro.length && !filtro.includes(v.id)) continue;
    const { total, doc } = html(v);
    await page.setContent(doc, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const mp4 = path.join(SAIDA, `${v.id}.mp4`);
    const ff = ffmpeg(mp4);
    const fim = new Promise((ok, erro) => ff.on('close', c => c === 0 ? ok() : erro(new Error('ffmpeg ' + c))));
    const n = Math.round(total * FPS);
    for (let f = 0; f < n; f++) {
      await page.evaluate(t => window.render(t), f / FPS);
      const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
    ff.stdin.end();
    await fim;
    // capa: fim da cena de gancho (texto todo visível)
    await page.evaluate(t => window.render(t), Math.min(v.cenas[0].dur - 0.3, 2.7));
    await page.screenshot({ path: path.join(SAIDA, `${v.id}-capa.jpg`), type: 'jpeg', quality: 92 });
    console.log(v.id, total.toFixed(1) + 's', n, 'quadros');
  }
  await browser.close();
})();
