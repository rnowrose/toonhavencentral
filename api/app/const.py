from enum import Enum


class GameCategory(Enum):
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
        (MAIN_GAME, 'Main Game'),
        (DLC_ADDON, 'DLC Addon'),
        (EXPANSION, 'Expansion'),
        (BUNDLE, 'Bundle'),
        (STANDALONE_EXPANSION, 'Standalone Expansion'),
        (MOD, 'Mod'),
        (EPISODE, 'Episode'),
        (SEASON, 'Season'),
        (REMAKE, 'Remake'),
        (REMASTER, 'Remaster'),
        (EXPANDED_GAME, 'Expanded Game'),
        (PORT, 'Port'),
        (FORK, 'Fork'),
        (PACK, 'Pack'),
        (UPDATE, 'Update'),
    )
    Map = dict(Choices)

class Status(Enum):
    RELEASED = 0
    ALPHA = 2
    BETA = 3
    EARLY_ACCESS = 4
    OFFLINE = 5
    CANCELLED = 6
    RUMORED = 7
    DELISTED = 8
    Choices = (
        (RELEASED, 'Released'),
        (ALPHA, 'Alpha'),
        (BETA, 'Beta'),
        (EARLY_ACCESS, 'Early Access'),
        (OFFLINE, 'Offline'),
        (CANCELLED, 'Cancelled'),
        (RUMORED, 'Rumored'),
        (DELISTED, 'Delisted'),
    )
    Map = dict(Choices)

class WebsiteCategory(Enum):
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
        (OFFICIAL, 'Official'),
        (WIKIA, 'Wikia'),
        (WIKIPEDIA, 'Wikipedia'),
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (TWITCH, 'Twitch'),
        (INSTAGRAM, 'Instagram'),
        (YOUTUBE, 'Youtube'),
        (IPHONE, 'IPhone'),
        (IPAD, 'IPad'),
        (ANDROID, 'Android'),
        (STEAM, 'Steam'),
        (REDDIT, 'Reddit'),
        (ITCH, 'Itch'),
        (EPICGAMES, 'Epic Games'),
        (GOG, 'GOG'),
        (DISCORD, 'Discord'),
    )
    
class UserGameStatus(Enum):
    NOT_PLAYING = 0
    PLAN_TO_PLAY = 1
    CURRENTLY_PLAYING = 2
    FINISHED = 3
    FAVORITE = 10
    STOP_PLAYING = -1
    Choices = (
        (NOT_PLAYING, 'Not Playing'), 
        (CURRENTLY_PLAYING, 'Currently Playing'),
        (FINISHED, 'Finished'),
        (STOP_PLAYING, 'Stop Playing')
    )
    