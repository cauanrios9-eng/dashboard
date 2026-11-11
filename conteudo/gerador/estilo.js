// Identidade visual compartilhada (cores do painel.html da CR Automações)
const FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800&family=DM+Mono:wght@500&display=block" rel="stylesheet">';

const BASE_CSS = `
*{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#0d0f14;--bg2:#13161e;--bg3:#1a1e28;--text:#f0f2f7;--muted:#8a90a8;
--blue:#4f8ef7;--green:#3dd68c;--orange:#f7a94f;--purple:#a78bfa;--red:#f7614f}
html,body{background:var(--bg);color:var(--text);font-family:'DM Sans','Inter',sans-serif;-webkit-font-smoothing:antialiased}
.mono{font-family:'DM Mono',monospace}
.bg{position:absolute;inset:0;overflow:hidden;background:var(--bg)}
.bg .g1{position:absolute;width:900px;height:900px;border-radius:50%;filter:blur(140px);opacity:.35;background:var(--blue);top:-380px;right:-320px}
.bg .g2{position:absolute;width:700px;height:700px;border-radius:50%;filter:blur(140px);opacity:.22;background:var(--green);bottom:-320px;left:-280px}
.bg .grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:60px 60px;mask-image:linear-gradient(180deg,#000 0%,transparent 85%)}
.brand{display:flex;align-items:center;gap:14px;font-weight:700;font-size:28px;letter-spacing:-.3px}
.brand .dot{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,var(--blue),var(--green));display:flex;align-items:center;justify-content:center;font-size:20px;color:#0d0f14;font-weight:800}
.hl{color:var(--green)}
.hlb{color:var(--blue)}
`;

const BRAND_HTML = (marca) => `<div class="brand"><div class="dot">CR</div>${marca}</div>`;

const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

module.exports = { FONT_LINK, BASE_CSS, BRAND_HTML, esc };
