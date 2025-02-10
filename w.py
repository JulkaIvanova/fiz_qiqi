import datetime
import schedule

output_message = "Ку"
flag_diaposon = False
message = input("Введите сообщение, которое будет выводиться в консоль (для использования значения по умолчанию нажмите клавишу 'ввод')")
diaposon = input("Введите диапозон, в который кукшка будет молчать (для использования значения по умолчанию нажмите клавишу 'ввод')")
print(message)
if message != "":
    output_message = message
if flag_diaposon != '':
    flag_diaposon = True
    diaposon_list = []
    for i in range(int(diaposon.split('-')[0]), int(diaposon.split('-')[1])):
        diaposon_list.append(i)
def job():
    w = datetime.datetime.now().hour
    if w == 0:
        w = 12
    elif w > 12:
        w -= 12
    if flag_diaposon:
        if datetime.datetime.now().hour in diaposon_list:
            return
    for i in range(w):
        print(output_message)


schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
