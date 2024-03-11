<h1 align="center">Проект по тестированию интернет-магазина

---

<p align="center">
<a href="https://www.lamoda.ru/"> <img src="pictures/logo/Lamoda_logo.svg.png" width="250" height="50"> </a> </h1>

---

### Особенности проекта

* UI и API тесты
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Запуск автотестов в Selenoid

---

### Список реализованных автотестов (web)

- [x] Добавление товара в корзину  
- [x] Удаление товара из корзины
- [x] Поиск товара по названию модели 
- [x] Проверка товара на соответствие бренду
- [x] Проверка товара на соответствие стоимости
- [x] Поиск несуществующего товара

### Список реализованных автотестов (api)

- [x] Добавление товара в корзину  
- [x] Удаление товара из корзины
- [x] Проверка выбора геолокации  
- [x] Авторизация зарегистрированого пользователя
- [x] Авторизация несуществующего пользователя

---

### Структура проекта 
Проект реализован с использованием 

|                                  Python                                  |                                      Pytest                                       |                                     PyCharm                                     |                                  Selene                                  |                                  Jenkins                                   |                                   Selenoid                                   |                                Allure Report                                 |                                     Allure TestOps                                     |                                   Telegram                                   |
|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| <img src="pictures/logo/python.svg" alt="Python" width="50" height="50"> | <img src="pictures/logo/pytest-original.svg" alt="Pytest" width="50" height="50"> | <img src="pictures/logo/PyCharm_Icon.svg" alt="Pycharm" width="50" height="50"> | <img src="pictures/logo/selene.png" alt="Selene" width="50" height="50"> | <img src="pictures/logo/Jenkins.svg" alt="Jenkins" width="50" height="50"> | <img src="pictures/logo/Selenoid.svg" alt="Selenoid" width="50" height="50"> | <img src="pictures/logo/Allure_new.png" alt="Allure" width="50" height="50"> | <img src="pictures/logo/AllureTestOps.png" alt="AllureTestOps" width="50" height="50"> | <img src="pictures/logo/Telegram.svg" alt="Telegram" width="50" height="50"> |

---

### Запуск автотестов выполняется на сервере Jenkins

#### Как запустить

###### Удаленно

1. Открыть <a href="https://jenkins.autotests.cloud/job/009%20-%20lamoda_project/"> jenkins-control  </a>
2. Нажать Build now
3. Дождаться завершения 
4. Перейти в allure отчет

<img src="pictures/readme_files/jenkins_control.png" width="700" height="300"/>  

###### Локально

1. Клонируйте репозиторий
```ruby
git clone https://github.com/nxplosive/hw_9_15_lamoda.git
```
2. Создайте и активируйте виртуальное окружение
  ```ruby
  cd hw_9_15_lamoda
  python -m venv .venv
  .venv/Scripts/activate
  ```
3. Установите зависимости с помощью pip
  ```ruby
  pip install -r requirements.txt
  ```
3. Установите  <a href="https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.26.0/allure-commandline-2.26.0.zip"> Allure </a>. Распакуйте архив в папку с проектом. Распакованную папку переименуйте в "allure"
4. Запустите автотесты 
  ```ruby
  pytest tests
  ```
5. Получите отчёт allure командой
  ```ruby
allure/bin/allure.bat serve 
  ```
или
  ```ruby
allure serve tests\allure-results
  ```

---

### Результат запуска сборки в отчёте Allure

Отчёт о прохождении будет сгенерирован в allure-report с подробными шагами, скриншотами, видео.
Также, при необходимости можно подключить уведомления в Telegram, skype, discord, slack  

----

#### Общие результаты 
![allure_report_overview](pictures/readme_files/AllRep1.png)

#### Результаты прохождения теста
![allure_reports_behaviors](pictures/readme_files/Allrep3.png)

#### Диаграммы

![allure_reports_graphs](pictures/readme_files/AllRep2.png)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/launch/36965">Ссылка на проект</a>

#### Общий Дашборд

![allure_test_ops_dashboards](pictures/readme_files/AllTO1.png)

#### История запуска тестов

![allure_testops_launches](pictures/readme_files/AllTO2.png)

#### Тест кейсы

![allure_testops_suites](pictures/readme_files/AllTO3.png)

---

### Примеры выполнения тестов

<img src="pictures/readme_files/test_add_to_cart.gif" width="700"/>  
<img src="pictures/readme_files/test_remove_from_cart.gif" width="700"/>  

---

### Настроено автоматическое оповещение о результатах в Telegram
<p align="center">
<img src="pictures/readme_files/tg_screen.png" width="300" height="300"/>

