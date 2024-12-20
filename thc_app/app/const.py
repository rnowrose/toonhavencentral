from enum import Enum


class GameCategory:
    MAIN_GAME = 0
    DLC_ADDON = 1
    EXPANSION = 2
    BUNDLE = 3
    STANDALONE_EXPANSION = 4
    MOD = 5
    EPISODE = 6
    SEASON = 7
    REMAKE = 8
    REMASTER = 9
    EXPANDED_GAME = 10
    PORT = 11
    FORK = 12
    PACK = 13
    UPDATE = 14
    Choices = (
        (MAIN_GAME, "Main Game"),
        (DLC_ADDON, "DLC Addon"),
        (EXPANSION, "Expansion"),
        (BUNDLE, "Bundle"),
        (STANDALONE_EXPANSION, "Standalone Expansion"),
        (MOD, "Mod"),
        (EPISODE, "Episode"),
        (SEASON, "Season"),
        (REMAKE, "Remake"),
        (REMASTER, "Remaster"),
        (EXPANDED_GAME, "Expanded Game"),
        (PORT, "Port"),
        (FORK, "Fork"),
        (PACK, "Pack"),
        (UPDATE, "Update"),
    )
    Map = dict(Choices)


class Status:
    RELEASED = 0
    ALPHA = 2
    BETA = 3
    EARLY_ACCESS = 4
    OFFLINE = 5
    CANCELLED = 6
    RUMORED = 7
    DELISTED = 8
    Choices = (
        (RELEASED, "Released"),
        (ALPHA, "Alpha"),
        (BETA, "Beta"),
        (EARLY_ACCESS, "Early Access"),
        (OFFLINE, "Offline"),
        (CANCELLED, "Cancelled"),
        (RUMORED, "Rumored"),
        (DELISTED, "Delisted"),
    )
    Map = dict(Choices)


class WebsiteCategory:
    OFFICIAL = 1
    WIKIA = 2
    WIKIPEDIA = 3
    FACEBOOK = 4
    TWITTER = 5
    TWITCH = 6
    INSTAGRAM = 8
    YOUTUBE = 9
    IPHONE = 10
    IPAD = 11
    ANDROID = 12
    STEAM = 13
    REDDIT = 14
    ITCH = 15
    EPICGAMES = 16
    GOG = 17
    DISCORD = 18
    Choices = (
        (OFFICIAL, "Official"),
        (WIKIA, "Wikia"),
        (WIKIPEDIA, "Wikipedia"),
        (FACEBOOK, "Facebook"),
        (TWITTER, "Twitter"),
        (TWITCH, "Twitch"),
        (INSTAGRAM, "Instagram"),
        (YOUTUBE, "Youtube"),
        (IPHONE, "IPhone"),
        (IPAD, "IPad"),
        (ANDROID, "Android"),
        (STEAM, "Steam"),
        (REDDIT, "Reddit"),
        (ITCH, "Itch"),
        (EPICGAMES, "Epic Games"),
        (GOG, "GOG"),
        (DISCORD, "Discord"),
    )
    Map = dict(Choices)


class UserGameStatus:
    NOT_PLAYING = 0
    PLAN_TO_PLAY = 1
    CURRENTLY_PLAYING = 2
    FINISHED = 3
    FAVORITE = 10
    STOP_PLAYING = -1
    Choices = (
        (NOT_PLAYING, "Not Playing"),
        (CURRENTLY_PLAYING, "Currently Playing"),
        (FINISHED, "Finished"),
        (STOP_PLAYING, "Stop Playing"),
    )
    Map = dict(Choices)


class PlatformCategory:
    NONE = 0
    CONSOLE = 1
    ARCADE = 2
    PLATFORM = 3
    OPERATING_SYSTEM = 4
    PORTABLE_CONSOLE = 5
    COMPUTER = 6
    Choices = (
        (NONE, "----"),
        (CONSOLE, "Console"),
        (ARCADE, "Arcade"),
        (PLATFORM, "Platform"),
        (OPERATING_SYSTEM, "Operating System"),
        (PORTABLE_CONSOLE, "Portable Console"),
        (COMPUTER, "Computer"),
    )
    Map = dict(Choices)


class PlatformWebsite:
    OFFICIAL = 1
    WIKIA = 2
    WIKIPEDIA = 3
    FACEBOOK = 4
    TWITTER = 5
    TWITCH = 6
    INSTAGRAM = 8
    YOUTUBE = 9
    IPHONE = 10
    IPAD = 11
    ANDROID = 12
    STEAM = 13
    REDDIT = 14
    DISCORD = 15
    GOOGLE_PLUS = 16
    TUMBLR = 17
    LINKEDIN = 18
    PINTREST = 19
    SOUNDCLOUD = 20
    Choices = (
        (OFFICIAL, "Official"),
        (WIKIA, "Wikia"),
        (WIKIPEDIA, "Wikipedia"),
        (FACEBOOK, "Facebook"),
        (TWITTER, "Twitter"),
        (TWITCH, "Twitch"),
        (INSTAGRAM, "Instagram"),
        (YOUTUBE, "Youtube"),
        (IPHONE, "IPhone"),
        (IPAD, "IPad"),
        (ANDROID, "Android"),
        (STEAM, "Steam"),
        (REDDIT, "Reddit"),
        (DISCORD, "Discord"),
        (GOOGLE_PLUS, "Google Plus"),
        (TUMBLR, "Tumblr"),
        (LINKEDIN, "LinkedIn"),
        (PINTREST, "Pintrest"),
        (SOUNDCLOUD, "SoundCloud"),
    )
    Map = dict(Choices)

class ReleaseDateCategory:
    YYYYMMMMDD = 0;
    YYYYMMMM = 1
    YYYY = 2
    YYYYQ1 = 3
    YYYYQ2 = 4
    YYYYQ3 = 5
    YYYYQ4 = 6
    TBD = 7
    Choices = (
        (YYYYMMMMDD, "YYYYMMMMDD"),
        (YYYYMMMM, "YYYYMMMM"),
        (YYYY, "YYYY"),
        (YYYYQ1, "YYYYQ1"),
        (YYYYQ2, "YYYYQ2"),
        (YYYYQ3, "YYYYQ3"),
        (YYYYQ4, "YYYYQ4"),
        (TBD, "TBD"),
    )
    Map = dict(Choices)


class Region:
    EUROPE = 1
    NORTH_AMERICA = 2
    AUSTRAILIA = 3
    NEW_ZEALAND = 4
    JAPAN = 5
    CHINA = 6
    ASIA = 7
    WORLDWIDE = 8
    KOREA = 9
    BRAZIL = 10
    Choices = (
        (EUROPE, "Europe"),
        (NORTH_AMERICA, "North America"),
        (AUSTRAILIA, "Austrailia"),
        (NEW_ZEALAND, "New Zealand"),
        (JAPAN, "Japan"),
        (CHINA, "China"),
        (ASIA, "Asia"),
        (WORLDWIDE, "WorldWide"),
        (KOREA, "Korea"),
        (BRAZIL, "Brazil"),
    )
    Map = dict(Choices)


class Moods:
    Map = {
        "H": "Happy",  # the old spoon
        "F": "Relaxed",  # the new spoon
        "R": "Frustrated",
    }
