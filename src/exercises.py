EXERCISES = {

    "Elevación lateral de brazos": {

        "metric": "shoulder",

        "target_min": 80,
        "target_max": 95,

        "feedback": {
            "low": "⬆️ Sube más los brazos",
            "ok": "✅ Movimiento correcto",
            "high": "⚠️ No excedas la elevación"
        }
    },

    "Postura cervical neutra": {

        "metric": "cervical",

        "target_min": 120,
        "target_max": 180,

        "feedback": {
            "low": "⚠️ Endereza el cuello",
            "ok": "✅ Cabeza alineada",
            "high": "⚠️ Postura cervical inestable"
        }
    },

    "Posición de cabeza": {

        "metric": "head",

        "target_min": 85,
        "target_max": 100,

        "feedback": {
            "low": "⬅️ Corrige inclinación",
            "ok": "✅ Cabeza estable",
            "high": "➡️ Evita sobre inclinación"
        }
    }
}


def evaluate_exercise(angle, config):

    if angle == "--" or angle is None:
        return "Sin datos", "gray"

    if angle < config["target_min"]:
        return config["feedback"]["low"], "orange"

    elif angle > config["target_max"]:
        return config["feedback"]["high"], "red"

    else:
        return config["feedback"]["ok"], "green"