# import re
#
#
# def not_string(str):
#
#     if re.search("not", str):
#         print("in if")
#         return str
#     else:
#         print("in else")
#         return "not " + str
#
#
# a = not_string("not x")
# print(a)
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str