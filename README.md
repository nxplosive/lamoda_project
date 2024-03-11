# Проект по тестированию сайта банка "ВТБ"
> <a target="_blank" href="https://vtb.ru/">VTB bank</a>

![main page](pictures/main_page.png)

----

### Особенности проекта

* UI и API тесты
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Запуск автотестов в Selenoid

### Список проверок, реализованных в автотестах (web)

- [x] Проверить, что текст "Новости"- отображается в разделе "Акционерам"
- [x] Проверить, что текст "Признаны лучшими в разных сферах"- отображается в разделе "О банке"
- [x] Проверить, что текст "Тарифы для бизнеса"- отображается в разделе "Бизнесу"
- [x] Проверить, что текст "Услуги"- отображается в разделе "Кредитным организациям"
- [x] Проверить, что текст "Предложения банка:"- отображается в разделе "Частным лицам"
- [x] Проверить, что текст "Кому подойдет самозанятость"- отображается в разделе "Самозанятым"
----
### Список проверок, реализованных в автотестах (api)
- [x] Проверить, что рубли конвертируются в евро
- [x] Проверить, что рубли конвертируются в доллары
- [x] Проверить, что открывается страница курсов валют
- [x] Проверить, что открывается страница территориального расположения
- [x] Проверить, что открывается страница выдачи персонального кредита
### Используемый стэк

<img title="Python" src="pictures/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="pictures/icons/pytest-original.svg" height="40" width="40"/><img title="Allure Report" src="pictures/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="pictures/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="pictures/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" 
src="pictures/icons/selenoid.png" height="40" width="40"/> <img title="Selenium" src="pictures/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="pictures/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="pictures/icons/pycharm.png" height="40" width="40"/> <img title="Jenkins" src="pictures/icons/jenkins-original.svg" height="40" width="40"/>

----

### Локальный запуск автотестов

#### Выполнить в cli:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser-version=100
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/diploma_24//">Jenkins_build</a>

#### Параметры сборки

```python
BROWSER_VERSION = 100 # Версия браузера
ENVIRONMENT = ['PREPROD', 'PROD'] # Окружение
COMMENT = 'some comment' # Комментарий
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/diploma_24/">проект</a>

![jenkins project main page](pictures/jenkins_project_main_page.png)

2. Нажать "Build with Parameters"
3. В поле "BROWSER_VERSION" ввести: 100
4. Из списка "ENVIRONMENT" выбрать: PROD
5. Нажать "Build"

![jenkins_build](pictures/jenkins_build.png)

----

### Allure отчет
#### Общие результаты 
![allure_report_overview](pictures/allure_report_overview.png)

#### Результаты прохождения теста
![allure_reports_behaviors](pictures/allure_reports_behaviors.png)

#### Диаграммы

![allure_reports_graphs](pictures/alluere_reports_graphs_1.png)


----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/4117/dashboards">Ссылка на проект</a>

#### Общий Дашборд

![allure_test_ops_dashboards](pictures/allure_testops_launches.png)

#### История запуска тестов

![allure_testops_launches](pictures/allure_testops_dashboards.png)

#### Тест кейсы

![allure_testops_suites](pictures/allure_testops_suites.png)



----



### Видео прохождения одного из автотеста
![autotest_gif](pictures/autotest.gif)

----

