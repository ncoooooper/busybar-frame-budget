# Frame Budget

Read a running game’s FPS from PresentMon or MangoHud, or inspect long frame intervals in a Chrome trace.

Leave the count on the desk while you inspect the trace on the main monitor. Each long gap has a timestamp relative to the first matching frame, so you can locate the relevant part of the recording.

The bars rank up to eight frame gaps from longest to shortest. They use measured durations from the selected trace. A pale bar identifies the gap currently on screen.

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

## Additional source setup

Windows: use PresentMon’s console capture with `PresentMon.exe --process_name ExampleGame.exe --output_file capture.csv` while the game is running. Set `process` to the executable name in the CSV. Linux: enable MangoHud logging for the game, start the logging hotkey (normally Left Shift + F2), point `file` at the current CSV and omit `process` for a single-game MangoHud log. Keep the capture writing to disk. If the logger buffers writes, increase `stale_seconds` to match its flush interval. The original trace mode still accepts Chrome DrawFrame events.

From the repository root, copy the example and start the companion with Python 3.10 or newer.

```sh
cp companion/live-example.json config.json
# Edit config.json for your source before starting the server.
python3 companion/serve.py --config config.json
```

In the emulator, run `~/.busy-emulator/bin/busy-emulator allow-local 8770` and approve that port. Open **Apps → Frame Budget → Setup**, set **Local companion URL** to `http://127.0.0.1:8770/reading`, save, then reopen the app. For a physical bar, start the companion with `--host YOUR_LAN_IP` and replace `127.0.0.1` with that address. Bind only to your trusted network. Open `/reading` on the host to inspect the current reading. Keep credentials in the host environment.

## Read the game frame rate

Open GAME FPS while playing. The display reports the rate calculated from up to sixty recent presentation intervals, or from FPS samples in the MangoHud log. A stopped or old capture reads Stale.

![The example moves from 60 FPS to the mean frame interval.](media/guide/use-1.gif)

## Check frame pacing

Turn to FRAME TIME for the mean interval in milliseconds. At a steady 60 FPS it is about 16.7 ms. Turn back to FPS while changing an in-game graphics setting. The companion reads capture data recorded by the host, so no game modification is required.

![The frame-time reading returns to the game FPS page.](media/guide/use-2.gif)

The recordings use example responses on emulator firmware. Each display pixel is enlarged to a 9 × 9 square.

[Intel PresentMon](https://github.com/GameTechDev/PresentMon) · [MangoHud logging](https://github.com/flightlessmango/MangoHud).
