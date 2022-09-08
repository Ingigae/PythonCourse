all_list = [7, 18.9, True, "string", (125,7,9, "lol"), ['hmmm', 4.5, 7], {42:'wut', 17: 'notwut'}, None]
for n, v in enumerate(all_list):
    print(f"{n}: {v} - {type(v)}")