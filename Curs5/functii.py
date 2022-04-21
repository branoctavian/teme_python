def pitagora(c1, c2, ip):
    if ip**2 == c1**2 + c2**2:
        return True
    else:
        return False

def val_max(l):
        v_max = l[0]
        for i in range(len(l)):
            if l[i] > v_max:
                v_max = l[i]
        print(v_max)
        return v_max