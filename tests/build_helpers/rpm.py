#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the helper for building projects from source."""

from __future__ import unicode_literals

import os
import unittest

from l2tdevtools.build_helpers import rpm
from l2tdevtools import projects
from l2tdevtools import source_helper


class TestSourceHelperWithFailingCreate(source_helper.SourceHelper):
  """Test source helper that with failing Create function."""

  def Create(self):
    """Creates the source directory.

    Returns:
      str: name of the source directory or None on error.
    """
    return None

  def GetProjectIdentifier(self):
    """Retrieves the project identifier for a given project name.

    Returns:
      str: project identifier or None on error.
    """
    return 'test'


class BaseRPMBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build mRPM packages (.rpm)."""

  # TODO: add tests for _BuildFromSpecFile
  # TODO: add tests for _BuildFromSourcePackage
  # TODO: add tests for _CheckIsInstalled
  # TODO: add tests for _CopySourcePackageToRPMBuildSources
  # TODO: add tests for _CreateRPMbuildDirectories
  # TODO: add tests for _CreateSpecFile
  # TODO: add tests for _CopySourceFile
  # TODO: add tests for _GetFilenameSafeProjectInformation
  # TODO: add tests for _GetSetupPySpecFilePath
  # TODO: add tests for _MoveFilesToCurrentDirectory
  # TODO: add tests for CheckBuildDependencies


class RPMBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build RPM packages (.rpm)."""

  # TODO: add tests for _RemoveBuildDirectory
  # TODO: add tests for _RemoveOlderBuildDirectory
  # TODO: add tests for _RemoveOlderRPMs
  # TODO: add tests for CheckBuildRequired


class ConfigureMakeRPMBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build RPM packages (.rpm)."""

  # TODO: add tests for _MoveRPMs

  @unittest.skipUnless(
      os.path.isfile('/usr/bin/rpmbuild'), 'Missing rpmbuild')
  def testBuild(self):
    """Tests the Build function."""
    # TODO: implement
    pass

  # TODO: add tests for Clean


class SetupPyRPMBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build RPM packages (.rpm)."""

  # TODO: add tests for _GenerateSpecFile
  # TODO: add tests for _MoveRPMs

  @unittest.skipUnless(
      os.path.isfile('/usr/bin/rpmbuild'), 'Missing rpmbuild')
  def testBuild(self):
    """Tests the Build function."""
    # TODO: implement
    pass

  # TODO: add tests for Clean


class SRPMBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build source RPM packages (.src.rpm)."""

  # TODO: add tests for _MoveRPMs
  # TODO: add tests for _RemoveOlderSourceRPMs
  # TODO: add tests for CheckBuildRequired
  # TODO: add tests for Clean


class ConfigureMakeSRPMBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build source RPM packages (.src.rpm)."""

  @unittest.skipUnless(
      os.path.isfile('/usr/bin/rpmbuild'), 'Missing rpmbuild')
  def testBuild(self):
    """Tests the Build function."""
    # TODO: implement
    pass


class SetupPySRPMBuildHelperTest(unittest.TestCase):
  """Tests for the helper to build source RPM packages (.src.rpm)."""

  # pylint: disable=protected-access

  def testGenerateSpecFile(self):
    """Tests the _GenerateSpecFile function."""
    # TODO: test _GenerateSpecFile success

    l2tdevtools_path = '.'
    project_definition = projects.ProjectDefinition('test')
    source_helper_object = TestSourceHelperWithFailingCreate(
        'test', project_definition)

    build_helper = rpm.SetupPySRPMBuildHelper(
        project_definition, l2tdevtools_path)

    output_file_path = build_helper._GenerateSpecFile(
        'test', '1.0.0', 'test-1.0.0.tar.gz', source_helper_object)
    self.assertIsNone(output_file_path)

  @unittest.skipUnless(
      os.path.isfile('/usr/bin/rpmbuild'), 'Missing rpmbuild')
  def testBuild(self):
    """Tests the Build function."""
    l2tdevtools_path = '.'
    project_definition = projects.ProjectDefinition('test')

    build_helper = rpm.SetupPySRPMBuildHelper(
        project_definition, l2tdevtools_path)

    # TODO: implement
    _ = build_helper


if __name__ == '__main__':
  unittest.main()
