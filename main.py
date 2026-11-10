import argparse
import sys

# Standard pricing estimates per 1,000 tokens in USD
PRICING_TABLE = {
    "claude-3-5-sonnet": {"input": 0.003, "output": 0.015},
    "claude-3-opus": {"input": 0.015, "output": 0.075},
    "gpt-4o": {"input": 0.005, "output": 0.015},
    "gpt-4o-mini": {"input": 0.00015, "output": 0.00060},
}

def estimate_tokens(text: str) -> int:
    """Estimates token count using standard word heuristic (1 word ≈ 1.33 tokens)."""
    words = len(text.split())
    return int(words * 1.33)

def calculate_cost(prompt: str, model: str = "claude-3-5-sonnet") -> tuple[int, float]:
    model_pricing = PRICING_TABLE.get(model, PRICING_TABLE["claude-3-5-sonnet"])
    tokens = estimate_tokens(prompt)
    cost = (tokens / 1000) * model_pricing["input"]
    return tokens, cost

def main():
    parser = argparse.ArgumentParser(description="LLM Cost & Token Budgeting Tool")
    parser.add_argument("--prompt", type=str, help="The prompt text to analyze")
    parser.add_argument("--model", type=str, default="claude-3-5-sonnet", help="Model name to estimate against")
    parser.add_argument("--limit", type=float, default=0.05, help="Budget limit cap in USD")

    args = parser.parse_args()

    if not args.prompt:
        print("Usage: python main.py --prompt \"Your text here\" --model claude-3-5-sonnet --limit 0.05")
        sys.exit(1)

    tokens, cost = calculate_cost(args.prompt, args.model)

    print(f"\n--- LLM Cost & Token Report ---")
    print(f"Target Model:    {args.model}")
    print(f"Estimated Tokens:{tokens}")
    print(f"Estimated Cost:  ${cost:.5f}")

    if cost > args.limit:
        print(f"\n[ALERT] Estimated cost of ${cost:.5f} EXCEEDS limit of ${args.limit:.5f}!")
    else:
        print(f"\n[OK] Prompt is within daily threshold budget.")

if __name__ == "__main__":
    main()
