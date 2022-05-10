import datetime

ONE_DAY = datetime.timedelta(days=1)
rate_values = {
    'h': 'HIGH COST',
    'l': 'LOW COST'
}

def validate_date(date_str):
    converted_date = None
    try:
        converted_date = datetime.datetime.strptime(date_str, '%m/%d/%y').date()
    except:
        try:
            converted_date = datetime.datetime.strptime(date_str, '%m/%d/%Y').date()
        except:
            print('Oops!  Please enter dates in the format mm/dd/yy or mm/dd/yyyy.')
            print('')
    return converted_date


def validate_rate(rate_str):
    rate_value = None
    if rate_str.lower() in ('h', 'l'):
        rate_value = rate_values[rate_str.lower()]
    else:
        print('Oops!  Please enter project rates in the format "H", "h", "L", or "l".')
        print('')
    return rate_value


input_done = False
high_cost_dates = []
low_cost_dates = []
print('')
print('Welcome to the project reimbursement calculator.')
print('Please enter all of the required information for at least one project.')
print('')

while not input_done:
    start_date_valid = False
    while not start_date_valid:
        start_date_input = input("Enter the project start date. (Format: mm/dd/yyyy or mm/dd/yy): ")
        start_date = validate_date(start_date_input)
        if start_date is not None:
            start_date_valid = True

    end_date_valid = False
    while not end_date_valid:
        end_date_input = input("Enter the project end date. (Format: mm/dd/yyyy or mm/dd/yy): ")
        end_date = validate_date(end_date_input)
        if end_date is not None:
            end_date_valid = True

    rate_valid = False
    while not rate_valid:
        rate_input = input("Enter the project rate. (H/h for High Cost or L/l for Low Cost): ")
        rate = validate_rate(rate_input)
        if rate is not None:
            rate_valid = True

    print('')
    print('Project record entered -> (Start: ' + start_date.strftime('%m/%d/%Y') + ' End: ' + end_date.strftime('%m/%d/%Y') + ' Rate: ' + rate + ')')
    print('')

    # project_records.append((start_date, end_date, rate))

    work_date = start_date
    while work_date <= end_date:
        if rate == rate_values['h']:
            high_cost_dates.append(work_date)
        else:
            low_cost_dates.append(work_date)
        work_date = work_date + ONE_DAY

    input_done_valid = False
    while not input_done_valid:
        user_done_input = input("Would you like to enter another project record? (Y/y for Yes or N/n for No): ")
        if user_done_input.lower() == 'y':
            input_done_valid = True
            input_done = False
            print('')
        elif user_done_input.lower() == 'n':
            input_done_valid = True
            input_done = True
        else:
            print('Oops!  Please enter your response in the format "Y", "y", "N", or "n".')
            print('')

print(low_cost_dates)
print(high_cost_dates)

all_dates_and_rates = []
for date in high_cost_dates:
    record = (date, rate_values['h'])
    if record not in all_dates_and_rates:
        all_dates_and_rates.append(record)
for date in low_cost_dates:
    record = (date, rate_values['l'])
    if date not in high_cost_dates and record not in all_dates_and_rates:
        all_dates_and_rates.append(record)

sorted_dates = sorted(all_dates_and_rates, key=lambda x: x[0])
print(sorted_dates)

