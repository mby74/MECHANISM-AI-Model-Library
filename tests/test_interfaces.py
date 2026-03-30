from interfaces.input_schema import MolecularInput
from interfaces.output_schema import MolecularOutput


def test_molecular_input_creation():
    x = MolecularInput(binding_score=0.7)
    assert x.binding_score == 0.7


def test_molecular_output_creation():
    y = MolecularOutput(binding_score=0.8, confidence=0.9)
    assert y.confidence == 0.9
