def brut_force(stocks, budget, portfolio=[]):
    if stocks:
        best_value1, best_portfolio1 = brut_force(stocks[1:], budget, portfolio)
        stock = stocks[0]
        if stock[1] <= budget:
            best_value2, best_portfolio2 = brut_force(stocks[1:], budget - stock[1], portfolio + [stock])
            if best_value1 < best_value2:
                return best_value2, best_portfolio2

        return best_value1, best_portfolio1
    else:
        return sum([i[2] for i in portfolio]), portfolio
    
# Fonction brut_force(stocks, budget, portfolio=[]):
#     Si stocks est non vide :
#         best_value1, best_portfolio1 = Appeler récursivement brut_force(stocks[1:], budget, portfolio)
#         stock = stocks[0]
#         Si stock[1] <= budget :
#             best_value2, best_portfolio2 = Appeler récursivement brut_force(stocks[1:], budget - stock[1], portfolio + [stock])
#             Si best_value1 < best_value2 :
#                 Retourner best_value2, best_portfolio2
        
#         Retourner best_value1, best_portfolio1
#     Sinon :
#         Retourner la somme des valeurs [i[2] pour i dans portfolio] et portfolio

