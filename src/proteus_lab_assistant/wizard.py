from __future__ import annotations
from .autodraw import draw_and_save
from .calibrate import run_calibration
from .checklist import make_checklist
from .console import ask_yes_no, ok, title
from .doctor import run_doctor
from .profile import Profile
from .tasks import available_tasks

def run_wizard() -> int:
    title("Welcome to Proteus Lab Automation Assistant")
    print("This wizard helps a new GitHub user calibrate, choose a task, dry-run, draw, and save.")
    if ask_yes_no("Run system doctor first?", True):
        run_doctor()
    try:
        Profile.load()
        ok("Existing profile found.")
        if ask_yes_no("Recalibrate profile?", False):
            run_calibration()
    except FileNotFoundError:
        print("No profile found. Calibration is required.")
        run_calibration()

    print()
    print("Available tasks:")
    for key, value in available_tasks().items():
        print(f"  {key:20} {value}")
    task = input("Task id [task1_xnor]: ").strip() or "task1_xnor"
    filename = input("Output filename [Lab3_Task1_XNOR.pdsprj]: ").strip() or "Lab3_Task1_XNOR.pdsprj"
    profile = Profile.load()

    if ask_yes_no("Run dry-run first?", True):
        draw_and_save(task, profile, filename, dry_run=True, interactive=False)
    if ask_yes_no("Run real interactive drawing now?", False):
        draw_and_save(task, profile, filename, dry_run=False, interactive=True)
    if ask_yes_no("Create submission checklist?", True):
        out = make_checklist("submission_checklist.md")
        ok(f"Checklist created: {out}")
    ok("Wizard completed.")
    return 0
