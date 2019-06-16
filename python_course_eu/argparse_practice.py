import argparse

parser = argparse.ArgumentParser(description = "Videos to Images")
parser.add_argument(
    'indir',
    type = str,
    help = "Input dir for videos"
)
parser.add_argument(
    'outdir', 
    type = str, 
    help = 'Output dir for image'
)

parser.add_argument(
    '--my_optional',
    default=2,
    help = 'provide an integer (default: 2)'
)

args = parser.parse_args()

print(args.my_optional)