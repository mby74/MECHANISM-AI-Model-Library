from interfaces.output_schema import MolecularOutput, ReceptorOutput


def map_molecular_to_receptor(molecular_output: MolecularOutput) -> ReceptorOutput:
    binding = molecular_output.binding_score or 0.0
    confidence = molecular_output.confidence or 0.5

    activation_state = min(1.0, max(0.0, 0.8 * binding))
    dimerization_state = min(1.0, max(0.0, 0.6 * binding))

    return ReceptorOutput(
        activation_state=activation_state,
        dimerization_state=dimerization_state,
        confidence=confidence,
    )
