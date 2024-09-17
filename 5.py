from dataclasses import dataclass, field


@dataclass
class Team:

    penalty: int = 0
    """in minuets"""

    servers: int = 0
    tries: dict[str, int] = field(default_factory=dict)


def time_to_int(time: str):
    h, m, s = map(int, time.split(":"))

    return h * 60 * 60 + m * 60 + s


results: dict[str, Team] = {}


begin = time_to_int(input())
n = int(input())
next_day = False

previous_time = -1
for i in range(n):
    name, time_stamp, server, status = input().split()

    time = time_to_int(time_stamp)
    if time < begin:
        next_day = True

    previous_time = time

    if next_day and time >= begin:
        continue  # should be same as break, time is up!

    if next_day:
        time += 24 * 60 * 60

    if name not in results:
        results[name] = Team()
    team = results[name]

    if status == "ACCESSED":
        team.servers += 1
        team.penalty += team.tries.get(server, 0) * 20
        team.penalty += (time - begin) // 60

    if status == "DENIED" or status == "FORBIDEN":
        team.tries[server] = team.tries.get(server, 0) + 1


result = [(name, team.servers, team.penalty) for name, team in results.items()]
result.sort(key=lambda x: x[0])
result.sort(key=lambda x: x[2])
result.sort(key=lambda x: x[1])
previous = None
for i, line in enumerate(result):
    if previous is not None and previous[1][1:] == line[1:]:
        i = previous[0]
    print(i+1, *line)

    previous = (i, line)