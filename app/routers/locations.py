from fastapi import APIRouter

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("")
def get_locations():
    return {
        "columns": ["id", "location"],
        "data": [
            [0, {"country": "Argentina", "city": "Buenos Aires", "latitude": -34.6037, "longitude": -58.3816}],
            [1, {"country": "Chile", "city": "Santiago", "latitude": -33.4489, "longitude": -70.6693}],
            [5, {"country": "Brasil", "city": "São Paulo", "latitude": -23.5505, "longitude": -46.6333}],
        ],
    }
