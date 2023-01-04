import pandas as pd
import matplotlib.pyplot as plt

prices = [
    (1, 2.12),
    (2, 2.56),
    (3, 3.10),
    (4, 3.16),
    (5, 3.58),
    (6, 5.12),
    (7, 5.16),
    (8, 5.20),
    (9, 4.12),
    (10, 4.10),
    (11, 3.65),
    (12, 4.25),
]
df = pd.DataFrame(prices,columns=['month','price_usd'])
df = df.set_index('month')
df.describe()

price_pln = df['price_usd'].apply(lambda  prices: prices * 4)
df = pd.DataFrame(price_pln,columns=['month', 'price_pln'])
df = df.set_index('month')
df['prices'] = price_pln
plt.grid(which='major', alpha=1)
plt.title('Prices of goods (PLN)')
plt.plot(price_pln, color='red', linestyle='--')
plt.show()