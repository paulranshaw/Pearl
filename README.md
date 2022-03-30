<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]]()
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

![Pearl](https://user-images.githubusercontent.com/78688623/160734480-1241d33f-7bd2-422c-b6b0-789eb8693da5.png)

**Pearl** is a custom [**Discord**](https://discord.com/) bot solution developed within [**discord.py**](https://github.com/Rapptz/discord.py), an API wrapper written in Python.

Inspired from living with a certain feline whilst being at university, **Pearl** has discovered the Internet and is interactive in a server near you!

<!-- TABLE OF CONTENTS -->
#### Table of Contents
* [Installation](#installation)
* [Commands](#commands)
* [License](#license)

<!-- INSTALLATION -->
## Installation

To run Pearl, download this repository and ensure that you are running `Python 3.5.3` or higher and have `discord.py[voice]` installed:

`python3 -m pip install -U discord.py[voice]`

Then set your bot token: `token=''` within `config.py`, run `pearl.py` and away you go!

<!-- COMMANDS -->
## Commands

| Command Usage | Description | Permission |
| ------- | ----------- | ----------- |
| `p!connect <@channel>` | **Pearl** will join the requested voice channel, if no channel param is provided Pearl will join the channel of the command author. | administrator |
| `p!disconnect` | **Pearl** will leave the current voice channel. | administrator |
| `p!say <content>` | **Pearl** will output the passed argument as a message within the current text channel. | administrator |

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/paulranshaw