from interfaces.output_schema import ReceptorOutput, SignalingOutput


def map_receptor_to_signaling(receptor_output: ReceptorOutput) -> SignalingOutput:
    activation = receptor_output.activation_state or 0.0
    dimerization = receptor_output.dimerization_state or 0.0
    confidence = receptor_output.confidence or 0.5

    nfkb_response = 0.5 * activation + 0.5 * dimerization

    return SignalingOutput(
        nfkb_response=nfkb_response,
        trajectory_summary={
            "activation": activation,
            "dimerization": dimerization,
        },
        confidence=confidence,
    )
