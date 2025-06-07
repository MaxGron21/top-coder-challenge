#!/usr/bin/env python3
import json
from run    import compute_reimbursement

# 1) Load private cases
with open('private_cases.json') as f:
    cases = json.load(f)

# 2) Open output
with open('private_results.txt', 'w') as out:
    # 3) Compute directly in Python (no subprocess)
    for c in cases:
        d = c['trip_duration_days']
        m = c['miles_traveled']
        r = c['total_receipts_amount']
        pred = compute_reimbursement(d, m, r)
        out.write(f"{pred:.2f}\n")
  

print("✅ Wrote private_results.txt")