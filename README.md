# mosvg
Monolithic SVG helper python script

Installation
============

Copy `mosvg.py` to wherever it is most convenient for your project. For example `./lib/mosvg.py`, 
where `.` is the root of your pythonpath.

Examples
========

```
import lib.mosvg
svg = lib.mosvg.SVG(style={
  'circle' : {
    'stroke': '#ff0000',
    'fill': 'black',
  },
})
svg.circle(10, 10, 7)
svg.write("mydrawing.svg", 32, 32)
```
