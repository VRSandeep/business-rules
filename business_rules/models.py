from __future__ import absolute_import
from collections import namedtuple

ConditionResult = namedtuple('ConditionResult', ['result', 'name', 'operator', 'input_value', 'computed_value', 'parameters'])
