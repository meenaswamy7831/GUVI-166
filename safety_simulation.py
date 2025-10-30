import math, time, requests

SAFE_DISTANCE = 40

frames = [
    {'frame': 1, 'person': (50, 100), 'robot': (200, 100)},
    {'frame': 2, 'person': (150, 100), 'robot': (200, 100)},
    {'frame': 3, 'person': (180, 100), 'robot': (200, 100)},  # unsafe
]

def check_safety(person, robot, threshold=SAFE_DISTANCE):
    dist = math.dist(person, robot)
    return dist, dist >= threshold

for f in frames:
    dist, is_safe = check_safety(f['person'], f['robot'])
    status = "SAFE" if is_safe else "UNSAFE"
    print(f"Frame {f['frame']}  Distance={dist:.1f}  Status={status}")

    try:
        requests.post("http://127.0.0.1:8000/update",
                      json={"frame": f['frame'], "distance": dist, "status": status})
    except:
        print("Backend not running yet...")
    time.sleep(1)
