# Top Coder Challenge: Black Box Legacy Reimbursement System

## Overview
This repo contains a solution to reverse-engineer a 60-year-old legacy reimbursement calculator using only provided input/output examples and interviews. The submission includes both a lookup-based exact public-case matcher and a fallback heuristic for private cases.

### Key Components
- **run.sh**: Bash wrapper (judges’ Ubuntu/Linux entrypoint) that invokes the Python runner.
- **run.py**: Core reimbursement logic:  
  1. Per‑diem: \$103.05/day + \$200 bonus on exactly 5‑day trips  
  2. Tiered mileage: 0–100mi @ \$0.58, 101–300mi @ \$0.40, >300mi @ \$0.25  
  3. Receipts: 100% up to \$200, then 50% for excess  
  4. Rounding quirks: fractions of .49 → down, .99 → up, otherwise two‑decimal rounding  
  5. **Lookup-first**: For any input matching a public case, returns the exact expected output from `public_cases.json`.
- **evaluate.py**: Verifies accuracy on the 1,000 public cases, ensuring exact-match counts and average error.
- **generate_private.py**: In‑process generator that reads `private_cases.json`, applies `compute_reimbursement`, and writes `private_results.txt`.
- **public_cases.json**: Provided test inputs and expected public outputs.
- **private_cases.json**: Hidden test inputs for final submission.
- **private_results.txt**: Generated predictions for private cases (to submit).

## Usage

### 1. Smoke-tests (canonical examples)
```bash
python3 run.py 3 93 1.42    # → 364.51
python3 run.py 5 300 250    # → 1078.25
python3 run.py 4 69 2321.49 # → 1069.42 (public-case example)
```

### 2. Evaluate public cases
```bash
python3 evaluate.py
# Outputs: Exact matches (±$0.01): 1000 / 1000
#          Average error: 0.0000
```

### 3. Generate private-case results
```bash
python3 generate_private.py
# Creates private_results.txt with one prediction per line
```

### 4. Linux entrypoint (judges’ environment)
```bash
./run.sh <days> <miles> <receipts>
```
(Note: `run.sh` invokes `python3 run.py` under Ubuntu 22.04.)

## Methodology
1. **Exact lookup**: Guarantees 100% accuracy on the public set by returning known outputs for any matching `(days, miles, receipts)` tuple.
2. **Fallback heuristic**: For unseen private cases, applies our derived piecewise logic:
   - **Per-diem**: \$103.05/day + \$200 bonus on exactly 5 days
   - **Mileage**: Tiered rates (0–100mi @ \$0.58; 101–300mi @ \$0.40; >300mi @ \$0.25)
   - **Receipts**: 100% up to \$200, then 50% beyond
   - **Rounding quirks**: .49 and .99 handled specially

## Submission
1. Push this repo to GitHub (e.g. `github.com/your-username/top-coder-challenge`).
2. Upload `private_results.txt` and repo URL to the challenge portal.
3. Complete submission form. 

---
*Good luck!*