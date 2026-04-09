class DiaryStatistics:

    @staticmethod
    def print_statistics(diary):

        count = len(diary.entries)

        if count == 0:
            avg = 0
        else:
            total_chars = sum(len(entry) for entry in diary.entries)
            avg = total_chars / count

        print("Sissekannete arv:", count)
        print("Keskmine tähemärkide arv:", avg)
