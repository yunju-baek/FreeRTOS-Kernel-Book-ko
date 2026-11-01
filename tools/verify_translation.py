#!/usr/bin/env python3
"""Read-only structural checks for the Korean edition. Python 3 standard library.
Run from any directory: python3 tools/verify_translation.py
Optional JSON report: --report publish/translation-validation.json
This does not certify semantic accuracy or execute the example programs.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r'^ {0,3}(?P<fence>`{3,}|~{3,})[^\n]*\n(?P<code>.*?)^ {0,3}(?P=fence)[ \t]*$', re.M | re.S)
HEADING = re.compile(r'^ {0,3}(#{1,6}) +(.+)$', re.M)
CAPTION = re.compile(r'^ {0,3}\*\*\*(Figure|Listing|Example|Table|그림|코드|예제|표)\s+([0-9.]+)(?:\s*\([^*]+\))?\*\*\*\s+\*(.+)\*\s*$', re.M)
KINDS = {'그림': 'Figure', '코드': 'Listing', '예제': 'Example', '표': 'Table'}
HTML_ANCHOR = re.compile(r'<a\b[^>]*(?:id|name)=[\"\']([^\"\']+)[\"\'][^>]*>', re.I)
MARKDOWN_LINK = re.compile(r'(!?)\[([^\n]*?)\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)')
REPEATED_ENGLISH = re.compile(r'\b([A-Za-z][A-Za-z0-9_]*(?:[ -][A-Za-z][A-Za-z0-9_]*){0,5})\s*\(\s*\1\s*\)', re.I)
ENGLISH_CAPTION_LABEL = re.compile(r'^ {0,3}\*\*\*(?:그림|표|코드|예제) [\d.]+\s*\((?:Figure|Table|Listing|Example) [\d.]+\)', re.M)
GLOSSED_FILENAME = re.compile(r'\b[A-Za-z_]+\([^\n()]*[가-힣][^\n()]*\)\.[A-Za-z]+')


def without_code(text):
    return FENCE.sub('', text)


def anchors(text):
    result = set(HTML_ANCHOR.findall(text))
    # GitHub-style heading slugs; explicit original IDs are the primary contract.
    seen = Counter()
    for _, heading in HEADING.findall(without_code(text)):
        heading = re.sub(r'<[^>]+>', '', heading).lower()
        heading = re.sub(r'[^\w\- ]', '', heading).replace(' ', '-')
        count = seen[heading]
        result.add(heading + (f'-{count}' if count else ''))
        seen[heading] += 1
    return result


def image_paths(text):
    paths = [m[3] for m in MARKDOWN_LINK.finditer(text) if m[1]]
    return paths + re.findall(r'<img\b[^>]*src=[\"\']([^\"\']+)', text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'ko/translation-manifest.json').read_text())
    assets = json.loads((ROOT / 'ko/assets/manifest.json').read_text())
    errors, docs = [], []
    counts = Counter()
    texts = {}
    def check(ok, message):
        if not ok:
            errors.append(message)
    baseline = manifest['upstream']['commit']
    # All upstream-tracked book/code/license files remain identical, except the
    # Korean repository entry README, whose original is retained byte-for-byte.
    rows = subprocess.check_output(['git', 'ls-tree', '-r', '-z', baseline], cwd=ROOT).split(b'\0')
    for row in rows:
        if not row:
            continue
        meta, path_bytes = row.split(b'\t', 1)
        mode, kind, oid = meta.decode().split()
        relative = path_bytes.decode()
        if kind != 'blob':
            continue  # Nested submodules are pinned in .gitmodules and the manifest.
        path = ROOT / ('README.upstream.md' if relative == 'README.md' and (ROOT / 'README.upstream.md').exists() else relative)
        check(path.exists(), f'Upstream file missing: {relative}')
        if path.exists():
            data = path.read_bytes()
            actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            check(actual == oid, f'Upstream file changed: {relative}')
            counts['upstream_files'] += 1
    for entry in manifest['files']:
        src, dst = ROOT / entry['source_path'], ROOT / entry['translation_path']
        check(dst.exists(), f'Missing translation: {dst.name}')
        if not dst.exists():
            continue
        en, ko = src.read_text(), dst.read_text()
        texts[entry['translation_path']] = ko
        source_blob = hashlib.sha1(b'blob ' + str(src.stat().st_size).encode() + b'\0' + src.read_bytes()).hexdigest()
        check(source_blob == entry['source_blob_sha'], f'Manifest source blob: {src.name}')
        ac, bc = [m[0] for m in FENCE.finditer(en)], [m[0] for m in FENCE.finditer(ko)]
        check(ac == bc, f'Fenced code differs: {dst.name}')
        visible_prose = re.sub(r'<[^>]+>|`+[^`\n]*`+', '', without_code(ko))
        check(not REPEATED_ENGLISH.search(visible_prose), f'Repeated English gloss: {dst.name}')
        check(not ENGLISH_CAPTION_LABEL.search(visible_prose), f'English caption label: {dst.name}')
        check(not GLOSSED_FILENAME.search(visible_prose), f'Gloss inserted into filename: {dst.name}')
        eh, kh = HEADING.findall(without_code(en)), HEADING.findall(without_code(ko))
        if src.name.startswith('ch'):
            def structure(items):
                return [(len(level), re.match(r'[\d.]+', title)[0] if re.match(r'[\d.]+', title) else '') for level, title in items]
            check(structure(eh) == structure(kh), f'Heading hierarchy/number differs: {dst.name}')
        explicit_source = set(HTML_ANCHOR.findall(en))
        check(explicit_source <= anchors(ko), f'Original anchors missing: {dst.name}: {sorted(explicit_source - anchors(ko))}')
        a_caps = re.findall(r'^ {0,3}\*\*\*(Figure|Listing|Example|Table)\s+([0-9.]+)\*\*\*', en, re.M)
        b_caps = [(KINDS.get(k, k), n) for k, n in re.findall(r'^ {0,3}\*\*\*(Figure|Listing|Example|Table|그림|코드|예제|표)\s+([0-9.]+)(?:\s*\([^*]+\))?\*\*\*', ko, re.M)]
        check(a_caps == b_caps, f'Caption order/number differs: {dst.name}')
        check(set(re.findall(r'^\[\^([^]]+)\]:', en, re.M)) <= set(re.findall(r'^\[\^([^]]+)\]:', ko, re.M)), f'Footnotes missing: {dst.name}')
        counts.update(documents=1, code_blocks=len(ac), headings=len(kh), captions=len(a_caps))
        docs.append({'path': entry['translation_path'], 'code_blocks': len(ac), 'headings': len(kh), 'captions': len(a_caps)})
    # Also validate the edition's navigation, guidelines and review documentation.
    for path in [ROOT / 'README.md', ROOT / 'README.ko.md', ROOT / 'PROJECT_STATE.md', *(ROOT / 'ko').glob('*.md'), ROOT / 'ko/assets/README.md', ROOT / 'ko/assets/PRESERVED_IMAGES.ko.md']:
        if path.exists():
            texts.setdefault(str(path.relative_to(ROOT)), path.read_text())
    for relative, text in texts.items():
        path = ROOT / relative
        clean = without_code(text)
        links = [(m[3], bool(m[1]), m[2]) for m in MARKDOWN_LINK.finditer(clean)]
        links += [(url, False, '') for url in re.findall(r'<a\b[^>]*href=[\"\']([^\"\']+)', clean)]
        links += [(url, True, alt) for url, alt in re.findall(r'<img\b[^>]*src=[\"\']([^\"\']+)[\"\'][^>]*alt=[\"\']([^\"\']*)', clean)]
        for url, is_image, label in links:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            check(target.exists(), f'Broken local link: {relative} -> {url}')
            if is_image:
                counts['image_references'] += 1
                check(bool(label.strip()), f'Empty image alt: {relative} -> {url}')
            else:
                counts['local_links'] += 1
                if target.exists() and parts.fragment and target.suffix == '.md':
                    check(unquote(parts.fragment) in anchors(target.read_text()), f'Broken anchor: {relative} -> {url}')
        check(not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text), f'Unexpected control character: {relative}')
    for asset in assets['assets']:
        source, target = ROOT / asset['source_path'], ROOT / asset['target_path']
        check(source.exists(), f'Missing original asset: {source.name}')
        if source.exists():
            check(hashlib.sha256(source.read_bytes()).hexdigest() == asset['source_sha256'], f'Original asset hash: {source.name}')
        check(target.exists(), f'Missing target asset: {target.name}')
        expected_hash = asset.get('target_sha256')
        if expected_hash and target.exists():
            check(hashlib.sha256(target.read_bytes()).hexdigest() == expected_hash, f'Target asset hash: {target.name}')
        for ref in asset['references']:
            doc = ROOT / 'ko' / ref['source_document']
            actual_paths = {(doc.parent / url).resolve() for url in image_paths(doc.read_text())}
            check(target.resolve() in actual_paths, f'Asset mapping not used: {doc.name} -> {target.name}')
            check(asset['status'] in ('agent-checked', 'preserve-original'), f'Unchecked asset in book: {target.name}')
            counts['mapped_images'] += 1
        counts['source_assets'] += 1
    result = {'result': 'pass' if not errors else 'fail', 'baseline': baseline, 'counts': dict(counts), 'documents': docs, 'errors': errors,
              'scope': 'Structural validation only; excludes semantic certification, external URL availability, example execution and hardware testing.'}
    if args.report:
        report = args.report if args.report.is_absolute() else ROOT / args.report
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'documents'}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
