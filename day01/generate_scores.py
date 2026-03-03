import random

def gen_students(n: int = 10):
    names = [f"Student{i+1}" for i in range(n)]
    data = {name: random.randint(60, 100) for name in names}
    return data

def summary(data: dict):
    scores = list(data.values())
    avg = sum(scores) / len(scores)
    mx = max(scores)
    mn = min(scores)
    return avg, mx, mn

def level_count(data: dict):
    res = {"excellent": 0, "good": 0, "pass": 0, "fail": 0}
    for score in data.values():
        if score >= 90:
            res["excellent"] += 1
        elif score >= 80:
            res["good"] += 1
        elif score >= 60:
            res["pass"] += 1
        else:
            res["fail"] += 1
    return res

def ranking(data: dict):
    items = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return items

if __name__ == "__main__":
    data = gen_students(10)
    print("Raw:", data)

    avg, mx, mn = summary(data)
    print(f"avg={avg:.2f}, max={mx}, min={mn}")

    print("\nRanking:")
    for i,(name,score) in enumerate(ranking(data), start=1):
        print(f"{i:02d}.{name:<10} {score}")

    print("\nlevel Count:", level_count(data))