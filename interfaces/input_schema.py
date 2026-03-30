from dataclasses import dataclass, field
from typing import Dict, Any, Optional


@dataclass
class MolecularInput:
    binding_score: Optional[float] = None
    conformational_change_score: Optional[float] = None
    sequence_features: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ReceptorInput:
    activation_level: Optional[float] = None
    dimerization_probability: Optional[float] = None
    clustering_index: Optional[float] = None


@dataclass
class SignalingInput:
    receptor_activity: Optional[float] = None
    nfkb_baseline: Optional[float] = None
    pathway_parameters: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CellularInput:
    signaling_output: Optional[float] = None
    cytokine_baseline: Optional[float] = None
    gene_expression_context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExperimentalContext:
    cell_type: str = "BMDM"
    condition: str = "baseline"
    metadata: Dict[str, Any] = field(default_factory=dict)
