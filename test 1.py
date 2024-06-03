import csv
from enum import Enum
from CSV_LOAD_save import display_data, load_data, save_data
from sumModule import number_of_ideal_diamonds, sum_of_diamonds
from AVGmodule import average_carat, average_price_by_color, median_weight
from prices_color import colors_of_diamonds, highest_price
from delete import delete_diamond
from add import add_diamond
class Diamond_market(Enum):
    DISPLAY = 1
    SAVE = 2
    NUMBER_OF_IDEAL_DIAMOND = 3
    SUM_OF_DIAMONDS = 4
    HIGHEST_PRICE = 5
    COLOR_OF_DIAMONDS = 6
    AVG_CRT = 7
    AVG_PRICE_BY_COLOR = 8
    MEDIAN_WEIGHT = 9
    ADD = 10
    DELETE = 11
    EXIT = 12



if __name__ == "__main__":
    file_path = 'data.csv'
    data = load_data(file_path)

    if data is None:
        print("No data loaded. Exiting.")
    else:
        while True:
            try:
                print("\nChoose an option:")
                for action in Diamond_market:
                    print(f"{action.value}. {action.name.replace('_', ' ').title()}")
                
                choice = int(input("Enter your choice (number): "))

                if choice == Diamond_market.DISPLAY.value:
                    display_data(data)
                elif choice == Diamond_market.SAVE.value:
                    save_data(data, 'output.csv')
                elif choice == Diamond_market.NUMBER_OF_IDEAL_DIAMOND.value:
                    print(f"Number of Ideal diamonds: {number_of_ideal_diamonds(data)}")
                elif choice == Diamond_market.SUM_OF_DIAMONDS.value:
                    print(f"Sum of diamonds prices: {sum_of_diamonds(data)}")
                elif choice == Diamond_market.HIGHEST_PRICE.value:
                    print(f"Highest priced diamond: {highest_price(data)}")
                elif choice == Diamond_market.COLOR_OF_DIAMONDS.value:
                    print(f"Colors of diamonds: {colors_of_diamonds(data)}")
                elif choice == Diamond_market.AVG_CRT.value:
                    print(f"Average carat: {average_carat(data)}")
                elif choice == Diamond_market.AVG_PRICE_BY_COLOR.value:
                    avg_prices = average_price_by_color(data)
                    for color, avg_price in avg_prices.items():
                        print(f"Average price for color {color}: {avg_price}")
                elif choice == Diamond_market.MEDIAN_WEIGHT.value:
                    print(f"Median weight of diamonds: {median_weight(data)}")
                elif choice == Diamond_market.ADD.value:
                    add_diamond(data)
                elif choice == Diamond_market.DELETE.value:
                    delete_diamond(data)
                elif choice == Diamond_market.EXIT.value:
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Please enter a number from the list.")
            
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")
