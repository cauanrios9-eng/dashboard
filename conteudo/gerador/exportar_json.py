"""Exporta posts.py para posts.json (lido pelos renderizadores em Node)."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import posts

out = pathlib.Path(__file__).parent / "posts.json"
out.write_text(json.dumps({"marca": posts.MARCA, "fuso": posts.FUSO,
                           "carrosseis": posts.CARROSSEIS, "videos": posts.VIDEOS},
                          ensure_ascii=False, indent=1))
print("ok", out)
