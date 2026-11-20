"""Generate inclusive Sunday–Saturday planning blocks, with no API writes."""
import argparse
import json
from datetime import date, timedelta


def blocks(field_start, count):
    if count < 1:
        raise ValueError('week count must be positive')
    sunday = field_start - timedelta(days=(field_start.weekday() + 1) % 7)
    return [dict(week=i + 1, start=(sunday + timedelta(weeks=i)).isoformat(),
                 end=(sunday + timedelta(weeks=i, days=6)).isoformat())
            for i in range(count)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('field_start', type=date.fromisoformat)
    parser.add_argument('weeks', type=int)
    args = parser.parse_args()
    if args.weeks < 1:
        parser.error('week count must be positive')
    print(json.dumps(blocks(args.field_start, args.weeks), indent=2))


if __name__ == '__main__':
    main()
