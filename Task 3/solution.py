import sys
import json

def fill_values(tests_list, values_map):
    for test in tests_list:
        if 'id' in test and test['id'] in values_map:
            test['value'] = values_map[test['id']]
        if 'values' in test:
            fill_values(test['values'], values_map)
    return tests_list

if __name__ == "__main__":
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    with open(values_file, 'r') as f:
        values_data = json.load(f)

    values_map = {}
    for v in values_data['values']:
        values_map[v['id']] = v['value']

    with open(tests_file, 'r') as f:
        tests_data = json.load(f)

    report = {'tests': fill_values(tests_data['tests'], values_map)}

    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
