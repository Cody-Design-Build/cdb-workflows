import runpy
import unittest
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
blocks = runpy.run_path(str(ROOT / 'skills/jobtread-scheduling/scripts/week_blocks.py'))['blocks']


class SchedulingTests(unittest.TestCase):
    def test_monday_anchors_to_prior_sunday(self):
        rows = blocks(date(2030, 12, 2), 13)
        self.assertEqual(len(rows), 13)
        self.assertEqual(rows[0]['start'], '2030-12-01')
        for row in rows:
            start, end = (date.fromisoformat(row[k]) for k in ('start', 'end'))
            self.assertEqual((start.weekday(), end.weekday()), (6, 5))
            self.assertEqual(end - start, timedelta(days=6))
        for a, b in zip(rows, rows[1:]):
            self.assertEqual(date.fromisoformat(b['start']) - date.fromisoformat(a['end']), timedelta(days=1))

    def test_sunday_stays_sunday_and_invalid_count_is_rejected(self):
        sunday = date(2030, 12, 1)
        self.assertEqual(blocks(sunday, 1)[0]['start'], str(sunday))
        with self.assertRaises(ValueError):
            blocks(sunday, 0)
