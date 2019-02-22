from mosvg import SVG


def make():
    xs = [0, 1, 2, 3, 4, 5, 6]
    y1 = [2, 4, 0, 0, 2, 4, 5]
    y2 = [1, 2, 1, 3, 2, 3, 1]
    svg = SVG(style={
        ".dataline.lines2": {
            "stroke": "#55aa55",
        },
        ".datapoint.lines1": {
            "fill": "white",
        },
        ".datapoint.lines2": {
            "fill": "#55aa55",
        },
    })
    chart = svg.xychart(50, 50, 450, 250, 0.0, 6.0, -1.0, 5.0)
    chart.plot([xs, y1], shape="line", cls="lines1", style="stroke:red;stroke-width:2px;")
    chart.plot([xs, y2], shape="line", cls="lines2")
    chart.plotarea()
    return svg


