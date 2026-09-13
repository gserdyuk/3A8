"""Check that the version probe's manifest matches the engine stamp of every agent on disk.

Usage: python tools/check_probe.py [repo_root]
"""
import re, sys, glob, os

root = sys.argv[1] if len(sys.argv) > 1 else "."
PROBE = os.path.join(root, "agents", "version-probe.md")

on_disk = {}
for path in glob.glob(os.path.join(root, "agents", "*.md")):
    name = os.path.splitext(os.path.basename(path))[0]
    if name == "version-probe":
        continue
    m = re.search(r"You are engine `([^`]+)`", open(path, encoding="utf-8").read())
    on_disk[name] = m.group(1) if m else None

text = open(PROBE, encoding="utf-8").read()
block = re.search(r"Reply with exactly these lines.*?```\r?\n(.*?)```", text, re.S)
manifest = {}
for line in (block.group(1).splitlines() if block else []):
    if line.strip():
        name, stamp = line.split(None, 1)
        manifest[name] = stamp.strip()

bad = 0
for name in sorted(set(on_disk) | set(manifest)):
    disk, probe = on_disk.get(name), manifest.get(name)
    if disk is None and name in on_disk:
        print(f"FAIL {name}: no 'You are engine `...`' line in its definition"); bad += 1
    elif disk != probe:
        print(f"FAIL {name}: on disk {disk!r}, probe says {probe!r}"); bad += 1
    else:
        print(f"ok   {name:<26} {disk}")
print(f"\n{len(on_disk)} agents, {bad} failing")
sys.exit(1 if bad else 0)
