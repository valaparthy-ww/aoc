def read_input():
    device_map = {}
    with open("input.txt", 'r') as file:
        for line in file.readlines():
            temp_input_device = line.split(":")[0]
            device_map[temp_input_device] = {x: None for x in line.split(":")[1].strip().split(" ")}
        return device_map


def find_device_path(device_map, devices):
    total_path_count = 0
    if len(devices) == 1:
        device = devices[0]
        if device == "out":
            return 1
        elif device in device_map:
            return find_device_path(device_map, list(device_map[device].keys()))
    else:
        for device in devices:
            paths_count = find_device_path(device_map, [device])
            total_path_count += paths_count
    return total_path_count

def main():
    device_map  = read_input()
    paths = find_device_path(device_map, ["you"])
    return paths, 0


if __name__ == "__main__":
    res_part1, res_part2 = main()
    print(f"part1: {res_part1}")
    print(f"part2: {res_part2}")