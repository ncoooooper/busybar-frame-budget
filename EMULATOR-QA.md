# Emulator verification

Synthetic Chrome trace, parsed by the production reader.

One of three gaps exceeded the frame budget. The longest gap was 43 ms.

13 distinct frames were recorded on firmware 1.3.1. App io.ncoooooper.framebudget exited: finished; heap peak 82.4 of 128 KiB. Screenshots are in screenshots/ and the recording is in media/.

## Display capture

Firmware 1.3.1 rendered both README examples. The display run replayed sample inputs in a separate emulator project. The source test above describes how those readings were obtained. Each square in a guide GIF is one front-display pixel enlarged to 9 × 9. The production archive was built from the source in this repository.
