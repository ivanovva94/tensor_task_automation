# Тензор тестовое задание
Задание выполнено с помощью chromedriver, функционал создания отчетов реализован с помощью Allure.

ВАЖНО: для корректного получения отчета Allure должен быть установлен на ОС.

**Установка Allure на Windows 10 с помощью оболочки PowerShell:**
  1) Устанавливаем Scoop командой: `irm get.scoop.sh | iex`
  2) Устанавливаем Allure командой: `scoop install allure`
  3) Устанавливаем Java -> [Install Java](https://www.java.com/ru/download/)
  4) Добовляем переменную `JAVA_HOME` в переменные среды Windows с указанием дериктории где находится Java
  
  
### Запуск теста: 
`pytest test_yandex.py -v --alluredir report`

В корневой папке проекта после выполнения теста появится папка "report", где будут храниться файлы отчета.

### Получить отчет Allure: 
`allure serve report`
