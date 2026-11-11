"""Gera conteudo/PLANO.md (calendário + legendas) e conteudo/metricool/*.json
(payloads prontos para o createScheduledPost do Metricool).

uso: python3 gerar_plano.py [URL_BASE_DA_MIDIA]
URL_BASE padrão: raw do GitHub fixado num commit (passe o SHA depois do push).
"""
import json, pathlib, sys
from datetime import datetime

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import posts

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
BASE = sys.argv[1] if len(sys.argv) > 1 else \
    "https://raw.githubusercontent.com/cauanrios9-eng/dashboard/claude/instagram-tiktok-auto-content-zwpd0u/conteudo/midia"


def texto_final(p):
    return p["legenda"] + "\n\n" + " ".join(p["hashtags"])


def quando(p):
    d = datetime.fromisoformat(p["data"])
    return f'{DIAS[d.weekday()]} {d:%d/%m %H:%M}'


def payload(p, video):
    if video:
        media = [f'{BASE}/videos/{p["id"]}.mp4']
        ig = {"type": "REEL", "showReelOnFeed": True, "isAiGenerated": False}
        tt = {"privacyOption": "PUBLIC_TO_EVERYONE", "isAigc": False,
              "title": p["cenas"][0]["texto"]}
    else:
        n = len(p["slides"])
        media = [f'{BASE}/carrosseis/{p["id"]}/slide-{i:02d}.png' for i in range(1, n + 1)]
        ig = {"type": "POST", "isAiGenerated": False}
        tt = {"privacyOption": "PUBLIC_TO_EVERYONE", "autoAddMusic": True, "photoCoverIndex": 0,
              "title": p["slides"][0]["titulo"][:90]}
    extra = {"videoThumbnailUrl": f'{BASE}/videos/{p["id"]}-capa.jpg'} if video else {}
    return {
        **extra,
        "autoPublish": True, "draft": False, "descendants": [], "firstCommentText": "",
        "hasNotReadNotes": False, "shortener": False, "smartLinkData": {"ids": []},
        "media": media, "mediaAltText": [],
        "providers": [{"network": "instagram"}, {"network": "tiktok"}],
        "publicationDate": {"dateTime": p["data"], "timezone": posts.FUSO},
        "text": texto_final(p),
        "instagramData": ig, "tiktokData": tt,
    }


todos = sorted([(p, False) for p in posts.CARROSSEIS] + [(p, True) for p in posts.VIDEOS],
               key=lambda x: x[0]["data"])

# ---- payloads Metricool
mdir = RAIZ / "metricool"
mdir.mkdir(exist_ok=True)
for p, v in todos:
    (mdir / f'{p["id"]}.json').write_text(json.dumps(payload(p, v), ensure_ascii=False, indent=1))

# ---- PLANO.md
L = [f"# Plano de conteúdo — {posts.MARCA}", "",
     "Instagram + TikTok · 2 semanas · 6 carrosséis + 6 vídeos (Reels/TikTok).",
     f"Fuso: `{posts.FUSO}`. Arquivos de mídia em `conteudo/midia/`.", "",
     "## Calendário", "", "| quando | id | formato | gancho | objetivo |", "|---|---|---|---|---|"]
for p, v in todos:
    gancho = p["cenas"][0]["texto"] if v else p["slides"][0]["titulo"]
    L.append(f'| {quando(p)} | `{p["id"]}` | {"Reel/TikTok" if v else "Carrossel"} | {gancho} | {p["formula"]} |')
L += ["", "Pilares: dor (cliente perdido) · educação (como funciona) · quebra de objeção · bastidores do painel · oferta.",
      "CTAs de comentário (AUTOMAÇÃO, PAINEL, FUNIL) servem para puxar a conversa pro direct.", ""]

for p, v in todos:
    L += ["---", "", f'## {p["id"]} · {"Vídeo" if v else "Carrossel"} · {quando(p)}', "", f'Fórmula: {p["formula"]}', ""]
    if v:
        L.append(f'Mídia: `midia/videos/{p["id"]}.mp4` (capa: `{p["id"]}-capa.jpg`)')
        L += ["", "**Cenas na tela:**", ""]
        for c in p["cenas"]:
            t = c.get("texto") or c.get("titulo") or c.get("legenda") or " / ".join(m[1] for m in c.get("msgs", []))
            extra = " · ".join(c.get("itens", [])) or c.get("sub", "")
            L.append(f'- `{c["tipo"]}` ({c["dur"]}s): {t}' + (f" — {extra}" if extra else ""))
        L += ["", f'**Fala (opcional, se quiser gravar voz por cima):** {p["roteiro_fala"]}']
    else:
        L.append(f'Mídia: `midia/carrosseis/{p["id"]}/slide-01..{len(p["slides"]):02d}.png`')
        L += ["", "**Slides:**", ""]
        for i, s in enumerate(p["slides"], 1):
            t = s.get("titulo") or s.get("mito")
            L.append(f"{i}. {t}")
    L += ["", "**Legenda:**", "", "```", texto_final(p), "```", ""]

(RAIZ / "PLANO.md").write_text("\n".join(L))
print("PLANO.md +", len(todos), "payloads em", mdir)
