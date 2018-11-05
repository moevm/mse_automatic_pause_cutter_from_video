# mse_automatic_pause_cutter_from_video

### Инструкция по установке
1. Создать виртульное пространство (virtualenv)
    ```bash
    python3 -m virtualenv env
    ```
2. Перейти в созданное виртуальное пространство (virtualenv)
    ```bash
   source ./env/bin/activate
    ```
3. Установить необходимые зависимости
    ```bash
    pip3 install -r requirments.txt
    ```
4. Запустить прогрумму
    ```bash
    python3 main.py
    ```
    Параметры запуска:
    1. Обязательные:
    ```bash
        -i FILE, --input FILE - путь к исходному файлу
    ```    
    2. Необязательные:
    ```bash
        -m MIN, --min MIN - минимальная длина пауза для вырезки
    ```  
    ```bash
        -t THRESH, --thresh THRESH - максимальный порог "тишины". Все сегменты, где звук громчке этого параметра будут сохранены, остальные - вырезаны
    ``` 
        
### Презентации
[Первая итерация](https://github.com/moevm/mse_automatic_pause_cutter_from_video/blob/master/cutter.pptx)
