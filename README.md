
# Tathyam: Academic RL Environments

&gt; *Automated AI agent evaluation for Indian academia, built by a recent AIML grad.*

**Status**: Pre-alpha. 10 environments in active development.

## Quick Start

```bash
# Install directly from GitHub
pip install -e git+https://github.com/tathyam-ai/academic-rl-envs.git#egg=tathyam

# Test your first environment
python -c "import tathyam; env = tathyam.load('debug-pytest'); print(env.reset())"

Environment Catalog

| Env Name           | Domain    | Description                         | Status         |
| ------------------ | --------- | ----------------------------------- | -------------- |
| `debug-pytest`     | Coding    | Fix a failing unit test             | 🚧 In Progress |
| `plan-trip`        | Reasoning | Plan a budget-constrained itinerary | 📝 Planned     |
| `extract-pdf`      | Tool-use  | Extract data from messy PDFs        | 📝 Planned     |
| `multi-hop-search` | Research  | Answer multi-hop Wikipedia queries  | 📝 Planned     |

Want an environment for your use case? Open an issue.

For Professors

Tired of manually grading AI projects?
Instant Feedback: Students get automated scores in 2 seconds
Plagiarism-Proof: Each task is unique; no copy-paste solutions
NEP 2020 Aligned: Skill-based evaluation, not memorization
Free Pilot: Email ruby@tathyam.ai to run Tathyam in your  AI courses for one semester. 
No setup, no cost.

For Students

Struggling to test your agent?

# Example: Evaluate your agent on a coding task
from tathyam import load

env = load('debug-pytest')
task = env.reset()
solution = my_agent.solve(task)
score = env.verify(solution)  # Instant feedback!

Contribute: Build a new environment → Earn ₹5,000 + recommendation letter.
Why India?
Cost: Runs entirely on AWS Mumbai free tier (no credit card needed)
Context: Tasks use Indian scenarios (GST calculations, local travel, etc.)
Support: Built by someone who faced the exact same problem you did
Contribute
Fork the repo
Create a new environment in tathyam/envs/
Add a test in tests/
Submit a pull request
We hire IIT/NIT interns. Current openings: GitHub Issues

Contact

GitHub: github.com/tathyam-ai

Made with ❤️ by a student, for students.


---

