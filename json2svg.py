import os, sys
import plotly.graph_objects as go
import json
import argparse
import logging
import datetime


def builder():
    parser = argparse.ArgumentParser(description='Build SVG from a JSON representation of a linechart. '
                                                 'Assumption is that the x/y values are assigned to variables t and v')
    parser.add_argument("filePath", help="path to json")
    parser.add_argument("-d", "--debug", help="turn on extra logging level", action="store_true")
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(stream=sys.stdout, filemode="a",
                            format="%(asctime)s - %(module)-12s - %(levelname)-8s - %(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S",
                            level=logging.DEBUG)
        logging.debug("Logging level set to DEBUG")
    else:
        logging.basicConfig(stream=sys.stdout, filemode="a",
                            format="%(asctime)s - %(module)-12s - %(levelname)-8s - %(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S",
                            level=logging.INFO)

    path = args.filePath
    if not path.lower().endswith('.json'):
        logging.critical("Only files with .json extension are supported!")
        sys.exit()
    logging.debug("Filepath is " + path)

    with open(path) as file:
        data = json.load(file)
    logging.debug("JSON successfully loaded!")

    x = []
    y = []
    for o in data:
        x.append(o['t'])
        y.append(o['v'])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y,
                             mode='lines',
                             name='lines'))

    fig.layout.autosize = False
    fig.layout.width = 1400
    fig.layout.height = 600
    # fig.update_layout(paper_bgcolor='#ffffff')
    fig.layout.plot_bgcolor = '#ffffff'
    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_xaxes(visible=False, showticklabels=False)

    if not os.path.exists("output"):
        logging.debug("Output folder does not exist, creating...")
        os.mkdir("output")

    timestamp = str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    img_name = "img" + "_" + timestamp + ".svg"
    fig.write_image("output/" + img_name)
    logging.info("Image saved as " + img_name)


if __name__ == '__main__':
    builder()
