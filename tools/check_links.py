"""Check that relative links in Markdown files resolve to real files or folders.

Usage:
    python tools/check_links.py            # README.md, docs/, shared/ and every Day folder
    python tools/check_links.py --web      # also check http(s) links (needs network)

The archive folder is not checked. Exit code 1 if any link is broken.
"""
import glob
import os
import re
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def md_files():
    files = glob.glob(os.path.join(ROOT, "*.md"))
    for pattern in ("docs/**/*.md", "shared/**/*.md", "Day*/**/*.md", "FDE-Mindset-Source/**/*.md"):
        files += glob.glob(os.path.join(ROOT, pattern), recursive=True)
    return sorted(set(f for f in files if "node_modules" not in f))


def check_web(url):
    import urllib.request
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "link-check"})
        urllib.request.urlopen(req, timeout=10)
        return True
    except Exception:
        return False


def main():
    web = "--web" in sys.argv
    broken, total = [], 0
    for f in md_files():
        text = open(f, encoding="utf-8").read()
        text = re.sub(r"```.*?```", "", text, flags=re.S)        # ignore links inside code blocks
        for target in LINK.findall(text):
            total += 1
            if target.startswith(("http://", "https://")):
                if web and not check_web(target):
                    broken.append((f, target))
                continue
            if target.startswith(("#", "mailto:")):
                continue
            path = unquote(target.split("#")[0])
            full = os.path.normpath(os.path.join(os.path.dirname(f), path))
            if not os.path.exists(full):
                broken.append((f, target))
    for f, t in broken:
        print(f"BROKEN  {os.path.relpath(f, ROOT)} -> {t}")
    print(f"{total - len(broken)}/{total} links OK.")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
