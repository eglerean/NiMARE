# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Coordinate-based meta-analysis estimators
"""
import warnings

from .base import CBMAEstimator
from ...due import due, Doi


@due.dcite(Doi('10.1093/scan/nsm015'),
           description='Introduces the MKDA algorithm.')
class MKDA(CBMAEstimator):
    """
    Multilevel kernel density analysis
    """
    def __init__(self, dataset, voxel_thresh=0.01, corr='FDR', prior=0.5,
                 min_studies=1):
        self.dataset = dataset
        self.voxel_thresh = voxel_thresh
        self.corr = corr
        self.prior = prior
        self.min_studies = min_studies

    def fit(self, sample):
        pass
