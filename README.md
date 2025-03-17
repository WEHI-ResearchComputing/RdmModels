# RDM Models

A shared library of Pydantic models for WEHI RDM.

## Installation

```bash
uv add git+ssh://git@github.com/WEHI-ResearchComputing/RdmModels.git
```

## Usage

```python
from rdm_models.merscope import Experiment

# Parse a JSON input
parsed = Experiment.model_validate('{"fooBar": 123}')
```
