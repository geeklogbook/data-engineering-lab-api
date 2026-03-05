from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])


@router.get("")
def get_products():
    return {
        "columns": ["product_id", "sku", "colors", "source", "updated_at"],
        "data": [
            [1001, "remera_basica", ["rojo", "negro", "blanco"], "web", "2026-02-06"],
            [1002, "zapatilla_runner", ["negro", "gris"], "proveedor", "2026-02-06"],
            [1003, "campera_pluma", ["azul", "negro", "verde"], "proveedor", "2026-02-05"],
            [1004, "gorra_trucker", ["azul", "negro", "verde"], "web", "2026-02-06"],
            [1005, "mochila_urbana", ["azul", "negro", "verde"], "csv_import", "2026-02-01"],
        ],
    }
