from collections import defaultdict

SAMPLE = [("food", 14.5), ("transport", 3.2), ("food", 9.8)]

def summarize(items):
    totals = defaultdict(float)
    for cat, amt in items:
        totals[cat] += amt
    return dict(sorted(totals.items(), key=lambda x: -x[1]))

if __name__ == "__main__":
    print(summarize(SAMPLE))
