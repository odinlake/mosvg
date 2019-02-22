from mosvg import SVG


def make():
    xs = [0, 1, 2, 3, 4, 5, 6]
    y1 = [2, 4, 0, 0, 2, 4, 5]
    y2 = [1, 2, 1, 3, 2, 3, 1]
    y3 = [4, 2, 1, 2, 3, 2, 1]
    svg = SVG(style={
        ".bars1": {
            "fill": "#cc8866",
        },
        ".bars2": {
            "fill": "#77cc77",
        },
        ".bars3": {
            "fill": "#6688cc",
        },
    })
    chart = svg.xychart(50, 50, 450, 250, -0.5, 6.5, 0.0, 10.0).config({
        "xtype": "enum",
    })
    with chart.stack() as ctx:
        ctx.plot([xs, y1], shape="bar", cls="bars1")
        ctx.plot([xs, y2], shape="bar", cls="bars2")
        ctx.plot([xs, y3], shape="bar", cls="bars3")
    chart.plotarea()
    return svg


