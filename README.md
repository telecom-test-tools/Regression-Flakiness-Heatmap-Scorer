# Regression-Flakiness-Heatmap-Scorer


### Innovation Idea: The "Regression Flakiness Heatmap & Scorer"

**The Problem:**
When we trigger daily executions for gNB and simulator builds, we often encounter "flaky" tests—test cases that fail randomly due to test environment glitches, simulator timing issues, or CPU spikes, rather than genuine bugs in the 5G NodeB software. When we see a failure, we waste time debating, "Is this a real software bug, or did the simulator just choke again?" We often end up manually re-triggering the test just to see if it passes the second time.

**The Solution:**
A lightweight analytics script that parses your daily regression result files (like JUnit XML, CSV, or whatever your test framework outputs) over a rolling 14-day window. It calculates a "Flakiness Score" for each test case and generates a simple, color-coded HTML heatmap showing the pass/fail history across recent gNB builds.

#### How It Works (The Workflow):

1. **Data Harvesting:** After the nightly regression completes, a Python script quickly scoops up the test result file.
2. **Scoring Logic:** The script looks at the historical data for each Test Case ID.
* If a test fails on Build A, passes on Build B, and fails on Build C (without any related code commits), it flags the test as **High Flakiness**.
* If a test consistently passes, and then suddenly fails continuously after a specific gNB software upgrade, it flags it as a **Hard Failure** (highly likely to be a real bug).


3. **Visual Output:** The script generates a static HTML page with a grid. The rows are Test Case IDs, the columns are Build Numbers, and the cells are Green (Pass), Red (Fail), or Yellow (Flaky/Inconsistent).
4. **Notification:** It drops the link to this HTML dashboard into your team's chat (Teams, Slack, etc.) or emails it out with the morning regression summary.

#### Why is this "Easily Implementable"?

* **No Database Required:** You don’t need to set up a complex SQL database. The script can just keep a running CSV file as its "memory" of past executions.
* **Standard Libraries:** You only need Python with the `pandas` library to crunch the data and standard HTML/CSS to generate the table.
* **Passive Execution:** It simply reads post-execution reports. It doesn't interact with the live gNB or simulator, meaning there is zero risk of it breaking your actual test environment.

#### The Value Add (ROI):

* **Faster Triage:** Instead of manually investigating every red "FAIL", the team can instantly look at the heatmap. If it's flagged as "Flaky," they know to investigate the simulator environment first. If it's a "Hard Failure," they immediately raise a Problem Report.
* **Metrics for Management:** It provides concrete data to management to show *why* the automation team needs dedicated time to fix unstable test scripts or why the simulator vendor needs to fix stability issues.

---
