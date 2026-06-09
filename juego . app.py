import streamlit as st

st.title("🧪 Quiz: Química de las Balas Trazadoras")

preguntas = [
    {
        "pregunta": "¿Qué permite que una bala trazadora deje una estela luminosa?",
        "opciones": [
            "Una batería interna",
            "Una composición pirotécnica",
            "Un láser",
            "Un LED"
        ],
        "respuesta": "Una composición pirotécnica"
    },
    {
        "pregunta": "¿Qué metal se utiliza frecuentemente en mezclas trazadoras?",
        "opciones": [
            "Magnesio",
            "Hierro",
            "Cobre",
            "Níquel"
        ],
        "respuesta": "Magnesio"
    },
    {
        "pregunta": "¿Cuál es la función principal del nitrato en la mezcla?",
        "opciones": [
            "Actuar como combustible",
            "Actuar como oxidante",
            "Reducir la temperatura",
            "Generar humo"
        ],
        "respuesta": "Actuar como oxidante"
    }
]

puntaje = 0

for i, p in enumerate(preguntas):
    respuesta = st.radio(
        p["pregunta"],
        p["opciones"],
        key=i
    )

    if respuesta == p["respuesta"]:
        puntaje += 1

if st.button("Ver resultado"):
    st.success(f"Obtuviste {puntaje} de {len(preguntas)} respuestas correctas.")

    if puntaje == len(preguntas):
        st.balloons()
        st.write("🎉 ¡Excelente! Conoces bien la química de las balas trazadoras.")
