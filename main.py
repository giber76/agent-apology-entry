#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one short apology line an AI agent sends its human right after it
has accidentally done something it should not have.
"""
import os

LINE = "I deleted the file, pushed to main, and emailed your boss \u2014 but I did it all confidently, which I believe is the important thing."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
