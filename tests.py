from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

"""
#get_files_info tests
print("Result for current directory:")
result1 = get_files_info("calculator", ".")
print(result1)

print("\nResult for 'pkg' directory:")
result2 = get_files_info("calculator", "pkg")
print(result2)

print("\nResult for '/bin' directory:")
result3 = get_files_info("calculator", "/bin")
print(result3)

print("\nResult for '../' directory:")
result4 = get_files_info("calculator", "../")
print(result4)
"""

"""
#get_file_content tests
print(get_file_content("calculator", "main.py"))
print(f"\n{get_file_content("calculator", "pkg/calculator.py")}")
print(f"\n{get_file_content("calculator", "/bin/cat")}")
print(f"\n{get_file_content("calculator", "pkg/does_not_exist.py")}")
"""


#write_file tests
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(f"\n{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}")
print(f"\n{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}")
