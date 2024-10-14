import streamlit as st
import random

# Función para generar ejercicios de cinemática
def generar_ejercicio():
    # Parámetros aleatorios para el ejercicio
    v0 = random.randint(1, 20)  # Velocidad inicial en m/s
    a = random.randint(1, 10)   # Aceleración en m/s^2
    t = random.randint(1, 10)    # Tiempo en segundos

    # Fórmula: d = v0 * t + (1/2) * a * t^2
    distancia = v0 * t + 0.5 * a * t**2
    return v0, a, t, distancia

# Generar un nuevo ejercicio
v0, a, t, distancia_correcta = generar_ejercicio()

# Título de la aplicación
st.title("Ejercicios de Cinemática")

# Mostrar el ejercicio
st.write(f"Un objeto se mueve con una velocidad inicial de {v0} m/s.")
st.write(f"La aceleración es de {a} m/s² durante {t} segundos.")
st.write("¿Cuál es la distancia recorrida por el objeto?")

# Campo para la respuesta del usuario
respuesta_usuario = st.number_input("Ingresa tu respuesta (en metros):", step=0.1)

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    if respuesta_usuario == distancia_correcta:
        st.success("¡Correcto! La distancia es efectivamente {:.2f} metros.".format(distancia_correcta))
    else:
        st.error("Incorrecto. La distancia correcta es {:.2f} metros.".format(distancia_correcta))

