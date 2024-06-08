from enum import Enum


class ImageTransformer(str, Enum):

    CANNY = "Canny"
    DEPTHZOE = "DepthZoe"
    SOFTEDGEPIDINET = "SoftedgePidinet"
    REMBG = "Rembg"
