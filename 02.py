# A PART
with open("02.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [[int(a) for a in command.split()] for command in commands]
good_reports = [[command[i] - command[i+1] for i in range(len(command)-1)] for command in commands]
for report, command in zip(good_reports,commands):
    if set(report).issubset({1,2,3}) or set(report).issubset({-1,-2,-3}):
        counter += 1
    else:
        for j in range(len(command)):
            command1 = command[:j] + command[j+1:]
            new_report = [command1[i] - command1[i+1] for i in range(len(command1)-1)]
            #print(new_report)
            if set(new_report).issubset({1,2,3}) or set(new_report).issubset({-1,-2,-3}):
                counter += 1
                break

print(counter)