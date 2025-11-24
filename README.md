# How it works?

## Run the file `main.py`

You input a directory, for example `D:/test`<br>
<img width=50% height=50% alt="image" src="https://github.com/user-attachments/assets/b79533d4-9d58-4109-abbf-2b19cbbb5e27" />

And the program will output this:<br>
<img width=50% height=50% alt="image" src="https://github.com/user-attachments/assets/f391ef3e-e00f-4b8e-b372-cb7ee023e7d6" />

By default, the program won't show you files, whose size is less then 3% of total size<br>
But you can...

## Configure the program

The config is located in `folder_analyzer/config.json`<br>
Open it and it will look smth like this:<br>
<img width=50% height=50% alt="image" src="https://github.com/user-attachments/assets/09723624-50c5-4e1b-a1a5-5b8f3ff9ff43" />

- do_small_files (`true`/`false`) - will enable/disable showing small files (that are less then `min_` of total size)
- min_ (`0.0`-`1.0`) - defines what minimum procent of total size will program show
- alw_in_bytes (`true`/`false`) - will/won't show total size in bytes
