# ProteusLab AutoDraw Orchestrator (PLADO): A Calibration-Aware GUI Automation Framework for Proteus ISIS Digital-Circuit Schematic Construction, Guided Verification, and Submission Artifact Packaging

**Author:** Yasser Idbouzkri  
**Version:** 0.6.2 Identity Release  
**Project Type:** Calibration-aware GUI automation framework for Proteus ISIS digital electronics laboratories  
**Short Name:** ProteusLab AutoDraw Orchestrator  
**Acronym:** PLADO  

---

## Abstract

ProteusLab AutoDraw Orchestrator (PLADO) is a calibration-aware GUI automation framework designed to convert educational digital-circuit laboratory tasks into guided Proteus ISIS schematic construction workflows. The system addresses a practical friction point in electronics education: students frequently understand the required circuit logic but lose time navigating component search, placement, wiring, screenshot capture, and project packaging inside Proteus.

PLADO introduces a task-template architecture combined with user-specific GUI calibration. Each user records the coordinates of key Proteus interface elements and a schematic origin point. Circuit templates then express components and wiring paths relative to that origin. During execution, PLADO translates task templates into mouse and keyboard actions, allowing the user to draw circuits, capture verification screenshots, and request real Proteus project saves on the Desktop.

The framework does not bypass license restrictions, does not reverse-engineer proprietary `.pdsprj` formats, and does not create fake project files. Its design principle is legal GUI orchestration: the automation layer performs the same actions a user could perform manually, but with repeatable structure and reduced operational friction.

---

## 1. Problem Statement

Digital electronics laboratories often require students to build several circuits inside Proteus ISIS: gates, latches, decoders, counters, clocks, and adders. For beginners, Proteus introduces a workflow burden that is separate from the educational objective. The student must repeatedly:

1. search for components;
2. select exact device variants;
3. place components on a schematic;
4. connect pins precisely;
5. test logic states;
6. capture working screenshots;
7. save project files;
8. organize final submission artifacts.

This mechanical workflow can become the main source of delay and error. PLADO is designed to reduce this operational burden while keeping the student inside the legitimate Proteus environment.

---

## 2. Design Philosophy

PLADO follows five engineering principles.

### 2.1 Legal GUI Orchestration

The framework controls the real Proteus interface. It does not manipulate proprietary files directly and does not attempt to bypass saving restrictions.

### 2.2 User-Calibrated Portability

Every workstation has different coordinates, screen resolution, scaling, Proteus theme, and zoom level. PLADO solves this through a local calibration profile.

### 2.3 Task-Template Abstraction

A circuit is represented as a task template containing:

- required components;
- relative schematic placements;
- relative wiring paths;
- verification expectations.

### 2.4 Beginner-Safe Execution

The tool supports dry-run and interactive execution. Users can inspect or approve each step before real clicking.

### 2.5 Submission-Oriented Workflow

The framework includes checklist and packaging commands because lab work is not complete until the report, screenshots, and project files are organized for submission.

---

## 3. System Architecture

PLADO is organized as a layered automation stack.

```text
User Task
   ↓
Task Template
   ↓
Calibration Profile
   ↓
Coordinate Translation
   ↓
GUI Automation Engine
   ↓
Proteus ISIS
   ↓
Screenshots / Real Save Dialog / Submission Pack
```

### 3.1 Task Layer

The task layer defines circuits such as:

- XNOR gate;
- NAND latch;
- 3-bit decoder;
- 4-bit full adder.

Each task is stored as structured data. This makes the framework extensible.

### 3.2 Calibration Layer

The calibration layer stores:

- Pick Devices button location;
- component search box location;
- OK button location;
- schematic origin;
- grid step.

The profile is stored locally at:

```text
~/.proteus_lab_assistant/profile.json
```

### 3.3 GUI Engine

The GUI engine executes:

- clicks;
- hotkeys;
- text entry;
- waits;
- screenshots;
- save-dialog interaction.

### 3.4 Safety Layer

The safety layer prevents unsafe use cases such as fake `.pdsprj` generation or license bypass claims.

---

## 4. Core Commands

### 4.1 System Check

```bash
proteus-lab doctor
```

Checks the Python environment, PyAutoGUI availability, Desktop path, and calibration profile.

### 4.2 Calibration

```bash
proteus-lab calibrate
```

Guides the user through first-time coordinate capture.

### 4.3 Wizard Mode

```bash
proteus-lab wizard
```

Runs a beginner-friendly workflow from system check to optional drawing and checklist generation.

### 4.4 Task Listing

```bash
proteus-lab tasks
```

Lists all available AutoDraw task templates.

### 4.5 Task Explanation

```bash
proteus-lab explain --task task1_xnor
```

Explains components and wire paths for a selected task.

### 4.6 Dry Run

```bash
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --dry-run
```

Prints all planned actions without clicking.

### 4.7 Interactive AutoDraw

```bash
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --interactive
```

Executes the task step by step with user confirmation.

### 4.8 Checklist Generation

```bash
proteus-lab checklist --output submission_checklist.md
```

Creates a lab submission checklist.

### 4.9 Packaging

```bash
proteus-lab pack --output lab_submission_pack.zip --include screenshots submission_checklist.md
```

Creates a submission ZIP from selected files and directories.

---

## 5. Included Digital Electronics Templates

### 5.1 `task1_xnor`

Constructs a 2-input XNOR gate using a 74LS86 XOR stage followed by a 74LS04 inverter stage.

### 5.2 `task2_nand_latch`

Constructs the base layout for an Sbar/Rbar NAND latch using a 74LS00 integrated circuit.

### 5.3 `task3_decoder`

Constructs the base layout for a 3-bit decoder using the 74LS138 device.

### 5.4 `task5_adder`

Constructs a skeleton layout for a 4-bit full adder workflow.

---

## 6. Why Calibration Instead of Fixed Coordinates

A fixed coordinate script works only on one machine. A public GitHub project needs to support many users. PLADO solves this by asking each user to define their own interface geometry once. The task templates then use relative schematic positions, making the workflow more portable.

This design is not as rigid as a native API, but it is practical for Proteus ISIS, where direct schematic construction through a public API is not the standard workflow.

---

## 7. Safety and Licensing Boundary

PLADO requests a save through the real Proteus interface. If Proteus Demonstration Version blocks saving, PLADO cannot and will not bypass that restriction.

This boundary is intentional. It protects the project from unsafe use and keeps it suitable for public GitHub distribution.

---

## 8. Intended Users

PLADO is designed for:

- electronics students;
- laboratory assistants;
- digital logic course participants;
- educators preparing repeatable Proteus demonstrations;
- beginners who need step-by-step circuit construction support;
- students who must prepare report screenshots and project files.

---

## 9. Current Limitations

- Full automatic success depends on correct calibration.
- Wire paths may require adjustment between Proteus versions and symbol variants.
- Clock circuits are not yet fully automated because they require more detailed component-specific wiring.
- Saving depends entirely on the user’s Proteus license.
- The tool controls the GUI, not Proteus internals.

---

## 10. Development Roadmap

### Phase 1 — Public Usability

- wizard mode;
- calibration;
- dry-run;
- interactive execution;
- public documentation.

### Phase 2 — Template Expansion

- more gates;
- multiplexers and demultiplexers;
- counters;
- display drivers;
- clock circuits.

### Phase 3 — Visual Verification

- screenshot comparison;
- expected logic-state checking;
- component placement validation.

### Phase 4 — Community Profiles

- shared calibration examples;
- screen-resolution profiles;
- Proteus version notes;
- task-template gallery.

---

## 11. Conclusion

PLADO is a practical bridge between digital-electronics theory and Proteus-based laboratory execution. It provides a structured, repeatable, and legally safe automation layer for students who need to build, verify, screenshot, and package digital circuit simulations.

Its value is not in replacing Proteus, but in reducing repetitive GUI friction while preserving the real Proteus workflow.
