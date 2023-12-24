use std::cmp::Reverse;
/**
 * https://leetcode.com/problems/design-a-food-rating-system/
 * 2353. Design a Food Rating System
 */
use std::collections::{BinaryHeap, HashMap};

struct FoodRatings {
    food_ratings: HashMap<String, i32>,
    cuisine_ratings: HashMap<String, BinaryHeap<(i32, Reverse<String>)>>,
    food_cuisine: HashMap<String, String>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FoodRatings {
    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        let mut food_ratings = HashMap::new();
        let mut cuisine_ratings: HashMap<String, BinaryHeap<(i32, Reverse<String>)>> =
            HashMap::new();
        let mut food_cuisine = HashMap::new();
        for i in 0..foods.len() {
            let (food, cuisine, rating) = (&foods[i], &cuisines[i], ratings[i]);
            food_ratings.insert(food.clone(), rating);
            if let Some(q) = cuisine_ratings.get_mut(cuisine) {
                q.push((rating, Reverse(food.clone())));
            } else {
                let mut q = BinaryHeap::new();
                q.push((rating, Reverse(food.clone())));
                cuisine_ratings.insert(cuisine.clone(), q);
            }
            food_cuisine.insert(food.clone(), cuisine.clone());
        }

        Self {
            food_ratings,
            cuisine_ratings,
            food_cuisine,
        }
    }

    fn change_rating(&mut self, food: String, new_rating: i32) {
        self.food_ratings
            .entry(food.clone())
            .and_modify(|r| *r = new_rating)
            .or_insert(new_rating);
        let cuisine = self.food_cuisine.get(&food).unwrap();
        if let Some(q) = self.cuisine_ratings.get_mut(cuisine) {
            q.push((new_rating, Reverse(food.clone())));
        }
    }

    fn highest_rated(&mut self, cuisine: String) -> String {
        if let Some(q) = self.cuisine_ratings.get_mut(&cuisine) {
            while let Some(item) = q.peek() {
                let highest = self.food_ratings.get(&item.1 .0).unwrap();
                if item.0 == *highest {
                    return item.1 .0.clone();
                }
                q.pop();
            }
        }
        unreachable!()
    }
}
