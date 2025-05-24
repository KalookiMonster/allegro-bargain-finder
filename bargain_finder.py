class BargainFinder:
    def __init__(self, apis):
        self.apis = apis

    def find_bargains(self, query, threshold_ratio=0.7):
        all_prices = []
        all_items = []

        for api in self.apis:
            items = api.search_items(query)
            prices = [item['price'] for item in items]
            all_prices.extend(prices)
            all_items.extend(items)

        if not all_prices:
            return []

        avg_price = sum(all_prices) / len(all_prices)
        threshold = avg_price * threshold_ratio

        bargains = [item for item in all_items if item['price'] < threshold]
        return bargains
