<center><h1>CATlyn</h1></center>


[![Python Version](https://img.shields.io/static/v1?label=Python&message=v3.9.0&logo=python&logoColor=white&color=blue)](https://www.python.org/downloads/release/python-390/)
[![GitHub stars](https://img.shields.io/github/stars/TheUruz/CATlyn?style=flat&logo=github)](https://github.com/TheUruz/CATlyn/stargazers)

<br>

## :page_with_curl: Project Descrption

CATlyn is a wrapper around Riot API. it is meant to provide all the useful informations one can look for when it comes to League of Legends. This is an amateur work and still a WIP. Feel free to open pull requests to contribute, every help is very much appreciated :)

## :bulb: What do i need to run the code?

First you have to download the latest version of Riot's ***Data Dragon*** from [this page](https://developer.riotgames.com/docs/lol#data-dragon_versions) which is basically League of Legends's entire assets and data. After that, extract its content (which is a folder with the same name of the archive) and place it in the root directory of the project.

You will need to store your API key (get it from [here](https://developer.riotgames.com/) if you have not already. a developer key is enough to make this work) and place it in a json file along with your summoner name as follows

```json
    {
        "key": "your key",
        "summoner": "your in-game name"
    }
```

this above is how your `secrets.json` file should look like. Once you have it place it in the `/config_files` folder.

the last step depends on your intentions toward CATlyn:

- if you want to develop more functionalities run `python3 setup.py develop` to create a reference to the catlyn package in your current python environment.
- if you want to consume CATlyn's functionalities instead install it in your current environment with `python3 setup.py install`

both commands should be launched from the repository's root

For every other doubt i'm trying to keep all the docstring updated so you can just ask for `help()` about it.

And That's about it, you are good to go :smile:

## :heavy_exclamation_mark: Disclaimer

This code should not be used for production as i'm still a learner and it may be prone to bugs and not up to industry standards.

CATlyn is still under development and you can't yet download it from PyPI but as long as you download the source code from the repo and follow the steps above everything should work.