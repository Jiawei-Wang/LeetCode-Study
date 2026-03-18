from pydantic import BaseModel, ValidationError
from typing import Optional

class sensorPacket(BaseModel):
    timestamp: int  # milliseconds
    accel_x: float
    accel_y: float
    accel_z: float
    heart_rate: Optional[float] = None