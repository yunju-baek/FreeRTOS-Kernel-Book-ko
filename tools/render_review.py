#!/usr/bin/env python3
"""Build a local HTML review copy with pandoc. Canonical sources stay in ko/.
Requires pandoc on PATH. Output: publish/review/*.html (ignored by Git).
Preview from the repo root: python3 -m http.server 8765 --bind 127.0.0.1
Open http://127.0.0.1:8765/publish/review/toc.html
"""
import html
import json
import posixpath
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'publish/review'
CSS = '''body{margin:0;background:#fff;color:#20242a;font:17px/1.8 -apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo",sans-serif}main{max-width:1000px;margin:auto;padding:32px 28px}h1,h2,h3,h4{line-height:1.45;scroll-margin-top:20px}h2{margin-top:2.5em;border-bottom:1px solid #ddd;padding-bottom:.3em}a{color:#1261a0}img{display:block;max-width:100%;height:auto;margin:20px auto}pre{padding:18px;background:#f4f6f8;overflow:auto;font-size:14px;line-height:1.55}code{font-family:ui-monospace,monospace}table{border-collapse:collapse;display:block;overflow:auto;max-width:100%;font-size:15px}td,th{border:1px solid #cbd2d9;padding:8px 12px}th{background:#f1f4f7}blockquote{border-left:4px solid #bccbd8;margin:20px 0;padding:8px 18px;background:#f7f9fb}nav{font-size:14px;border-bottom:1px solid #ddd;padding:10px 0}figure{margin:24px 0}figcaption{text-align:center;font-size:15px} @media(max-width:600px){main{padding:18px 14px}body{font-size:16px}}'''


def main():
    if not shutil.which('pandoc'):
        raise SystemExit('pandoc is required; install it outside the repository.')
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((ROOT / 'ko/translation-manifest.json').read_text())
    sources = [ROOT / entry['translation_path'] for entry in manifest['files']]
    sources += [ROOT / 'ko/SOURCE_NOTES.md', ROOT / 'ko/REVIEW.md']
    rendered = {p.resolve(): p.stem + '.html' for p in sources if p.exists()}
    for source in sources:
        if not source.exists():
            continue
        body = subprocess.check_output(['pandoc', '-f', 'gfm+footnotes', '-t', 'html5', str(source)], text=True)
        def rewrite(match):
            attr, url = match[1], html.unescape(match[2])
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                return match[0]
            target = (source.parent / parts.path).resolve()
            new = rendered.get(target) or posixpath.relpath(target, OUT)
            if parts.fragment:
                new += '#' + parts.fragment
            return attr + '="' + html.escape(new, quote=True) + '"'
        body = re.sub(r'(href|src)="([^"]+)"', rewrite, body)
        page = '<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>FreeRTOS 한국어판 · '+html.escape(source.stem)+'</title><style>'+CSS+'</style><main><nav>비공식 한국어 번역 · <a href="toc.html">목차</a> · <a href="SOURCE_NOTES.html">원문 대조 사항</a></nav>'+body+'</main></html>'
        (OUT / (source.stem+'.html')).write_text(page)
    print(f'Rendered {len(rendered)} documents to publish/review/')


if __name__ == '__main__':
    main()
