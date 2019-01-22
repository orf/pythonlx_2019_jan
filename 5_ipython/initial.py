import pdb

abc = 1

try:
    raise RuntimeError()
except Exception:
    pdb.set_trace()
