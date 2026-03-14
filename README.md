# Regression Flakiness Scorer

> **Part of the [Telecom Test Toolkit](https://github.com/telecom-test-tools/telecom-test-toolkit) ecosystem.**

### The "Regression Flakiness Scorer"

**The Problem:**
When we trigger daily executions for gNB and simulator builds, we often encounter "flaky" tests—test cases that fail randomly due to test environment glitches, simulator timing issues, or CPU spikes, rather than genuine bugs in the 5G NodeB software.

**The Solution:**
A lightweight analytics script that parses your daily regression result files (like CSVs) over a rolling window (e.g., 14 builds). It calculates a "Flakiness Score" for each test case based on state transitions and generates a simple, color-coded HTML heatmap showing the pass/fail history.

#### Features
1. **Data Harvesting & Memory:** Merges daily test result CSVs into a running history.
2. **Scoring Logic:** Stability calculation based on state transitions (Pass <-> Fail flips).
3. **Visual Output:** Generates a static HTML heatmap.

#### Usage
Install via pip:
```bash
pip install .
```

Run via the command line:
```bash
flakiness-scorer --input test_results.csv --history historical_data.csv
```

* `--input`: (Required) Path to the latest daily test results CSV.
* `--history`: (Optional) Path to historical data CSV.
* `--output`: (Optional) Path to save HTML output.
* `--window`: (Optional) Number of latest builds to track (default: 14).

## 🌐 Part of Telecom Test Toolkit

This project is part of the **Telecom Test Toolkit ecosystem**.

Other tools:
- [telecom-test-toolkit](https://github.com/telecom-test-tools/telecom-test-toolkit) (Orchestrator)
- [testwatch](https://github.com/telecom-test-tools/testwatch)
- [5g-log-analyzer](https://github.com/telecom-test-tools/5g-log-analyzer)
- [5gtestscope](https://github.com/telecom-test-tools/5gtestscope)
- [test-report-gen](https://github.com/telecom-test-tools/test-report-gen)
- [test-monitor-dashboard](https://github.com/telecom-test-tools/test-monitor-dashboard)

🔗 Main project:
https://github.com/telecom-test-tools/telecom-test-toolkit
