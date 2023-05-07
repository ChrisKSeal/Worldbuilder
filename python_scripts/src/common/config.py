# pylint: disable=too-few-public-methods

"""Use pydantic and TOML to read in and configure things."""

from pydantic import BaseModel  # pylint: disable=E0611
from pydantic_config import SettingsModel


class LoggingConfig(BaseModel):  # type: ignore[misc]
    """Pydantic dataclass to hold the logging details.

    Attributes:
        BaseModel (_type_): _description_
    """

    level: str
    filename: str


class WorldBuilderConfig(SettingsModel):  # type: ignore[misc]
    """Pydantic settings from pydantic_settings package.

    Attributes:
        logging (LoggingConfig): Logging specific config.
    """

    logging: LoggingConfig

    class Config:  # pylint disable=R0903
        """Class specific config."""

        config_file = "worldbuilder.toml"
