import argparse


class ArgumentParser:
    def __init__(self):
        self.input = None


def parse_args():

    parser = argparse.ArgumentParser(description="Count words in files.")

    parser.add_argument(
        "input",
        type=str,
        help="Path to the input folder containing files to process",
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder for results",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def main():
    argument_parser = ArgumentParser()

    file_reader = FileReader(argument_parser.input)
    text_processor = TextProcessor()

    lines = file_reader.read_all_lines()
    preprocessed_lines = text_processor.preprocess(lines)
    words = text_processor()