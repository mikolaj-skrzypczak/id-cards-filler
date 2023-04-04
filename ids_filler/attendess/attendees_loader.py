import csv
import os


class AttendeesLoader:
    attendees_dir = f"{os.path.dirname(__file__)}/../resources/attendees"

    @classmethod
    def get_attendees_and_affiliations(cls, type_: str) -> list[dict]:
        filepath = f"{cls.attendees_dir}/{type_}.csv"
        return cls._load_attendees(filepath) if os.path.exists(filepath) else []

    @classmethod
    def _load_attendees(cls, filepath: str) -> list[dict]:
        with open(filepath, 'r') as fp:
            return [{"name": row[0], "affiliation": ",".join(row[1:])} for row in csv.reader(fp)]
