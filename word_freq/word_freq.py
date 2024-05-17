import argparse
import json
import wordfreq as wf

parser = argparse.ArgumentParser(
    prog="word_freq",
    description=("Generate the frequency of words in a JSON dictionary."),
)
parser.add_argument(
    "-i", "--input", help="File to use as a dictionary.", required=False
)
parser.add_argument(
    "-o",
    "--output",
    help="File where the output dictionary should be written",
    required=False,
)
parser.add_argument(
    "-e",
    "--error",
    action="store_true",
    help="Flag if error.log should be written to show words without frequencies.",
    required=False,
)

args = parser.parse_args()

if args.input:
    input_path = args.input
else:
    input_path = input("Path to source dict: ")

if args.output:
    output_path = args.output
else:
    output_path = input("Path to output dict: ")

with open(input_path, "r") as file:
    words = []
    for line in file.readlines():
        # words in freq are all lower
        # words in dict have newline chars
        words.append(line.lower().strip())

frequency_dict = wf.get_frequency_dict("en", wordlist="best")

dict_w_freq = {}
missing_freq = []
for word in words:
    try:
        dict_w_freq[word] = wf.freq_to_zipf(frequency_dict[word])
    except KeyError:
        missing_freq.append(word)

with open(output_path, "w") as out_file:
    json.dump(dict_w_freq, out_file, sort_keys=True, indent=4, ensure_ascii=False)

if args.error:
    with open("error.log", "w") as out_file:
        out_file.writelines([f"{n}\n" for n in missing_freq])
