"""Subprocess harness for trusted local practice submissions (NOT a security sandbox)."""
from __future__ import annotations

import contextlib
import io
import json
import runpy
import sys
import traceback


def main() -> int:
    path = sys.argv[1]
    request = json.loads(sys.stdin.read())
    with contextlib.redirect_stdout(io.StringIO()):
        scope = runpy.run_path(path, run_name="__dsa_submission__")
    solve = scope.get("solve")
    if not callable(solve):
        raise TypeError("Expected a function named solve")
    results = []
    for args in request["cases"]:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                result = solve(*json.loads(json.dumps(args)))
            json.dumps(result, allow_nan=False)
            results.append({"value": result})
        except Exception as error:
            results.append({"error": type(error).__name__ + ": " + str(error)})
    print(json.dumps(results, ensure_ascii=False, allow_nan=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(type(error).__name__ + ": " + str(error), file=sys.stderr)
        sys.exit(1)
