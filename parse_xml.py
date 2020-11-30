
# import packages
import argparse
import re

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to iBug 300-W data split XML file")
ap.add_argument("-t", "--output", required=True,
	help="path output data split XML file")
args = vars(ap.parse_args())

# define the integer indices for mouth
LANDMARKS = set(range(48, 68))

# to easily parse out the mouth locations from the XML file we can
# utilize regular expressions to determine if there is a 'part'
# element on any given line
PART = re.compile("part name='[0-9]+'")

# load the contents of the original XML file and open the output file
# for writing
print("[INFO] parsing data split XML file...")
rows = open(args["input"]).read().strip().split("\n")
output = open(args["output"], "w")

# loop over the input XML file to find and extract the mouth landmarks
for row in rows:
    parts = re.findall(PART, row)
    if len(parts) == 0:
        output.write("{}\n".format(row))
    else:
        attr = "name='"
        i = row.find(attr)
        j = row.find("'", i + len(attr) + 1)
        name = int(row[i + len(attr):j])
        if name in LANDMARKS:
            output.write("{}\n".format(row))
output.close()








