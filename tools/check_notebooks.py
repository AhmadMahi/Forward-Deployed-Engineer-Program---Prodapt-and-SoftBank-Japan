"""Run every course notebook top to bottom in offline demo mode.

Usage:
    python tools/check_notebooks.py                 # all Day folders and the capstone
    python tools/check_notebooks.py Day12 Day13     # only folders whose name starts with these
    python tools/check_notebooks.py --skip-pip      # comment out `!pip install` lines (packages already installed)

Sets OFFLINE=1 so GenAI cells use the offline stand-in and never call an API.
Cells tagged `skip-offline-check` are skipped (use only for cells that need Docker, Azure or a GPU).
The archive folder is not checked. Exit code 1 if any notebook fails.
"""
import glob
import os
import sys
import tempfile

import nbformat
from nbclient import NotebookClient

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def prepare(nb, skip_pip):
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        if "skip-offline-check" in cell.metadata.get("tags", []):
            cell.source = "print('skipped in offline check')"
            continue
        if skip_pip:
            cell.source = "\n".join(
                ("# " + line) if line.lstrip().startswith(("!pip", "%pip", "!npm", "!apt")) else line
                for line in cell.source.split("\n"))
    return nb


def run(path, skip_pip):
    nb = prepare(nbformat.read(path, as_version=4), skip_pip)
    with tempfile.TemporaryDirectory() as tmp:
        client = NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata": {"path": tmp}})
        client.execute()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    skip_pip = "--skip-pip" in sys.argv
    os.environ["OFFLINE"] = "1"
    os.environ.pop("OPENAI_API_KEY", None)
    paths = sorted(glob.glob(os.path.join(ROOT, "Day*", "**", "*.ipynb"), recursive=True))
    paths = [p for p in paths if ".ipynb_checkpoints" not in p]
    if args:
        paths = [p for p in paths if any(os.path.relpath(p, ROOT).startswith(a) for a in args)]
    failed = []
    for p in paths:
        rel = os.path.relpath(p, ROOT)
        try:
            run(p, skip_pip)
            print(f"PASS  {rel}")
        except Exception as e:
            msg = str(e).strip().splitlines()
            print(f"FAIL  {rel}\n      {msg[-1] if msg else type(e).__name__}")
            failed.append(rel)
    print(f"\n{len(paths) - len(failed)}/{len(paths)} notebooks passed in offline mode.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
