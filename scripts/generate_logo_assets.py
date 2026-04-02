"""
Generate all PNG logo assets from SVG sources.

Usage:
    pip install cairosvg
    python scripts/generate_logo_assets.py
"""

import os
from pathlib import Path

try:
    import cairosvg
except ImportError:
    raise SystemExit("Run: pip install cairosvg")

ASSETS = Path(__file__).parent.parent / "assets" / "logo"
SVGS = {
    "dark":        ASSETS / "memory-stack-logo.svg",
    "transparent": ASSETS / "memory-stack-logo-transparent.svg",
    "light":       ASSETS / "memory-stack-logo-light.svg",
    "mono":        ASSETS / "memory-stack-logo-monochrome.svg",
}

OUTPUTS = [
    # (subdir, filename, size, svg_variant)
    ("favicon",    "favicon-16x16.png",         16,   "dark"),
    ("favicon",    "favicon-32x32.png",          32,   "dark"),
    ("favicon",    "favicon-48x48.png",          48,   "dark"),
    ("app-icons",  "icon-192x192.png",          192,   "transparent"),
    ("app-icons",  "icon-512x512.png",          512,   "transparent"),
    ("social",     "social-400x400.png",        400,   "dark"),
    ("social",     "social-400x400-light.png",  400,   "light"),
    ("social",     "social-1200x1200.png",     1200,   "dark"),
    ("social",     "social-1200x1200-light.png",1200,  "light"),
    ("misc",       "logo-64x64.png",             64,   "transparent"),
    ("misc",       "logo-128x128.png",          128,   "transparent"),
    ("misc",       "logo-256x256.png",          256,   "transparent"),
]

def main():
    for subdir, filename, size, variant in OUTPUTS:
        out_dir = ASSETS / subdir
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / filename
        svg_path = SVGS[variant]

        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(out_path),
            output_width=size,
            output_height=size,
        )
        print(f"  ✓ {subdir}/{filename} ({size}x{size})")

    print(f"\nDone — {len(OUTPUTS)} files generated in {ASSETS}")

if __name__ == "__main__":
    main()
