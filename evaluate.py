#!/usr/bin/env python3
import json
import subprocess
import sys

def main():
    try:
        with open('public_cases.json') as f:
            cases = json.load(f)
    except FileNotFoundError:
        print("Error: public_cases.json not found", file=sys.stderr)
        sys.exit(1)

    total = len(cases)
    exact = 0
    total_error = 0.0

    for case in cases:
        inp = case['input']
        # Call our run.py
        proc = subprocess.run(
            ['python', 'run.py',
             str(inp['trip_duration_days']),
             str(inp['miles_traveled']),
             str(inp['total_receipts_amount'])],
            capture_output=True, text=True
        )
        if proc.returncode != 0:
            print("Error running run.py:", proc.stderr, file=sys.stderr)
            sys.exit(1)

        pred = float(proc.stdout.strip())
        exp  = float(case['expected_output'])
        err  = abs(pred - exp)

        if err <= 0.01:
            exact += 1
        total_error += err

    avg_err = total_error / total if total else 0.0
    print(f"Exact matches (±$0.01): {exact} / {total}")
    print(f"Average error: {avg_err:.4f}")

if __name__ == "__main__":
    main()
