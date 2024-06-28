from typing import Protocol


class ExcellScrapper(Protocol):
    """Protocol for Excel Scrapper

    Each institute scrapper should contain this methods
    """
    def get_times(self, week_day: str) -> list[str]:
        """
        Return times of the day schedule
        :param week_day: 'Monday', ...
        :return: list[str]
        """
        pass

    def get_lessons(self, week_day: str) -> list[str]:
        """
        Return lessons od the day schedule
        :param week_day:  'Monday', ...
        :return: list[str]
        """
        pass

    def get_date(self, week_day: str) -> str:
        """
        Return date of the day schedule
        :param week_day: 'Monday', ...
        :return: str
        """
        pass

