from Diary import Diary


class DiaryPersistence:

    @staticmethod
    def save_to_file(diary, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for entry in diary.entries:
                file.write(entry + "\n")

    @staticmethod
    def load_from_file(filename):
        diary = Diary()

        with open(filename, "r", encoding="utf-8") as file:
            diary.entries = [line.strip() for line in file]

        diary.counter = len(diary.entries)

        return diary
