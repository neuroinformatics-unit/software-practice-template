import datetime

# ===============================================================
# Instructions
# Change this variable to "pro" if you want to try the pro level.
# ===============================================================
my_level = "beginner"  # beginner or pro


# ===============================================================
# Beginner level
# All students should try first to solve the problem at this level.
# ===============================================================
def calculate_fastest_time(time_list):
    fastest_time = time_list[0]
    for time in time_list:
        if time > fastest_time:
            fastest_time = time
    return fastest_time


def print_fastest_time(time_list):
    fastest_time = time_list[0]
    for time in time_list:
        if time > fastest_time:
            fastest_time = time

    print(f"This is the fastest time: {fastest_time} 🚀")


# ===============================================================
# Pro level
# Only for students who have solved the problem at the beginner level
# ===============================================================
def time_range(
    start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0
):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (
        end_time_s - start_time_s
    ).total_seconds() / number_of_intervals + gap_between_intervals_s * (
        1 / number_of_intervals - 1
    )
    sec_range = [
        (
            start_time_s
            + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
            start_time_s
            + datetime.timedelta(
                seconds=(i + 1) * d + i * gap_between_intervals_s
            ),
        )
        for i in range(number_of_intervals)
    ]
    return [
        (ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S"))
        for ta, tb in sec_range
    ]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    return overlap_time


def time_range_less_precise(
    start_time, end_time, number_of_intervals=10, gap_between_intervals_s=5
):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (
        end_time_s - start_time_s
    ).total_seconds() / number_of_intervals + gap_between_intervals_s * (
        1 / number_of_intervals - 1
    )
    sec_range = [
        (
            start_time_s
            + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
            start_time_s
            + datetime.timedelta(
                seconds=(i + 1) * d + i * gap_between_intervals_s
            ),
        )
        for i in range(number_of_intervals)
    ]
    return [
        (ta.strftime("%Y-%m"), tb.strftime("%Y-%m")) for ta, tb in sec_range
    ]


# ===============================================================
# End of pro level
# ===============================================================


# The code below will only be executed if the file is run directly,
# not if it is imported from another file.
# __name__ is a special variable that gets a different value depending
# on how the file is run.
# If the file is run directly, __name__ is set to "__main__".
if __name__ == "__main__":
    if my_level == "beginner":
        time_list = [1, 2, 3, 4]
        print(calculate_fastest_time(time_list))
    elif my_level == "pro":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        print(compute_overlap_time(large, short))
