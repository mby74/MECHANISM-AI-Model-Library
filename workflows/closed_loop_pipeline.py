from interfaces.output_schema import MolecularOutput
from mediator.integration_engine import IntegrationEngine


def run_closed_loop_pipeline(binding_score: float = 0.75, confidence: float = 0.8):
    molecular_output = MolecularOutput(
        binding_score=binding_score,
        confidence=confidence,
        metadata={"source": "prototype_input"},
    )

    engine = IntegrationEngine()
    results = engine.run(molecular_output)
    return results
