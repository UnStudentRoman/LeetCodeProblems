import pandas as pd


def nth_highest_salary(employee, N) -> pd.DataFrame:
    pass


if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id': 'Int64', 'Salary': 'Int64'})
    n = 5

    print(nth_highest_salary(employee, n))