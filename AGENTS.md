# Agent Instructions

## Project shape

- This is a small Python research project focused on BDC and SEC EDGAR data.
- `BDC_exploring.ipynb` is the main exploratory workflow; `hello.py` is a small Python smoke example.
- Keep changes focused and easy to run from the repository root.

## Environment and validation

- Use the existing `.venv` when available.
- Install the pinned dependencies with `python -m pip install -r requirements.txt`.
- For Python-only changes, run `python -m py_compile hello.py`.
- For notebook changes, verify the file remains valid JSON and run cells in order when the required packages and SEC network access are available.
- Do not commit `.edgar-data` or other generated cache files.

## Python and notebook style

- Prefer the simplest readable implementation: direct code and existing pandas or edgartools APIs over new abstractions.
- Add comments for purpose, data-source assumptions, non-obvious transformations, and notebook steps. Avoid comments that merely restate the next line.
- Keep notebook cells small and sequential so intermediate DataFrames and API objects are easy to inspect.
- Preserve the notebook's valid JSON structure. Every cell must have `metadata.language` set to `markdown` or `python`; existing cells must retain a unique `metadata.id`.
- When editing notebook JSON, preserve existing outputs and metadata unless the change requires updating them. Do not expose credentials; use configuration or environment variables for identity values.

## Data and API behavior

- SEC requests require a valid identifying email through edgartools. Treat it as configuration, not source code to copy into new examples.
- Keep EDGAR cache data inside the project as configured by the notebook, and account for network-dependent results when validating.
- Preserve pinned versions in `requirements.txt` unless dependency updates are explicitly requested.

## Documentation

- Keep project-specific setup notes in [README.md](README.md); avoid duplicating them in code comments.