#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from os.path import abspath
from unittest import TestCase
import mock

from preggy import expect

from thumbor.detectors.profile_detector import Detector


class ProfileDetectorTestCase(TestCase):
    def test_detector_uses_proper_cascade(self):
        cascade = './tests/fixtures/haarcascade_profileface.xml'
        ctx = mock.Mock(
            config=mock.Mock(
                PROFILE_DETECTOR_CASCADE_FILE=abspath(cascade),
            )
        )

        detector = Detector(ctx, 1, [])
        expect(detector).not_to_be_null()
