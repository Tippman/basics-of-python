def user(name, sirname, b_year, location, e_mail, tel):
    """Выводит данные о пользователе"""
    return f"{name} {sirname}, {b_year} г.р., проживает в г.{location}, e-mail: {e_mail}, телефон: {tel}"


print(user(name=input("Введите имя: "),
           sirname=input("Введите фамиию: "),
           b_year=input("Введите год рождения: "),
           location=input("Введите город проживания: "),
           e_mail=input("Введите ваш e-mail: "),
           tel=input("Введите ваш телефон: ")))
