from typing import *

from pydantic import BaseModel, Field


class TimeSpan(BaseModel):
    """
    None model

    """

    ticks: Optional[int] = Field(alias="ticks", default=None)

    days: Optional[int] = Field(alias="days", default=None)

    hours: Optional[int] = Field(alias="hours", default=None)

    milliseconds: Optional[int] = Field(alias="milliseconds", default=None)

    microseconds: Optional[int] = Field(alias="microseconds", default=None)

    nanoseconds: Optional[int] = Field(alias="nanoseconds", default=None)

    minutes: Optional[int] = Field(alias="minutes", default=None)

    seconds: Optional[int] = Field(alias="seconds", default=None)

    totalDays: Optional[float] = Field(alias="totalDays", default=None)

    totalHours: Optional[float] = Field(alias="totalHours", default=None)

    totalMilliseconds: Optional[float] = Field(alias="totalMilliseconds", default=None)

    totalMicroseconds: Optional[float] = Field(alias="totalMicroseconds", default=None)

    totalNanoseconds: Optional[float] = Field(alias="totalNanoseconds", default=None)

    totalMinutes: Optional[float] = Field(alias="totalMinutes", default=None)

    totalSeconds: Optional[float] = Field(alias="totalSeconds", default=None)
