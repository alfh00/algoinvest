def brut_force(elements, capacite, elements_selection = []):
    if elements:
        val1, lstVal1 = brut_force(elements[1:], capacite, elements_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lstVal2 = brut_force(elements[1:], capacite - val[1], elements_selection + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection
        # return sum([i[2] for i in elements_selection]), elements_selection