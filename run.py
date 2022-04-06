from src_1.utils import *
import yaml
import argparse

parser = argparse.ArgumentParser(description='Predict Temperature using Linear Regression')
parser.add_argument('--config', default='src_1/config.yaml', type=str, help='configure file')
parser.add_argument('--mode', default=0, type=int, help='running mode: 0 - regression mode, 1 - explore feature for linear model')
args = parser.parse_args()

def load_config():
    with open(args.config, 'r') as f:
        return yaml.safe_load(f)

def explore_feature():
    cfg = load_config()
    train_df = pd.read_csv(cfg['train'])

    choose_features = {}
    correlation_csv = {}
    for pred in cfg['predict_features']:
        choose_features[pred] = []

    # ==== Calculate correlation ====
    print('--- [CORRELATION CALC] ---')
    for col in train_df.columns:
        if train_df[col].dtype == 'object':
            continue

        if check_if_column_nan(train_df[col].to_numpy()):
            print(f'Error: Found {col} column in nan!')
            continue

        if col in cfg['predict_features']:
            continue
        
        correlation_csv[col] = []
        attr1 = train_df[col].to_numpy()
        for pred_col in cfg['predict_features']:
            attr2 = train_df[pred_col].to_numpy()
            correlation_score = correlation_of_two_variables(attr1, attr2)
            correlation_csv[col].append(correlation_score)
            if abs(correlation_score) >= cfg['correlation_threshold']:
                choose_features[pred_col].append(col)
            print(f'Correlation of {col} and {pred_col}', correlation_score)
        print('======')

    print('--- [Result] ---')
    print(choose_features)
    df = pd.DataFrame(correlation_csv, cfg['predict_features']).T
    df.to_csv(cfg['correlation_csv_path'])
    print('Save csv successfully')

def main():
    cfg = load_config()
    train_df = pd.read_csv(cfg['train'])
    test_df = pd.read_csv(cfg['test'])

    # ==== TRAIN ====
    print('--- [TRAIN] ---')
    input_data = extract_features(train_df, cfg['features'])
    output_data = extract_features(train_df, cfg['predict_features'])
    model_dict = {}
    print('======')
    for idx, predict_feature in enumerate(cfg['predict_features']):
        print(f'[=] {predict_feature}', end = ':\n')
        model_dict[predict_feature] = train(input_data, output_data[:, idx])
        model_dict[predict_feature].save(cfg['weight_path'] + f'{predict_feature}.pkl')
    print()

    # ==== TEST ====
    print('--- [TEST] ---')
    input_data = extract_features(test_df, cfg['features'])
    output_data = extract_features(test_df, cfg['predict_features'])
    print('======')
    for idx, predict_feature in enumerate(cfg['predict_features']):
        print(f'[=] {predict_feature}', end = ':\n')
        evaluate(model_dict[predict_feature], input_data, output_data[:, idx])

if __name__ == '__main__':
    if args.mode == 0:
        main()
    elif args.mode == 1:
        explore_feature()
    else:
        print('Mode not found!')