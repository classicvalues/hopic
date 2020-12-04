# Copyright (c) 2020 - 2020 TomTom N.V.
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

from .. import config_reader


def test_example(example_file):
    config_reader.read(example_file, volume_vars={'WORKSPACE': None})


def test_simple_example(simple_example_file):
    config_reader.read(
        simple_example_file,
        {
            'WORKSPACE': None,
            'CT_DEVENV_HOME': '/tools/devenv',
        },
    )


def test_embed_example(embed_example_file):
    config_reader.read(embed_example_file, volume_vars={'WORKSPACE': None})
