#add import
from question_c import use_global

global_variable = 5
print(f"Initial value of global_variable: {global_variable}")

use_global()
print(f"Modified value of global_variable: {global_variable}")