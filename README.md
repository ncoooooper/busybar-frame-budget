# Frame Budget

Find the longest gaps between displayed frames in a Chrome trace and jump to their timestamp.

Export a Chrome or Chromium performance trace as uncompressed JSON. Set file, fps and the frame event name (default DrawFrame). Optionally set track to pid:tid. Otherwise the busiest matching track is selected. Gaps compare successive timestamps on that single track and include intentional idle time. Interpret them within the animation you recorded.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
