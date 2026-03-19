
SPECIAL = "!@#$%^&*()-_=+[]{};:,.?"
def analyze_password(passwd,
                     min_len=8,
                     require_digit=True,
                     require_upper=True,
                     require_symbol=False,
                     banned_words=None):

    if banned_words is None:
        banned_words = ["password", "12345", "heslo"]

    missing_rules = []
    active_rules = 1

    if len(passwd) < min_len:
        missing_rules.append("min_len")
    if require_digit:
        active_rules += 1
        if not any(ch.isdigit() for ch in passwd):
            missing_rules.append("digit")
    if require_upper:
        active_rules += 1
        if not any(ch.isupper() for ch in passwd):
            missing_rules.append("upper")

    if require_symbol:
        active_rules += 1
        if not any(ch in SPECIAL for ch in passwd):
            missing_rules.append("symbol")

    active_rules += 1
    lower_pass = passwd.lower()
    if any(bw.lower() in lower_pass for bw in banned_words):
        missing_rules.append("banned_words")

    passed_rules = active_rules - len(missing_rules)
    score_percent = int((passed_rules / active_rules) * 100)
    is_strong = len(missing_rules) == 0
    return is_strong, score_percent, missing_rules

result1 = analyze_password("Abcdef1!")
print(result1)

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [3, 1, 4])
plt.show()