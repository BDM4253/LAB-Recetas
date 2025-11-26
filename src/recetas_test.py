from recetas import *
ruta = "./data/recetas.csv"

def test_lee_recetas():
    print (f"Registros leídos: {len(lee_recetas(ruta))}")
    print (f"Los dos primeros: {lee_recetas(ruta)[:2]} \n")
    print (f"Los dos últimos: {lee_recetas(ruta)[-2:]}")

def test_ingredientes_en_unidad():
    recetas = lee_recetas(ruta)
    
    unidad = None
    print (f"Hay {ingredientes_en_unidad(recetas, unidad)} ingredientes distintos que se miden en {unidad}")
    unidad = "gr"
    print (f"Hay {ingredientes_en_unidad(recetas, unidad)} ingredientes distintos que se miden en {unidad}")
    unidad = "cl"
    print (f"Hay {ingredientes_en_unidad(recetas, unidad)} ingredientes distintos que se miden en {unidad}")
    
def test_recetas_con_ingredientes():
    recetas = lee_recetas(ruta)
    
    ingredientes = {"harina", "azúcar"}
    print (f"Las recetas con algunos de los siguientes ingredientes {ingredientes}, son {recetas_con_ingredientes(recetas, ingredientes)}")
    ingredientes = {"pimiento", "tomate", "cebolla"}
    print (f"Las recetas con algunos de los siguientes ingredientes {ingredientes}, son {recetas_con_ingredientes(recetas, ingredientes)}")
    
def test_receta_mas_barata():
    recetas = lee_recetas(ruta)
    tipos = {'Postre', 'Entrante'}
    print(f"La receta más barata de alguno de los siguientes tipos {tipos} es : {receta_mas_barata(recetas, tipos)}")
    tipos = {'Postre', 'Plato Principal'}
    print(f"La receta más barata de alguno de los siguientes tipos {tipos} entre las 5 con menos calorías es: {receta_mas_barata(recetas, tipos, 5)}")
   
def test_recetas_baratas_con_menos_calorias():
    recetas = lee_recetas(ruta)
    n = 3
    print(f"Las {n} recetas con menos calorías con precio menor que el promedio son: {recetas_baratas_con_menos_calorias(recetas, n)}")
    n = 5
    print(f"Las {n} recetas con menos calorías con precio menor que el promedio son: {recetas_baratas_con_menos_calorias(recetas, n)}")
    
if __name__ == "__main__":
    #test_lee_recetas(ruta)
    #test_ingredientes_en_unidad()
    #test_recetas_con_ingredientes()
    #test_receta_mas_barata()
    test_recetas_baratas_con_menos_calorias()