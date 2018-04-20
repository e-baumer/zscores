import numpy as np
from ..zscore_finder import ZScores


def test_zscore():

    test_zs = ZScores('data')

    test_zs.data['wfa_boys']['test'] = test_zs.data['wfa_boys'].apply(
        lambda x: test_zs.z_score(gender=1, measure='wfa', weight=x['SD0'], age=x['Month']), axis=1
    )

    for index, row in test_zs.data['wfa_boys'].iterrows():
        print(row['test'])
        assert np.round(row['test'], 0) == 0
