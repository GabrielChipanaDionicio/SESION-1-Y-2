import streamlit as st

st.title("Resolver ecuaciones de primer grado")

st.write("Vamos a resolver una ecuación del tipo **ax + b = c**")

# Definir coeficientes (puedes cambiarlos o hacerlos aleatorios)
a = 3
b = 5
c = 20

st.latex(f"{a}x + {b} = {c}")

# Resultado correcto
resultado_correcto = (c - b) / a

# Input del usuario
respuesta = st.number_input("Ingresa el valor de x:", step=0.1)

# Botón para verificar
if st.button("Verificar resultado"):
    if abs(respuesta - resultado_correcto) < 1e-6:
        st.success("¡Correcto! 🎉")
        st.balloons()
    else:
        st.error("Resultado incorrecto. Intenta nuevamente.")
