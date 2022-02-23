<center><h1>CATlyn</h1></center>

<br>

## :page_with_curl: Project Descrption

CATlyn is a wrapper around Riot endpoints. it is meant to provide all the useful informations one can look for when it comes to League of Legends.

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

After all those things are set up you can create a CATlyn instance in `main.py` and use its public methods to fetch informations!

For every other doubt i'm trying to keep all the docstring updated so you can just ask for `help()` about it.

And That's about it, you are good to go :smile:

## :heavy_exclamation_mark: Disclaimer

This code should not be used for production as i'm still a learner and it may be prone to bugs and not up to industry standards.
