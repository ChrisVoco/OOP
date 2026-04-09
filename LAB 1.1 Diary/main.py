from Diary import Diary
from DiaryPersistence import DiaryPersistence
from DiaryStatistics import DiaryStatistics


if __name__ == "__main__":

    diary = Diary()

    diary.add_entry("Täna oli ilus ilm.")
    diary.add_entry("Õppisin programmeerimist.")
    diary.add_entry("SRP on tegelikult väga loogiline.")

    print("---- DIARY SISU ----")
    print(diary)
    print()

    print("---- STATISTIKA ----")
    DiaryStatistics.print_statistics(diary)
    print()

    filename = "diary.txt"

    DiaryPersistence.save_to_file(diary, filename)

    print("Salvestatud faili:", filename)
    print()

    loaded_diary = DiaryPersistence.load_from_file(filename)

    print("---- FAILIST LAETUD ----")
    print(loaded_diary)
    print()

    loaded_diary.add_entry("See lisati pärast laadimist.")

    print("---- PÄRAST UUT LISAMIST ----")
    print(loaded_diary)
