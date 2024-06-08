from enum import Enum


class Provider(str, Enum):

    CIVITAI = "Civitai"
    OCTOML = "OctoML"
    SALADML = "SaladML"
    PICFINDER = "PicFinder"
    RUNPODS = "RunPods"
    VALDIAI = "ValdiAI"
    OCTOMLNEXT = "OctoMLNext"
    RUNDIFFUSION = "RunDiffusion"
    SALADSHARED = "SaladShared"
