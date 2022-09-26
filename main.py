import pyautogui as pag
import webbrowser
import time


# 1-3 класса 11 кликов до скролла
# 9 класс и 11 класс 13 кликов до скролла
# 5-9 класса 12 кликов до скролла

xy = {661: 707, 693: 749, 671: 773, 691: 786, 707: 810}


def main(url, grade=int):
    for x, y in xy.items():
        webbrowser.open_new(url)
        pag.moveTo(577, 580, duration=1)
        pag.click()
        pag.moveTo(577, 608, duration=0.5)
        pag.click()
        pag.moveTo(577, 635, duration=0.5)
        pag.click()
        pag.moveTo(577, 662, duration=0.5)
        pag.click()
        pag.moveTo(577, 691, duration=0.5)
        pag.click()
        pag.moveTo(577, 719, duration=0.5)
        pag.click()
        pag.moveTo(577, 751, duration=0.5)
        pag.click()
        pag.moveTo(577, 779, duration=0.5)
        pag.click()
        pag.moveTo(577, 803, duration=0.5)
        pag.click()
        pag.moveTo(577, 831, duration=0.5)
        pag.click()
        pag.moveTo(577, 862, duration=0.5)
        pag.click()
        if grade == range(4, 9) or 10:
            pag.moveTo(607, 888)
            pag.click()
        if grade == 9 or 11:
            pag.moveTo(607, 888, duration=0.5)
            pag.click()
            pag.moveTo(608, 915, duration=0.5)
            pag.click()
        pag.scroll(-10000, y=1000)
        pag.moveTo(661, 707, duration=1)
        pag.click()
        pag.moveTo(x, y, duration=0.5)
        pag.click()
        pag.moveTo(490, 865, duration=0.5)
        pag.click()
        time.sleep(15)
        pag.moveTo(1805, 127, duration=0.5)
        pag.click()
        pag.moveTo(924, 705, duration=0.5)
        pag.click()


for i in range(1193, 1196):
    grade = int(input("Класс:"))
    url = f"https://school.bilimal.kz/gradebook/print?id={i}"
    main(url, grade)
