from interfaces.output_schema import MolecularOutput, PipelineOutput
from mappings.molecular_to_receptor import map_molecular_to_receptor
from mappings.receptor_to_signaling import map_receptor_to_signaling
from mappings.signaling_to_cellular import map_signaling_to_cellular


class IntegrationEngine:
    def run(self, molecular_output: MolecularOutput) -> PipelineOutput:
        receptor_output = map_molecular_to_receptor(molecular_output)
        signaling_output = map_receptor_to_signaling(receptor_output)
        cellular_output = map_signaling_to_cellular(signaling_output)

        return PipelineOutput(
            stage_outputs={
                "molecular": molecular_output,
                "receptor": receptor_output,
                "signaling": signaling_output,
                "cellular": cellular_output,
            },
            uncertainty_estimates={
                "molecular": molecular_output.confidence or 0.5,
                "receptor": receptor_output.confidence or 0.5,
                "signaling": signaling_output.confidence or 0.5,
                "cellular": cellular_output.confidence or 0.5,
            },
            selected_model="baseline_mechanistic_pipeline",
        )
