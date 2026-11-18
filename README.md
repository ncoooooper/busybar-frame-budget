# Frame Budget

Find the longest gaps between displayed frames in a Chrome trace and jump to their timestamp.

Leave the count on the desk while you inspect the trace on the main monitor. Each long gap has a timestamp relative to the first matching frame, so you can locate the relevant part of the recording.

## Locate the longest gap

1. Export an uncompressed Chrome trace and select the frame event and target frame rate.
2. Read **OVER BUDGET** as slow intervals out of all intervals on the chosen track. In the example one of three exceeded the budget.
3. Turn to **FRAME GAP** and read the relative timestamp on the rear. Find that time on the same track in the trace viewer.

![One of three intervals is over budget; the longest gap is 43.0 ms.](media/guide/inspect-longest-gap.gif)

## Compare another capture

1. Return to **OVER BUDGET** to check the target in milliseconds and the selected `pid:tid`.
2. Take a second trace of the same interaction and point the companion at it. Keep the frame rate and event or track selection comparable.
3. Click to refresh. Inspect the location of a gap before associating it with a dropped animation frame, since intentional idle periods can also be long.

![The frame gap of 43.0 ms returns to the 1/3 summary.](media/guide/return-to-count.gif)

## Example from the emulator

At 60 fps the nominal budget is about 16.67 ms. A 43 ms gap spans about 2.6 frame periods. Timestamps from unrelated tracks are kept separate. The companion parsed a synthetic Chrome trace for this recording.

## Set up the source

Export a Chrome or Chromium performance trace as uncompressed JSON. Set file, fps and the frame event name (default DrawFrame). Optionally set track to pid:tid. Otherwise the busiest matching track is selected. Gaps compare successive timestamps on that single track and include intentional idle time. Interpret them within the animation you recorded.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run in the emulator

Open BUSY Bar Emulator. From this repository, run:

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

Press **Back** to exit.

The GIFs are excerpts from the emulator recording. Each front-display pixel is shown at 9× its original width and height. The end frames pause for reading.

[Full recording](media/controls.mp4) · [Rear display](screenshots/back-1.png) · [Firmware test](EMULATOR-QA.md) · [MIT license](LICENSE)
