# Copyright (C) 2016 Allen Li
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import termios
from unittest import mock

from mir import termdbg


@mock.patch('termios.tcsetattr', autospec=True)
@mock.patch('termios.tcgetattr', autospec=True)
def test_TermAttrsContext(getter, setter):
    getter.return_value = old_attrs = mock.sentinel.old
    new_attrs = mock.sentinel.new
    with termdbg._TermAttrsContext(1):
        termios.tcsetattr(1, termios.TCSANOW, new_attrs)
        assert setter.call_args[0][2] == new_attrs
    assert setter.call_args[0][2] == old_attrs
