from fastapi import APIRouter

router = APIRouter(prefix="/colors", tags=["colors"])


@router.get("")
def get_colors():
    return {
        "columns": ["id", "timestamp", "color"],
        "data": [
            [0, None, "rojo"],
            [1, "2016-07-02 12:21:23", "amarillo"],
            [5, "2016-07-02 13:22:56", "rojo"],
            [1, "2016-07-02 13:27:07", None],
            [0, "2016-07-02 13:30:12", "verde"],
            [0, None, "rojo"],
            [1, "2016-07-02 13:57:07", None],
            [1, "2016-07-02 14:08:07", "verde"],
        ],
    }
