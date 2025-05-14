from include.kScraper import *
from include.mScraper import *

def main():
    gpu_model = input("\nWhat gpu model number to look for? (Example: 5080; 4070ti; b580; 9070xt; 7900xtx) > ")
    print(f"Looking for {gpu_model}...\n")

    komputronik_scrape(gpu_model)
    morele_scrape(gpu_model)

if __name__ == "__main__":
    main()