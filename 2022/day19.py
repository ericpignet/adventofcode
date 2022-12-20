import re
from dataclasses import dataclass


def parse_nums(line):
    num_re = r"-?\d+"
    return [int(n) for n in re.findall(num_re, line)]


def build(state, bp, instruction):
    # start robot construction
    if instruction == "ore":
        state["ore"] -= bp.ore_robot_required_ore
    elif instruction == "clay":
        state["ore"] -= bp.clay_robot_required_ore
    elif instruction == "obsidian":
        state["ore"] -= bp.obsidian_robot_required_ore
        state["clay"] -= bp.obsidian_robot_required_clay
    elif instruction == "geode":
        state["ore"] -= bp.geode_robot_required_ore
        state["obsidian"] -= bp.geode_robot_required_obsidian

    # collect resources
    state["ore"] += state["ore-robot"]
    state["clay"] += state["clay-robot"]
    state["obsidian"] += state["obsidian-robot"]
    state["geode"] += state["geode-robot"]

    # complete robot construction
    if instruction == "ore":
        state["ore-robot"] += 1
    elif instruction == "clay":
        state["clay-robot"] += 1
    elif instruction == "obsidian":
        state["obsidian-robot"] += 1
    elif instruction == "geode":
        state["geode-robot"] += 1


@dataclass
class Blueprint:
    nb: int
    ore_robot_required_ore: int
    clay_robot_required_ore: int
    obsidian_robot_required_ore: int
    obsidian_robot_required_clay: int
    geode_robot_required_ore: int
    geode_robot_required_obsidian: int


blueprints: list[Blueprint] = []
with open("2022/input_files/day19") as f:
    for data in f:
        nums = parse_nums(data.rstrip())
        blueprints.append(Blueprint(*nums))

part1_time = 24
part1_nb_blueprints = 30
part1_quality_with_mult = 0

part2_time = 32
part2_nb_blueprints = 3
part2_quality_product = 1

for bp in blueprints:
    state = {
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0,
        "ore-robot": 1,
        "clay-robot": 0,
        "obsidian-robot": 0,
        "geode-robot": 0,
    }
    part1_max_geode = 0
    part2_max_geode = 0
    queue = [(state, 1)]
    cur_time = 1

    while queue:
        if queue[0][1] > cur_time:
            print(f"New time: {queue[0][1]} {len(queue)=}")
            # all elements in queue should have the same time
            def score(state):
                return (
                    state["geode"] * 10000
                    + state["geode-robot"] * 1000
                    + state["obsidian-robot"] * 100
                    + state["clay-robot"] * 10
                    + state["obsidian"]
                    + state["clay"]
                )

            queue.sort(key=lambda x: score(x[0]), reverse=True)
            queue = queue[:100]
            cur_time = queue[0][1]

        state, time = queue.pop(0)

        # exit condition
        if time == part1_time:
            new_state = state.copy()
            build(new_state, bp, "")
            if new_state["geode"] > part1_max_geode:
                part1_max_geode = new_state["geode"]
                print(f"{new_state=}")
            if bp.nb > part2_nb_blueprints:
                continue
        elif time >= part2_time:
            build(state, bp, "")
            if state["geode"] > part2_max_geode:
                part2_max_geode = state["geode"]
                print(f"{state=}")
            continue

        # choose what to do next
        if (
            state["obsidian"] >= bp.geode_robot_required_obsidian
            and state["ore"] >= bp.geode_robot_required_ore
        ):
            new_state = state.copy()
            build(new_state, bp, "geode")
            queue.append((new_state, time + 1))
        else:
            nb_builds = 0
            if (
                state["clay"] >= bp.obsidian_robot_required_clay
                and state["ore"] >= bp.obsidian_robot_required_ore
                and state["obsidian-robot"] < bp.geode_robot_required_obsidian
                and state["obsidian"]
                < (part2_time - time) * bp.geode_robot_required_obsidian
            ):
                new_state = state.copy()
                build(new_state, bp, "obsidian")
                queue.append((new_state, time + 1))
                nb_builds += 1
            if (
                time < part2_time - 3
                and state["ore"] >= bp.clay_robot_required_ore
                and state["clay-robot"] < bp.obsidian_robot_required_clay
            ):
                new_state = state.copy()
                build(new_state, bp, "clay")
                queue.append((new_state, time + 1))
                nb_builds += 1
            if (
                nb_builds < 2
                and time < part2_time - 3
                and state["ore"] >= bp.ore_robot_required_ore
                and state["ore-robot"] < bp.clay_robot_required_ore
            ):
                new_state = state.copy()
                build(new_state, bp, "ore")
                queue.append((new_state, time + 1))
            new_state = state.copy()
            build(new_state, bp, "")
            queue.append((new_state, time + 1))
    part1_quality_with_mult += part1_max_geode * bp.nb
    if bp.nb <= part2_nb_blueprints:
        part2_quality_product *= part2_max_geode
    print(f"{bp.nb=} {part1_max_geode=} {part2_max_geode=}")

print(f"{part1_quality_with_mult=} {part2_quality_product=}")
