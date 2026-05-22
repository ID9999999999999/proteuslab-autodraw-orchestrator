from __future__ import annotations
from pathlib import Path

CHECKLIST_TEXT = '''# Proteus Lab Submission Checklist

## Before submission

- [ ] PDF report is included.
- [ ] Real Proteus files are included.
- [ ] Files open in Proteus.
- [ ] Task 1 XNOR works for 00, 01, 10, 11.
- [ ] Task 2 NAND latch set/reset/hold tested.
- [ ] Task 3 decoder selects correct output.
- [ ] Task 4 clock screenshot included if automation is not complete.
- [ ] Task 5 adder test 0110 + 0011 = 1001 verified.
- [ ] No fake .pdsprj files.
- [ ] Files are packed in one ZIP if required.

## Suggested filenames

- Lab3_Task1_XNOR.pdsprj
- Lab3_Task2_Sbar_Rbar_NAND_Latch.pdsprj
- Lab3_Task3_3bit_Decoder_74LS138.pdsprj
- Lab3_Task4_Simple_2digit_Clock.pdsprj
- Lab3_Task4_24hour_Clock.pdsprj
- Lab3_Task5_4bit_Full_Adder.pdsprj
'''

def make_checklist(output: str | Path) -> Path:
    out = Path(output)
    out.write_text(CHECKLIST_TEXT, encoding="utf-8")
    return out
