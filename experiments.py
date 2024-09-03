import argparse

def main():
    # Read cmd line arguments with argparse
    parser = argparse.ArgumentParser(description='Run experiments')
    parser.add_argument('--model', type=str, default='gpt4', help='Model to evaluate')
    parser.add_argument('--prompting', type=str, default='zero_shot', help='Prompting strategy')
    parser.add_argument('--encoding', type=str, default='SQL', help='Encoding method for data and query')
    parser.add_argument('--operation', type=str, default='select', help='Dataset query operation')
    parser.add_argument('--select', type=str, default='all', help='Subcategory of select query operation')    
    parser.add_argument('--scale', type=int, default='300', help='Number of operations in the dataset')
    parser.add_argument('--balance', type=float, default=0.5, help='Ratio of insert in the operations in the dataset, a number between 0 and 1')
    parser.add_argument('--overlap', type=float, default=0.5, help='Ratio of overlap between the operations in the dataset, a number between 0 and 0.5')
    args = parser.parse_args()
    args_dict = vars(args)

    




    
if __name__ == "__main__":
    main()