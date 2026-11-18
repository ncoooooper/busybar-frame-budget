"""Measure gaps between presented frames on one Chrome trace track."""
import json
from pathlib import Path
from collections import defaultdict
from serve import page
INTERVAL=2
def snapshot(o,m):
    if o.get("mode") == "game":
        from live import reading
        return reading(o,m)
    file=Path(o["file"]).expanduser();fps=float(o.get("fps",60))
    if fps<=0:raise ValueError("Use a positive frame rate")
    data=json.loads(file.read_text());events=data.get("traceEvents",[]) if isinstance(data,dict) else data
    groups=defaultdict(set);frame_name=o.get("event","DrawFrame")
    for e in events:
        if e.get("name")!=frame_name or "ts" not in e or e.get("ph")=="E":continue
        track=str(e.get("pid"))+":"+str(e.get("tid"))
        if o.get("track") and track!=o["track"]:continue
        groups[track].add(float(e["ts"]))
    if not groups:raise ValueError("No matching frame events. Check event and pid:tid track")
    track,times=max(groups.items(),key=lambda v:len(v[1]));times=sorted(times)
    if len(times)<2:raise ValueError("Need two frames on one track")
    budget=1000/fps;gaps=[((b-a)/1000,(a-times[0])/1e6) for a,b in zip(times,times[1:])]
    slow=sum(g>budget+0.01 for g,_ in gaps);worst=sorted(gaps,reverse=True)
    pages=[page("OVER BUDGET",f"{slow}/{len(gaps)}",f"Target {budget:.2f}ms",f"Track {track}",fraction=slow/len(gaps))]
    for g,t in worst[:15]:pages.append(page("FRAME GAP",f"{g:.1f}ms",f"At +{t:.3f}s on track",f"{g/budget:.1f}x target frame"))
    return dict(state="Chrome frame cadence",key=str(slow),pages=pages)
