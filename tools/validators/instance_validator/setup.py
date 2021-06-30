# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup file for Instance Validator"""

from setuptools import setup, find_packages

setup(
    name='instance-validator',
    version='0.0.1',
    url='https://github.com/google/digitalbuildings',
    license='Apache License',
    author='(in alphabatical order)'
           'Keith Berkoben,'
           'Raymond Li,'
           'Charbel Kaed,'
           'Nigel Kilmer',
    packages=find_packages(),
    install_requires=['ruamel.yaml>=0.17.4',
                      'protobuf>=3.14.0',
                      'strictyaml>=1.1.1',
                      'google-cloud-pubsub',
                      'google-auth<2.0',
                      'googleapis-common-protos==1.52.0'],
    python_requires='>=3.7',
)
