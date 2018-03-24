#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the helper for building projects from source."""

from __future__ import unicode_literals

import unittest


class DPKGBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build dpkg packages (.deb)."""

  # TODO: add tests for _BuildPrepare
  # TODO: add tests for _BuildFinalize
  # TODO: add tests for _CheckIsInstalled
  # TODO: add tests for _CreateOriginalSourcePackage
  # TODO: add tests for _CreateOriginalSourcePackageFromZip
  # TODO: add tests for _CreatePackagingFiles
  # TODO: add tests for _RemoveOlderDPKGPackages
  # TODO: add tests for _RemoveOlderOriginalSourcePackage
  # TODO: add tests for _RemoveOlderSourceDPKGPackages
  # TODO: add tests for CheckBuildDependencies


class ConfigureMakeDPKGBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build dpkg packages (.deb)."""

  # TODO: add tests for Build
  # TODO: add tests for CheckBuildRequired
  # TODO: add tests for Clean


class ConfigureMakeSourceDPKGBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build source dpkg packages (.deb)."""

  # TODO: add tests for Build
  # TODO: add tests for CheckBuildRequired
  # TODO: add tests for Clean


class SetupPyDPKGBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build dpkg packages (.deb)."""

  # TODO: add tests for _GetFilenameSafeProjectInformation
  # TODO: add tests for Build
  # TODO: add tests for CheckBuildRequired
  # TODO: add tests for Clean


class SetupPySourceDPKGBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build source dpkg packages (.deb)."""

  # TODO: add tests for _GetFilenameSafeProjectInformation
  # TODO: add tests for Build
  # TODO: add tests for CheckBuildRequired
  # TODO: add tests for Clean


if __name__ == '__main__':
  unittest.main()
