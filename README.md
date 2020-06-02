# mosvg
Monolithic SVG helper python script

Installation
============

Copy `mosvg.py` to wherever it is most convenient for your project. For example `./lib/mosvg.py`, 
where `.` is the root of your pythonpath.

Examples
========

Basic create, draw and write:

```python
import lib.mosvg
svg = lib.mosvg.SVG()
svg.circle(10, 10, 7, style={"stroke":"red"})
svg.write("mydrawing.svg", 32, 32)
```

Drawing with better style definition:

```python
import lib.mosvg
svg = lib.mosvg.SVG(style={
  'circle.myclass' : {
    'stroke': '#ff0000',
    'fill': 'black',
  },
})
svg.circle(10, 10, 7, cls="myclass")
svg.write("mydrawing.svg", 32, 32)
```

Drawing with layers:

```python
import lib.mosvg
svg = lib.mosvg.SVG()
svg.declare_layers("bottom", "top")
svg["top"].circle(10, 10, 7)
svg["bottom"].rect(10, 10, 7, 7)
svg.write("mydrawing.svg", 32, 32)
```
