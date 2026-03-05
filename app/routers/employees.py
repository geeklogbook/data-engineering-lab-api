from fastapi import APIRouter

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("")
def get_employees():
    return {
        "columns": ["EmployeeID", "Nombre", "Apellido", "DepartmentID", "Salario", "Ingreso"],
        "data": [
            [1, "Alice", "Chain", 1, 600000, "2020-01-15"],
            [2, "Marcos", "Perez", 1, 750000, "2019-03-10"],
            [3, "Charlie", "Riquelme", 1, 500000, "2021-06-20"],
            [4, "David", "Gallardo", 2, 800000, "2018-11-05"],
            [5, "Eve", "Gaspar", 2, 650000, "2020-09-12"],
            [6, "Frank", "Garcia", 3, 550000, "2022-02-25"],
        ],
    }
