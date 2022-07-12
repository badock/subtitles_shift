import unittest
import tempora
from core.subtitles import detect_time_format, generate_time_formats, parse_time_delta


class TestUtils(unittest.TestCase):
    def test_date_format_detection(self):
        line1 = "00:05:00,400 --> 00:05:15,300"
        format1 = detect_time_format(line1)

        self.assertEqual(format1, ["\d+:\d+:\d+,\d+"])

        line2 = "00:05:00.400 --> 00:05:15.300"
        format2 = detect_time_format(line2)

        self.assertEqual(format2, ["\d+:\d+:\d+\.\d+"])

        line3 = "00:05:00 --> 00:05:15"
        format3 = detect_time_format(line3)

        self.assertEqual(format3, ["\d+:\d+:\d+(\s|$)"])

        line4 = "00:05:00 --> 00:05:15.300"
        format4 = detect_time_format(line4)

        self.assertEqual(format4, ["\d+:\d+:\d+\.\d+", "\d+:\d+:\d+(\s|$)"])

        line5 = "00:05:00,400 --> 00:05:15,300"
        format5 = detect_time_format(line5)

        self.assertEqual(format5, ["\d+:\d+:\d+\.\d+", "\d+:\d+:\d+(\s|$)"])

    def test_date_format_generation(self):
        line1 = "00:05:00,400 --> 00:05:15,300"
        format1 = generate_time_formats(line1)

        self.assertEqual(format1, "(\d+:\d+:\d+,\d+)")

        line2 = "00:05:00.400 --> 00:05:15.300"
        format2 = generate_time_formats(line2)

        self.assertEqual(format2, "(\d+:\d+:\d+\.\d+)")

        line3 = "00:05:00 --> 00:05:15"
        format3 = generate_time_formats(line3)

        self.assertEqual(format3, "(\d+:\d+:\d+(\s|$))")

        line4 = "00:05:00 --> 00:05:15.300"
        format4 = generate_time_formats(line4)

        self.assertEqual(format4, "(\d+:\d+:\d+\.\d+|\d+:\d+:\d+(\s|$))")

    def test_timedelta(self):
        time1 = "0:05:00,400"
        timedelta1 = parse_time_delta(time1)

        self.assertEqual(timedelta1.seconds, 300)
        self.assertEqual(timedelta1.microseconds, 400000)

        time2 = "0:05:00.400"
        timedelta2 = parse_time_delta(time2)

        self.assertEqual(timedelta2.seconds, 300)
        self.assertEqual(timedelta2.microseconds, 400000)
