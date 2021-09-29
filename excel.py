import pandas as pd


def get_excel_records():
    excel_file = pd.read_excel("clientes.xlsx")

    records = excel_file.to_records(index=False)

    return records
