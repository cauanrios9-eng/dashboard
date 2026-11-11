# Conteúdo Instagram + TikTok — CR Automações

| pasta / arquivo | o que é |
|---|---|
| `PLANO.md` | calendário das 2 semanas, slides, roteiros e legendas prontas |
| `midia/carrosseis/<id>/` | slides PNG 1080×1350 (4:5) de cada carrossel |
| `midia/videos/<id>.mp4` | vídeos 1080×1920 (Reels/TikTok) + `<id>-capa.jpg` |
| `metricool/<id>.json` | post pronto para o Metricool (Instagram + TikTok) |
| `gerador/posts.py` | **fonte de todo o texto**: edite aqui e renderize de novo |

## Gerar de novo / criar mais

```bash
cd conteudo/gerador
python3 exportar_json.py
node render_carrosseis.js          # ou: node render_carrosseis.js c01 c02
node render_videos.js              # ~2 min por vídeo
python3 gerar_plano.py <URL_BASE>  # atualiza PLANO.md e metricool/*.json
```

Ou peça ao Claude: "cria mais 2 semanas de conteúdo e agenda no Metricool"
(ele segue `.claude/skills/metricool-agendador`).

## Antes de publicar

- Os vídeos saem com **áudio mudo**. No TikTok o Metricool liga `autoAddMusic`;
  no Instagram vale trocar por um áudio em alta pelo app (ou gravar a voz com o
  roteiro de fala do `PLANO.md`).
- Os gráficos do painel nos vídeos v03/v04 são **ilustrativos** (está escrito na tela).
  Quando tiver números reais de cliente, troque e ganhe prova social.
