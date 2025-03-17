# RDM Models

A shared library of Pydantic models for WEHI RDM.

## Installation

```bash
uv sync
```

## Testing

```bash
pytest tests/
```

## Building the Package

```bash
uv build

# This builds to $root/dist
# To use in another project, do `uv pip install /path/to/root/dist/rdm_models-X.Y.Z-py3-none-any.whl`
```
