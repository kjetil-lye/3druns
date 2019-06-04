import argparse
import xml.dom.minidom
import shutil
import os

from xml_tools import set_in_xml, get_xml_node, get_in_xml, read_config
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="""
Splits a configuration into multiple configuration with different 
            """)

    parser.add_argument('--number_of_samples_per_run', type=int, required=True,
                        help='Number of samples per run/individual file')

    parser.add_argument('--config', type=str, required=True,
                        help="Path to configuration file")

    args = parser.parse_args()

    config = read_config(args.config)

    samples = get_in_xml(config, "config.uq.samples")

    if int(samples) % args.number_of_samples_per_run:
        raise Exception("number_of_samples_per_run must be a multiple of the total number of samples. Given:" +\
                        f"\tnumber_of_samples_per_run: {args.number_of_samples_per_run}\n" +\
                        f"\ttotal number of samples  : {samples}")


    number_of_config_files = int(samples) // args.number_of_samples_per_run



    for n in range(number_of_config_files):
        sample_start = n * args.number_of_samples_per_run
        sample_end = (n+1)*args.number_of_samples_per_run

        outfolder = f"sample_{sample_start}_{sample_end}"

        os.mkdir(outfolder)

        set_in_xml(config, "config.uq.samples", args.number_of_samples_per_run)
        try:
            set_in_xml(config, "config.uq.sampleStart", sample_start)
        except:
            uq_node = get_xml_node(config, 'config.uq')

            sample_start_node = config.createElement("sampleStart")
            sample_start_text = config.createTextNode(str(sample_start))

            sample_start_node.appendChild(sample_start_text)

            uq_node.appendChild(sample_start_node)

        python_file = get_in_xml(config, "config.initialData.python")

        shutil.copyfile(os.path.join(os.path.dirname(args.config), python_file),
                             os.path.join(outfolder, python_file))



        with open(os.path.join(outfolder, os.path.basename(args.config)), 'w') as f:
            config.writexml(f)
