from __future__ import annotations
import argparse
import json
from .autodraw import draw_and_save
from .calibrate import run_calibration
from .checklist import make_checklist
from .doctor import run_doctor
from .engine import GuiEngine
from .packer import pack_submission
from .profile import Profile
from .safety import legal_notice
from .tasks import available_tasks, get_task
from .template_creator import create_task_template
from .wizard import run_wizard

def cmd_wizard(args): return run_wizard()
def cmd_doctor(args): return run_doctor()
def cmd_calibrate(args): run_calibration(); return 0

def cmd_profile(args):
    if args.profile_action == "show":
        profile = Profile.load()
        print(json.dumps(profile.data, indent=2, ensure_ascii=False))
    elif args.profile_action == "export":
        out = Profile.load().export(args.output)
        print(f"Profile exported: {out}")
    elif args.profile_action == "import":
        out = Profile.import_profile(args.input)
        print(f"Profile imported to: {out}")
    return 0

def cmd_tasks(args):
    for key, title in available_tasks().items():
        print(f"{key:20} {title}")
    return 0

def cmd_explain(args):
    task = get_task(args.task)
    print(f"{args.task}: {task['title']}")
    print("Components:")
    for c in task.get("components", []):
        print(f"- {c['name']} x{len(c.get('placements', []))}")
    print("Wires:")
    for w in task.get("wires", []):
        print(f"- {w['label']}")
    return 0

def cmd_auto(args):
    print(legal_notice())
    profile = Profile.load(args.profile)
    draw_and_save(args.task, profile, args.filename, args.dry_run, args.interactive)
    return 0

def cmd_mouse(args):
    p = GuiEngine().current_position()
    print(f"x={p.x}, y={p.y}")
    return 0

def cmd_screenshot(args):
    out = GuiEngine().screenshot(args.output)
    print(f"Saved: {out}")
    return 0

def cmd_checklist(args):
    out = make_checklist(args.output)
    print(f"Checklist created: {out}")
    return 0

def cmd_pack(args):
    out = pack_submission(args.output, args.include)
    print(f"Submission pack created: {out}")
    return 0

def cmd_new_task(args):
    out = create_task_template(args.task, args.title, args.output)
    print(f"Task template created: {out}")
    return 0

def build_parser():
    parser = argparse.ArgumentParser(prog="proteus-lab")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("wizard"); p.set_defaults(func=cmd_wizard)
    p = sub.add_parser("doctor"); p.set_defaults(func=cmd_doctor)
    p = sub.add_parser("calibrate"); p.set_defaults(func=cmd_calibrate)

    p = sub.add_parser("profile")
    profile_sub = p.add_subparsers(dest="profile_action", required=True)
    ps = profile_sub.add_parser("show"); ps.set_defaults(func=cmd_profile)
    ps = profile_sub.add_parser("export"); ps.add_argument("--output", required=True); ps.set_defaults(func=cmd_profile)
    ps = profile_sub.add_parser("import"); ps.add_argument("--input", required=True); ps.set_defaults(func=cmd_profile)

    p = sub.add_parser("tasks"); p.set_defaults(func=cmd_tasks)
    p = sub.add_parser("explain"); p.add_argument("--task", required=True); p.set_defaults(func=cmd_explain)

    p = sub.add_parser("auto")
    p.add_argument("--task", required=True)
    p.add_argument("--filename", required=True)
    p.add_argument("--profile", default=None)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--interactive", action="store_true")
    p.set_defaults(func=cmd_auto)

    p = sub.add_parser("mouse"); p.set_defaults(func=cmd_mouse)
    p = sub.add_parser("screenshot"); p.add_argument("--output", required=True); p.set_defaults(func=cmd_screenshot)
    p = sub.add_parser("checklist"); p.add_argument("--output", default="submission_checklist.md"); p.set_defaults(func=cmd_checklist)

    p = sub.add_parser("pack")
    p.add_argument("--output", default="lab_submission_pack.zip")
    p.add_argument("--include", nargs="+", default=["screenshots", "submission_checklist.md"])
    p.set_defaults(func=cmd_pack)

    p = sub.add_parser("new-task")
    p.add_argument("--task", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--output", default="new_task_template.json")
    p.set_defaults(func=cmd_new_task)
    return parser

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
