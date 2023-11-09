import numpy as np

def task() -> list:
    sums, products = set(), set()
    for i in range(1, 7):
        for j in range(1, 7):
            sums.add(i + j)
            products.add(i * j)
    
    sums, products = sorted(sums), sorted(products)
    sum_lookup = {s: sums.index(s) for s in sums}
    product_lookup = {p: products.index(p) for p in products}
    counts = np.zeros((len(sums), len(products)))
    for i in range(1, 7):
        for j in range(1, 7):
            counts[sum_lookup[i + j], product_lookup[i * j]] += 1
    
    probabilities = counts / 36
    
    #H(AB)
    entropy_AB = -np.sum(probabilities * np.log2(probabilities, where=np.abs(probabilities) > 0.0001))
    
    #H(A)
    probabilities_A = np.sum(probabilities, axis=1)
    entropy_A = -np.sum(probabilities_A * np.log2(probabilities_A, where=np.abs(probabilities_A) > 0.0001))
    
    #H(B)
    probabilities_B = np.sum(probabilities, axis=0)
    entropy_B = -np.sum(probabilities_B * np.log2(probabilities_B, where=np.abs(probabilities_B) > 0.0001))
    
    #Ha(B)
    entropy_A_B = entropy_AB - entropy_A
    
    #Ia,b
    information_AB = entropy_B - entropy_A_B
    
    return [round(i, 2) for i in [entropy_AB, entropy_A, entropy_B, entropy_A_B, information_AB]]

#print("H(AB), H(A), H(B), Ha(B), Ia,b:",task())
    
    

    
    