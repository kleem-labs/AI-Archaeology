"""Turn raw animal observations into consistent feature records."""

FEATURES = ("legs", "mass_kg", "has_stripes", "tooth_cm")


def extract_features(observation):
    return tuple(float(observation[name]) for name in FEATURES)


if __name__ == "__main__":
    animals = {
        "tiger": {"legs": 4, "mass_kg": 180, "has_stripes": 1, "tooth_cm": 7.0},
        "zebra": {"legs": 4, "mass_kg": 350, "has_stripes": 1, "tooth_cm": 2.5},
        "deer": {"legs": 4, "mass_kg": 90, "has_stripes": 0, "tooth_cm": 1.5},
    }
    print("feature order:", FEATURES)
    for name, observation in animals.items():
        print(f"{name:>5}: {extract_features(observation)}")
