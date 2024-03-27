from nipoppy.tree import run

def test_tree_run(tmp_path):
    run(tmp_path)
    assert all((tmp_path / x).exists() for x in ["bids", "derivatives", "dicom", "proc", "tabular"])
