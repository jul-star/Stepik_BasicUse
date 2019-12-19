import csv
from datetime import datetime
from os import path


class Crimes:
    """
    input csv:
     fieldname: ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,
     Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code
     search: year = 2015 and field = 'Primary Type'
    """

    @staticmethod
    def getCsv(file_name: str, _field_names: list) -> csv.DictReader:
        _full_path = '../data/{0}'.format(file_name)
        if path.isfile(_full_path):
            with open(_full_path, newline='') as _csv_file:
                yield from csv.DictReader(_csv_file, fieldnames=_field_names)
        else:
            print('No such file: {0}'.format(_full_path))
        return None

    @staticmethod
    def search(dct: csv.DictReader, date_field_name: str, year: int, field_to_search: str) -> str:
        """
        10/30/2013
        :param dct:
        :param date_field_name:
        :param year:
        :param field_to_search:
        :return:
        """
        _stat = Crimes.build_statistics(date_field_name, dct, field_to_search, year)
        if not _stat:
            print("Statistic is empty")
            return str(None)

        max_stat_key = Crimes.get_max_value_key(_stat)
        return max_stat_key

    @staticmethod
    def get_max_value_key(stat: dict) -> str:
        if not stat:
            return str(None)

        max_stat_key: str = next(iter(stat))
        for keys in stat.keys():
            if stat[keys] > stat[max_stat_key]:
                max_stat_key = keys
        return max_stat_key

    @staticmethod
    def build_statistics(date_field_name: str, dct: csv.DictReader, field_to_search: str, year: int) -> dict:
        stat: dict = {}
        if not dct:
            print('DicReader is empty')
            return {}

        for row in dct:
            _year = Crimes.get_year(row[date_field_name])
            if _year == year:
                if row[field_to_search] in stat.keys():
                    stat[row[field_to_search]] += 1
                else:
                    stat[row[field_to_search]] = 1
        return stat

    @staticmethod
    def get_year(_date: str) -> int:
        _year: int = -1
        if _date:
            try:
                dt = datetime.strptime(_date, '%m/%d/%Y %H:%M:%S %p')
                _year = dt.year
            except ValueError:
                print(ValueError.args, " : ", _date)
        else:
            print('Date is None? : ', _date)
        return _year

    @staticmethod
    def run(csv_file_name):
        _field_names = ['ID', 'Case Number', 'Date', 'Block', 'IUCR', 'Primary Type', 'Description',
                        'Location Description', 'Arrest', 'Domestic', 'Beat', 'District', 'Ward', 'Community Area',
                        'FBI Code']
        _dict = Crimes.getCsv(csv_file_name, _field_names)
        _result = Crimes.search(_dict, 'Date', 2015, 'Primary Type')
        return _result


if __name__ == "__main__":
    csv_file = 'Crimes.csv' # Crimes_small
    print(Crimes.run(csv_file))
