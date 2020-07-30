# Tweenie

[![Discord](https://img.shields.io/discord/417389758470422538)](https://discord.gg/3aTVQtz)

Discord bot that uses NLP to add a reaction to messages when appropriate.

Makes use of:
* [smalld.py](https://github.com/princesslana/smalld.py)
* [torchMoji](https://github.com/huggingface/torchMoji)

## Invite

[Invite Tweenie to your server.](https://discord.com/api/oauth2/authorize?client_id=718890456108499015&permissions=0&scope=bot)

## Self Host

Tweenie is designed to be run with Docker.

```console
$ docker run -e SMALLD_TOKEN=<your token here> tweenie:latest
```

## Building

To build with Docker:

```console
$ docker build . -t tweenie:latest
```

## Contact

Reach out to the [Discord Projects Hub](https://discord.gg/3aTVQtz)
