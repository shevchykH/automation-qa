# Solution N1
def is_merge(s, part1, part2):
    queue = [(s,part1,part2)]
    while queue:
        str, p1, p2 = queue.pop()
        if str:
            if p1 and str[0] == p1[0]:
                queue.append((str[1:], p1[1:], p2))
            if p2 and str[0] == p2[0]:
                queue.append((str[1:], p1, p2[1:]))
        else:
            if not p1 and not p2:
                return True
    return False

# Solution N2
def is_merge1(s, part1, part2):
    temp_list = []
    flag = False
    s_list = list(s)
    part1_list = list(part1[:])
    part2_list = list(part2[:])
    for index, char in enumerate(s_list):
        if part1_list.count(char) and part1_list.index(char) == 0 \
                and part2_list.count(char) and part2_list.index(char) == 0:
            temp = part1_list.pop(0)
            part2_list.pop(0)
            flag = True
            temp_list.append(temp)
            continue
        elif flag:
            flag = False
            if part1_list.count(char) and part1_list.index(char) == 0:
                temp_list.extend(part2_list)
                part2_list = temp_list
            else:
                temp_list.extend(part1_list)
                part1_list = temp_list
            temp_list = []
        if char in part1_list and char ==  part1_list[0]:
            part1_list.pop(0)
        elif char in part2_list and char ==  part2_list[0]:
            part2_list.pop(0)
        else:
            return False
    if len(part1) + len(part2) == len(s):
        return True
    else:
        return False


# Solution N3
def is_merge3(s, part1, part2):
    if not part1:
      return s == part2
    if not part2:
      return s == part1
    if not s:
      return part1 + part2 == ''
    if s[0] == part1[0] and is_merge3(s[1:], part1[1:], part2):
      return True
    if s[0] == part2[0] and is_merge3(s[1:], part1, part2[1:]):
      return True
    return False