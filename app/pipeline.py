"""Note processing pipeline: load, transform, and summarize notes."""
from app.pipeline_io import load_raw, save_summary
from app.pipeline_helpers import normalize, summarize


def run_pipeline(source: str, dest: str) -> dict:
    """Load notes from source, normalize, summarize, and write to dest."""
    raw = load_raw(source)
    cleaned = [normalize(r) for r in raw]
    summary = summarize(cleaned)
    save_summary(dest, summary)
    return summary
