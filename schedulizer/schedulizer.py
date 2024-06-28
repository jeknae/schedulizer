from schedulizer.excell_scrapper.core.protocol import ExcellScrapper


class Schedulizer:
    """
        Return scrapped data in dictionary format
    """
    def __init__(self, scrapper: ExcellScrapper):
        self.scrapper = scrapper
    
    def get_day_schedule(self, week_day: str) -> dict:
        """Return one day schedule

        :return: dict"""
        lessons = self.scrapper.get_lessons(week_day)
        if len(lessons) > 0:
            times = self.scrapper.get_times(week_day)
            date = self.scrapper.get_date(week_day)

            data = []
            for time, lesson in zip(times, lessons):
                data.append({'time': time, 'lesson': lesson})

            return {'date': str(date), 'data': data}
        return {'date': None, 'data': None}

    def get_week_schedule(self) -> dict:
        """Return week schedule
        :return: dict
        """
        week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')
        schedule = {}
        for day in week:
            schedule[day] = self.get_day_schedule(day)
        return schedule
