# Myme

Map scores in [MyAnimeList](https://myanimelist.net/) list exports to new values.

## Rationale

MyAnimeList's list export format is the most common format used for transferring lists across anime list sites (think [AniList](https://anilist.co/), [Kitsu](https://kitsu.io/), and [Anime-Planet](https://anime-planet.com)). This causes issues with the other sites, however, as the format is optimized for MyAnimeList. Me personally, I use AniList and occasionally create exports of [my lists](https://anilist.co/user/KlayLay/) on [AniList](https://anilist.co/) with [MAL Scraper](https://malscraper.azurewebsites.net/). It works, but uses AniList's score mapping, since the site supports more scoring systems than MyAnimeList's 10-points system. This is a bit annoying, as the scores they map to aren't consistent with how I treat them (e.g. a 2-star on AniList should always be a 4 on MyAnimeList and not a 3).

Myme is a simple tool which takes a MAL list export and remaps the scores based on input.

## Installation

1. Download or clone the repository (e.g. `git clone https://github.com/KyleErhabor/myme`)
2. Run `python3 myme/main.py <input> <mappings...>`

## Usage

The first argument to the program is the path to the MAL list export. A mapping is an existing score (i.e. a score in the list export) matched with a new score. The scores are separated by colons, and the mappings are separated by spaces. The existing score supports ranges to map multiple existing scores to a single new score.

### Examples

On AniList, the 5-star scoring system uses five stars to denote user rating. This maps MAL ratings 1 and 2 to a 1, 3 and 4 to a 4, 5 and 6 to a 6, 7 and 8 to an 8, and 9 and 10 to a 10.

```sh
python3 myme/main.py ~/Downloads/anime.xml 1-2:1 3-4:4 5-6:6 7-8:8 9-10:10
```

In total, there are only five ratings that can be assigned in this form.

If you use the 3-smileys scoring system, you could map 1s, 2s, and 3s, and 4s to a 4, 5s, 6s, and 7s to a 5, and 8s, 9s, and 10s to a 6.

```sh
python3 myme/main.py ~/Downloads/anime.xml 1-4:4 5-7:5 8-10:6
```

Remember, this is mapping MAL scores to new MAL scores. This just may be useful when exporting from other sites.
