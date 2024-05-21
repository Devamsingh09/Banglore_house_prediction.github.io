from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
lr= LinearRegression()





from sklearn.model_selection import GridSearchCV, ShuffleSplit
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

def find_best_model_using_gridsearchcv(X, y):
    algos = {
        'linear_regression': {
            'model': LinearRegression(),
            'params': {
                'fit_intercept': [True, False]
            }
        },
        'lasso': {
            'model': Lasso(),
            'params': {
                'alpha': [1, 2],
                'selection': ['random', 'cyclic']
            }
        },
        'decision_tree': {
            'model': DecisionTreeRegressor(),
            'params': {
                'criterion': ['mse', 'friedman_mse'],
                'splitter': ['best', 'random']
            }
        }
    }
    
    scores = []
    cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
    
    for algo_name, config in algos.items():
        gs = GridSearchCV(config['model'], config['params'], cv=cv, return_train_score=False)
        gs.fit(X, y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params': gs.best_params_
        })
    
    return pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])


import warnings
warnings.filterwarnings('ignore')


find_best_model_using_gridsearchcv(X,y)
# Above line code will give the model, its best score with best parameter with the help of GridSearchCV
# for example-
#	         model	        best_score        best_params
#---------------------------------------------------------------------------------------------
#  0	linear_regression	0.819001	      {'fit_intercept': False}
#  1	lasso	            0.687444	      {'alpha': 2, 'selection': 'random'}
#  2	decision_tree	    0.718037	      {'criterion': 'friedman_mse', 'splitter': 'best'}

#Function for predicting the price:
def predict_price(location,sqft,bath,bhk):
    loc_index = np.where(X.columns==location)[0][0]
    
    x=np.zeros(len(X.columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
        
    return lr.predict([x])[0]
