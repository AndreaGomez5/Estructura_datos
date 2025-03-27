from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

@app.post("/ticketCreate")
def crear_turno(turno: Ticket):
    
    add_queue(turno, ticketTypes)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}


@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    return {"mensaje": "El siguiente turno es", "datos_turno": ""}


@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    return {"mensaje": "Lista de turnos en cola", "datos_turnos": ""}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
