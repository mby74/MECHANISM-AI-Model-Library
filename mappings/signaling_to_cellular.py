from interfaces.output_schema import SignalingOutput, CellularOutput


def map_signaling_to_cellular(signaling_output: SignalingOutput) -> CellularOutput:
    nfkb = signaling_output.nfkb_response or 0.0
    confidence = signaling_output.confidence or 0.5

    phenotype = "pro-inflammatory" if nfkb > 0.6 else "controlled"

    return CellularOutput(
        cytokine_output=nfkb,
        phenotype_label=phenotype,
        confidence=confidence,
    )
