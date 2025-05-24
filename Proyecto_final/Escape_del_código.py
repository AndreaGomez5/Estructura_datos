import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

data = {
    'Usuario': ['U1', 'U2', 'U3', 'U4', 'U5'],
    'Película A': [5, 4, 2, 1, 3],
    'Película B': [4, 5, 3, 2, 1],
    'Película C': [1, 3, 5, 4, 2],
    'Película D': [2, 1, 4, 5, 3],
    'Película E': [3, 2, 1, 3, 5]
}

df = pd.DataFrame(data)

ratings_matrix = df.set_index('Usuario').values

cosine_sim = cosine_similarity(ratings_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=df['Usuario'], columns=df['Usuario'])

print("Matriz de similitud entre usuarios:")
print(cosine_sim_df)

def obtener_recomendaciones(usuario, ratings_matrix, cosine_sim_df):
    similares = cosine_sim_df[usuario].sort_values(ascending=False)[1:]  
    
    recomendaciones = {}

    for usuario_similar, similitud in similares.items():
        peliculas_no_vistas = ratings_matrix[usuario_similar].nonzero()[0]
        for pelicula_id in peliculas_no_vistas:
            if ratings_matrix[usuario][pelicula_id] == 0:  
                if pelicula_id not in recomendaciones:
                    recomendaciones[pelicula_id] = similitud * ratings_matrix[usuario_similar][pelicula_id]
                else:
                    recomendaciones[pelicula_id] += similitud * ratings_matrix[usuario_similar][pelicula_id]
    
    recomendaciones_ordenadas = sorted(recomendaciones.items(), key=lambda x: x[1], reverse=True)
    return recomendaciones_ordenadas

usuario = 'U1'
recomendaciones = obtener_recomendaciones(usuario, ratings_matrix, cosine_sim_df)

print("\nRecomendaciones para el usuario", usuario)
for pelicula_id, puntaje in recomendaciones[:5]:  
    print(f"Película {df.columns[pelicula_id+1]} - Puntaje estimado: {puntaje:.2f}")