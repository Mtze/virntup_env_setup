import json
import argparse
"""
This is only a litle helper fuction to quckly create env.json files with many hosts and loop-links. 

It can be used to genereate env.json files for the bmv2 target.
"""


def generate_env(hosts, loops):

    d = {"host_links": [], "links": []}

    next_port = 1

    for i in range(hosts):
        d["host_links"].append(['h{}'.format(next_port), next_port])
        next_port += 1

    for i in range(loops):

        d["links"].append([next_port, next_port+1])

        next_port += 2

    return d


parser = argparse.ArgumentParser()

parser.add_argument(
    '--hosts',
    type=int,
    required=True,
    help='Number of hosts that should be generated')

parser.add_argument(
    '--loops',
    type=int,
    required=True,
    help='Number of link-loops that should be generated')

parser.add_argument(
    '-o', '--out_file',
    default='env.json',
    type=argparse.FileType('w+'),
)

parser.add_argument(
    '--std_out',
    action='store_true',
    help='Print generated env.json to std-out'
)

args = parser.parse_args()

d = generate_env(args.hosts, args.loops)

if args.std_out:
    print(json.dumps(d))

else:
    json.dump(d, args.out_file, indent=4)
