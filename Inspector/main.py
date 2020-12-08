import os
from utils.get_feature_values import GetFeatures
from config import UDPIPE_MODEL, chkr, BASE_DIR
import pickle
import csv
import re
from tqdm.auto import tqdm

DATASET = os.path.join(BASE_DIR, 'data', 'feature_result.csv')
JSON_FILE = os.path.join(BASE_DIR, 'data', 'files_with_json.txt')
RESULT_FILE = os.path.join(BASE_DIR, 'data', 'result.json')
gf = GetFeatures(UDPIPE_MODEL)


def tokenizer(text):
    return text.split()


DON_MODEL_PATH = os.path.join(BASE_DIR, 'models', 'shell.pickle')
with open(DON_MODEL_PATH, 'rb') as mdl:
    DON_MODEL = pickle.load(mdl)


def check_spelling(text):
    chkr.set_text(text)
    for err in chkr:
        suggestions = err.suggest()
        if suggestions:
            suggest = suggestions[0]
            err.replace(suggest)
    text = chkr.get_text()
    return text


def read_file(path):
    with open(path, 'r', encoding='utf-8') as fr:
        text = fr.read()
    return text


def main(text):
    text = check_spelling(text)
    gf.get_info(text)
    result = {}
    result['av_depth'] = gf.av_depth()
    result['max_depth'] = gf.max_depth()
    result['min_depth'] = gf.min_depth()
    result['num_acl'], result['num_rel_cl'], result['num_advcl'] = gf.count_dep_sent()
    result['num_sent'] = gf.count_sent()
    result['num_tok'] = gf.count_tokens()
    result['av_tok_before_root'] = gf.tokens_before_root()
    result['av_len_sent'] = gf.mean_len_sent()
    result['num_cl'], result['num_tu'], result['num_compl_tu'] = gf.count_units()
    result['num_coord'] = gf.count_coord()
    result['num_poss'], result['num_prep'] = gf.count_poss_prep()
    result['num_adj_noun'] = gf.count_adj_noun()
    result['num_part_noun'] = gf.count_part_noun()
    result['num_noun_inf'] = gf.count_noun_inf()
    result['pos_sim_nei'], result['lemma_sim_nei'] = gf.simularity_neibour()
    result['pos_sim_all'], result['lemma_sim_all'] = gf.simularity_mean()
    result['density'] = gf.density()
    result['ls'] = gf.LS()
    result['vs'], result['corrected_vs'], result['squared_vs'] = gf.VS()
    result['lfp_1000'], result['lfp_2000'], result['lfp_uwl'], result['lfp_rest'] = gf.LFP()
    result['ndw'] = gf.NDW()
    result['ttr'], result['corrected_ttr'], result['root_ttr'], result['log_ttr'], result['uber_ttr'] = gf.TTR()
    result['d'] = gf.D()
    result['lv'] = gf.LV()
    result['vvi'], result['squared_vv'], result['corrected_vv'], result['vvii'] = gf.VV()
    result['nv'] = gf.NV()
    result['adjv'] = gf.AdjV()
    result['advv'] = gf.AdvV()
    result['modv'] = gf.ModV()
    (result['der_level3'], result['der_level4'],
     result['der_level5'], result['der_level6']) = gf.derivational_suffixation()
    result['mci'] = gf.MCI()
    result['freq_finite_forms'] = gf.freq_finite_forms()
    result['freq_aux'] = gf.freq_aux()
    (result['num_inf'], result['num_gerunds'], result['num_pres_sing'],
     result['num_pres_plur'], result['num_past_part'], result['num_past_simple']) = gf.num_verb_forms()
    result['num_linkings'] = gf.num_linkings().get('link_all')
    result['num_4grams'] = gf.num_4grams()
    result['num_func_ngrams'] = gf.num_func_ngrams().get('4grams_all')
    result['num_shell_noun'] = gf.shell_nouns(DON_MODEL)
    result['num_misspelled_tokens'] = gf.number_of_misspelled()
    result['punct_mistakes_pp'] = gf.count_punct_mistakes_participle_phrase()
    result['punct_mistakes_because'] = gf.count_punct_mistakes_before(before='because')
    result['punct_mistakes_but'] = gf.count_punct_mistakes_before(before='but')
    result['punct_mistakes_compare'] = gf.count_punct_mistakes_before(before='than') \
                                       + gf.count_punct_mistakes_before(before='like')
    result['million_mistake'] = gf.count_million_mistakes()
    result['side_mistake'] = gf.if_side_mistake()
    return result


def get_metadata(table_name, n=2):
    """
    функция примнимает название таблицы вида:
    text_name,errors
    путь_к_эссе,количество_ошибок
    ...
    некоторы_строки_с_информацией (n -- количество таких строк)
    """

    global columns
    with open(table_name) as f:
        lines = csv.reader(f)
        lines = list(lines)[1:-n]
    names = [x[0] for x in lines]
    errors = [x[1] for x in lines]
    if table_name.endswith('derivation.csv'):
        columns = [
            'name',
            'errors',
            'der_level3',
            'der_level4',
            'der_level5',
            'der_level6',
            'mci',
            'num_inf',
            'num_gerunds'
        ]
    elif table_name.endswith('lexical_choice_verb_pattern.csv'):
        columns = [
            'name',
            'errors',
            'density',
            'ls',
            'vs',
            'corrected_vs',
            'squared_vs',
            'lfp_1000',
            'lfp_2000',
            'lfp_uwl',
            'lfp_rest',
            'ndw',
            'ttr',
            'corrected_ttr',
            'root_ttr',
            'log_ttr',
            'uber_ttr',
            'lv',
            'vvi',
            'squared_vv',
            'corrected_vv',
            'vvii',
            'nv',
            'adjv',
            'advv',
            'modv'
        ]
    elif table_name.endswith('prepositions.csv'):
        columns = [
            'name',
            'errors',
            'num_prep'
        ]
    elif table_name.endswith('rhetorical.csv'):
        columns = [
            'name',
            'errors',
            'num_linkings',
            'num_shell_noun'
        ]
    elif table_name.endswith('syntax.csv'):
        columns = [
            'name',
            'errors',
            'av_depth',
            'max_depth',
            'min_depth',
            'num_acl',
            'num_advcl',
            'num_sent',
            'num_tok',
            'av_tok_before_root',
            'av_len_sent',
            'num_cl',
            'num_tu',
            'num_compl_tu',
            'num_coord',
            'num_adj_noun',
            'num_part_noun',
            'num_noun_inf',
            'pos_sim_nei',
            'lemma_sim_nei',
            'pos_sim_all',
            'lemma_sim_all'
        ]
    elif table_name.endswith('verb_morphology.csv'):
        columns = [
            'name',
            'errors',
            'num_inf',
            'num_gerunds',
            'num_pres_sing',
            'num_pres_plur',
            'num_past_part',
            'num_past_simple',
            'num_noun_inf'
        ]
    elif table_name.endswith('writing_conventions.csv'):
        columns = [
            'name',
            'errors',
            'num_misspelled_tokens',
            'punct_mistakes_pp',
            'punct_mistakes_because',
            'punct_mistakes_but',
            'punct_mistakes_compare'
        ]
    return names, errors, columns


def create_table(table_name, folder='.'):
    """
    функция прогоняет нужные эссе из таблицы
    и кладёт их в папку folder
    """

    names, errors, columns = get_metadata(table_name)
    all_features = []
    for name in tqdm(enumerate(names), total=len(names)):
        with open(f'./exam/{name[1]}', encoding='utf-8') as f:
            letters = f.read()
            letters = re.sub(r'<.*?@\n', '', letters)
            features = main(letters)
            data = {}
            features['name'] = name[1]
            features['errors'] = errors[name[0]]
            for column in columns:
                data[column] = features[column]
            all_features.append(data)

    path = os.path.join(folder, f"dataset_{table_name.split('/')[-1]}")
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for data in all_features:
            writer.writerow(data)


def create_distinct_datasets(table_name, folder='.'):
    """
    функция разбивает общий датасет на два по типам эссе
    """
    path = os.path.join(folder, f"dataset_{table_name.split('/')[-1]}")
    with open(path) as f:
        data = list(csv.reader(f))

    path_1 = os.path.join(folder, f"dataset_{table_name.split('/')[-1][:-4]}_1.csv")
    path_2 = os.path.join(folder, f"dataset_{table_name.split('/')[-1][:-4]}_2.csv")

    with open(path_1, 'w') as file_1, open(path_2, 'w') as file_2:
        writer_1 = csv.writer(file_1)
        writer_2 = csv.writer(file_2)
        writer_1.writerow(data[0])
        writer_2.writerow(data[0])
        for line in data[1:]:
            if line[0].endswith(('1.txt', '1(full).txt')):
                writer_1.writerow(line)
            elif line[0].endswith(('2.txt', '2(full).txt')):
                writer_2.writerow(line)


if __name__ == '__main__':
    for file in os.listdir('./tables'):
        if file.endswith('csv'):
            print(file)
            create_table(f'./tables/{file}')
            create_distinct_datasets(f'./tables/{file}')
