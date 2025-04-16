import os


def parse_time(time_str):
    """Convert a time string into minutes from midnight."""
    if ":" in time_str:
        hours, minutes = map(int, time_str.split(":"))
    else:
        hours = int(time_str)
        minutes = 0

    if hours >= 24:
        raise ValueError("Invalid hour: hours should be less than 24.")

    return hours * 60 + minutes


def convert_to_24hr(time_str, previous_time):
    """Convert a time string to a 24-hour format in minutes from midnight."""
    time_in_minutes = parse_time(time_str)
    if time_in_minutes < previous_time:
        time_in_minutes += 12 * 60
        if time_in_minutes >= 24 * 60:
            time_in_minutes -= 12 * 60
    return time_in_minutes


def sum_timesheet(path):
    absolute_path = os.path.abspath(path)
    print(f"Lendo arquivo: {absolute_path}")

    if not os.path.exists(absolute_path):
        print(f"Erro: Arquivo não encontrado - {absolute_path}")
        return

    with open(absolute_path, "r") as file:
        content = file.read()

    total_minutes = 0

    for line in content.splitlines():
        intervals = line.split(",")
        previous_end = 0

        for interval in intervals:
            interval = interval.strip().replace(" ", "")
            parts = interval.split("-")

            if len(parts) != 2:
                print(f"Erro: Intervalo mal formatado - {interval}")
                continue

            start_str, end_str = parts
            start_minutes = convert_to_24hr(start_str, previous_end)
            end_minutes = convert_to_24hr(end_str, start_minutes)

            if end_minutes < start_minutes:
                end_minutes += 12 * 60

            total_minutes += end_minutes - start_minutes
            previous_end = end_minutes

    total_hours = total_minutes / 60.0
    return round(total_hours, 2)


# Exemplo de uso
result_12 = sum_timesheet("12.txt")
print(f"Total de horas no arquivo 12.txt: {result_12}")

result_04 = sum_timesheet("timesheets/04.txt")
print(f"Total de horas no arquivo timesheets/04.txt: {result_04}")
