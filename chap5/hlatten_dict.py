def flatten_dict(d, result={}, prv_keys=[]):

    for k, v in d.iteritems():
        if isinstance(v, dict):
            flatten_dict(v, result, prv_keys + [k])
        else:
            result['.'.join(prv_keys + [k])] = v

    return result
s={'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
result={}
prv_keys=[]
print flatten_dict(s,result,prv_keys)           
