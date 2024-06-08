from enum import Enum


class AssetType(str, Enum):

    LORA = "Lora"
    HYPERNETWORK = "Hypernetwork"
    TEXTUALINVERSION = "TextualInversion"
    LYCORIS = "Lycoris"
    CHECKPOINT = "Checkpoint"
    VAE = "Vae"
    LOCON = "LoCon"
    CONTROLNET = "ControlNet"
