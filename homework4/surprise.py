# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def star_name(name):
    for i in name:
        print(i)
star_name(targets)

def star_spectral(type):
    for star, spectral in type.items():
        print(f"{star}: {spectral['Spectral Type']}")
star_spectral(targets)

def bright_stars(targets):
    for star, info in targets.items():
        if info["Magnitude"] > 0.1:
            print(f"{star}: {info['Magnitude']}")
bright_stars(targets)

targets["Altair"] = {"RA": "19h 50m 47.0s", "Dec": "+08° 52' 06″", "Magnitude": 0.77, "Spectral Type": "A7V"}
print(targets["Altair"])


def closest_to_20(targets):
    closest_star = None
    closest_diff = float('inf')
    brightest_mag = float('inf')

    for star, info in targets.items():
        dec_str = info["Dec"].split("°")[0]
        dec_value = float(dec_str.replace("+", "").replace("−", "-"))
        diff = abs(dec_value - 20)
        if diff < closest_diff or (diff == closest_diff and info["Magnitude"] < brightest_mag):
            closest_diff = diff
            brightest_mag = info["Magnitude"]
            closest_star = star

    return closest_star
print(closest_to_20(targets))

# My favorite costellation is Orion