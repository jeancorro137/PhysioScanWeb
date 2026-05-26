import streamlit as st
import cv2
import time

from src.processor import VideoProcessor
from src.exercises import (
    EXERCISES,
    evaluate_exercise
)

# --------------------------------
# CONFIG
# --------------------------------
st.set_page_config(
    page_title="PhysioScan Web",
    page_icon="assets/icono.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------
# SESSION STATE
# --------------------------------
if "camera_running" not in st.session_state:
    st.session_state.camera_running = False

if "processor" not in st.session_state:
    st.session_state.processor = None

# --------------------------------
# ESTADOS BIOMECÁNICOS
# --------------------------------
def get_posture_status(angle, metric_type):

    if angle == "--":
        return "⚪ Sin datos"

    # Cervical
    if metric_type == "cervical":

        if angle >= 130:
            return "🟢 Normal"

        elif angle >= 110:
            return "🟡 Precaución"

        else:
            return "🔴 Riesgo"

    # Hombros
    if metric_type == "shoulder":

        if angle >= 150:
            return "🟢 Normal"

        elif angle >= 120:
            return "🟡 Precaución"

        else:
            return "🔴 Riesgo"

    # Cabeza
    if metric_type == "head":

        if angle >= 90:
            return "🟢 Normal"

        elif angle >= 75:
            return "🟡 Precaución"

        else:
            return "🔴 Riesgo"

    return "⚪ Sin datos"

# --------------------------------
# SIDEBAR
# --------------------------------
with st.sidebar:

    st.title("PhysioScan Web")
    st.caption("Evaluador Postural con IA - Talento Tech")

    st.divider()

    st.button(
        "🏠 Inicio",
        use_container_width=True,
        disabled=True

    )

    st.button(
        "📈 Análisis",
        use_container_width=True,
        disabled=True
    )

    st.button(
        "🕓 Historial",
        use_container_width=True,
        disabled=True
    )

    st.button(
        "ℹ️ Acerca de",
        use_container_width=True,
        disabled=True
    )

    st.divider()

    st.subheader("🧠 Ejercicio")

    selected_exercise = st.selectbox(
        "Selecciona ejercicio",
        list(EXERCISES.keys())
    )

    st.divider()

    if st.session_state.camera_running:
        st.success("🟢 Cámara activa")
    else:
        st.warning("⚪ Cámara inactiva")

    fps_placeholder = st.empty()

# --------------------------------
# HEADER
# --------------------------------
col1, col2 = st.columns([4, 1])

with col1:

    st.title(
        "Análisis Postural en Tiempo Real"
    )

    st.caption(
        "Visualiza tu postura y "
        "los ángulos articulares"
    )

with col2:

    if not st.session_state.camera_running:

        if st.button(
            "▶ Iniciar cámara",
            use_container_width=True
        ):

            st.session_state.processor = (
                VideoProcessor()
            )

            st.session_state.camera_running = True
            st.rerun()

    else:

        if st.button(
            "⏹ Detener cámara",
            use_container_width=True
        ):

            st.session_state.camera_running = False

            if st.session_state.processor:

                st.session_state.processor.release()

                st.session_state.processor = None

            st.rerun()

st.divider()

# --------------------------------
# LAYOUT
# --------------------------------
video_col, metric_col = st.columns([3, 2])

# --------------------------------
# VIDEO
# --------------------------------
with video_col:

    st.subheader("Video en vivo")

    video_placeholder = st.empty()

# --------------------------------
# MÉTRICAS
# --------------------------------
with metric_col:

    st.subheader(
        "Ángulos articulares"
    )

    metrics_placeholder = st.empty()

# --------------------------------
# STREAM
# --------------------------------
if st.session_state.camera_running:

    with st.spinner(
        "Procesando cámara..."
    ):
        prev_time = 0

        while st.session_state.camera_running:

            frame, metrics = (
                st.session_state.processor
                .process_frame()
            )
            # --------------------------------
            # FPS
            # --------------------------------
            current_time = time.time()

            fps = 0

            if current_time != prev_time:
                fps = 1 / (current_time - prev_time)

            prev_time = current_time

            fps_placeholder.metric(
                "FPS",
                f"{int(fps)}"
            )

            if frame is not None:

                frame = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )

                video_placeholder.image(
                    frame,
                    channels="RGB",
                    use_container_width=True
                )

            # ---------------------
            # MÉTRICAS
            # ---------------------
            if metrics is not None:

                cervical_value = (
                    metrics["cervical"]
                    if metrics["cervical"] is not None
                    else "--"
                )

                left_shoulder_value = (
                    metrics["left_shoulder"]
                    if metrics["left_shoulder"] is not None
                    else "--"
                )

                right_shoulder_value = (
                    metrics["right_shoulder"]
                    if metrics["right_shoulder"] is not None
                    else "--"
                )

                head_value = (
                    metrics["head"]
                    if metrics["head"] is not None
                    else "--"
                )

                # --------------------------------
                # EJERCICIO ACTIVO
                # --------------------------------
                exercise_config = (
                    EXERCISES[selected_exercise]
                )

                metric_type = (
                    exercise_config["metric"]
                )

                # --------------------------------
                # MAPEO MÉTRICAS
                # --------------------------------
                if metric_type == "shoulder":

                    valid_angles = []

                    if left_shoulder_value != "--":
                        valid_angles.append(
                            left_shoulder_value
                        )

                    if right_shoulder_value != "--":
                        valid_angles.append(
                            right_shoulder_value
                        )

                    current_angle = (
                        sum(valid_angles)
                        / len(valid_angles)
                        if valid_angles
                        else "--"
                    )

                elif metric_type == "cervical":
                    current_angle = cervical_value

                elif metric_type == "head":
                    current_angle = head_value

                else:
                    current_angle = "--"

                # --------------------------------
                # EVALUACIÓN TERAPÉUTICA
                # --------------------------------
                feedback_message, feedback_color = (
                    evaluate_exercise(
                        current_angle,
                        exercise_config
                    )
                )

                with metrics_placeholder.container():

                    cervical_status = get_posture_status(
                        cervical_value,
                        "cervical"
                    )

                    left_status = get_posture_status(
                        left_shoulder_value,
                        "shoulder"
                    )

                    right_status = get_posture_status(
                        right_shoulder_value,
                        "shoulder"
                    )

                    head_status = get_posture_status(
                        head_value,
                        "head"
                    )

                    # --------------------------------
                    # FEEDBACK IA
                    # --------------------------------
                    st.markdown(
                        f"""
                        <h2 style='color:{feedback_color};'>
                            {feedback_message}
                        </h2>
                        """,
                        unsafe_allow_html=True
                    )

                    with st.container(border=True):

                        st.metric(
                            "Cuello / Cervical",
                            f"{cervical_value}°"
                        )
                        st.caption(cervical_status)

                        st.metric(
                            "Hombro Izquierdo",
                            f"{left_shoulder_value}°"
                        )
                        st.caption(left_status)

                        st.metric(
                            "Hombro Derecho",
                            f"{right_shoulder_value}°"
                        )
                        st.caption(right_status)

                        st.metric(
                            "Cabeza",
                            f"{head_value}°"
                        )
                        st.caption(head_status)

                    st.caption(
                        "Análisis biomecánico "
                        "en tiempo real"
                    )

            time.sleep(0.01)

else:

    with video_placeholder.container(border=True):

        st.info(
            "Presiona "
            "'Iniciar cámara'"
        )

    with metrics_placeholder.container():

        with st.container(border=True):

            st.metric(
                "Cuello / Cervical",
                "--°"
            )

            st.metric(
                "Hombro Izquierdo",
                "--°"
            )

            st.metric(
                "Hombro Derecho",
                "--°"
            )

            st.metric(
                "Cabeza",
                "--°"
            )

        st.caption(
            "Estimaciones biomecánicas "
            "en tiempo real"
        )

# --------------------------------
# RECOMENDACIONES
# --------------------------------
st.divider()

with st.container(border=True):

    st.subheader(
        "Recomendaciones"
    )

    st.write(
        "Mantén postura erguida, "
        "realiza movimientos "
        "controlados y evita "
        "sobrecargar las articulaciones."
    )