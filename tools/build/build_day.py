"""Build one or more day folders from tools/build/specs/dayNN.py.

Usage:
    python tools/build/build_day.py 12          # one day
    python tools/build/build_day.py 2 3 4       # several days
    python tools/build/build_day.py all         # every spec found

Writes the deck, pre-read, post-read, hands-on PDF, workbook and Colab notebook.
App_Build_Prompts.md, the quiz and Hotel_Lab.md are plain files kept in the day folder.
"""
import glob
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import fde_render as R  # noqa: E402


def load(n):
    path = os.path.join(HERE, "specs", f"day{int(n):02d}.py")
    s = importlib.util.spec_from_file_location(f"day{int(n):02d}", path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def build(n):
    spec = load(n)
    folder = os.path.join(ROOT, spec.FOLDER)
    os.makedirs(folder, exist_ok=True)
    p = f"Day{spec.DAY:02d}_"
    slug = spec.SLUG
    out = {
        "deck": os.path.join(folder, f"{p}Deck_{slug}.pptx"),
        "pre": os.path.join(folder, f"{p}PreRead_{slug}.pdf"),
        "post": os.path.join(folder, f"{p}PostRead_{slug}_Recap_and_Beyond.pdf"),
        "hands": os.path.join(folder, f"{p}HandsOn_Problem_Statements.pdf"),
        "wb": os.path.join(folder, f"{p}Workbook_Interactive.docx"),
        "nb": os.path.join(folder, f"{p}{slug}_Colab.ipynb"),
    }
    R.build_deck(spec, out["deck"])
    R.build_read(spec, "pre", out["pre"])
    R.build_read(spec, "post", out["post"])
    R.build_handson(spec, out["hands"])
    R.build_workbook(spec, out["wb"])
    R.build_notebook(spec, out["nb"])
    for extra in getattr(spec, "EXTRA_NOTEBOOKS", []):
        R.build_notebook(extra, os.path.join(folder, extra.FILENAME))
    print(f"Day {spec.DAY:02d}: built {len(out)} files in {spec.FOLDER}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["all"]:
        args = sorted(int(os.path.basename(f)[3:5]) for f in glob.glob(os.path.join(HERE, "specs", "day*.py")))
    for a in args:
        build(a)
