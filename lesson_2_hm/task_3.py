month = int(input('[list method] Enter month as a number:'))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if winter.count(month) == 1:
    print('It is winter')
elif spring.count(month) == 1:
    print('It is spring')
elif summer.count(month) == 1:
    print('It is summer')
else:
    print('It is autumn')

month2 = int(input('[dict method] Enter month as a number:'))
year = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
print('It is winter') if year.get('winter').count(month2) > 0 else False
print('It is spring') if year.get('spring').count(month2) > 0 else False
print('It is summer') if year.get('summer').count(month2) > 0 else False
print('It is autumn') if year.get('autumn').count(month2) > 0 else False