import hashlib, os, sys
def folder_receipt(root: str) -> str:
    h = hashlib.sha256()
    for dirpath, _, files in os.walk(root):
        for f in sorted(files):
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, root).replace(os.sep, "/")
            h.update(rel.encode())
            with open(p, "rb") as fh:
                for chunk in iter(lambda: fh.read(1 << 16), b""):
                    h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    print(folder_receipt(sys.argv[1] if len(sys.argv) > 1 else "."))
