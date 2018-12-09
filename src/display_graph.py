from webweb.webweb import webweb
import argparse

from graphify import Graphify
from analyze import get_section_sequence

SAVE_GRAPH_PATH = '../data/graph/'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--chronological', '-c', default=False, action="store_true", help="chronological or book time")

    args = parser.parse_args()

    gg = Graphify(300, 50)
    gg.load(SAVE_GRAPH_PATH, range(1,193))

    web = webweb()
    web.display.colorBy = 'degree'
    web.display.sizeBy = 'degree'
    web.display.l = 60
    web.display.c = 120
    web.display.w = 600
    web.display.h = 600

    section_sequence = get_section_sequence(chronological=False)

    for G in gg.graph_by_sections(section_sequence, aggregate=True):
        web.networks.infinite_jest.add_frame_from_networkx_graph(G)

    section_sequence = get_section_sequence(chronological=True)
    for G in gg.graph_by_sections(section_sequence, aggregate=True):
        web.networks.infinite_jest_chronological.add_frame_from_networkx_graph(G)

    web.draw()