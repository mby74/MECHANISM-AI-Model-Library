from interfaces.output_schema import MolecularOutput
from mappings.molecular_to_receptor import map_molecular_to_receptor


def test_molecular_to_receptor_mapping():
    mol = MolecularOutput(binding_score=0.8, confidence=0.9)
    rec = map_molecular_to_receptor(mol)
    assert rec.activation_state is not None
