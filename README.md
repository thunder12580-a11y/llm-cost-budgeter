# llm-cost-budgeter

A zero-dependency Python CLI utility to calculate token counts, estimate API query expenses, and block requests that breach token budget limits.

## Features
- **Fast Estimation:** Token estimates powered by word-ratio heuristics.
- **Cost Calculation:** Tracks pricing across modern Claude and OpenAI models.
- **Budget Capping:** Prevents accidental overspending on local LLM scripts.

## Installation & Usage

```bash
git clone [https://github.com/thunder12580-a11y/llm-cost-budgeter.git](https://github.com/thunder12580-a11y/llm-cost-budgeter.git)
cd llm-cost-budgeter

# Example Command
python main.py --prompt "Explain quantum computing in simple terms." --model claude-3-5-sonnet --limit 0.01
