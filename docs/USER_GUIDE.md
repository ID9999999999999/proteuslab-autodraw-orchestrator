# User Guide

## Beginner workflow

1. Install.
2. Run `proteus-lab doctor`.
3. Open Proteus.
4. Run `proteus-lab calibrate`.
5. Run `proteus-lab wizard`.

## Safe testing

Always start with dry-run:

```bash
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --dry-run
```

Then use interactive mode:

```bash
proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --interactive
```
