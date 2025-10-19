#add import
from question_c import use_global, global_variable

print(f"Initial value of global_variable: {global_variable}")

use_global()

from question_c import global_variable

print(f"Modified value of global_variable: {global_variable}")