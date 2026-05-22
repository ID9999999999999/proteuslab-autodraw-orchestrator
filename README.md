# ProteusLab AutoDraw Orchestrator (PLADO): A Calibration-Aware GUI Automation Framework for Proteus ISIS Digital-Circuit Schematic Construction, Guided Verification, and Submission Artifact Packaging

**Short name:** ProteusLab AutoDraw Orchestrator  
**Acronym:** PLADO  
**Repository name:** `proteuslab-autodraw-orchestrator`  
**Author and maintainer:** Yasser Idbouzkri  
**Version:** 0.6.2 Identity Release  
**Domain:** Educational EDA workflow automation, Proteus ISIS GUI orchestration, digital electronics lab tooling.

---

## Executive Summary

ProteusLab AutoDraw Orchestrator (PLADO) is a calibration-aware GUI automation framework designed to accelerate the construction of digital-electronics laboratory schematics in Proteus ISIS. The system converts task-level circuit descriptions into repeatable GUI operations: component selection, schematic placement, calibrated wire routing, screenshot capture, and real Proteus save-dialog execution.

PLADO is built for students and laboratory environments where the main bottleneck is not the digital logic itself, but the repetitive manual work of rebuilding circuits inside Proteus. The framework provides a public, user-calibrated workflow so that every user can adapt the automation layer to their own screen, Proteus layout, zoom level, and workstation configuration.

PLADO does not bypass licensing restrictions, does not generate fake `.pdsprj` files, and does not reverse-engineer the Proteus project format. It operates as a legal human-action accelerator over the real Proteus GUI.

---

## Core Capabilities

- Calibration-based coordinate profile for each user.
- Task-to-schematic AutoDraw workflow.
- Component search and placement through the real Proteus GUI.
- Relative schematic coordinates derived from the user’s calibrated origin.
- Calibrated wire-click sequences for reproducible circuit construction.
- Interactive mode for safe step-by-step execution.
- Dry-run mode for previewing all actions without clicking.
- Screenshot capture for documentation and verification.
- Real Proteus save-dialog execution to the Desktop when saving is permitted by the installed Proteus license.
- Submission checklist generation.
- Submission ZIP helper.
- Task template creation for future labs.
- Public-user workflow with `doctor`, `calibrate`, `wizard`, `tasks`, `explain`, and `auto` commands.

---

## Public Safety Statement

PLADO is a legitimate educational productivity tool. It does not crack Proteus, does not bypass Demonstration Version restrictions, does not manufacture fake project files, and does not rename text files as `.pdsprj`.

The framework only controls the real GUI actions a user could perform manually: clicking, typing, selecting components, placing elements, wiring pins, taking screenshots, and invoking the real Proteus save command.

---

## Quick Start

```bash
python -m pip install -e .
proteus-lab doctor
proteus-lab calibrate
proteus-lab wizard
```

For a safe preview:

```bash
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --dry-run
```

For guided drawing:

```bash
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --interactive
```

---

## Included Task Templates

- `task1_xnor` — 2-input XNOR using `74LS86` and `74LS04`.
- `task2_nand_latch` — Sbar/Rbar NAND latch using `74LS00`.
- `task3_decoder` — 3-bit decoder using `74LS138`.
- `task5_adder` — 4-bit full adder skeleton.

Clock tasks are documented as future advanced templates because they depend heavily on component variants, display models, counter wiring, and reset logic choices.

---

## Recommended GitHub Repository Description

`Calibration-aware GUI automation framework for Proteus ISIS digital-circuit schematic AutoDraw, guided verification, and lab submission packaging.`

---

## Documentation

Start here:

```text
docs/EASY_USAGE_GUIDE.md
docs/TECHNICAL_WHITEPAPER.md
docs/PROJECT_IDENTITY.md
docs/FAQ.md
docs/TROUBLESHOOTING.md
```
