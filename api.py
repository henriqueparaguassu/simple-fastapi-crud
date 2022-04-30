from fastapi import FastAPI, Path, Query, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from menu import menu

app = FastAPI(
    title="CafeAPI",
    description="API para o menu de um café.",
    version="0.1.0"
)


class Item(BaseModel):
    id: int = None
    name: str
    price: float


class UpdateItem(BaseModel):
    name: str
    price: float


@app.get("/get-menu")
def get_menu():
    """Retorna o menu do café"""
    return JSONResponse(menu, status.HTTP_200_OK)


@app.get("/get-item/{item_id}")
def get_item_by_id(item_id: int = Path(None, description="ID do item no menu")):
    """Retorna o item do menu"""

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search:
        res = {"item": search[0]}
        return JSONResponse(res, status.HTTP_200_OK)

    res = {"error": "Item não encontrado"}
    return JSONResponse(res, status.HTTP_404_NOT_FOUND)


@app.get("/get-item")
def get_item_by_name(name: str = Query(None, description="Nome do item no menu")):
    """Retorna o item do menu"""

    search = list(filter(lambda x: x["name"] == name, menu))

    if search:
        res = {"item": search[0]}
        return JSONResponse(res, status.HTTP_200_OK)

    res = {"error": "Item não encontrado"}
    return JSONResponse(res, status.HTTP_404_NOT_FOUND)


@app.post("/add-item")
def add_item(item: Item):
    """Adiciona um item ao menu"""

    item.id = len(menu) + 1
    dict_item = item.dict()

    menu.append(dict_item)
    res = {"item": dict_item}
    return JSONResponse(res, status.HTTP_201_CREATED)


@app.put("/update-item/{item_id}")
def update_item(item: UpdateItem, item_id: int = Path(None, description="ID do item no menu")):
    """Atualiza um item do menu"""

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search:
        item_index = menu.index(search[0])
        menu[item_index]["name"] = item.name
        menu[item_index]["price"] = item.price
        res = {"item": search[0]}
        return JSONResponse(res, status.HTTP_200_OK)

    res = {"error": "Item não encontrado"}
    return JSONResponse(res, status.HTTP_404_NOT_FOUND)


@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int = Path(None, description="ID do item no menu")):
    """Remove um item do menu"""

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search:
        menu.remove(search[0])
        res = {"item": search[0]}
        return JSONResponse(res, status.HTTP_200_OK)

    res = {"error": "Item não encontrado"}
    return JSONResponse(res, status.HTTP_404_NOT_FOUND)
