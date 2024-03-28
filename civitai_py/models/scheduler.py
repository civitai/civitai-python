# scheduler.py

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Scheduler(str, Enum):
    """
    Scheduler
    """

    """
    allowed enum values
    """
    EULERA = 'EulerA'
    EULER = 'Euler'
    LMS = 'LMS'
    HEUN = 'Heun'
    DPM2 = 'DPM2'
    DPM2A = 'DPM2A'
    DPM2SA = 'DPM2SA'
    DPM2M = 'DPM2M'
    DPMSDE = 'DPMSDE'
    DPMFAST = 'DPMFast'
    DPMADAPTIVE = 'DPMAdaptive'
    LMSKARRAS = 'LMSKarras'
    DPM2KARRAS = 'DPM2Karras'
    DPM2AKARRAS = 'DPM2AKarras'
    DPM2SAKARRAS = 'DPM2SAKarras'
    DPM2MKARRAS = 'DPM2MKarras'
    DPMSDEKARRAS = 'DPMSDEKarras'
    DDIM = 'DDIM'
    PLMS = 'PLMS'
    UNIPC = 'UniPC'
    UNDEFINED = 'Undefined'
    LCM = 'LCM'
    DDPM = 'DDPM'
    DEIS = 'DEIS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Scheduler from a JSON string"""
        return cls(json.loads(json_str))
