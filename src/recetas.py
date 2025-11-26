from typing import NamedTuple
from datetime import *
import csv

Ingrediente = NamedTuple("Ingrediente",
					[("nombre",str),
					 ("cantidad",float),
					 ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", list[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])

def lee_recetas (ruta:str) -> list[Receta]:
    with open (ruta, encoding = "utf 8") as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)

        res = []
        
        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            ingredientes = parsea_ingredientes(ingredientes)
            tiempo = int(tiempo)
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            precio = float(precio.replace(",", "."))
            res.append(Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio))
        return res
            

def parsea_ingredientes(ingredientes:str) -> list[Ingrediente]:
    lista = ingredientes.split(",")
    return [parsea_ingrediente(i) for i in lista]

def parsea_ingrediente(ingrediente:str) -> Ingrediente:
    if (ingrediente == ""):
        return []
    lista = ingrediente.split("-")
    
    return Ingrediente(lista[0], float(lista[1]), lista[2])

def ingredientes_en_unidad(recetas:list[Receta], unidad_buscar:str = None) -> int:
    ingredientes_distintos = set() 
    
    for receta in recetas:
        for ing in receta.ingredientes:
            if ing != [] and (unidad_buscar == None or ing.unidad == unidad_buscar):
                ingredientes_distintos.add(ing.nombre)
                
    return len(ingredientes_distintos)

def recetas_con_ingredientes(recetas:list[Receta], ingredientes_buscar:set[str]) -> list[tuple[str, float, float]]:
    res = []
    
    for receta in recetas:
        for ing in receta.ingredientes:
            if ing != [] and ing.nombre in ingredientes_buscar:
                res.append((receta.denominacion, receta.calorias, receta.precio))
                break
    return res

def receta_mas_barata(recetas:list[Receta], tipos:set[str], n:int = None) -> Receta:
    recetas_filtradas = [i for i in recetas if i.tipo in tipos]
    
    if not recetas_filtradas:
        return None 
    
    recetas_baratas = sorted(recetas_filtradas, key = lambda n: n.calorias)
    
    if n != None:
        recetas_baratas = recetas_baratas[:n]
    
    return min(recetas_baratas, key = lambda n: n.precio)

def recetas_baratas_con_menos_calorias(recetas:list[Receta], n:int) -> list[tuple[str, int]]:
    precio_promedio = sum(i.precio for i in recetas) / len(recetas)
    
    recetas_filtradas =  [i for i in recetas if i.precio < precio_promedio]
    
    if not recetas_filtradas:
        return None 
    
    recetas_calorias = sorted(recetas_filtradas[:n], key = lambda n: n.calorias)
    
    res = [(i.denominacion, i.calorias) for i in recetas_calorias]
    
    return 