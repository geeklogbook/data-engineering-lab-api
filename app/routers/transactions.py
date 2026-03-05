from fastapi import APIRouter
from datetime import datetime
import hashlib
import os

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("")
def get_transactions():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def rid():
        return hashlib.sha256(os.urandom(8)).hexdigest()[:8]
    return {
        "columns": ["id", "timestamp", "status"],
        "data": [
            [rid(), None, "confirmed"],
            [rid(), now, "pending"],
            [rid(), now, "confirmed"],
            [rid(), now, None],
            [rid(), now, "confirmed"],
            [rid(), None, "pending"],
            [rid(), now, None],
            [rid(), now, "confirmed"],
        ],
    }
