---
name: metricool-agendador
description: "Gera e agenda conteúdo da CR Automações (carrosséis e vídeos verticais) no Instagram e TikTok via Metricool. Use quando o usuário pedir novos posts, novas semanas de conteúdo, re-renderizar mídia ou agendar/reagendar posts no Metricool."
---

# Agendador Metricool — CR Automações

Substitui o passo "publish via Publora" das skills `ig-*`: aqui a publicação é
feita pelo conector **Metricool** (`mcp__Metricool_Social_Media_Management__*`).

## Fluxo

1. **Escrever** o conteúdo em `conteudo/gerador/posts.py` (um bloco por post),
   usando as skills `ig-content-planner`, `ig-carousel-planner`,
   `ig-caption-writer`, `ig-hashtag-strategist` e `ig-humanizer`.
   Nunca inventar número, resultado ou nome de cliente.
2. **Renderizar** (dentro de `conteudo/gerador/`):
   ```
   python3 exportar_json.py
   node render_carrosseis.js [ids]   # PNG 1080x1350 em conteudo/midia/carrosseis/<id>/
   node render_videos.js [ids]       # MP4 1080x1920 30fps em conteudo/midia/videos/
   ```
   Conferir algumas imagens/quadros antes de seguir.
3. **Commit + push**. A mídia precisa de URL pública: usar o raw do GitHub
   fixado no SHA do commit (não muda nem se a branch for apagada):
   `https://raw.githubusercontent.com/cauanrios9-eng/dashboard/<SHA>/conteudo/midia`
4. **Payloads**: `python3 gerar_plano.py <URL_BASE>` regenera `conteudo/PLANO.md`
   e `conteudo/metricool/<id>.json`.
5. **Agendar**: `getBrandSettings` (pega `blogId` e fuso) → para cada payload,
   `createScheduledPost(blogId, date=<data com offset>, info=<json>)`.
   Antes, `getScheduledPosts` no intervalo para não duplicar.
   Se a rede ainda não estiver conectada, o Metricool devolve erro: pedir ao
   usuário para conectar em app.metricool.com/brands/connections.

## Regras

- Carrossel: 2–10 imagens, só imagem. Vídeo: Reel no IG + vídeo no TikTok.
- 3–5 hashtags por post. Gancho nos primeiros 125 caracteres da legenda.
- `tiktokData.autoAddMusic: true` (os vídeos saem com áudio mudo). No Instagram,
  ideal é o usuário trocar o áudio por um em alta pelo app, ou usar
  `instagramData.audioConfiguration` se a conta for Business ligada a uma Página.
- Dados de painel nos vídeos são ilustrativos e o vídeo diz isso na tela.
