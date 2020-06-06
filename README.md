# Tweenie

[![Discord](https://img.shields.io/discord/417389758470422538)](https://discord.gg/3aTVQtz)

Discord bot that uses NLP to add a reaction to messages when appropriate.

Makes use of:
* [smalld.py](https://github.com/princesslana/smalld.py)
* [torchMoji](https://github.com/huggingface/torchMoji)

## Usage

Is designed to be run with docker.

To build

```console
$ docker build . -t tweenie:latest
```

To run

```console
$ docker run -e SMALLD_TOKEN=<your token here> tweenie:latest
```

## Contact

Reach out to the [Discord Projects Hub](https://discord.gg/3aTVQtz)
