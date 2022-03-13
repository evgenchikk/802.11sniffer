report = None
line_n = 1
def write_to_report(line):
    global line_n
    report.write(f'{line_n};{line}')
    line_n += 1
