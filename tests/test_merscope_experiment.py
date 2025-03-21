import json
import pytest
from rdm_models.merscope import Experiment


@pytest.fixture
def merscope_experiment_json_str():
    data = """
    {
      "softwareVersion": "1.0.0",
      "startDateTime": "2025-01-01T00:00:00+00:00",
      "endDateTime": "2025-01-01T00:00:00+00:00",
      "userId": "deidentified_user",
      "experimentId": "deidentified_experiment_id",
      "experimentName": "Deidentified Experiment",
      "experimentDescription": "",
      "experimentDirectory": "/deidentified/path",
      "codebookName": "deidentified_codebook.csv",
      "codebookId": "deidentified_codebook",
      "panelName": "deidentified_panel",
      "sampleThickness": "10",
      "additionalStains": ["Stain A", "Stain B", "Stain C", "Stain D", "Stain E"],
      "fiducialColor": "deidentified_color",
      "usedReadouts": ["Readout1", "Readout2", "Readout3", "Readout4"],
      "usedHybridizationBuffers": ["Buffer1", "Buffer2", "Buffer3"],
      "cartridgeBarcode": "deidentified_barcode",
      "regionSummaries": [
        { "name": "Region 1", "startIndex": 0, "endIndex": 1000 }
      ],
      "measurementStartDateTime": "2025-01-01T00:00:00+00:00",
      "fovCount": 1000,
      "runMode": "Experiment"
    }
    """
    return json.loads(data)


def test_merscope_experiment(merscope_experiment_json_str):
    parsed = Experiment.model_validate(merscope_experiment_json_str)

    assert parsed.experiment_id == merscope_experiment_json_str["experimentId"]
    assert parsed.experiment_id == "deidentified_experiment_id"
    assert parsed.experiment_name == merscope_experiment_json_str["experimentName"]
    assert parsed.experiment_name == "Deidentified Experiment"
    assert (
        parsed.region_summaries[0].name
        == merscope_experiment_json_str["regionSummaries"][0]["name"]
    )
    assert parsed.region_summaries[0].name == "Region 1"
    # etc...
