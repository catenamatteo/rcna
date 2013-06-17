#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Social Network Analysis of the UAMS's CTSA grant"""
'''
	utils.py for grant_data
''' 
__appname__ = "Research Collaboration Social Network Analysis"
__author__  = "Jiang Bian"
__version__ = "0.0.1"
__license__ = "MIT"

import logging
import os
from network_analysis.networks import GrantResearcherNetwork

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def root_folder():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))


def load_network_for(budgetYears):

	startBudgetYear = budgetYears[0]
	endBudgetYear = budgetYears[-1]
	
	filename = '%s/data/networks/%d-%d.graphml'%(root_folder(),startBudgetYear, endBudgetYear)
	network = GrantResearcherNetwork.read(filename)

	return network