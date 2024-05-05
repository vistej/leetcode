class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.ratings = ratings
        self.cuisines = cuisines
        self.model = {}
        for i in range(len(foods)):
            cs = cuisines[i]
            food = foods[i]
            rating = ratings[i]
            if cs not in self.model:
                self.model[cs] = {}
            csi = self.model[cs]
            if rating not in csi:
                csi[rating] = []
            csi[rating].append(food)



    def changeRating(self, food: str, newRating: int) -> None:
        i = self.foods.index(food)
        cr = self.ratings[i]
        cs = self.cuisines[i]
        self.model[cs][cr].remove(food)
        if not self.model[cs][cr]:
            del self.model[cs][cr]

        self.ratings[i] = newRating
        if newRating not in self.model[cs]:
            self.model[cs][newRating] = []
        self.model[cs][newRating].append(food)

    def highestRated(self, cuisine: str) -> str:
        r = max(self.model[cuisine].keys())
        return min(self.model[cuisine][r])




# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)