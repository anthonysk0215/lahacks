from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class LocationInput(BaseModel):
    latitude: float
    longitude: float
    timestamp: Optional[datetime] = None
    landmarks: Optional[List[dict]] = None

    class Config:
        arbitrary_types_allowed = True

class Landmark(BaseModel):
    id: str
    name: str
    latitude: float
    longitude: float
    description: Optional[str] = None
    category: str
    rating: Optional[float] = None
    distance: Optional[float] = None
    estimated_time: Optional[int] = None
    crowd_level: Optional[str] = None
    best_time_to_visit: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True

class TourRecommendation(BaseModel):
    landmarks: List[Landmark]
    route_order: List[int]
    total_time: int

    class Config:
        arbitrary_types_allowed = True 