from enum import Enum


class Scheduler(str, Enum):

    EULERA = "EulerA"
    EULER = "Euler"
    LMS = "LMS"
    HEUN = "Heun"
    DPM2 = "DPM2"
    DPM2A = "DPM2A"
    DPM2SA = "DPM2SA"
    DPM2M = "DPM2M"
    DPMSDE = "DPMSDE"
    DPMFAST = "DPMFast"
    DPMADAPTIVE = "DPMAdaptive"
    LMSKARRAS = "LMSKarras"
    DPM2KARRAS = "DPM2Karras"
    DPM2AKARRAS = "DPM2AKarras"
    DPM2SAKARRAS = "DPM2SAKarras"
    DPM2MKARRAS = "DPM2MKarras"
    DPMSDEKARRAS = "DPMSDEKarras"
    DDIM = "DDIM"
    PLMS = "PLMS"
    UNIPC = "UniPC"
    UNDEFINED = "Undefined"
    LCM = "LCM"
    DDPM = "DDPM"
    DEIS = "DEIS"
