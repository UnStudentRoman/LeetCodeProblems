def carFleet(target: int, position, speed) -> int:
    pos_speed = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
    fleets_stack = []
    while pos_speed:
        if fleets_stack:

        else:
            fleets_stack.append(pos_speed.pop(0))

    return

if __name__ == '__main__':
    target = 13
    position = [10,2,5,7,4,6,11]
    speed = [7,5,10,5,9,4,1]
    print(carFleet(target,position,speed))