# Easy Usage Guide

This guide explains the simplest way to use **ProteusLab AutoDraw Orchestrator (PLADO)**.

PLADO helps you draw simple digital circuits in Proteus by controlling the mouse and keyboard. It does not create fake Proteus files. It asks the real Proteus program to draw and save the project.

## Simplified calibration

Open Proteus first.

Then open the **Pick Devices** window manually:

- press `P`, or
- click the Pick Devices button.

Keep the Pick Devices window visible.

Now run:

```bash
proteus-lab calibrate
```

The tool asks for only three useful points:

1. the **Pick Devices search/keyword box**;
2. the **Pick Devices OK button**;
3. one clean point on the schematic page after you close Pick Devices.

The tool does **not** ask for the Pick Devices `P` button anymore.

## Safe workflow

```bash
proteus-lab doctor
proteus-lab calibrate
proteus-lab tasks
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --dry-run
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --interactive
```
