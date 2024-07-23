from fastapi import APIRouter,HTTPException

from starlette.middleware.cors import CORSMiddleware

from sqlalchemy import select

from models.chatbot import chat

from database.basedatos import conexion

rutas=APIRouter()

@rutas.get("/firulais")

def consultarChat():
    try:
        consulta=select(chat)
        resultado=conexion.execute(consulta).fetchall()
        resultadoJSON=[{'id':row.id,'pregunta':row.pregunta,'Respuesta':row.Respuesta} for row in resultado]
        return resultadoJSON

    except Exception as error:
        raise HTTPException(status_code=500,detail=str(error))