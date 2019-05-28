from xml_tools import read_config, get_in_xml
import sys
import os
import subprocess
from pathlib import Path

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="""
Submits the configuration file leonhard. NOTE: Will run in folder of configuration file!
""")


    parser.add_argument('--alsuqcli_path', type=str, default=str(os.path.join(str(Path.home()), 'alsvinn/build/alsuqcli/alsuqcli')),
                        help="path to alsuqlci")
    parser.add_argument('--config', type=str, required=True,
                        help="Path to configuration file")
    parser.add_argument('--wait_time', type=int, default=24,
                        help='Wait time in hours')
    parser.add_argument('--multi_sample', type=int, default=1,
                        help='Number of processes to use in the sample direction')
    parser.add_argument('--dry_run', action='store_true',
                        help='Only do a dry run, no actual submission done')

    args = parser.parse_args()
    configuration_file = args.config

    configuration_path = os.path.dirname(configuration_file)

    config = read_config(configuration_file)

    resolution = int(get_in_xml(config, 'config.fvm.grid.dimension').split(" ")[0])

    number_of_nodes_per_direction = max(1, resolution // 256)

    total_number_of_nodes = number_of_nodes_per_direction**3*args.multi_sample



    r_command_append = "rusage[ngpus_excl_p=8,mem=8000] span[ptile=8]"

    command_to_run = [

        'bsub',
        '-R',
        r_command_append,
        '-W',
        f'{args.wait_time}:00',
        '-n',
        str(total_number_of_nodes),
        'mpirun',
        '-np',
        str(total_number_of_nodes),
        args.alsuqcli_path,
        '--multi-sample',
        str(args.multi_sample),
        '--multi-x',
        str(number_of_nodes_per_direction),
        '--multi-y',
        str(number_of_nodes_per_direction),
        '--multi-z',
        str(number_of_nodes_per_direction),
        os.path.basename(configuration_file),
    ]

    if args.dry_run:
        command_to_run = ['echo', *command_to_run]


    subprocess.run(command_to_run, check = True, cwd = configuration_path)

