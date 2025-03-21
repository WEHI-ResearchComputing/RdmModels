from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelBase(BaseModel):
    """
    Base model for handling JSON input with camelCase keys.

    This configuration converts snake_case attribute names to camelCase keys during
    serialization and deserialization using Pydantic's alias generator.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class RegionSummary(CamelBase):
    name: str
    start_index: int
    end_index: int


class Experiment(CamelBase):
    """
    Model for the experiment.json metadata file output by the Merscope processing.
    """

    software_version: str
    start_date_time: str
    user_id: str
    experiment_id: str
    experiment_name: str
    experiment_description: str
    experiment_directory: str
    codebook_name: str
    codebook_id: str
    panel_name: str
    sample_thickness: str
    additional_stains: list[str]
    fiducial_color: str
    used_readouts: list[str]
    used_hybridization_buffers: list[str]
    cartridge_barcode: str
    region_summaries: list[RegionSummary]
    measurement_start_date_time: str
    end_date_time: str
    fov_count: int
    run_mode: str
