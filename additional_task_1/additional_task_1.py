def duplicate_deletion(tickets):
    add_dictionary = dict()
    seen = set()
    for key, values in tickets.items():
        add_dictionary[key] = []
        for value in values:
            if value not in seen:
                seen.add(value)
                add_dictionary[key].append(value)
    return add_dictionary


def linking_function(types, tickets):
    output = dict()
    for key, value in types.items():
        output[value] = tickets[key]
    return output


types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = linking_function(types=types, tickets=duplicate_deletion(tickets))

print(tickets_by_type)
