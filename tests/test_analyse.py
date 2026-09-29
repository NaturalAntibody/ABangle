from pathlib import Path

import abangle.analyse as analyse


def test_analyse_uses_packaged_data_directory():
    """data/ now lives inside abangle/ (see setup.py package_data), so the primary
    path resolves directly; the repo-root fallback is no longer exercised here."""
    expected = Path(__file__).resolve().parents[1] / "abangle" / "data"

    assert Path(analyse.data_path) == expected


def test_analyse_uses_repo_config_fallback():
    expected = Path(__file__).resolve().parents[1] / "config"

    assert Path(analyse.config_path) == expected
