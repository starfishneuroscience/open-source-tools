import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import re

base_file = "logs/run_04/aletwin_ssquare_15.log"
target_msg_1 = "The file stripes.cfg has been copied from the native linux filesystem to the local filesystem."
target_stripe_pattern = re.compile(r"Setting state of stripe (\d+) \[ID:.*?\] to SEQ_CONVERTED")

timestamps = []
stripe_results = []

index = 0
while True:
    if index == 0:
        current_file = base_file
    else:
        current_file = f"{os.path.splitext(base_file)[0]}_{index}.log"

    if not os.path.exists(current_file):
        print("no file found:", current_file)
        break

    with open(current_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f):
            parts = line.strip().split('\t')
            if len(parts) < 6:
                continue

            message = parts[5]

            # Match stripes.cfg message
            if target_msg_1 in message:
                try:
                    date_str = parts[0]
                    time_str = parts[1]
                    dt_obj = datetime.strptime(f"{date_str} {time_str}", "%Y/%m/%d %H:%M:%S.%f")
                    timestamps.append(dt_obj)
                except Exception as e:
                    print(f"Error parsing line {line_num} in {current_file}: {e}")

            # Match stripe state change
            stripe_match = target_stripe_pattern.search(message)
            if stripe_match:
                try:
                    stripe_number = int(stripe_match.group(1))
                    date_str = parts[0]
                    time_str = parts[1]
                    dt_obj = datetime.strptime(f"{date_str} {time_str}", "%Y/%m/%d %H:%M:%S.%f")
                    epoch_time = dt_obj.timestamp()
                    stripe_results.append((os.path.basename(current_file), line_num, stripe_number, epoch_time))
                except Exception as e:
                    print(f"Error parsing stripe line {line_num} in {current_file}: {e}")
    index += 1


# Prepare data
y_vals_1 = list(range(len(timestamps)))
x_vals_1 = timestamps

x_vals_2 = [datetime.fromtimestamp(r[3]) for r in stripe_results]
y_vals_2 = [r[2] for r in stripe_results]  # stripe numbers

fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()  # Secondary y-axis

# Plot primary data (cfg copied)
sc1 = ax1.scatter(x_vals_1, y_vals_1, s=20, label="stripes.cfg copied", color='tab:blue')

# Plot secondary data (stripe converted)
sc2 = ax2.scatter(x_vals_2, y_vals_2, s=30, marker='x', label="stripe converted", color='tab:red')

# Annotation box
annot = ax1.annotate("", xy=(0, 0), xytext=(15, 15), textcoords="offset points",
                     bbox=dict(boxstyle="round", fc="w"),
                     arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

# Axis formatting
ax1.set_xlabel("Time")
ax1.set_ylabel("Message Index", color='tab:blue')
ax2.set_ylabel("Stripe Number", color='tab:red')
ax1.set_title("Log Events Over Time")
ax1.xaxis.set_major_formatter(DateFormatter("%H:%M:%S"))
ax1.grid(True)
fig.tight_layout()
plt.show()