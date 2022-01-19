import sys
from argparse import ArgumentParser
import csv

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input_csv', help='input csv file')
    parser.add_argument('output_csv', help='output csv file')
    parser.add_argument('--in-delimiter', dest='delimiter', help='input csv delimiter')
    parser.add_argument('--in-quote', dest='quote', help='input csv delimiter')

    args = parser.parse_args(sys.argv[1:])

    with open(args.input_csv, mode='r', newline='') as input_csv, open(args.output_csv, mode='w', newline='') as output_csv:
        arguments = {}
        if args.delimiter:
            arguments['delimiter'] = args.delimiter
        if args.quote:
            arguments['quotechar'] = args.quote

        if not args.delimiter and not args.quote:
            arguments['dialect'] = csv.Sniffer().sniff(input_csv.read(1024))
            input_csv.seek(0)

        csv_reader = csv.reader(input_csv, **arguments)
        csv_writer = csv.writer(output_csv)
        csv_writer.writerows(csv_reader)

# import sys
# from argparse import ArgumentParser
# import csv
#
# if __name__ == '__main__':
#     parser = ArgumentParser()
#     parser.add_argument('input_csv', help='input csv file')
#     parser.add_argument('output_csv', help='output csv file')
#     parser.add_argument('--in-delimiter', default="|", dest='delimiter', help='input csv delimiter')
#     parser.add_argument('--in-quote', default='"', dest='quote', help='input csv delimiter')
#
#     args = parser.parse_args(sys.argv[1:])
#
#     with open(args.input_csv, mode='r') as input_csv, open(args.output_csv, mode='w') as output_csv:
#         csv_reader = csv.reader(input_csv, delimiter=args.delimiter, quotechar=args.quote)
#         csv_writer = csv.writer(output_csv)
#         csv_writer.writerows(csv_reader)
