from workflows.closed_loop_pipeline import run_closed_loop_pipeline


def main():
    results = run_closed_loop_pipeline()

    print("MECHANISM-AI Prototype Pipeline")
    print("=" * 40)

    for stage, output in results.stage_outputs.items():
        print(f"\n[{stage.upper()}]")
        print(output)

    print("\nUncertainty Estimates:")
    for stage, score in results.uncertainty_estimates.items():
        print(f"  {stage}: {score:.3f}")

    print(f"\nSelected model: {results.selected_model}")


if __name__ == "__main__":
    main()
