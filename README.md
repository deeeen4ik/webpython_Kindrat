# Денис Кіндрат ІПЗ-31
<a id="anchor"></a>

---

## Список лабораторних робіт:
1. [Лабораторна №1](#lab1) 
2. [Лабораторна №2](#lab2) 
3. [Лабораторна №3](#lab3) 
4. [Лабораторна №4](#lab4) 
5. [Лабораторна №5](#lab5) 
6. [Лабораторна №6](#lab6) 
0. [Самостійна робота](#ind) 
7. [Лабораторна №7](#lab7) 
8. [Лабораторна №8](#lab8) 
9. [Лабораторна №9](#lab9) 
11. [Лабораторна №11](#lab11) 
13. [Лабораторна №13](#lab13) 
14. [Лабораторна №14](#lab14) 
0. [Самостійна робота №2](#ind2) 
15. [Лабораторна №15](#lab15) 

---

<a id="lab1"></a>

### Лабораторна №1
#### Завдання 1:
+ Створено звичаний ТСР сервер для обміну сповіщеннями з одним клієнтом

--- 

#### Скріншоти:
__Ex1_1__:
![ex1_1](lab1/screens/ex1_1.png)

__Ex1_2__:
![ex1_2](lab1/screens/ex1_2.png)

__Ex1_3-4__:
![ex1_3-4](lab1/screens/ex1_3-4.png)

---
#### Завдання 2:
+ Створено звичайну багатопоточну чат-кімнату
---
__Ex2_1__:
![ex2_1](lab1/screens/ex2_1.png)

__Ex2_2__:
![ex2_2](lab1/screens/ex2_2.png)

[Вверх](#anchor)

---

<a id="lab2"></a>

### Лабораторна №2
#### Завдання 1_1:
+ Написати СGI-сценарій обробки форми
---
#### Скріншоти:

__Ex1_1-1__:

![ex1_1-1](lab2/screens/ex1_1-1.png)

__Ex1_1-2__:

![ex1_1-2](lab2/screens/ex1_1-2.png)

---

#### Завдання 1_2: 
+ Реалізувати cookies, зокрема має бути лічильник кількості заповнених форм користувачем. Також реалізуйте кнопку, яка видаляє всі cookies.
--- 

#### Скріншоти:

__1. Показ кількості заповння форми__:

![ex1_2-1](lab2/screens/ex1_2-1.png)

__2. Видалення cookies__:

![ex1_2-2](lab2/screens/ex1_2-2.png)

[Вверх](#anchor)

---

<a id="lab3"></a>

### Лабораторна №3
#### Завдання 1:
+ Створити базову сторінку за допомогою flask, скріншоти виконання завдання викладені нижче.

#### Скріншоти:

__1. Портфоліо__:

![lab3_portfolio](Kindrat_Project/app/static/images/lab3/lab3_portfolio.png)

__2. Резюме__:

![lab3_resume](Kindrat_Project/app/static/images/lab3/lab3_resume.png)

__3. Загальна сторінка з навичками__:

![lab3_skills](Kindrat_Project/app/static/images/lab3/lab3_skills.png)

__4. Сторінка, коли вибрана одна навичка__:

![lab3_skill](Kindrat_Project/app/static/images/lab3/lab3_select-skill.png)

[Вверх](#anchor)

---

<a id="lab4"></a>

### Лабораторна №4
#### Завдання 1:
+ Зробити рефакторинг проєкту

#### Скріншоти:

__1. Рефакторинг__:

![](Kindrat_Project/app/static/images/lab4/refactoring.png)

__2. Логін__:

![](Kindrat_Project/app/static/images/lab4/login.png)

__3. Сторінка "info"__:

![](Kindrat_Project/app/static/images/lab4/info1.png)
![](Kindrat_Project/app/static/images/lab4/info2.png)
![](Kindrat_Project/app/static/images/lab4/info3.png)

__4. Додавання cookies__:

![](Kindrat_Project/app/static/images/lab4/adding_cookies.png)
![](Kindrat_Project/app/static/images/lab4/adding_cookies_succsess.png)

__4. Зміна пароля через форму__:

![](Kindrat_Project/app/static/images/lab4/pswrd_before_change.png)
![](Kindrat_Project/app/static/images/lab4/pswrd_after_change.png)

[Вверх](#anchor)

---

<a id="lab5"></a>

### Лабораторна №5
#### Завдання:
+ Переробити форму для входу із попередньої лабораторної роботи, використовуючи WTF-форми + завдання додані комітом update.

#### Скріншоти:

__1. Футер тепер тільки на портфоліо__:

![](Kindrat_Project/app/static/images/lab5/footer_only_portfolio.png)

__2. Новий Логін__:

![](Kindrat_Project/app/static/images/lab5/new_login_page.png)

__3. Попередження щодо входу__:

![](Kindrat_Project/app/static/images/lab5/attention_login.png)

__4. Успішний вхід без "remember me"(з теж працює і перекидає на "info")__:

![](Kindrat_Project/app/static/images/lab5/flash_for_login.png)

__5. Додавання cookies(flash)__:

![](Kindrat_Project/app/static/images/lab5/flash_for_add_cookies.png)

__6. Зміна пароля через форму(flash)__:

![](Kindrat_Project/app/static/images/lab5/change_pass.png)
![](Kindrat_Project/app/static/images/lab5/change_pass_succ.png)

[Вверх](#anchor)

---

<a id="lab6"></a>

### Лабораторна №6
#### Завдання:
+ Розробити сторінку з інтерфейсом операцій CRUD щодо моделі Todo та добавити пункт “Todo” у меню проекту.

#### Скріншоти:

__1. Todo List__:

![](Kindrat_Project/app/static/images/lab6/Todo_page.png)

__2. База даних__:

![](Kindrat_Project/app/static/images/lab6/todo_db.png)

__3. Додавання справи в Todo List__:

![](Kindrat_Project/app/static/images/lab6/add_test_msg.png)

__4. База даних після додавання справи__:

![](Kindrat_Project/app/static/images/lab6/db_after_add.png)

__5. Сторінка зміни справи(Edit Todo)__:

![](Kindrat_Project/app/static/images/lab6/edit_page.png)

__6. Видалення справи з Todo List__:

![](Kindrat_Project/app/static/images/lab6/todo_after_delete.png)
![](Kindrat_Project/app/static/images/lab6/db_after_delete.png)

[Вверх](#anchor)

---

<a id="ind"></a>

### Самостійна робота
#### Завдання:
+ Додати до існуючого проекту форму відгуку, що залишають користувачі. Дані зберігати у базі даних. Cигналізувати про успішні чи не успішні дії flash-повідомленнями. На тій же самій сторінці, що форма, відобразити всі залишені відгуки. Використати WTF-форми і ORM Flask-SQLAlchemy

#### Скріншоти:

__1. Feedback Page__:

![](Kindrat_Project/app/static/images/individial/feedbacks_page.png)

__2. Успішне додавання відгуку__:

![](Kindrat_Project/app/static/images/individial/add_feedback.png)

__3. База даних feedback__:

![](Kindrat_Project/app/static/images/individial/db_feedback.png)


[Вверх](#anchor)

---

<a id="lab7"></a>

### Лабораторна №7
#### Завдання 1:
+ Побудувати модель user і переробити login під базу даних, також реалізувати реєстрацію на сайті

#### Скріншоти:

__1. Оновлена сторінка Login__:

![](Kindrat_Project/app/static/images/lab7/login_page.png)

__2. Сторінка Register__:

![](Kindrat_Project/app/static/images/lab7/register_page.png)

__3. Успішна реєстрація і вхід користувача(user3)__:

![](Kindrat_Project/app/static/images/lab7/create_account.png)
![](Kindrat_Project/app/static/images/lab7/logining.png)

__4. Пароль User1 був зарєстрований до встановлення хешування паролю, ось БД__:

![](Kindrat_Project/app/static/images/lab7/db_hash.png)

__5. Сторінка Users__:

![](Kindrat_Project/app/static/images/lab7/users.png)

__6. Помилка при використання наявних даних в БД при реєстрації__:
![](Kindrat_Project/app/static/images/lab7/novalid.png)

__7. Помилка при вході(введені дані яких немає в БД)__:
![](Kindrat_Project/app/static/images/lab7/novalid_login.png)

[Вверх](#anchor)

---

<a id="lab8"></a>

### Лабораторна №8
#### Завдання 1:
+ Управління сеансами користувачів для зареєстрованих
користувачів.Flask-Login

#### Скріншоти:

__1. Успішних вхід__:

![](Kindrat_Project/app/static/images/lab8/logining.png)

__2. Успішних вихід__:

![](Kindrat_Project/app/static/images/lab8/logged_out.png)

__3. Якщо користувач не увійшов і хоче зайти на сторінки Users або Info, видає ось таке__:

![](Kindrat_Project/app/static/images/lab8/need_to_login.png)

__4. Сторінка My Account після входу__:

![](Kindrat_Project/app/static/images/lab8/my_account.png)

[Вверх](#anchor)

---

<a id="lab9"></a>

### Лабораторна №9
#### Завдання 1:
+ Створити нове оновлення профілю

#### Скріншоти:

__1. Новий Профіль Користувача__:

![](Kindrat_Project/app/static/images/lab9/new_account.png)

__2. Форма зміни даних на аккаунті__:

![](Kindrat_Project/app/static/images/lab9/updating_account.png)

__3. Зміна даних на аккаунті(логіка зміни фото теж прописана, але я так і не зміг розібратися у чому проблема і воно не переписує його у БД)__:

![](Kindrat_Project/app/static/images/lab9/updating_info.png)

__4. Помилка при використанні пошти яка уже використовується__:

![](Kindrat_Project/app/static/images/lab9/error_updating.png)

[Вверх](#anchor)

---

<a id="lab11"></a>

### Лабораторна №11
#### Завдання 1:
+ Створити CRUD модель Post та добавити пагінацію.

#### Скріншоти:

__1. Posts__:

![](Kindrat_Project/app/static/images/lab11/posts.png)

__2. Pagination__:

![](Kindrat_Project/app/static/images/lab11/pagination.png)

__3. Post__:

![](Kindrat_Project/app/static/images/lab11/post.png)

__4. Редагувати Пост__:

![](Kindrat_Project/app/static/images/lab11/edit_post.png)

__5. Створити Пост__:

![](Kindrat_Project/app/static/images/lab11/create.png)

__6. Видалити Пост__:

![](Kindrat_Project/app/static/images/lab11/delele.png)

[Вверх](#anchor)


---

<a id="lab13"></a>

### Лабораторна №13
#### Завдання 1:
+ Створити нове оновлення профілю

#### Скріншоти:

__1. GET(отримання всіх Todo)__:

![](Kindrat_Project/app/static/images/lab13/get_all.png)

__2. PUSH(запис нового Todo)__:

![](Kindrat_Project/app/static/images/lab13/push.png)

__3. GET_ID(отримання Todo за допомогою id)__:

![](Kindrat_Project/app/static/images/lab13/get_by_id.png)

__4. PUT(редагування певного Todo)__:

![](Kindrat_Project/app/static/images/lab13/put.png)

__5. DELETE(видалення певного Todo)__:

![](Kindrat_Project/app/static/images/lab13/delete.png)
![](Kindrat_Project/app/static/images/lab13/get_after_delete.png)

[Вверх](#anchor)

---

<a id="lab14"></a>

### Лабораторна №14
#### Завдання 1:
+ Використати Basic Auth (модуль Flask-HTTPAuth) для реалізації отримання access  jwt-токена тільки для зареєстрованого користувача на сайті. 
+ Розмежуйте доступ до операцій Сreate, Update, Delete для моделі Todo ( доступ до цих операцій тільки по валідному jwt-токену).
+ Обробити всі можливі ситуації при виконанні запитів.

#### Скріншоти:

__1. GET JWT Token__:

![](Kindrat_Project/app/static/images/lab14/get_jwt.png)

__2. Post з jwt token__:

![](Kindrat_Project/app/static/images/lab14/post_jwt.png)

__3. GET todo з jwt__:

![](Kindrat_Project/app/static/images/lab14/get_all.png)

__4. Get з помилкою бо нема jwt__:

![](Kindrat_Project/app/static/images/lab14/get_error.png)

[Вверх](#anchor)

---

<a id="ind2"></a>

### Самостійна робота №2
#### Завдання 1:
+ Створіть RESTful API окремим блюпринтом у вашому проекті з базовими операціями CRUD (створення, читання, оновлення і видалення) для об`єктів моделі у обраній предметній області згідно варіанту (поля моделі придумайте самі, має бути принаймні 3 поля, крім id). Приділіть увагу валідації вхідних даних та обробку помилок, що можуть виникнути під час запиту.
+ Розширте попередній пункт, зокрема, подбайте про безпеку виконання операції оновлення і видалення, використовуючи доступ по валідному токену JWT. Зареєстровані користувачі можуть отримати токен.
+ Протестуйте і заскрініть запити за допомогою Postman.

#### Скріншоти:

__1. Post resume__:

![](Kindrat_Project/app/static/images/ind2/post_resume.png)

__2. Get all resumes__:

![](Kindrat_Project/app/static/images/ind2/get_all_resume.png)

__3. GET without jwt__:

![](Kindrat_Project/app/static/images/ind2/get_error.png)

__4. Update resume__:

![](Kindrat_Project/app/static/images/ind2/update_resume.png)

__5. Delete resume__:

![](Kindrat_Project/app/static/images/ind2/delete_resume.png)

[Вверх](#anchor)

---

<a id="lab15"></a>

### Лабораторна №15
#### Завдання 1:
+ Використати модуль flask_restful для розробки відповідних ендпоінтів  get, post, put, delete. Рекомендується використати  marshmallow/flask_marshmallow для серіалізації  даних у json і десереалізації даних із http-запиту, зокрема і для валідації даних із запиту. Обробити помилки, які можуть виникати під час запитів.
+ Протестувати і заскрінити запити за допомогою Postman.
+ Прикрутити Swagger UI для документації даного API (окремим блюпринтом, використавши, наприклад модуль flask_swagger_ui). Описати.

#### Скріншоти:

__1. Post(Postman)__:

![](Kindrat_Project/app/static/images/lab15/post_user.png)

__2. GET_ALL(Postman)__:

![](Kindrat_Project/app/static/images/lab15/get_all_users.png)

__3. Swagger.ui__:

![](Kindrat_Project/app/static/images/lab15/swagger.png)

__4. GET_ALL(Swagger)__:

![](Kindrat_Project/app/static/images/ind2/swagger_all_user.png)

[Вверх](#anchor)