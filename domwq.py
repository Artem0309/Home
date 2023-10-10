# result = []
#
# def divider(a, b):
#     try:
#         if a < b:
#             raise ValueError
#         if b > 100:
#             raise IndexError
#         return a/b
#     except ValueError:
#         print(f"Ошибка: a ({a}) должно быть больше или равно b ({b})")
#     except IndexError:
#         print(f"Ошибка: b ({b}) должно быть меньше или равно 100")
#
# data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
#
# for key in data:
#     try:
#         res = divider(key, data[key])
#         result.append(res)
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
# print(result)









# result = []
#
# def divider(a, b):
#     try:
#         a = float(a)
#         b = float(b)
#         if a < b:
#             raise ValueError(f"Ошибка: {a} должно быть больше или равно {b}")
#         if b > 100:
#             raise IndexError(f"Ошибка: {b} должно быть меньше или равно 100")
#         return a/b
#     except (ValueError, IndexError) as e:
#         print(e)
#
# data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
#
# for key in data:
#     try:
#         res = divider(key, data[key])
#         if res is not None:
#             result.append(res)
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
# print(result)
# result = []
#
# def divider(a, b):
#     try:
#         if a < b:
#             raise ValueError
#         if b > 100:
#             raise IndexError
#         return a/b
#     except ValueError:
#         print(f"Ошибка: a ({a}) должно быть больше или равно b ({b})")
#     except IndexError:
#         print(f"Ошибка: b ({b}) должно быть меньше или равно 100")
#
# data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
#
# for key in data:
#     try:
#         res = divider(key, data[key])
#         result.append(res)
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
# print(result)

