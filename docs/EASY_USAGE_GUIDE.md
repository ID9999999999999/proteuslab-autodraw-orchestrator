# Easy Usage Guide

This guide explains the simplest way to use **Proteus Lab Automation Assistant**.

The tool helps you draw simple digital circuits in Proteus by controlling the mouse and keyboard. It does not create fake Proteus files. It asks the real Proteus program to draw and save the project.

---

## 1. What you need

Before using the tool, make sure you have:

- Windows
- Python installed
- Proteus installed
- A Proteus version that allows saving if you want `.pdsprj` files

If your Proteus version is a Demonstration Version and says saving is disabled, this tool cannot fix that.

---

## 2. Install the tool

Open the project folder.

Double-click:

```text
scripts/setup_windows.bat
```

Wait until installation finishes.

---

## 3. Start the beginner wizard

Double-click:

```text
scripts/launch_wizard.bat
```

Or run this command:

```bash
proteus-lab wizard
```

The wizard will guide you step by step.

---

## 4. Check your system

You can check if everything is ready with:

```bash
proteus-lab doctor
```

This checks Python, pyautogui, Desktop path, and the calibration profile.

---

## 5. Calibrate once

Calibration means teaching the tool where important buttons are on your screen.

Open Proteus first, then run:

```bash
proteus-lab calibrate
```

The tool will ask you to move your mouse to:

1. the **Pick Devices** button;
2. the **Pick Devices search box**;
3. the **OK** button in the Pick Devices window;
4. a clean point on the schematic page.

After this, a profile is saved automatically here:

```text
~/.proteus_lab_assistant/profile.json
```

You usually need to do this only once.

---

## 6. See available tasks

Run:

```bash
proteus-lab tasks
```

Current task examples:

```text
task1_xnor
task2_nand_latch
task3_decoder
task5_adder
```

---

## 7. Try without clicking first

Before letting the tool click in Proteus, run a dry test:

```bash
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --dry-run
```

Dry-run mode only prints the actions. It does not click anything.

---

## 8. Draw slowly, step by step

Use interactive mode for safety:

```bash
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --interactive
```

In this mode, the tool asks you to press Enter before each action. This is the safest mode for beginners.

---

## 9. Save the project

At the end, the tool presses the real Proteus save command and types a Desktop path such as:

```text
Desktop/Lab3_Task1_XNOR.pdsprj
```

If Proteus allows saving, the real project file will be saved.

If Proteus blocks saving, you need a licensed or university Proteus version.

---

## 10. Create a submission checklist

Run:

```bash
proteus-lab checklist --output submission_checklist.md
```

This creates a checklist to verify your report and Proteus files before submission.

---

## 11. Pack files into a ZIP

After you have screenshots and checklist, run:

```bash
proteus-lab pack --output lab3_submission_pack.zip --include screenshots submission_checklist.md
```

You can also manually add your PDF report and real Proteus files to the ZIP.

---

## Best beginner workflow

Use this order:

```bash
proteus-lab doctor
proteus-lab calibrate
proteus-lab tasks
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --dry-run
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --interactive
proteus-lab checklist --output submission_checklist.md
```

That is the simplest safe workflow.
