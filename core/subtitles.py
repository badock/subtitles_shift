import re
import tempora


POSSIBLE_DATE_FORMATS = [
    "\d+:\d+:\d+\.\d+",
    "\d+:\d+:\d+,\d+",
    "\d+:\d+:\d+(\s|$)",
]


def detect_time_format(line):
    formats = []
    for possible_format in POSSIBLE_DATE_FORMATS:
        result = re.search(possible_format, line)
        if result is not None:
            formats += [possible_format]
    return formats


def generate_time_formats(line):
    time_formats = detect_time_format(line)
    generated_time_formats = f"({'|'.join(time_formats)})"

    return generated_time_formats


def shift_subtitles_line(line_content, time_delay):
    time_formats = detect_time_format(line_content)

    generated_time_formats = f"({'|'.join(time_formats)})"

    regex_timestamps_pattern = f"({generated_time_formats} --> {generated_time_formats})"

    direction = "+"
    if time_delay < 0.0:
        direction = "-"

    cleaned_line = line_content.strip()

    search_result = re.search(regex_timestamps_pattern, cleaned_line)

    parsed_time_delay = tempora.parse_timedelta(f"{time_delay}")

    if search_result is None:
        result = f"{cleaned_line}"
    else:
        groups = search_result.groups()

        (t1, t2) = [t.strip() for t in groups[0].split("-->")]

        parsed_t1 = tempora.parse_timedelta(t1)
        parsed_t2 = tempora.parse_timedelta(t2)

        if direction == "+":
            new_t1 = parsed_t1 + parsed_time_delay
            new_t2 = parsed_t2 + parsed_time_delay
        else:
            new_t1 = parsed_t1 - parsed_time_delay
            new_t2 = parsed_t2 - parsed_time_delay

        new_t1_str = f"{new_t1}"
        new_t2_str = f"{new_t2}"

        new_cleaned_line = cleaned_line.replace(t1, new_t1_str).replace(t2, new_t2_str)

        result = f"{new_cleaned_line}"

    return result


def shift_subtitles_file(filename, time_delay):
    input_file = f"inputs/{filename}"
    output_file = f"outputs/{filename}"

    result = ""

    with open(input_file, "r") as fp:
        for line in fp.readlines():
            shifted_line = shift_subtitles_line(line, time_delay)
            result += f"{shifted_line}\n"

    with open(output_file, "w") as fp:
        fp.write(result)

    return True
