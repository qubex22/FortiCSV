import csv
import sys

if len(sys.argv) < 2:
    print("Usage: python parser.py <log_file>")
    sys.exit(1)

log_file_name = sys.argv[1]

with open(log_file_name, 'r') as log_file, open('output.csv', 'w', newline='') as csv_file:
    fieldnames = ['date', 'time', 'eventtime', 'tz', 'logid', 'type', 'subtype', 'level', 'vd', 'srcip',
                  'srcname', 'srcport', 'srcintf', 'srcintfrole', 'dstip', 'dstport', 'dstintf', 'dstintfrole',
                  'srccountry', 'dstcountry', 'sessionid', 'proto', 'action', 'policyid', 'policytype', 'user',
                  'authserver', 'service', 'trandisp', 'transip', 'poluuid', 'sentdelta', 'rcvddelta', 'policyname', 
                  'sslaction', 'countssl', 'applist', 'apprisk', 'countapp', 'appid', 'utmref', 'app', 'utmaction', 
                  'transport', 'identifier', 'duration', 'sentbyte', 'rcvdbyte', 'sentpkt', 'rcvdpkt',
                  'appcat', 'crscore', 'craction', 'crlevel', 'srchwvendor', 'devtype', 'srcfamily', 'osname',
                  'srchwversion', 'srcswversion', 'mastersrcmac', 'srcmac', 'srcserver']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for line in log_file:
        log_dict = {}
        for item in line.strip().split(' '):
            try:
                key, value = item.split('=')
            except ValueError:
                continue
            log_dict[key] = value.strip('"')
        for field in fieldnames:
            if field not in log_dict:
                log_dict[field] = ""

        writer.writerow(log_dict)
