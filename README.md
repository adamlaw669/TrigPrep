# TrigPrep

A Streamlit application to help learn and practice trig ratios with active recall.

## Run locally

1. Create a virtual environment (recommended) and install dependencies:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   streamlit run trig.py
   ```

## Change the UI / Theme

You can customize colors, fonts, and base theme via Streamlit's theme config at `.streamlit/config.toml`.

```toml
[theme]
base = "light"            # "light" or "dark"
primaryColor = "#3B82F6"  # Accent color
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F8FAFC"
textColor = "#0F172A"
font = "sans serif"        # "sans serif", "serif", or "monospace"
```

After saving changes, reload the Streamlit page to see the updated UI.

## Features

- Single-question quiz flow with progress and score
- Sine, Cosine, Tangent modes with common angles
- Tolerance-based checking (`math.isclose`) with adjustable decimals
- Reference table for quick lookup

## Notes

- `tan(90°)` is undefined and excluded from questions.
