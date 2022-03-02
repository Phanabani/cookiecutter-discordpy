# {{ cookiecutter.project_name }}

[![release](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_github }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_github }}/releases)
[![license](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_github }})](LICENSE)

{{ cookiecutter.project_short_description }}

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Config](#config)
- [Commands](#commands)
- [Developers](#developers)
- [License](#license)

## Install

### Prerequisites

- [Poetry](https://python-poetry.org/docs/#installation) – dependency manager
- (Optional) pyenv – Python version manager
    - [pyenv](https://github.com/pyenv/pyenv) (Linux, Mac)
    - [pyenv-win](https://github.com/pyenv-win/pyenv-win) (Windows)
- (Optional) [PM2](https://pm2.keymetrics.io/docs/usage/quick-start) – process manager

### Install {{ cookiecutter.project_name }}

To get started, clone the repo.

```shell
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug_github }}.git
cd {{ cookiecutter.project_slug_github }}
```

Install the dependencies with Poetry. {{ cookiecutter.project_name }} requires Python {{ cookiecutter.python_version }}+.

```shell
poetry install --no-root --no-dev
```

## Usage

### Set up configuration

Create a json file `{{ cookiecutter.project_slug }}/config.json` (or copy [{{ cookiecutter.project_slug }}/config_example.json]({{ cookiecutter.project_slug }}/config_example.json)).
The only value you need to set is the `bot_token`.

```json
{
    "bot_token": "YOUR_BOT_TOKEN"
}
```

See [config](#config) for more info.

### Running {{ cookiecutter.project_name }}

#### Basic

In the top level directory, simply run {{ cookiecutter.project_name }} as a Python module with Poetry.

```shell script
poetry run python -m {{ cookiecutter.project_slug }}
```

#### With PM2

You can run the bot as a background process using PM2. Ensure you've followed
the virtual environment setup described above, then simply run the following
command in {{ cookiecutter.project_name }}'s root directory:

```shell script
pm2 start
```

This starts the process as a daemon using info from [ecosystem.config.js](ecosystem.config.js).

### Inviting {{ cookiecutter.project_name }} to your Discord server

{{ cookiecutter.project_name }} requires the following permissions to run normally:

{% for perm in cookiecutter.discord_permissions.split(', ') -%}
- {{ perm }}
{% endfor %}
## Config

{{ cookiecutter.project_name }} can be configured with a JSON file at `{{ cookiecutter.project_slug }}/config.json`.
[{{ cookiecutter.project_slug }}/config_example.json]({{ cookiecutter.project_slug }}/config_example.json) contains
default values and can be used as a template. `bot_token` is the only required
field.

See [Config](docs/config.md) for detailed information about setting up the
config file.

## Commands

See [Commands](docs/commands.md) for info about {{ cookiecutter.project_name }}'s commands.

## Developers

### Installation

Follow the installation steps in [install](#install) and use Poetry to 
install the development dependencies:

```bash
poetry install --no-root
```

## License

[MIT © {{ cookiecutter.full_name }}.](LICENSE)
