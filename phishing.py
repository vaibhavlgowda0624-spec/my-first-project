import tkinter as tk
from tkinter import messagebox
import re

# Check phishing
def check_url():
    url = entry.get().strip()
    score = 0
    reasons = []

    # Rule 1: IP address instead of domain
    if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", url):
        score += 1
        reasons.append("Uses IP address instead of domain")

    # Rule 2: Too long URL
    if len(url) > 50:
        score += 1
        reasons.append("URL is too long")

    # Rule 3: Suspicious symbols
    if "@" in url or "-" in url:
        score += 1
        reasons.append("Contains suspicious symbols (@ or -)")

    # Rule 4: Fake HTTPS
    if "https" in url and "http://" in url:
        score += 1
        reasons.append("Fake HTTPS structure")

    # Rule 5: Multiple dots
    if url.count(".") > 3:
        score += 1
        reasons.append("Too many subdomains")

    # Result
    if score == 0:
        result_label.config(text="Safe ✅", fg="green")
    elif score <= 2:
        result_label.config(text="Suspicious ⚠️", fg="orange")
    else:
        result_label.config(text="Phishing ❌", fg="red")

    # Show reasons
    reason_box.delete(1.0, tk.END)
    for r in reasons:
        reason_box.insert(tk.END, "- " + r + "\n")

# GUI
window = tk.Tk()
window.title("Phishing URL Detector 🔐")
window.geometry("450x350")

tk.Label(window, text="Enter URL:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(pady=5)

tk.Button(window, text="Check URL", command=check_url).pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=5)

reason_box = tk.Text(window, width=50, height=10)
reason_box.pack(pady=10)

window.mainloop()
