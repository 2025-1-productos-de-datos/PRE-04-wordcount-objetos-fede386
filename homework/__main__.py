"""Entry point for the homework package."""

# python3 -m homework 10 data/raw data/input data/output

from .src.main import WordCountApp

if __name__ == "__main__":
    WordCountApp().run()