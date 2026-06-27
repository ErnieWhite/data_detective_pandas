from levels import LEVELS

def main() -> None:
    score = 0
    print("🕵️ Welcome to Data Detective: Pandas Edition")
    print("Solve each case using data reasoning. Type 'hint' if you get stuck.\n")
    for i, level in enumerate(LEVELS, start=1):
        print(f"\n--- Level {i}/{len(LEVELS)} ---")
        won = level.run_level()
        score += int(won)
    print("\n" + "=" * 72)
    print(f"Final score: {score}/{len(LEVELS)}")
    if score == len(LEVELS):
        print("🏆 Perfect investigation. You cracked every case!")
    elif score >= len(LEVELS) * 0.7:
        print("🎯 Strong detective work. Review the reference solutions and replay to master them.")
    else:
        print("📚 Good start. Replay the levels and practice each pandas pattern in a notebook.")
    print("="*72)

if __name__ == '__main__':
    main()
