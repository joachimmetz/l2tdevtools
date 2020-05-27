# -*- coding: utf-8 -*-
"""Writer for GIFT PPA script files."""

from __future__ import unicode_literals

import io
import os

from l2tdevtools.dependency_writers import interface


class GIFTPPAInstallScriptPY3Writer(interface.DependencyFileWriter):
  """GIFT PPA installation script file writer for Python 3."""

  _TEMPLATE_FILE = os.path.join(
      'data', 'templates', 'linux_scripts', 'gift_ppa_install.sh')

  PATH = os.path.join('config', 'linux', 'gift_ppa_install_py3.sh')

  def Write(self):
    """Writes a gift_ppa_install_py3.sh.sh file."""
    template_mappings = {'project_name': self._project_definition.name}

    template_file = os.path.join(self._l2tdevtools_path, self._TEMPLATE_FILE)
    file_content = self._GenerateFromTemplate(template_file, template_mappings)

    with io.open(self.PATH, 'w', encoding='utf-8') as file_object:
      file_object.write(file_content)
