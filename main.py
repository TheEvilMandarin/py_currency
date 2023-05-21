import matplotlib.pyplot as plt
import numpy as np

import requests

from fetch_currency import fetch_currency

daily_json_url = "https://www.cbr-xml-daily.ru/daily_json.js"

labels = []
prev_vals = []
cur_vals = []


def append_currency(code, prev, current, name):
    labels.append(str(name) + ' (' + str(code) + ')')
    prev_vals.append(prev)
    cur_vals.append(current)


def currency_rates():
    resp = requests.get(url=daily_json_url)
    json_rates = resp.json()  # Check the JSON Response Content documentation below

    for i in ["USD", "EUR", "CNY"]:
        append_currency(i, *(fetch_currency(json_rates, i)))

    fig, ax = plt.subplots()

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    ax.bar(x - width / 2, prev_vals, width, label='Предыдущий')
    ax.bar(x + width / 2, cur_vals, width, label='Текущий')
    ax.set_xticks(x)  # values
    for i, v in enumerate(prev_vals):
        ax.text(i - width / 2, v + 0.1, str(v), ha='center', fontsize=9)
    for i, v in enumerate(cur_vals):
        ax.text(i + width / 2, v + 0.1, str(v), ha='center', fontsize=9)
    ax.set_xticklabels(labels)  # labels
    ax.legend()
    fig.suptitle('Курс валют ЦБ РФ', fontweight="bold")
    print(f"Plot currency rates for: {labels}")

    plt.show()


if __name__ == '__main__':
    currency_rates()
