#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Philipp Niedermayer"
__contact__ = "eltos@outlook.de"


__version__ = "0.4.1-rc7"

# allow usage of xplt.mpl.* without importing matplotlib
import matplotlib as mpl

from .units import register_property
from .colors import *
from .line import KnlPlot, FloorPlot
from .phasespace import PhaseSpacePlot
from .timestructure import (
    TimePlot,
    TimeBinPlot,
    TimeFFTPlot,
    TimeIntervalPlot,
    TimeVariationPlot,
    TimeVariationScalePlot,
)
from .twiss import TwissPlot
from .util import average, normalized_coordinates, denormalized_coordinates


from . import hooks

try:
    hooks.register_matplotlib_options()
except:
    pass

try:
    hooks.register_pint_options()
except:
    pass
