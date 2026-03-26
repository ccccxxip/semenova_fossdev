from pathlib import Path

SRC_DIR = Path("src")
REQ_FILE = Path("requirements.txt")

all_imports = set()
for py_file in SRC_DIR.rglob("*.py"):
    with open(py_file) as f:
        for line in f:
            line = line.strip()
            if line.startswith("import "):
                name = line.split()[1].split(".")[0]
                all_imports.add(name)
            elif line.startswith("from "):
                name = line.split()[1].split(".")[0]
                all_imports.add(name)

if not REQ_FILE.exists():
    print("не нашли requirements.txt")
    exit(1)

declared = set()
with open(REQ_FILE) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            declared.add(line.split("==")[0])

missing = all_imports - declared
if missing:
    print("не хватает requirements.txt:", ", ".join(sorted(missing)))
    exit(1)
else:
    print("все есть :)")

