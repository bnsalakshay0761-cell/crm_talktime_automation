import pandas as pd
from tkinter import filedialog
import os

# Select CRM report - Directly use the file path as it's already in the environment.
file = "/content/3g status.xlsx"

# ---------- SHEET 1 ----------
master = pd.read_excel(file, sheet_name="Sheet1")

master["Status"] = master["Status"].astype(str).str.strip().str.upper()
master["Connected Status"] = master["Connected Status"].astype(str).str.strip().str.upper()

# Get all dispositions marked YES
connected_dispositions = master.loc[
    master["Connected Status"] == "YES", "Status"
].tolist()


# ---------- SHEET 2 ----------
df = pd.read_excel(
    file,
    sheet_name="Sheet2",
    header=4
)

df.columns = df.columns.astype(str).str.strip()

# Remove blank agent rows
df = df[df["USER NAME"].notna()].copy()


# ---------- TIME CONVERSION ----------
def seconds(x):
    if pd.isna(x):
        return 0

    if hasattr(x, "hour"):
        return x.hour * 3600 + x.minute * 60 + x.second

    try:
        return pd.to_timedelta(x).total_seconds()
    except:
        return 0


# Convert required time columns
for col in ["WAIT", "TALK", "DISPO", "CUSTOMER"]:
    df[col + "_SEC"] = df[col].apply(seconds)


# ---------- TOTAL TALKTIME ----------
df["TOTAL_TALKTIME"] = (
    df["WAIT_SEC"]
    + df["TALK_SEC"]
    + df["DISPO_SEC"]
)


# ---------- CONNECTED CALLS ----------
# Only use disposition columns that:
# 1. Are marked YES in Sheet1
# 2. Actually exist in today's Sheet2

available_connected = [
    d for d in connected_dispositions
    if d in df.columns
]

if available_connected:
    df["CONNECTED_CALLS"] = df[available_connected].apply(
        pd.to_numeric, errors="coerce"
    ).fillna(0).sum(axis=1)
else:
    df["CONNECTED_CALLS"] = 0


# ---------- COUNSELOR-WISE REPORT ----------
report = df.groupby("USER NAME").agg(
    **{
        "Total Calls": ("CALLS", "sum"),
        "Total Talktime": ("TOTAL_TALKTIME", "sum"),
        "Connected Talktime": ("CUSTOMER_SEC", "sum"),
        "Connected Calls": ("CONNECTED_CALLS", "sum")
    }
).reset_index()

report = report.rename(columns={"USER NAME": "Agent Name"})


# ---------- CONVERT SECONDS TO HH:MM:SS ----------
def time_format(x):
    x = int(x)
    return f"{x//3600:02d}:{(x%3600)//60:02d}:{x%60:02d}"


report["Total Talktime"] = report["Total Talktime"].apply(time_format)
report["Connected Talktime"] = report["Connected Talktime"].apply(time_format)


# ---------- FINAL 5 COLUMNS ----------
report = report[
    [
        "Agent Name",
        "Total Calls",
        "Total Talktime",
        "Connected Talktime",
        "Connected Calls"
    ]
]


# ---------- SAVE ----------
output = os.path.join(
    os.path.dirname(file),
    "Daily_Talktime_Report.xlsx"
)

report.to_excel(output, index=False)

print("Report created successfully:")
print(output)
