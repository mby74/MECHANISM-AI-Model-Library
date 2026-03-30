from dataclasses import dataclass, field
from typing import Dict, Any, Optional


@dataclass
class MolecularOutput:
    binding_score: Optional[float] = None
    confidence: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ReceptorOutput:
    activation_state: Optional[float] = None
    dimerization_state: Optional[float] = None
    confidence: Optional[float] = None


@dataclass
class SignalingOutput:
    nfkb_response: Optional[float] = None
    trajectory_summary: Dict[str, Any] = field(default_factory=dict)
    confidence: Optional[float] = None


@dataclass
class CellularOutput:
    cytokine_output: Optional[float] = None
    phenotype_label: Optional[str] = None
    confidence: Optional[float] = None


@dataclass
class PipelineOutput:
    stage_outputs: Dict[str, Any] = field(default_factory=dict)
    uncertainty_estimates: Dict[str, float] = field(default_factory=dict)
    selected_model: Optional[str] = None
