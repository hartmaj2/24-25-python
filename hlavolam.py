OPERATIONS = {
    "x":(0,1),
    "y":(2,3),
    "z":(0,2),
    "w":(1,3)
}

OPERATIONS_SEQ = ["x","y","z","w"]

STARTING_CONF = ["A","B","B","C"]

def apply_operation(op_code,config):
    operation = OPERATIONS[op_code]
    new_config = config
    new_config[operation[0]],new_config[operation[1]] = config[operation[1]], config[operation[0]]
    return new_config

def st(config):
    return ''.join(config)

def all_configs():
    configs = []
    ALL_BS = ['B','B','B','B']
    for i in range(len(ALL_BS)):
        for j in range(len(ALL_BS)):
            if i != j:
                new_conf = ALL_BS.copy()
                new_conf[i] = "A"
                new_conf[j] = "C"
                configs.append(tuple(new_conf))
    return configs
                    

def get_config_dict():
    config_dict = {}
    for config in all_configs():
        config_dict[config] = -1
    return config_dict

config_hist = get_config_dict()
config = STARTING_CONF

for conf in all_configs():
    print(st(conf))

for i in range(0,12):
    print(st(config))
    config_hist[tuple(config)] = i
    op_code = OPERATIONS_SEQ[i%len(OPERATIONS_SEQ)]
    config = apply_operation(op_code,config)

for i in range(13,17):
    print(st(config))
    config_hist[tuple(config)] = i
    op_code = OPERATIONS_SEQ[i%len(OPERATIONS_SEQ)]
    config = apply_operation(op_code,config)

for i in range(19,21):
    print(st(config))
    config_hist[tuple(config)] = i
    op_code = OPERATIONS_SEQ[i%len(OPERATIONS_SEQ)]
    config = apply_operation(op_code,config)

for config in config_hist.keys():
    print(f"{config} -> {config_hist[config]}")
