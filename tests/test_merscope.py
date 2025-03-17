import json
import os
from rdm_models.merscope import Experiment


def test_merscope_experiment_creation():
    fixture_path = os.path.join(
        os.path.dirname(__file__), "fixtures", "merscope_experiment.json"
    )
    with open(fixture_path, "r", encoding="utf-8") as f:
        raw = json.load(f)

        parsed = Experiment.model_validate(raw)

    # Assert Experiment was created correctly from JSON
    assert parsed.experiment_id == raw["experimentId"]
    assert parsed.experiment_id == "deidentified_experiment_id"
    assert parsed.experiment_name == raw["experimentName"]
    assert parsed.experiment_name == "Deidentified Experiment"
    assert parsed.region_summaries[0].name == raw["regionSummaries"][0]["name"]
    assert parsed.region_summaries[0].name == "Region 1"
