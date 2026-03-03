from typing import List, Dict

def calc_avg(scores: List[float]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def find_max(scores: List[float]) -> float:
    if not scores:
        raise ValueError("score is empty")
    return max(scores)

def normalize_name(name: str) -> str:
    name = name.strip()
    parts = [p for p in name.split(" ") if p]
    name = " ".join(parts)
    return name[:1].upper() + name[1:]

def top_k(scores: List[float], k: int) -> List[float]:
    if k <= 0:
        return []
    return sorted(scores, reverse=True)[:k]

def count_garde_level(scores: List[float]) -> Dict[str ,int]:
    res = {"excellent": 0, "good": 0, "pass": 0, "fail": 0}
    for x in scores:
        if x >= 90:
            res["excellent"] += 1
        elif x >= 80:
            res["good"] += 1
        elif x >= 60:
            res["pass"] += 1
        else:
            res["fail"] +=1
    return res

if __name__ == "__main__":
    s = [95, 88, 72, 61, 59, 100]
    print("ave:", calc_avg(s))
    print("max:", find_max(s))
    print("normalize_name:", normalize_name( " zhang san "))
    print("top3:", top_k(s, 3))
    print("level:", count_garde_level(s))