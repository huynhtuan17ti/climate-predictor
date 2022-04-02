from src_1.utils import *
import yaml

def load_config():
    with open('src_1/config.yaml', 'r') as f:
        return yaml.safe_load(f)

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
        print(f'[=] {predict_feature}', end = ': ')
        model_dict[predict_feature] = train(input_data, output_data[:, idx])
        model_dict[predict_feature].save(cfg['weight_path'] + f'{predict_feature}.pkl')
    print()

    # ==== TEST ====
    print('--- [TEST] ---')
    input_data = extract_features(test_df, cfg['features'])
    output_data = extract_features(test_df, cfg['predict_features'])
    print('======')
    for idx, predict_feature in enumerate(cfg['predict_features']):
        print(f'[=] {predict_feature}', end = ': ')
        evaluate(model_dict[predict_feature], input_data, output_data[:, idx])

if __name__ == '__main__':
    main()