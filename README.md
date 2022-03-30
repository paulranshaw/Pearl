![Pearl](https://user-images.githubusercontent.com/78688623/160734480-1241d33f-7bd2-422c-b6b0-789eb8693da5.png)

**Pearl** is a custom [**Discord**](https://discord.com/) bot solution developed within [**discord.py**](https://github.com/Rapptz/discord.py), an API wrapper written in Python.

Inspired from living with a certain feline whilst being at university, **Pearl** has discovered the Internet and is interactive in a server near you!

#### Table of Contents
* [Installation](#installation)
* [Commands](#commands)
* [License](#license)

## Installation

To run Pearl, download this repository and ensure that you are running `Python 3.5.3` or higher and have `discord.py[voice]` installed:

`python3 -m pip install -U discord.py[voice]`

Then set your bot token: `token=''` within `config.py`, run `pearl.py` and away you go!

## Commands

| Command Usage | Description | Permission |
| ------- | ----------- | ----------- |
| `p!connect <@channel>` | **Pearl** will join the requested voice channel, if no channel param is provided Pearl will join the channel of the command author. | administrator |

## License

Distributed under the MIT License. See `LICENSE` for more information.