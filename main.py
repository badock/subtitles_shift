from core.subtitles import shift_subtitles_file

CONFIG = {
    "2021-11-25_07_00_00_mentendstu_0021.vtt": -3.2,
    "2021-11-25_07_00_00_mentendstu_0022.vtt": -1.8,
    "2021-11-25_07_00_00_mentendstu_0023.vtt": -0.9,
    "2021-11-25_07_00_00_mentendstu_0024.vtt": -0.9,
    "2021-11-25_07_00_00_mentendstu_0025.vtt": 0.0,
    "2021-11-25_07_00_00_mentendstu_0026.vtt": -0.9,
    "2021-11-25_07_00_00_mentendstu_0027.vtt": -0.9,
    "2021-11-25_07_00_00_mentendstu_0028.vtt": 7.2,
    "2021-11-25_07_00_00_mentendstu_0029.vtt": -0.9,
    "2021-11-25_07_00_00_mentendstu_0030.vtt": -0.5,
}


def _main():
    for (filename, time_delay) in CONFIG.items():
        shift_subtitles_file(filename, time_delay)


if __name__ == '__main__':
    _main()
