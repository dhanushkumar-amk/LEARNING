import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch

# ── data (same seed as student.py) ──────────────────────────────────────────
np.random.seed(40)
marks = np.random.randint(10, 101, size=(20, 5))

subjects       = ["Math", "Science", "English", "History", "CS"]
student_labels = [f"S{i+1}" for i in range(20)]

total_marks        = np.sum(marks, axis=1)
average_by_student = np.mean(marks, axis=1)
average_by_subject = np.mean(marks, axis=0)

rank_order = np.argsort(total_marks)[::-1]   # index sorted best→worst
topper_idx = np.argmax(total_marks)
lowest_idx = np.argmin(total_marks)

passes = np.sum(marks >= 35, axis=0)
fails  = np.sum(marks < 35,  axis=0)

# ── global style ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor":  "#0D1117",
    "axes.facecolor":    "#161B22",
    "axes.edgecolor":    "#30363D",
    "axes.labelcolor":   "#C9D1D9",
    "xtick.color":       "#8B949E",
    "ytick.color":       "#8B949E",
    "text.color":        "#C9D1D9",
    "grid.color":        "#21262D",
    "grid.linewidth":    0.6,
    "font.family":       "DejaVu Sans",
})

ACCENT   = "#58A6FF"   # blue
GREEN    = "#3FB950"
RED      = "#F85149"
GOLD     = "#F0C742"
PURPLE   = "#BC8CFF"

# ── figure  (1 row × 3 columns, square-ish for LinkedIn) ─────────────────────
fig = plt.figure(figsize=(20, 7))
fig.patch.set_facecolor("#0D1117")

gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# ════════════════════════════════════════════════════════════════════════════
# CHART 1 — Top 10 Student Ranking (horizontal bar)
# ════════════════════════════════════════════════════════════════════════════
ax1 = fig.add_subplot(gs[0])

top10_idx    = rank_order[:10]
top10_totals = total_marks[top10_idx]
top10_labels = [student_labels[i] for i in top10_idx]

# gradient: gold → blue going down
grad_colors = [GOLD] + [ACCENT] * 4 + [PURPLE] * 5

bars = ax1.barh(
    top10_labels[::-1], top10_totals[::-1],
    color=grad_colors[::-1],
    height=0.62, edgecolor="#0D1117", linewidth=0.8
)

# value labels on bars
for bar, val in zip(bars, top10_totals[::-1]):
    ax1.text(bar.get_width() - 6, bar.get_y() + bar.get_height() / 2,
             str(val), va="center", ha="right", fontsize=9,
             fontweight="bold", color="#0D1117")

ax1.set_title("🏆  Top 10 Student Rankings", fontsize=13,
              fontweight="bold", color="white", pad=14)
ax1.set_xlabel("Total Marks  (out of 500)", fontsize=9)
ax1.set_xlim(0, max(top10_totals) + 30)
ax1.grid(axis="x", alpha=0.4)
ax1.spines[["top", "right"]].set_visible(False)

# rank badges on y-axis
for i, label in enumerate(ax1.get_yticklabels()):
    rank = 10 - i
    medals = {1: "🥇", 2: "🥈", 3: "🥉"}
    prefix = medals.get(rank, f"#{rank} ")
    label.set_text(f"{prefix} {top10_labels[9 - i]}")
ax1.set_yticklabels([f"{'🥇' if i==9 else '🥈' if i==8 else '🥉' if i==7 else f'#{10-i} '} {top10_labels[9-i]}"
                     for i in range(10)], fontsize=9)

# ════════════════════════════════════════════════════════════════════════════
# CHART 2 — Subject Average with difficulty indicator
# ════════════════════════════════════════════════════════════════════════════
ax2 = fig.add_subplot(gs[1])

subj_colors = [GREEN if v == max(average_by_subject) else
               RED   if v == min(average_by_subject) else
               ACCENT for v in average_by_subject]

bars2 = ax2.bar(subjects, average_by_subject,
                color=subj_colors, width=0.55,
                edgecolor="#0D1117", linewidth=0.8)

# value on top of each bar
for bar, val in zip(bars2, average_by_subject):
    ax2.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.8,
             f"{val:.1f}", ha="center", va="bottom",
             fontsize=10, fontweight="bold", color="white")

# pass line
ax2.axhline(35, color=RED, linestyle="--", linewidth=1.3, alpha=0.7, label="Pass Line (35)")

# annotation
hardest = np.argmin(average_by_subject)
easiest = np.argmax(average_by_subject)
ax2.annotate("Hardest ↑", xy=(hardest, average_by_subject[hardest]),
             xytext=(hardest, average_by_subject[hardest] + 8),
             fontsize=8, ha="center", color=RED, fontweight="bold",
             arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
ax2.annotate("Easiest ↑", xy=(easiest, average_by_subject[easiest]),
             xytext=(easiest, average_by_subject[easiest] + 8),
             fontsize=8, ha="center", color=GREEN, fontweight="bold",
             arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))

ax2.set_title("📚  Subject-Wise Average Score", fontsize=13,
              fontweight="bold", color="white", pad=14)
ax2.set_ylabel("Average Marks", fontsize=9)
ax2.set_ylim(0, 110)
ax2.grid(axis="y", alpha=0.4)
ax2.spines[["top", "right"]].set_visible(False)
ax2.legend(fontsize=8, facecolor="#161B22", edgecolor="#30363D", labelcolor="white")

# ════════════════════════════════════════════════════════════════════════════
# CHART 3 — Pass / Fail stacked bar (clean & bold)
# ════════════════════════════════════════════════════════════════════════════
ax3 = fig.add_subplot(gs[2])

x = np.arange(len(subjects))
width = 0.5

b_pass = ax3.bar(x, passes, width, label="✅ Pass", color=GREEN,
                 edgecolor="#0D1117", linewidth=0.8)
b_fail = ax3.bar(x, fails, width, bottom=passes, label="❌ Fail",
                 color=RED, edgecolor="#0D1117", linewidth=0.8, alpha=0.88)

# labels inside bars
for i in range(len(subjects)):
    ax3.text(i, passes[i] / 2, str(passes[i]),
             ha="center", va="center", fontsize=11, fontweight="bold", color="white")
    if fails[i] > 0:
        ax3.text(i, passes[i] + fails[i] / 2, str(fails[i]),
                 ha="center", va="center", fontsize=11, fontweight="bold", color="white")

ax3.set_xticks(x)
ax3.set_xticklabels(subjects, fontsize=10)
ax3.set_title("📊  Pass vs Fail by Subject", fontsize=13,
              fontweight="bold", color="white", pad=14)
ax3.set_ylabel("Number of Students", fontsize=9)
ax3.set_ylim(0, 25)
ax3.grid(axis="y", alpha=0.4)
ax3.spines[["top", "right"]].set_visible(False)
ax3.legend(fontsize=9, facecolor="#161B22", edgecolor="#30363D",
           labelcolor="white", loc="upper right")

# ── main title & footer ──────────────────────────────────────────────────────
fig.text(0.5, 1.01,
         "Student Performance Analysis  |  NumPy Mini Project",
         ha="center", fontsize=16, fontweight="bold", color="white")
fig.text(0.5, -0.02,
         "Data: 20 students · 5 subjects · Random seed 40  |  Built with NumPy & Matplotlib",
         ha="center", fontsize=9, color="#8B949E")

plt.tight_layout()
plt.savefig("student_linkedin.png", dpi=180, bbox_inches="tight",
            facecolor="#0D1117")
print("✅  Saved as student_linkedin.png")
plt.show()
