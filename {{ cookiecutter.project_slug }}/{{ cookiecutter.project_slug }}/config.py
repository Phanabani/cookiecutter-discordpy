from __future__ import annotations
from functools import cached_property
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Annotated, Literal, Union

from pydantic import BaseModel, Field, SecretStr, conint, validator

import {{ cookiecutter.project_slug }}

__all__ = [
    'Config',
    'ConfigBot',
    'ConfigLogging'
]

_root_path = Path({{ cookiecutter.project_slug }}.__path__[0])


def maybe_relative_path(path: Union[Path, str]):
    if not isinstance(path, Path):
        path = Path(path)
    if not path.is_absolute():
        return _root_path / path
    return path


class ConfigBot(BaseModel):
    command_prefix: str = '{{ cookiecutter.default_command_prefix }}'
    description: str = '{{ cookiecutter.project_short_description }}'


_logging_levels = Literal[
    'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
]


class ConfigLogging(BaseModel):

    class Config:
        allow_mutation = False
        validate_all = True
        keep_untouched = (cached_property,)

    {{ cookiecutter.project_slug }}_logging_level: _logging_levels = 'INFO'
    discord_logging_level: _logging_levels = 'WARNING'
    output_file: Path = Path('./logs/{{ cookiecutter.project_slug }}.log')
    when: Literal['S', 'M', 'H', 'D', 'midnight'] = 'midnight'
    interval: Annotated[int, conint(ge=1)] = 1
    backup_count: Annotated[int, conint(ge=0)] = 7
    format: str = "%(asctime)s %(levelname)s %(name)s | %(message)s"

    _normalize_output_file = validator('output_file', allow_reuse=True)(maybe_relative_path)

    @cached_property
    def formatter(self):
        return logging.Formatter(self.format)

    @cached_property
    def handler(self):
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        handler = TimedRotatingFileHandler(
            filename=self.output_file,
            when=self.when,
            interval=self.interval,
            backupCount=self.backup_count,
        )
        handler.setFormatter(self.formatter)
        return handler


class Config(BaseModel):
    bot_token: SecretStr
    bot: Annotated[ConfigBot, Field(default_factory=ConfigBot)]
    logging: Annotated[ConfigLogging, Field(default_factory=ConfigLogging)]
