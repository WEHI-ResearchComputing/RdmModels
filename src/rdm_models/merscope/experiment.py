from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


# For use with JSON input that has camelCase keys
class BaseModelWithCamelAlias(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class RegionSummary(BaseModelWithCamelAlias):
    name: str
    start_index: int
    end_index: int


class Experiment(BaseModelWithCamelAlias):
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
