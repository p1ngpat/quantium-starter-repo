# test_app.py
from app import app

def test_header_is_present():
    layout = app.layout
    # Check the H1 exists with correct text
    h1 = layout.children[0]
    assert h1.children == "Soul Foods Pink Morsel Sales"

def test_visualisation_is_present():
    layout = app.layout

    graph_div = layout.children[3] # The graph div is the 3rd child
    graph = graph_div.children[0]
    assert graph.id == "sales-graph"

def test_region_picker_is_present():
    layout = app.layout
    radio_div = layout.children[2] #3 rd child region picker div
    radio = radio_div.children[1]
    assert radio.id == "radio-items"