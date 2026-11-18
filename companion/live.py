"""Read recent frame samples from a running PresentMon or MangoHud capture."""
import csv,io,os,time
from pathlib import Path
from serve import page
def reading(o,m):
    p=Path(o["file"]).expanduser()
    if time.time()-p.stat().st_mtime>float(o.get("stale_seconds",8)):
        return dict(state="Capture stopped",key="stale",pages=[page("GAME FPS","Stale","Start logging in the game")])
    with p.open("rb") as f:
        head=f.read(8192).decode("utf-8-sig","replace").splitlines()
        header=next(line for line in head if any(key in line.lower().split(",") for key in ("fps","msbetweenpresents","frametime")))
        start=max(0,p.stat().st_size-262144);f.seek(start)
        if start:f.readline()
        data=f.read().decode("utf8","replace").splitlines()
    if header in data:data=data[data.index(header)+1:]
    samples=[]
    for row in csv.DictReader([header,*data]):
        try:
            row={str(k).strip().lower():v for k,v in row.items()}
            if o.get("process") and row.get("application","").casefold()!=o["process"].casefold():continue
            if row.get("fps"):
                ms=1000/float(row["fps"])
            else:
                ms=float(row.get("msbetweenpresents") or row["frametime"])
            if 0<ms<60000:samples.append(ms)
        except (ValueError,KeyError,TypeError,ZeroDivisionError):continue
    if not samples:raise ValueError("No matching game samples")
    samples=samples[-60:];fps=round(1000*len(samples)/sum(samples))
    return dict(state="Game capture",key=str(fps),pages=[page("GAME FPS",fps,o.get("process","Selected capture"),f"Last {len(samples)} samples"),page("FRAME TIME",f"{sum(samples)/len(samples):.1f}ms","Mean presentation interval")])
