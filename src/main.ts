import {marks} from "./front";
import {instrument} from "@shared/instrument";

instrument({
  marks,
  "title": "FRAME BUDGET",
  "primary": "Frame Budget",
  "accent": "#E7AB67",
  "cadence": 2000,
  "motion": {enabled:false},
  "setup": "Start companion/serve.py"
});
