import os
import os.path
import importlib
import sys


def build_examples():
    """
    Build the examples directory in /build under repository root.
    """
    target = os.path.normpath("build/examples")
    path = os.getcwd()
    sys.path.append(os.path.join(path, "pylib"))
    pending_dirs = [ "pylib/examples" ]

    while pending_dirs:
        basedir = os.path.normpath(pending_dirs.pop())
        for fn in os.listdir(basedir):
            if any(fn.startswith(x) for x in ["_", "."]):
                continue
            starget = os.path.join(basedir, fn)
            if os.path.isdir(starget):
                pending_dirs.append(starget)
            else:
                name = fn.strip(".py")
                rpathlist = starget.split(os.sep)[1:]
                modname = '.'.join(rpathlist).strip(".py")
                ftargetpath = os.path.join(target, os.path.join(*rpathlist[1:-1]))
                ftarget = os.path.join(ftargetpath, name + ".svg")
                print(starget)
                print("    =>", ftarget, "...")
                try:
                    os.makedirs(ftargetpath)
                except OSError:
                    pass
                mod = importlib.import_module(modname)
                svg = mod.make()
                svg.write(ftarget, 800, 600)


if __name__ == "__main__":
    import __main__
    path = os.path.basename(__main__.__file__).strip(".py")
    sys.path.append(os.path.join(path, "pylib"))
    build_examples()

