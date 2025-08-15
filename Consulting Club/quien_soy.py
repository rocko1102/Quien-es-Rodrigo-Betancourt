import streamlit as st
import pandas as pd
import plotly.express as px
import random

# ================== CONFIG ==================
st.set_page_config(page_title="¿Quién soy?", layout="centered")

st.markdown(
    """
    <style>
        body {background-color: #0e1117; color: white;}
        h1, h2, h3 {color: #00ffcc;}
        .stButton>button {
            background-color: #00aaff;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
        }
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ================== MENÚ LATERAL ==================
st.sidebar.title("Navegación")
pagina = st.sidebar.radio("Ir a:", ["Presentación", "Dashboard"])

# ================== FRASES ALEATORIAS ==================
frases = [
    "No bajes tus sueños a la altura de tus capacidades aparentes, más bien estira tus capacidades a la altura de tus sueños.--Mario Alonso Puig",
    "Mas vale proponerse la meta de la excelencia y no lograrla que proponerse la meta de la mediocridad y lograrla.--Carlos Llano",
    "Quien no vive para servir, no sirve para vivir.--Madre Teresa de Calcuta",
    "Lo unico que vence al dinero es el talento",
    "Ganar no lo es todo, pero querer ganar si lo es --Vince Lombardi"
]

# ================== PÁGINAS ==================
if pagina == "Presentación":
    st.markdown("<h1 style='text-align:center; font-size:80px; color:#FFD700;'>¿QUIÉN SOY?</h1>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center; font-size:50px; color:#FFD700;'>Rodrigo Betancourt Martinez</h1>", unsafe_allow_html=True)

    # Botón de frase inspiradora
    if st.button("💡 Conoce frases que me inspiran"):
        st.info(random.choice(frases))

    # ================== FORTALEZAS ==================
    st.markdown("<h2 style='color:#00BFFF;'>Fortalezas</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; color: white;'>
    Soy Rodrigo Betancourt una persona determinada en el crecimiento personal, me gustan los retos, aprender y mejorar. 
    Es por esto que desde varios años he buscado aumentar y mejorar mis fortalezas. Hoy por hoy, si tuviera que nombrar solo 
    5 fortalezas que me hacen sobresalir y mejorar todos los dias yo diría que son las siguientes:

    1. **Capacidad de análisis:** El estudiar en una carrera cuyo principal enfoque es la analítica de datos, se me facilita entender el cómo se compone la información así como su origen.

    2. **Adaptabilidad:** A lo largo de mi vida he tenido muchos cambios en diferentes ámbitos. El haber estado en diferentes competencias académicas, así como en diversas actividades deportivas, me ha enfrentado ante diversas personas y problemas, por lo que el cambiar y modificarme a mi entorno es un proceso que se me facilita.

    3. **Pensamiento Analítico:** El tener una buena capacidad de análisis y el entender el origen de la información, me permite tomar decisiones estratégicas y realizar las acciones más acordes al análisis anteriormente hecho.

    4. **Creatividad:** Me considero una persona creativa, siempre trato de ser una persona que trata de destacar. Me gusta abrirme a nuevas oportunidades y herramientas y usarlas a mi favor, lo que me facilita innovar y desarrollar cosas diferentes al promedio.

    5. **Resiliencia:** Ser una persona que se encuentra en constante cambio me ha hecho realizar muchas veces actividades en las cuales no soy bueno al principio y muchas veces esa falta de conocimiento se convierte en fracaso. Sin embargo, mi resiliencia me ha permitido aprender del fracaso y no rendirme, haciendo que con el tiempo aquello en lo que fracasé se convierta en conocimientos y experiencias.
        </p>
    """, unsafe_allow_html=True)

    st.image("fortalezas.jpg", width=500, )

    # ================== DEBILIDADES ==================
    st.markdown("<h2 style='color:#FF69B4;'>Debilidades</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; color: white;'>
             Como cualquier persona cuento con debilidades que me alejan de mi mejor versión.
    De igual manera si tuviera que nombrar 5 debilidades serían las siguientes

    1.**Franqueza:** Soy una persona a la que le gusta decir las cosas como las piensa y de manera sincera, lo que puede hacer que las personas en algunos momentos me juzguen como alguien frío. Es por esto que últimamente me he obligado a guardar mis pensamientos a menos que me lo pidan de manera explícita.

    2.**Impaciencia:** En lo personal, detesto quedarme estancado en algo. Cuando siento que no llego a los resultados deseados después de varios intentos, tiendo a desesperarme. Sin embargo, es en estos momentos cuando pongo a prueba mi creatividad y resiliencia para salir de la circunstancia.

    3.**Perfeccionismo:** Soy una persona que cree que si algo se puede hacer mejor trato de hacerlo. No me gusta dejar las cosas incompletas, y muchas veces este deseo de perfeccionismo me lleva a ser muy exigente conmigo, ya que no me gusta sentir que hice menos de lo que sabía hacer.

    4.**Delegar trabajo:** A pesar de que me gusta trabajar en equipo, si no conozco muy bien a las personas con las que trabajo me cuesta confiar en las actividades más importantes. Sin embargo, he aprendido a conocerme y aceptar lo que puedo y no puedo hacer, lo que ha permitido que sea más fácil el soltar actividades.

    **Ignorancia:** Esta es una debilidad que creo que tenemos todos. Yo creo que nadie sabe todo, así que pensando en un rol dentro de la consultoría, creo que existen muchas cosas que no sé bien cómo se hace. Pero creo que mi gusto por aprender y mi adaptabilidad hacen que sea una persona que aprende rápido, haciendo que con el tiempo la ignorancia disminuya.
    </p>
    """, unsafe_allow_html=True)
    st.image("debilidades.jpg", width=500)

    # ================== ÉXITO ==================
    st.markdown("<h2 style='color:#ADFF2F;'>Éxito</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; color: white;'>
    Para mí el éxito es la unión de metas y deseos logrados a través de mis capacidades en el ámbito que deseo en mi vida, 
    ya sea laboral, familiar, personal y espiritual, complementando con aquellas cosas que me dan felicidad en mi vida.
    </p>
    """, unsafe_allow_html=True)
    st.image("exito.jpg", width=500)

    # ================== VISIÓN 3 AÑOS ==================
    st.markdown("<h2 style='color:#FF8C00;'>Visión a 3 años</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; color: white;'>
    En 3 años me veo con grandes cambios, principalmente en el ámbito laboral y personal.

    **Ámbito laboral:** Me veo graduado de mi licenciatura, así como ya estar trabajando en una empresa de carácter internacional en alguna de las siguientes industrias:  
    1. Consultora  
    2. Tecnológica  
    3. Consumo  

    Ya contaría con algo de experiencia laboral y esto me estaría abriendo la oportunidad de empezar a tener roles de un poco mayor responsabilidad dentro de la empresa en la que esté. También me veo empezando a ver diferentes opciones para una especialización acorde a mi carrera profesional.

    **Ámbito personal:** Me veo con una mayor madurez que la que cuento hoy, así como un amplio conocimiento en diferentes cosas. Y por último, al ser una persona apasionada por el deporte, me veo con un aspecto físico mejor al que me encuentro hoy.
    </p>
    """, unsafe_allow_html=True)
    st.image("vision.jpg", width=500)

elif pagina == "Dashboard":
    st.markdown("<h1 style='color:#FFD700;'>Dashboard Personal</h1>", unsafe_allow_html=True)

    # Datos
    fortalezas = pd.DataFrame({
        "Fortaleza": ["Capacidad de análisis", "Adaptabilidad", "Pensamiento Analítico", "Creatividad", "Resiliencia"],
        "Puntaje": [9, 10, 9, 8, 8.5]
    })

    debilidades = pd.DataFrame({
        "Debilidad": ["Franqueza", "Impaciencia", "Perfeccionismo", "Delegar trabajo", "Ignorancia"],
        "Impacto Negativo": [8, 7, 8, 6, 5]
    })

    habilidades = pd.DataFrame({
        "Habilidad": ["Excel", "SQL", "PowerBi", "Tableau", "R","Power point","Python"],
        "Nivel": [10, 9, 9, 8, 3, 8, 5]
    })

    # Gráfico radar de fortalezas
    fig_fort = px.line_polar(
        fortalezas, r="Puntaje", theta="Fortaleza", line_close=True,
        title="Fortalezas Personales", color_discrete_sequence=["#00FFAA"]
    )
    fig_fort.update_traces(fill='toself')
    fig_fort.update_layout(
        polar=dict(
            radialaxis=dict(
                tickfont=dict(color="blue"),  # Números visibles
                gridcolor="#00FFAA"
            ),
            angularaxis=dict(
                tickfont=dict(color="green")
            )
        )
    )
    st.plotly_chart(fig_fort, use_container_width=False, width=850, height=850)

    # Gráfico de barras para debilidades
    fig_deb = px.bar(
        debilidades, x="Impacto Negativo", y="Debilidad", orientation='h',
        title="Debilidades Personales", color="Impacto Negativo",
        color_continuous_scale=["#00FFAA", "#007BFF"]
    )
    st.plotly_chart(fig_deb, use_container_width=True)

    # Nuevo gráfico de habilidades técnicas

    fig_hab = px.pie(
    habilidades, names="Habilidad", values="Nivel",
    title="Nivel de Habilidades Técnicas",
    color_discrete_sequence=px.colors.sequential.Teal
)
    st.plotly_chart(fig_hab, use_container_width=True)
