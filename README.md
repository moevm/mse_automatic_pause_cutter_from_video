
# mse_automatic_pause_cutter_from_video

### Инструкция по установке
1.  Установить необходимые глобальные зависимости
    ```bash
    sudo apt-get install ffmpeg vlc
    ```
2. Создать виртульное пространство (virtualenv)
    ```bash
    python3 -m virtualenv env --system-site-packages
    ```
3. Перейти в созданное виртуальное пространство (virtualenv)
    ```bash
   source ./env/bin/activate
    ```
4. Установить необходимые зависимости
    ```bash
    pip3 install -r requirments.txt
    ```
5. Запустить прогрумму
    1. Для запуска в режиме GUI
    ```bash
    python3 main.py --gui
    ```     
    2. Для запуска в режиме CLI
        ```bash
        python3 main.py [PARAMS]
        ``` 
	    1. Обязательные параметры
        ```bash
        -i FILE, --input FILE - путь к исходному файлу
        ```    
		2. Необязательные параметры
        ```bash
        -o FILE, --output FILE - путь для сохранения результата
        ```  
        ```bash
        -m MIN, --min MIN - минимальная длина пауза для вырезки
        ```  
        ```bash
        -t THRESH, --thresh THRESH - максимальный порог "тишины". Все сегменты, где звук громчке этого параметра будут сохранены, остальные - вырезаны
        ``` 
        
### Презентации
[Первая итерация](https://github.com/moevm/mse_automatic_pause_cutter_from_video/blob/master/docs/step_1.pptx)
[Вторая итерация](https://github.com/moevm/mse_automatic_pause_cutter_from_video/blob/master/docs/step_2.pptx)